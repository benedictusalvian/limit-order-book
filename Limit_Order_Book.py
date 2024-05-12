from sortedcontainers import SortedSet, SortedDict
import mysql.connector
import time
from print_order_book import print_order_book
from config import YOUR_DATABASE_HOST, YOUR_DATABASE_USER, YOUR_DATABASE_PASSWORD

start = time.time()

filename = 'VOO.log'
data = []

with open(filename, 'r') as file:
    for line in file:
        values = line.split()
        data.append(values)

file_path = "VOO_output.log"
file = open(file_path, "w")

db = mysql.connector.connect(
    host = YOUR_DATABASE_HOST,
    user = YOUR_DATABASE_USER,
    password = YOUR_DATABASE_PASSWORD,
    database = 'order_book',
)
cursor = db.cursor()
snapshots = []

bid = SortedDict()
ask = SortedDict()
price_book = [bid, ask]
order_book = SortedDict()
order_map = {}
bestbids = SortedSet()
bestasks = SortedSet()

for entry in data:
    epoch, order_id, symbol, order_side, order_category, price, quantity = entry
    identifier = (int(entry[1]), entry[3])
    price, quantity = float(entry[5]), int(entry[6])
    level_data = [price, quantity]
    if entry[3] == "BUY" and entry[4] == "NEW":
        order_map[identifier] = level_data
        order_book.setdefault(price, []).append(identifier)
        bid[price] = bid.get(price, 0) + quantity
        bestbids.add(price)
    elif entry[3] == "SELL" and entry[4] == "NEW":
        order_map[identifier] = level_data
        order_book.setdefault(price, []).append(identifier)
        ask[price] = ask.get(price, 0) + quantity
        bestasks.add(price)
    elif entry[3] == "BUY" and entry[4] == "CANCEL":
        del order_map[identifier]
        order_book[price].remove(identifier)
        if len(order_book[price]) == 0:
            del order_book[price]
        bid[price] -= quantity
        if bid[price] == 0:
            del bid[price]
            bestbids.remove(price)
    elif entry[3] == "SELL" and entry[4] == "CANCEL":
        del order_map[identifier]
        order_book[price].remove(identifier)
        if len(order_book[price]) == 0:
            del order_book[price]
        ask[price] -= quantity
        if ask[price] == 0:
            del ask[price]
            bestasks.remove(price)
    elif entry[3] == "BUY" and entry[4] == "TRADE":
        order_map[identifier][1] -= quantity
        bid[price] -= quantity
        if order_map[identifier][1] == 0:
            del order_map[identifier]
            order_book[price].remove(identifier)
            if len(order_book[price]) == 0:
                del order_book[price]
        if bid[price] == 0:
            del bid[price]
            bestbids.remove(price)
    elif entry[3] == "SELL" and entry[4] == "TRADE":
        order_map[identifier][1] -= quantity
        ask[price] -= quantity
        if order_map[identifier][1] == 0:
            del order_map[identifier]
            order_book[price].remove(identifier)
            if len(order_book[price]) == 0:
                del order_book[price]
        if ask[price] == 0:
            del ask[price]
            bestasks.remove(price)
    bestbidprices, bestaskprices = [], []
    bestbidquantities, bestaskquantities = [], []
    for i in range(5):
        bestbidprice = bestbids[-1 * (i + 1)] if len(bestbids) > i else "N.A"
        bestaskprice = bestasks[i] if len(bestasks) > i else "N.A"   
        bestbidquantity = bid[bestbidprice] if bestbidprice != "N.A" else "N.A"
        bestaskquantity = ask[bestaskprice] if bestaskprice != "N.A" else "N.A"
        bestbidprices.append(bestbidprice)
        bestaskprices.append(bestaskprice)
        bestbidquantities.append(bestbidquantity)
        bestaskquantities.append(bestaskquantity)
    output = (
        f"{symbol}, {epoch}, {bestbidquantities[4]}@{bestbidprices[4]} "
        f"{bestbidquantities[3]}@{bestbidprices[3]} {bestbidquantities[2]}@{bestbidprices[2]} "
        f"{bestbidquantities[1]}@{bestbidprices[1]} {bestbidquantities[0]}@{bestbidprices[0]} X "
        f"{bestaskquantities[0]}@{bestaskprices[0]} {bestaskquantities[1]}@{bestaskprices[1]} "
        f"{bestaskquantities[2]}@{bestaskprices[2]} {bestaskquantities[3]}@{bestaskprices[3]} "
        f"{bestaskquantities[4]}@{bestaskprices[4]}, "
        )
    if entry[4] == "TRADE":
        output += f"{price}, {quantity}\n"
    else:
        output += f"N.A, N.A\n"

    file.write(output)
    # print(output)

    snapshot = [symbol, epoch]

    for i in range(5):
        snapshot.append(bestbidquantities[4 - i] if bestbidquantities[4 - i] != "N.A" else None)
        snapshot.append(bestbidprices[4 - i] if bestbidprices[4 - i] != "N.A" else None)
    for i in range(5):
        snapshot.append(bestaskquantities[i] if bestaskquantities[i] != "N.A" else None)
        snapshot.append(bestaskprices[i] if bestaskprices[i] != "N.A" else None)
    if entry[4] == "TRADE":
        snapshot.append(price)
        snapshot.append(quantity)
    else:
        snapshot.append(None)
        snapshot.append(None)

    snapshots.append(snapshot)

query = """INSERT INTO orders(symbol, epoch, b4q, b4p, b3q, b3p, b2q, b2p, b1q, b1p, b0q, b0p, a0q, a0p, a1q, a1p, a2q, a2p, a3q, a3p, a4q, a4p, trade_price, trade_quantity)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
cursor.executemany(query, snapshots)
db.commit()

file.close()
cursor.close()
db.close()

end = time.time()
timeLength = end - start
print("Simulated 10,000 transactions.")
print("Program exited in", timeLength, "seconds.")
print()

# print(price_book, '\n')

max_bid = max(bid.keys())
print_order_book(order_book, order_map, max_bid)
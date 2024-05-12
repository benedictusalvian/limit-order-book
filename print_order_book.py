def print_order_book(order_book, order_map, max_bid):
    
    bid_arr, ask_arr= [], []

    for price, identifiers in order_book.items():
        quantities = []
        for identifier in identifiers:
            quantities.append(order_map[identifier][1])
        total_quantity = sum(quantities)
        if price <= max_bid:
            bid_arr.append([price, total_quantity, ' '.join(str(x) for x in quantities)])
        else:
            ask_arr.append([price, total_quantity, ' '.join(str(x) for x in quantities)])

    bid_arr = bid_arr[::-1]
    bid_widths = [max(len(str(bid[i])) for bid in bid_arr) for i in range(len(bid_arr[0]))]
    ask_widths = [max(len(str(ask[i])) for ask in ask_arr) for i in range(len(ask_arr[0]))]
    widths = [max(bid_widths[i], ask_widths[i]) for i in range(len(bid_widths))]
    min_len = min(len(bid_arr), len(ask_arr))

    print("Limit Order Book (Market by Order)".center(94), '\n')
    print('Orders'.rjust(25), 'Quantity'.rjust(10), 'Price'.rjust(8), '  ', 'Price'.ljust(8), 'Quantity'.ljust(10), 'Orders'.ljust(25))

    for i in range(min_len):
        temp = [str(elem) for elem in bid_arr[i][::-1] + ask_arr[i]]
        print(temp[0].rjust(25), temp[1].rjust(10), temp[2].rjust(8), '  ', temp[3].ljust(8), temp[4].ljust(10), temp[5].ljust(25))

    if len(bid_arr) > min_len:
        for i in range(min_len, len(bid_arr)):
            temp = [str(elem) for elem in bid_arr[i][::-1]]
            print(temp[0].rjust(25), temp[1].rjust(10), temp[2].rjust(8))

    elif len(ask_arr) > min_len:
        for i in range(min_len, len(ask_arr)):
            temp = [str(elem) for elem in ask_arr[i]]
            print(''.rjust(48), temp[0].ljust(8), temp[1].ljust(10), temp[2].ljust(25))


# Limit Order Book (Market by Order) &middot; [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/benedictusalvian/limit-order-book/issues)

Limit Order Book (Market by Order) is an limit order book for Delta One Index ETFs that generates best bids and asks snapshot after every order, with ability to write to disk or database, supporting lightning-fast query speeds. The Limit Order Book (Market by Order) is able to simulate 7,600 transactions per second on consumer hardware, and also provide a visual representation of the book itself for clarity and easy checking of market microstructure.

## Features

- Simply pass a `.log` file for initial limit order book population. The fields inside are all configurable, e.g. epoch, order ID, Delta One Index ETFs symbol, order type, action, as well as price and quantity.
- The program will automatically maintain the best 5 bids and asks snapshots after every order for every epoch and batch write to disk / database.
- Able to simulate 7,600 transactions per second on consumer hardware, and support native lightning-fast queries on MySQL.
- Visual representation of the book also available for easy checking and clarity.

## Tech

Limit Order Book (Market by Order) uses a number of open source projects to work properly:

- [sortedcontainers] - Sorted Containers is an Apache2 licensed sorted collections library, written in pure-Python, and fast as C-extensions.
- [mysql-connector-python] - MySQL driver written in Python which does not depend on MySQL C client libraries and implements the DB API v2.0 specification.

And of course Limit Order Book (Market by Order) itself is a free and open-source software with a [public repository][limit-order-book] 
on GitHub.

## Installation

Limit Order Book (Market by Order) has been developed and tested to run on [Python 3.12](https://www.python.org/downloads/).

Install [Python](https://www.python.org/downloads/release/python-3120/) if you have not already.

To use or contribute to Limit Order Book (Market by Order), first clone the repository.

Then, install the dependencies by typing the following command on your terminal:

```sh
pip3 install -r requirements.txt
```

Install [MySQL](https://www.mysql.com/downloads/) if you haven't already. Then, open up an instance of your local MySQL and create the database `order_book` as well as table `orders` with the command:

```sh
source schema.sql
```

Then, rename `config_example.py` to `config.py` and replace the database constants `YOUR_DATABASE_HOST`, `YOUR_DATABASE_USER`, and `YOUR_DATABASE_PASSWORD` with your own database constants.

You may then create your own initial limit order book population `.log` file or use the default provided for the program for Delta One Index ETF VOO contained in file `VOO.log`.

## Examples

Now run the following command on the terminal to run Limit Order Book (Market by Order):

```sh
python3 Limit_Order_Book.py
```

If you use the given `VOO.log` file as your initial Input Delta One Index ETF symbol, the following results will be printed (results have been truncated for brevity):

```sh
# Order Snapshots

VOO, 1609723108363714203, 5@476.58 6@476.59 5@476.6 7@476.61 9@476.62 X 8@476.63 2@476.64 14@476.65 4@476.66 8@476.67, N.A, N.A

VOO, 1609723108363996776, 5@476.58 6@476.59 5@476.6 7@476.61 9@476.62 X 7@476.63 2@476.64 14@476.65 4@476.66 8@476.67, 476.63, 1

VOO, 1609723108364143229, 5@476.58 6@476.59 5@476.6 7@476.61 9@476.62 X 6@476.63 2@476.64 14@476.65 4@476.66 8@476.67, 476.63, 1

# Program Timer

Simulated 10,000 transactions.
Program exited in 1.3075592517852783 seconds.

# Limit Order Book (MBO)

                              Limit Order Book (Market by Order)                               

                   Orders   Quantity    Price    Price    Quantity   Orders                   
            2 1 1 1 4 1 1         11   476.62    476.64   2          1 1                      
              2 1 1 1 1 1          7   476.61    476.65   15         1 10 1 1 1 1             
                  1 2 1 1          5    476.6    476.66   4          1 1 1 1                  
                1 1 2 1 1          6   476.59    476.67   7          1 1 2 1 1 1              
                  1 2 1 1          5   476.58    476.68   5          1 2 1 1                  
            1 1 2 1 1 1 1          8   476.57    476.69   10         1 2 1 1 1 1 1 1 1        
              1 1 1 1 1 1          6   476.56    476.7    5          1 1 1 1 1                
                1 1 2 1 1          6   476.55    476.71   3          1 1 1                    
                    1 1 2          4   476.54    476.72   11         1 1 9                    
                1 2 1 1 1          6   476.53    476.73   5          1 1 1 1 1                
            1 1 1 1 5 5 1         15   476.52    476.74   8          1 2 1 1 3                
                  1 1 2 1          5   476.51    476.75   4          1 1 1 1                  
              1 1 1 1 2 1          7    476.5    476.76   5          1 1 1 1 1                
```

The order snapshots above will then be batch written to the database to support native lightning-fast queries to search for snapshots based on epoch, or Order ID, or any other fields. The order snapshots above will also be written to an `_output.log` file for your own viewing convenience.

## Development

Want to contribute? Great!

Limit Order Book (Market by Order) uses Python for developing.
Make changes in your file and create a pull request!

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [sortedcontainers]: <https://grantjenks.com/docs/sortedcontainers/>
   [mysql-connector-python]: <https://pypi.org/project/mysql-connector-python/>
   [limit-order-book]: <https://github.com/benedictusalvian/limit-order-book/>
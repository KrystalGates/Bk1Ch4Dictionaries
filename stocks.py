# Example
stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE":"General Electric"
}
# Create a simple list of blocks of stock. Make them tuples with ticker symbols, number of shares, dates and price.

# Example
purchases = [
    ( 'GM', 100, '10-sep-2001', 35 ),
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]
# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

# for block in purchases:
#     stock_name = ""
#     for key,value in stockDict.items():
#         if key == block[0]:
#             stock_name = value
#     amount_purchased = block[1] * block[3]
#     print(f'I purchased {stock_name} stock for ${amount_purchased}.')


# Example output for one block: I purchased General Electric stock for $4800

# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

# purchases = [
#     ( 'GM', 100, '10-sep-2001', 35 ),
#     ( 'GE', 100, '10-sep-2001', 48 ),
#     ( 'CAT', 100, '1-apr-1999', 24 ),
#     ( 'GE', 200, '1-jul-1998', 56 )
# ]
total_investment = {}

for block in purchases:
    if block[0] not in total_investment:
        total_investment[block[0]] = [block]
    else:
        total_investment[block[0]].append(block)

for key,value in total_investment.items():
    total = 0
    for item in value:
        total += item[1] * item[3]
        print(f'---{key}--- {item[1]} shares at {item[3]} dollars each on {item[2]}')
        print(f' Total value of stock in portfolio:${total}')

print(total_investment)

# Example output:

# ------ GE ------
# 100 shares at 48 dollars each on 01-jul-1998
# 200 shares at 56 dollars each on 10-sep-2001

# Total value of stock in portfolio: $16000
""" A function that parses through a JSON document that contains 
multiple order lines and performs a search where the order value is greater than an amount. 
This example showcases a very suboptimal solution to the problem because it uses a nested loop, 
converts the JSON document to a list every time, and does not use any built-in methods or libraries.
"""

def search_orders(json_doc, amount):
  # initialize an empty list to store the matching orders
  result = []
  # loop through each order line in the JSON document
  for order_line in json_doc:
    # convert the order line to a dictionary
    order_dict = eval(order_line)
    # get the order value from the dictionary
    order_value = order_dict["value"]
    # check if the order value is greater than the amount
    if order_value > amount:
      # append the order line to the result list
      result.append(order_line)
  # return the result list
  return result

# example JSON document with multiple order lines
json_doc = [
  '{"id": "A001", "value": 100, "items": ["apple", "banana"]}',
  '{"id": "A002", "value": 200, "items": ["orange", "mango"]}',
  '{"id": "A003", "value": 150, "items": ["grape", "melon"]}',
  '{"id": "A004", "value": 50, "items": ["pear", "peach"]}'
]

# example amount to search for
amount = 120

# call the function and print the result
print(search_orders(json_doc, amount))

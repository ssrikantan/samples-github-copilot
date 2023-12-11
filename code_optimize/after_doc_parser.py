""" A function that parses through a JSON document that contains 
multiple order lines and performs a search where the order value is greater than an amount. 
This example showcases a very suboptimal solution to the problem because it uses a nested loop, 
converts the JSON document to a list every time, and does not use any built-in methods or libraries.
"""

import json

def search_orders(json_doc, amount):
  # load the JSON document into a list of dictionaries
  orders = [json.loads(line) for line in json_doc]
  # use a list comprehension to filter the orders by amount
  result = [line for line in json_doc if json.loads(line)["value"] > amount]
  # return the filtered list
  return result

# example JSON document with multiple order lines
json_doc = [
  '{"id": "A001", "value": 100, "items": ["apple", "banana"]}',
  '{"id": "A002", "value": 200, "items": ["orange", "mango"]}',
  '{"id": "A003", "value": 150, "items": ["grape", "melon"]}',
  '{"id": "A004", "value": 50, "items": ["pear", "peach"]}',
  '{"id": "A005", "value": 80, "items": ["pear", "peach"]}'
]

# example amount to search for
amount = 250

# call the function and print the result
print(search_orders(json_doc, amount))
import random
import json

""" Perform the steps mentioned below:
generate a random number between 1 and 1000
call the search_orders() with the the sample json document, and a random number as the amount
print each filtered order line in the format: Order ID: <id>, Value: <value> to console
"""


# Generate a random number between 1 and 1000
amount = random.randint(1, 130)
print("amount",amount)
# Generate a sample JSON document with 10 order lines
sample_doc = [
  '{"id": "A001", "value": 100, "items": ["apple", "banana"]}',
  '{"id": "A002", "value": 200, "items": ["orange", "mango"]}',
  '{"id": "A003", "value": 150, "items": ["grape", "melon"]}',
  '{"id": "A004", "value": 50, "items": ["pear", "peach"]}'
]






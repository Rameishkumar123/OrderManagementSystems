"""
Helper functions file

Step-by-step Instructions:
1. Implement:
   - validate_price(price)
   - validate_quantity(qty)
2. Add ID generator (e.g., order_id).
Hint: Use itertools.count() or uuid.uuid4() for unique IDs
"""

import itertools

_id_counter = itertools.count(1)

def validate_price(price):
    # TODO: Raise ValueError if price < 0
    pass

def validate_quantity(qty):
    # TODO: Raise ValueError if qty <= 0
    pass

def generate_id():
    # TODO: Return next id
    # Hint: return next(_id_counter)
    pass

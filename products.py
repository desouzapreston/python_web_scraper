from datetime import datetime

from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# TODO: Data needs to be passed in via dict valuekey pair form
PRODUCTS = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}

def read_all():
    # json string of all products available
    # read in from reader (dict key:value)
    return [PRODUCTS[key] for key in sorted(PRODUCTS.keys())]


def read_one(part_num):
    # Individual product selector
    if part_num in PRODUCTS:
        product = PRODUCTS.get(part_num)
    else:
        abort(
            404, "{part_num} not found. Please try again".format(part_num=part_num)
        ) #loop through to reentry

    return product

"""def delete(part_num):
    # Deletes product from product list PRODUCTS
    if part_num in PRODUCTS:
        del PRODUCTS[part_num]
        return make_response(
            "{part_num} successfully deleted".format(part_num=part_num), 200
        )
    else:
        abort(
            404, "product with last name {part_num} not found".format(part_num=part_num)
        )
"""

"""def create(product):
    # Create a new product
    part_num = product.get("part_num", None)
    fname = product.get("fname", None)

    # Does the product exist already?
    if part_num not in PRODUCTS and part_num is not None:
        PRODUCTS[part_num] = {
            "part_num": part_num,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{part_num} successfully created".format(part_num=part_num), 201 # Success
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406, # Product Exists
            "product with last name {part_num} already exists".format(part_num=part_num),
        )
"""

"""def update(part_num, product):
    # Updates existing product in product list PRODUCTS 
    if part_num in PRODUCTS:
        PRODUCTS[part_num]["fname"] = product.get("fname")
        PRODUCTS[part_num]["timestamp"] = get_timestamp()
        return PRODUCTS[part_num]
    else:
        abort(
            404, "product with last name {part_num} not found".format(part_num=part_num)
        )
"""

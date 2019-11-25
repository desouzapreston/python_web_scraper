from datetime import datetime

from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# TODO: Data needs to be passed in via dict valuekey pair form
PRODUCTS = {
    "211149-01": {
        "title": "SpareEartips small for VOY6200",
        "part_num": "211149-01",
        "timestamp": get_timestamp()
    },
    "211145-01": {
        "title": "BLACKWIRE 7225BW7225USB-CBLACKWW",
        "part_num": "211145-01",
        "timestamp": get_timestamp()
    },
    "81293-01": {
        "title": "Voyager 3200 UCWW",
        "part_num": "81293-01",
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

# This bottom code is more for if I can expand the site to act like a shopping cart. 
# It developed from the tutorial I was following 
""" def delete(part_num):
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


def create(product):
    # Create a new product
    part_num = product.get("part_num", None)
    title = product.get("title", None)

    # Does the product exist already?
    if part_num not in PRODUCTS and part_num is not None:
        PRODUCTS[part_num] = {
            "part_num": part_num,
            "title": title,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{part_num} successfully created".format(part_num=part_num), 201 # Success
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406, # Product Exists
            "product with Part Number {part_num} already exists".format(part_num=part_num),
        )


def update(part_num, product):
    # Updates existing product in product list PRODUCTS 
    if part_num in PRODUCTS:
        PRODUCTS[part_num]["title"] = product.get("title")
        PRODUCTS[part_num]["timestamp"] = get_timestamp()
        return PRODUCTS[part_num]
    else:
        abort(
            404, "product with part_num {part_num} not found".format(part_num=part_num)
        )

 """
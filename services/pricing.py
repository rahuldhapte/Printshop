def calculate_price(pages, copies, print_type):

    if print_type == "bw":
        price_per_page = 2
    else:
        price_per_page = 7

    total = pages * copies * price_per_page
    return total
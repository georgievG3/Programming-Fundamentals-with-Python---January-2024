import re

number = int(input())
pattern = r"(\@\#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#{1,})"

for n in range(number):
    barcode = input()
    product_group = "00"

    match = re.match(pattern, barcode)

    if match:
        new_product_group = ""
        result = re.findall("\d", barcode)

        for digit in result:
            new_product_group += digit

            product_group = new_product_group

        print(f"Product group: {product_group}")

    else:
        print(f"Invalid barcode")



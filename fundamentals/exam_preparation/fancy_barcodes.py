import re

number_of_lines = int(input())
pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"
barcodes = [input() for _ in range(number_of_lines)]

for barcode in barcodes:
    match = re.match(pattern, barcode)
    if match:
        product_group = "".join(re.findall(r"\d", barcode))
        product_group = product_group if product_group else "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")

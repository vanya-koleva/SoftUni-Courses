pens_price = 5.80
markers_price = 7.20
detergent_price = 1.20

number_of_pens = int(input())
number_of_markers = int(input())
litres_of_detergent = int(input())
discount_percentage = int(input())

price_before_discount = pens_price * number_of_pens + \
                        markers_price * number_of_markers + \
                        detergent_price * litres_of_detergent
total_price = price_before_discount - (price_before_discount * discount_percentage / 100)
print(total_price)
mackerel_price = float(input())
sprat_price = float(input())
kg_of_bonito = float(input())
kg_of_scad = float(input())
kg_of_mussels = int(input())

bonito_price = mackerel_price * 1.6
total_bonito = kg_of_bonito * bonito_price
scad_price = sprat_price * 1.8
total_scad = kg_of_scad * scad_price
total_sum = total_bonito + total_scad + kg_of_mussels * 7.50

print(f"{total_sum:.02f}")
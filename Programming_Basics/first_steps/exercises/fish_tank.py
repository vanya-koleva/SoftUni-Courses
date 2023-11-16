length = int(input())
width = int(input())
height = int(input())
percent_non_free_volume = float(input())

fish_tank_volume_in_centimeters = length * width * height
fish_tank_volume_in_liters = fish_tank_volume_in_centimeters * 0.001

#simple calculation
#free_percetage = (100 - percentage_non_free_volume) / 100
#needed_liters = fish_tank_volume_in_liters * free_percentage

percentage = percent_non_free_volume / 100  # * 0.01
needed_liters = fish_tank_volume_in_liters * (1 - percentage)
print(needed_liters)

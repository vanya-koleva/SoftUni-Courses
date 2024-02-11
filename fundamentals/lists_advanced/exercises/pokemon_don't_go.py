def manipulate_distances(distance_list, sum_of_distances, current_index):
    removed_distance = 0
    if current_index < 0:
        removed_distance = distance_list[0]
        distance_list[0] = distance_list[-1]
    elif current_index >= len(distance_list):
        removed_distance = distance_list[-1]
        distance_list[-1] = distance_list[0]
    else:
        removed_distance = distance_list.pop(current_index)
    sum_of_distances += removed_distance
    for i in range(len(distance_list)):
        if distance_list[i] <= removed_distance:
            distance_list[i] += removed_distance
        else:
            distance_list[i] -= removed_distance
    return distance_list, sum_of_distances


distance = [int(x) for x in input().split()]
sum_of_removed_distances = 0
while distance:
    index = int(input())
    distance, sum_of_removed_distances = manipulate_distances(distance,sum_of_removed_distances, index)
print(sum_of_removed_distances)

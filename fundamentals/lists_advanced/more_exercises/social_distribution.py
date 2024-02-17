def social_distribution(population_list, min_wealth):
    for i in range(len(population_list)):
        if population_list[i] < min_wealth:
            difference = min_wealth - population_list[i]
            wealthiest = max(population_list)
            wealthiest_index = population_list.index(wealthiest)
            if wealthiest - difference < min_wealth:
                return "No equal distribution possible"
            else:
                population_list[i] += difference
                population_list[wealthiest_index] -= difference
    return population_list


population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())
print(social_distribution(population, minimum_wealth))

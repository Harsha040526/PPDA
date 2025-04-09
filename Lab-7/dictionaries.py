import pandas as pd
population_dict = {'California': 38332521,
'Texas': 26448193,
'Florida': 19552860,
'Illinois': 12882135}
population = pd.Series(population_dict)
print(population_dict,type(population_dict),"\n")
print(population,type(population),"\n")

print(population[0:3])


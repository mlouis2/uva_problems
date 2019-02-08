import sys
import re
first = True
countries_and_women = {};

for line in sys.stdin:
    line = line.strip()
    if not first:
        (country, woman) = line.split(" ", 1)
        if (country not in countries_and_women):
            countries_and_women[country] = [woman]
        else:
            if(woman not in countries_and_women[country]):
                countries_and_women[country].append(woman)
    first = False

for country in sorted(countries_and_women.keys()):
    print(country + " " + str(len(countries_and_women[country])))

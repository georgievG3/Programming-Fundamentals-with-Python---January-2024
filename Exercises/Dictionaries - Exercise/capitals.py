country_names = input().split(", ")
capital_cities = input().split(", ")

x = zip(country_names, capital_cities)

for country, capital in dict(x).items():
    print(f"{country} -> {capital}")
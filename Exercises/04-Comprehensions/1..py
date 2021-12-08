countries = input().split(', ')
capitals = input().split(', ')

result = {country: capital for country, capital in zip(countries, capitals)}

print('\n'.join([f'{country} -> {city}' for country, city in result.items()]))

# for country, capital in result.items():
#     print(f'{country} -> {capital}')
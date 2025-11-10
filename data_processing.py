import csv, os
from pathlib import Path

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

class DataLoader:
    """Handles loading CSV data files."""
    
    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)
    
    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        data = []
        
        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))
        
        return data
    
class Table:

    def __init__(self, key, table):
        self.key = key
        self.table = table

    def filter(self, condition):
        filtered_data = []
        for row in self.table:
            if condition(row):
                filtered_data.append(row)
        return Table(self.key + "_filtered", filtered_data)

    def aggregate(self, func, column):
        try:
            values = []
            for row in self.table:
                if column in row and row[column] != '':
                    values.append(float(row[column]))
            
            return func(values)
        except (ValueError, KeyError) as e:
            print(e)

loader = DataLoader()
cities = loader.load_csv('Cities.csv')
my_table1 = Table('cities', cities)

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))



# Print first 5 cities only
for city in cities[:5]:
    print(city)


# Print the average temperature of all the cities
my_value = my_table1.aggregate(lambda x: sum(x)/len(x), 'temperature')
print(my_value)
print()

# Print all cities in Germany
my_cities = my_table1.filter(lambda x: x['country'] == 'Germany')
cities_list = [[city['city'], city['country']] for city in my_cities.table]
print("All the cities in Germany:")
for city in cities_list:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
my_cities = my_table1.filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12.0)
cities_list = [[city['city'], city['country'], city['temperature']] for city in my_cities.table]
print("All the cities in Spain with temperature above 12°C:")
for city in cities_list:
    print(city)
print()

# Count the number of unique countries
my_countries = my_table1.aggregate(lambda x: len(set(x)), 'country')
print("The number of unique countries is:")
print(my_countries)
print()     

# Print the average temperature for all the cities in Germany
my_value = my_table1.filter(lambda x: x['country'] == 'Germany').aggregate(lambda x: sum(x)/len(x), 'temperature')
print("The average temperature of all the cities in Germany:")
print(my_value)
print()

# Print the max temperature for all the cities in Italy
my_value = my_table1.filter(lambda x: x['country'] == 'Italy').aggregate(lambda x: max(x), 'temperature')
print("The max temperature of all the cities in Italy:")
print(my_value)
print()
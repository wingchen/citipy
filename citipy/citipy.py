import csv
import kdtree
import os


class City:
    '''
    City wraps up the info about a city, including its name, coordinates,
    and belonging country.
    '''
    def __init__(self, city_name, country_code):
        self.city_name = city_name
        self.country_code = country_code


# load the city data up
_current_dir, _current_filename = os.path.split(__file__)
_world_cities_csv_path = os.path.join(_current_dir, 'worldcities.csv')
_world_cities_kdtree = kdtree.create(dimensions=2)
WORLD_CITIES_DICT = {}

with open(_world_cities_csv_path, 'r') as csv_file:
    cities = csv.reader(csv_file)

    # discard the headers
    cities.__next__()

    # populate geo points into kdtree
    for city in cities:
        city_coordinate_key = (float(city[2]), float(city[3]))
        _world_cities_kdtree.add(city_coordinate_key)
        c = City(city[1], city[0])
        WORLD_CITIES_DICT[city_coordinate_key] = c


def nearest_city(latitude, longitude):
    nearest_city_coordinate = _world_cities_kdtree.search_nn((latitude, longitude, ))
    return WORLD_CITIES_DICT[nearest_city_coordinate[0].data]

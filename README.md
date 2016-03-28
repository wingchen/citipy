# citipy

Looking up for city names with geo-coordinates has always been a big problem when it comes to dealing with social data.

I hate going through web endpoints to look for the city names; we are often rate-limited and it's also such a waste.

We have only this many cities in the world, why isn't there any data set that provides the geo coordinates for all the

available cities, and we can use certain data structure/algorithm like kdtree to look up the nearest city given a set of geo coordinates?

Luckily, both Maxmind(www.maxmind.com/en/free-world-cities-database) and GeoNames(download.geonames.org/export/dump)

provide comprehensive data sets like this.

I then chose Maxmind because I think it's better. GeoNames lacks of many US cities.

# Example

## Installation

```
pip install citipy
```

## Looking up with coordinates

```
>>> from citipy import citipy
>>> city = citipy.nearest_city(22.99, 120.21)
>>> city
<citipy.City instance at 0x1069b6518>
>>>
>>> city.city_name     # Tainan, my home town
'tainan'
>>>
>>> city.country_code
'tw'                  # And the country is surely Taiwan
```

# World Cities Data Set

I use Maxmind's Free World Cities Database. You can get it here: https://www.maxmind.com/en/free-world-cities-database .

Please note that I only count in the cities whose population is over 500, otherwise the results are too noisy for me.

# Contribution

Just send me a PR. It's nice and easy :)

# License

MIT

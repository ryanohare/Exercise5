planets = {"mercury" : 57.91,
           "venus " : 108.2,
           "earth" : 149.597870,
           "mars" : 227.94
           }

for i, key in enumerate(planets.keys(), 1):
    print("{:2d} {:<10s} {:06.2f} Gm)".
          format(i, key, planets[key]))
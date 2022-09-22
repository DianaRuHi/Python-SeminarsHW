# Саьая далекая планета

def find_farthest_orbit(list_of_orbits):
    list_of_planets = list(filter(lambda x: x[0]!=x[1], list_of_orbits))
    planets_orbits = [i[0]*i[1] for i in list_of_planets]
    planet = list_of_planets[planets_orbits.index(max(planets_orbits))] 
    return planet

orbits = [(1, 3), (2.5, 10), (7, 2), (6,6), (4, 3)]
print(*find_farthest_orbit(orbits))

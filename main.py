from cities import Map

# ! Create generator of permutations
# Implementovat mutaciu
# Also save the information about which generation it is

if __name__ == '__main__':

    # Map size x, Map size Y, Number of Cities, Minimal distance between cities
    map = Map(200, 200, 40,20)
    map.start_evolution()
    #map.draw_generations()


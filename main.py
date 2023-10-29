from cities import Map

# ! Create generator of permutations
# Implementovat mutaciu
# Also save the information about which generation it is

if __name__ == '__main__':

    map = Map(200, 200, 10,15)
    map.connect_cities()
    map.draw_map()

    # for i in range(4):
    #
    #     map.connect_cities()
    #     map.draw_map()

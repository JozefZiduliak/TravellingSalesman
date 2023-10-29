import random
import matplotlib.pyplot as plt
from geneticAlgorithm import GeneticAlgorithm
class City:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connected_city = None


class Map:

    def __init__(self, x_size, y_size, number_of_cities,min_distance):
        self.my_x_size = x_size
        self.my_y_size = y_size
        self.my_number_of_cities = number_of_cities
        self.my_cities = []
        self.my_map = []
        self.min_distance = min_distance
        self.__create_map()
        self.genetic_algorithm = GeneticAlgorithm(self.my_cities)

    def __create_map(self):
        # sets all items in 2d list to 0
        self.my_map = [[0] * self.my_x_size for _ in range(self.my_y_size)]

        for i in range(self.my_number_of_cities):

            my_is_taken = True

            # Generates coordinates that have not been taken before by other city
            while(my_is_taken):

                random_x =  random.randint(0,self.my_x_size - 1)
                random_y = random.randint(0,self.my_y_size - 1)

                # Check if they are unique
                if self.my_map[random_y][random_x] != 0:
                    continue

                new_city = City(random_x, random_y)

                # Checks if the condition is met
                if all(self.__distance(new_city, city) > self.min_distance for city in self.my_cities):
                    self.my_map[random_y][random_x] = 1
                    self.my_cities.append(new_city)
                    my_is_taken = False


    def __distance(self, city1, city2):
        return ((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2) ** 0.5

    def connect_cities(self):

        # Connects each city to the city that follows it in the list
        # for i in range(len(self.my_cities) - 1):
        #     self.my_cities[i].connected_city = self.my_cities[i + 1]
        # # The last city is connected to the first to close the loop
        #     self.my_cities[-1].connected_city = self.my_cities[0]
        self.my_cities = self.genetic_algorithm.connect_cities()




    def draw_map(self, route=None):
        x, y = zip(*[(city.x, city.y) for city in self.my_cities])
        plt.figure(figsize=(8, 6))
        plt.scatter(x, y, c='b', marker='o', label='Cities')

        # Draw lines between cities based on their connections
        for city in self.my_cities:
            plt.plot([city.x, city.connected_city.x], [city.y, city.connected_city.y], c='r')

        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.gca().set_aspect('equal')
        plt.legend()
        plt.title("Map of Cities with Connections")
        plt.show()
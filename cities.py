import random
import matplotlib.pyplot as plt
from geneticAlgorithm import GeneticAlgorithm
from geneticAlgorithm import Agent

# Represents city in 2d space
class City:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connected_city = None # Is used to print roads between cities


# Class that creates map and draws it
class Map:

    def __init__(self, x_size, y_size, number_of_cities,min_distance):
        self.my_x_size = x_size # X size of map
        self.my_y_size = y_size # Y size of map
        self.my_number_of_cities = number_of_cities
        self.my_cities = [] # Coordinates of cities in list
        self.my_map = [] # 2d list. Cities are represented with 1 and empty space by 0
        self.min_distance = min_distance # Minimal distance between cities
        self.__create_map()
        # self.number_of_agents_in_generation = 20
        # self.number_of_generations = 10
        self.genetic_algorithm = GeneticAlgorithm(self.my_cities)
        self.current_generation = 0 # Number of current generation
        self.best_agents = None # List of best agent every 50th generations



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


    # Starts the evolution process in GeneticAlgorithm Class
    def start_evolution(self):
        self.best_agents = self.genetic_algorithm.start_evolution()

        #number_of_agents = len(self.best_agents)
        #print(f"Number of agents: {number_of_agents}")
        # Print permutation in each agent
        #print("Cities class")
        #for agent in self.best_agents:
           # print(agent.permutation)
            #print(agent.fitness)

        self.draw_generations()
        self.plot_average_fitness()


    # Connects cities based on permutation in given agent
    def connect_cities(self, agent):
        number_of_cities = len(self.my_cities)
        for i in range(number_of_cities):

            if i != number_of_cities -1:
                self.my_cities[agent.permutation[i]].connected_city = self.my_cities[agent.permutation[i + 1]]
            else:
                self.my_cities[agent.permutation[i]].connected_city = self.my_cities[agent.permutation[0]]

    def draw_generations(self):
        # Change the generation number based on generation later
        #generation = self.generations[0]

        #print("--------------------------------------------------")

        number_of_best_agents = len(self.best_agents)

        #print(f"Number of best agents: {number_of_best_agents}")


        for i in range(number_of_best_agents):
            #current_agent = generation[i]
            current_agent = self.best_agents[i]

            print(f"Agent number: {i}")


            self.connect_cities(current_agent)
            self.draw_map()

            #print(f"{current_agent.permutation}")
            #print(f"Fitness: {current_agent.fitness}")
            #print("--------------------------------------------------")

    def plot_average_fitness(self):

        average_fitness_values = self.genetic_algorithm.get_average_fitness()


        plt.figure(figsize=(10, 5))
        plt.plot(average_fitness_values, marker='o', linestyle='-', color='b')
        plt.title('Average Fitness per Generation')
        plt.xlabel('Generation')
        plt.ylabel('Average Fitness')
        plt.grid(True)
        plt.show()

    def draw_map(self, route=None):
        # Draw cities as blue circles
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

        # Draws the number of generation
        plt.annotate(f'Generation: {self.current_generation}', xy=(0, 0), xycoords='axes fraction',
                     xytext=(-20, -40), textcoords='offset points',
                     horizontalalignment='left', verticalalignment='bottom')

        plt.show()
import random

# Implement mutation
# Implement two different ways of creating children

class Agent:
    def __init__(self, generation_number, permutation, fitness):
        self.generation_number = generation_number
        self.permutation = permutation
        self.fitness = fitness


class GeneticAlgorithm:
    def __init__(self, cities, number_of_agents_in_generation):
        self.my_cities = cities
        self.cities_num = len(self.my_cities)
        self.generation = [] # Represent one generation that will be created in create_generation
        self.generations = []
        self.current_generation = 0
        self.number_of_agents_in_generation = number_of_agents_in_generation

    def __create_permutation(self):
        permutation = []
        # Loop runs as many times as the number of cities
        for i in range(self.cities_num):

            random_number = random.randint(0, self.cities_num - 1)

            # Check if the random number is already in the permutation
            while random_number in permutation:
                # If it is, generate a new random number
                random_number = random.randint(0, self.cities_num - 1)

            # Add the unique random number to the permutation list
            permutation.append(random_number)

        return permutation  # Return the generated permutation

    def create_generation(self):
        # self.generation = []
        permutation = []

        if self.current_generation == 0:

            for i in range(self.number_of_agents_in_generation):
                permutation = self.__create_permutation()
                agent = Agent(self.current_generation, permutation, 0)
                agent.fitness = self.agent_fitness(agent)
                self.generation.append(agent)

        self.generations.append(self.generation)
        return self.generations

    def agent_fitness(self,agent):

        total_distance = 0.0
        permutation = agent.permutation

        # Vypočítanie celkovej vzdialenosti
        for i in range(self.cities_num):
            city1 = self.my_cities[permutation[i]]
            city2 = self.my_cities[permutation[(i + 1) % self.cities_num]]
            distance = self.__distance(city1, city2)
            total_distance += distance

        fitness = 1/total_distance

        return fitness

    # Remake this method later
    def connect_cities(self):

        permutation = self.__create_permutation()

        for i in range(self.cities_num):

            if i != self.cities_num -1:
                self.my_cities[permutation[i]].connected_city = self.my_cities[permutation[i + 1]]
            else:
                self.my_cities[permutation[i]].connected_city = self.my_cities[permutation[0]]

        return self.my_cities

    def __distance(self, city1, city2):
        return ((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2) ** 0.5

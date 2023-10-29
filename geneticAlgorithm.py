import random


class GeneticAlgorithm:
    def __init__(self, cities):
        self.my_cities = cities
        self.cities_num = len(self.my_cities)
        self.__create_permutation()

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

        print(permutation)

        return permutation  # Return the generated permutation

    def connect_cities(self):

        permutation = self.__create_permutation()

        for i in range(self.cities_num):

            if i != self.cities_num -1:
                self.my_cities[permutation[i]].connected_city = self.my_cities[permutation[i + 1]]
            else:
                self.my_cities[permutation[i]].connected_city = self.my_cities[permutation[0]]

        return self.my_cities

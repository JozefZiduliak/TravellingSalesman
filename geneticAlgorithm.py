import random

# Implement mutation
# Implement two different ways of creating children

class Agent:
    def __init__(self, generation_number, permutation, fitness):
        self.generation_number = generation_number
        self.permutation = permutation
        self.fitness = fitness


class GeneticAlgorithm:
    def __init__(self, cities):
        self.my_cities = cities
        self.cities_num = len(self.my_cities)
        self.generation = [] # Represent one generation that will be created in create_generation
        self.best_agent_from_generation = [] # Arrays that stores the best agent every 50 generation
        self.number_of_agents_in_generation = 20
        self.number_of_generations = 1000
        self.save_every_x_generation = 100


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

    def start_evolution(self):

    # Initialize the list that will store the best agent from every 50th generation
        self.best_agent_from_generation = []

        # Create the first generation
        for i in range(self.number_of_agents_in_generation):
            permutation = self.__create_permutation()
            agent = Agent(0, permutation, 0)
            agent.fitness = self.agent_fitness(agent)
            self.generation.append(agent)

        # Assign newly created agent to the best agent from generation for testing

        #self.best_agent_from_generation.append(Agent(0, self.generation[0].permutation, self.generation[0].fitness))

        self.best_agent_from_generation.append(self.find_best_agent(self.generation))

        # Loop through the number of generations
        # I want to specity that this for loop starts at index 1

        for generation_number in range(2, self.number_of_generations + 1):

                # Select parents from the current generation
                #parents = self.choose_parents_roulette(self.generation)
                parents = self.choose_parents_tournament(self.generation)

                # Create children from the selected parents
                children = self.make_children(parents)


                # Loop trought generation and add them to combined_generation
                combined_generation = []
                for agent in self.generation:
                    combined_generation.append(agent)

                for child in children:
                    combined_generation.append(child)

                # Step 5: Sort the combined list based on fitness and select the top 20 agents
                combined_generation.sort(key=lambda x: x.fitness, reverse=True)


                self.generation = []
                #self.generation = combined_generation[:20]
                self.generation = combined_generation[:self.number_of_agents_in_generation]


                if generation_number % self.save_every_x_generation == 0:

                    self.best_agent_from_generation.append(self.find_best_agent(self.generation))

        return self.best_agent_from_generation



    def choose_parents_roulette(self, previous_generation):

        selected_parents = []
        indexes_of_selected_parents = set()  # Using set for faster lookup
        #number_of_parents = 10
        number_of_parents = self.number_of_agents_in_generation/2

        # Calculate the total fitness of the generation
        total_fitness = sum(agent.fitness for agent in previous_generation)

        # Calculate the relative probability for each agent
        probabilities = [agent.fitness / total_fitness for agent in previous_generation]

        # Multiply the probabilities by 100 to get percentages
        agents_percentage_chance = [prob * 100 for prob in probabilities]

        while len(selected_parents) < number_of_parents:

            # Generate a random number between 0 and 100
            roulette = random.randint(0, 100)

            # Initialize a variable to keep track of the sum of percentages
            sum_percent = 0

            # Loop through the agents to find which interval the random number falls into
            for i in range(len(agents_percentage_chance)):
                sum_percent += agents_percentage_chance[i]
                if roulette <= sum_percent:
                    if i in indexes_of_selected_parents:  # Check if this parent is already selected
                        break  # If so, break the inner loop to generate a new random number
                    selected_parents.append(previous_generation[i])
                    indexes_of_selected_parents.add(i)  # Add to set
                    break  # Exit the loop once we've found our chosen agent

        return selected_parents  # Return the chosen parents

    def choose_parents_tournament(self, previous_generation):

        previous_gen_copy = previous_generation.copy()
        selected_parents = []

        while len(previous_gen_copy) > 1:
            # Randomly select two agents
            agent1 = random.choice(previous_gen_copy)
            previous_gen_copy.remove(agent1)

            agent2 = random.choice(previous_gen_copy)
            previous_gen_copy.remove(agent2)

            # Duel them
            if agent1.fitness > agent2.fitness:
                selected_parents.append(agent1)
            else:
                selected_parents.append(agent2)

        return selected_parents

    # Method will go trough every agent in generation and will return the best one
    def find_best_agent(self, generation):
        best_agent = generation[0]

        for agent in generation:
            if agent.fitness > best_agent.fitness:
                best_agent = agent

        return best_agent

    # Add the Fresh blood functionality
    def make_children(self,parents):

        next_generation = []

        parent_generation = parents[0].generation_number

        # Fresh blood probability (in percentage)
        fresh_blood_prob = 15

        for i in range(0, int(self.number_of_agents_in_generation / 2), 2):
        #for i in range(0, int(self.number_of_agents_in_generation), 2):

            if random.randint(1, 100) <= fresh_blood_prob:
                # Generate a new random permutation
                permutation = self.__create_permutation()
                # Create a new agent with the new permutation
                new_parent = Agent(parent_generation, permutation, 0)
                new_parent.fitness = self.agent_fitness(new_parent)
                parent2 = new_parent

            parent1 = parents[i]
            parent2 = parents[i+1]

            # Parent generation
            next_generation.append(self.create_child(parent1, parent2, parent_generation))
            next_generation.append(self.create_child(parent2, parent1, parent_generation))

        #self.generation = next_generation
        return next_generation



    def create_child(self,parent1, parent2, parent_generation):

        permutation_1 = parent1.permutation
        permutation_2 = parent2.permutation

        child_permutation = []

        half_size_of_permutation = len(permutation_1) // 2

        permutation_from_first_parent = []

        # Takes the genetic information from the first parent
        for i in range(half_size_of_permutation):
            child_permutation.append(permutation_1[i])
            permutation_from_first_parent.append(permutation_1[i])

        # Takes the genetic information from the second parent
        permutation_2_mixed = []

        # Mixes the second parent
        for i in range(half_size_of_permutation, len(permutation_2)):
            permutation_2_mixed.append(permutation_2[i])

        # Mixes the second parent
        for i in range(half_size_of_permutation):
            permutation_2_mixed.append(permutation_2[i])

        # Removes the genetic information that is already in the child
        for i in range(len(permutation_2_mixed)):
            if permutation_2_mixed[i] in child_permutation:
                permutation_2_mixed[i] = -1

        # Add all number from permutation 2 mixed to child permutation that are not -1
        for i in range(len(permutation_2_mixed)):
            if permutation_2_mixed[i] != -1:
                child_permutation.append(permutation_2_mixed[i])

        mutation_chance = 20

        # Mutate the child
        if random.randint(1, 100) <= mutation_chance:
            # Generate two random indexes
            index1 = random.randint(0, len(child_permutation) - 1)
            index2 = random.randint(0, len(child_permutation) - 1)

            # Swap the values at the generated indexes
            child_permutation[index1], child_permutation[index2] = child_permutation[index2], child_permutation[index1]

        # Return the new agent
        # Parent generation
        new_child = Agent(parent_generation, child_permutation, 0)
        new_child.fitness = self.agent_fitness(new_child)
        return new_child

    def agent_fitness(self,  agent):

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

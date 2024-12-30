import random

def fitness_function(x, y):
    return x ** 2

population_size = 100
mutation_rate = 0.1
crossover_rate = 0.8
num_generations = 50
variable_bounds = [-10, 10]

def initialize_population(population_size, bounds):
    population = []
    for _ in range(population_size):
        x = random.uniform(bounds[0], bounds[1])
        y = random.uniform(bounds[0], bounds[1])
        population.append([x, y])
    return population

def evaluate_population(population):
    fitness_scores = []
    for individual in population:
        fitness_scores.append(fitness_function(individual[0], individual[1]))
    return fitness_scores

def selection(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    selected_population = []
    for _ in range(len(population)):
        pick = random.uniform(0, total_fitness)
        current = 0
        for individual, score in zip(population, fitness_scores):
            current += score
            if current > pick:
                selected_population.append(individual)
                break
    return selected_population

def crossover(parent1, parent2, crossover_rate):
    if random.random() < crossover_rate:
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
    else:
        child1, child2 = parent1, parent2
    return child1, child2

def mutate(individual, mutation_rate, bounds):
    if random.random() < mutation_rate:
        mutation_position = random.randint(0, len(individual) - 1)
        mutation_value = random.uniform(bounds[0], bounds[1])
        individual[mutation_position] = mutation_value
    return individual

def genetic_algorithm():
    # Display student information at the start
    print("Student Name: Likhith M")
    print("USN: 1BM22CS135")
    print("-" * 40)
    
    population = initialize_population(population_size, variable_bounds)
    overall_best_solution = None
    overall_best_fitness = float('-inf')

    for generation in range(num_generations):
        fitness_scores = evaluate_population(population)

        generation_best_fitness = max(fitness_scores)
        generation_best_solution = population[fitness_scores.index(generation_best_fitness)]

        if generation_best_fitness > overall_best_fitness:
            overall_best_fitness = generation_best_fitness
            overall_best_solution = generation_best_solution

        # Displaying the output for generations that are multiples of 10
        if (generation + 1) % 10 == 0:
            print(f"Generation {generation + 1}:")
            print(f"  Best fitness   = {generation_best_fitness}")
            print(f"  Best solution  = {generation_best_solution}")
            print("-" * 40)

        selected_population = selection(population, fitness_scores)
        next_population = []

        for i in range(0, population_size, 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i + 1]
            child1, child2 = crossover(parent1, parent2, crossover_rate)
            child1 = mutate(child1, mutation_rate, variable_bounds)
            child2 = mutate(child2, mutation_rate, variable_bounds)
            next_population.append(child1)
            next_population.append(child2)

        population = next_population

    print(f"Best solution found after {num_generations} generations: {overall_best_solution}")
    print(f"Best fitness value: {overall_best_fitness}")

genetic_algorithm()

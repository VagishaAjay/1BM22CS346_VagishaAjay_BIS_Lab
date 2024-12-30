import random
import math

# Objective Function
def objective_function(x):
    return sum(xi ** 2 for xi in x)

# Levy Flight Step
def levy_flight(Lambda, dim):
    sigma = (math.gamma(1 + Lambda) * math.sin(math.pi * Lambda / 2) /
             (math.gamma((1 + Lambda) / 2) * Lambda * 2 ** ((Lambda - 1) / 2))) ** (1 / Lambda)
    u = [random.gauss(0, sigma) for _ in range(dim)]
    v = [random.gauss(0, 1) for _ in range(dim)]
    step = [ui / abs(vi) ** (1 / Lambda) for ui, vi in zip(u, v)]
    return step

# Generate New Solution
def generate_new_solution(current_solution, alpha, Lambda, lower_bound, upper_bound):
    step = levy_flight(Lambda, len(current_solution))
    new_solution = [
        max(min(current_solution[i] + alpha * step[i], upper_bound), lower_bound)
        for i in range(len(current_solution))
    ]
    return new_solution

# Initialize Nests
def initialize_nests(n_nests, dim, lower_bound, upper_bound):
    return [[random.uniform(lower_bound, upper_bound) for _ in range(dim)] for _ in range(n_nests)]

# Cuckoo Search Algorithm
def cuckoo_search(objective, n_nests, max_iter, alpha, pa, lower_bound=-10, upper_bound=10, Lambda=1.5):
    nests = initialize_nests(n_nests, 2, lower_bound, upper_bound)
    fitness = [objective(nest) for nest in nests]
    best_nest = min(nests, key=objective)
    best_fitness = objective(best_nest)

    for iteration in range(max_iter):
        random_index = random.randint(0, n_nests - 1)
        cuckoo_solution = generate_new_solution(nests[random_index], alpha, Lambda, lower_bound, upper_bound)
        cuckoo_fitness = objective(cuckoo_solution)

        random_nest_index = random.randint(0, n_nests - 1)
        if cuckoo_fitness < fitness[random_nest_index]:
            nests[random_nest_index] = cuckoo_solution
            fitness[random_nest_index] = cuckoo_fitness

        num_to_abandon = int(pa * n_nests)
        worst_indices = sorted(range(n_nests), key=lambda i: fitness[i], reverse=True)[:num_to_abandon]
        for idx in worst_indices:
            nests[idx] = [random.uniform(lower_bound, upper_bound) for _ in range(2)]
            fitness[idx] = objective(nests[idx])

        current_best_index = min(range(n_nests), key=lambda i: fitness[i])
        if fitness[current_best_index] < best_fitness:
            best_nest = nests[current_best_index]
            best_fitness = fitness[current_best_index]

        # Output every 100 iterations
        if iteration % 100 == 0 or iteration == max_iter - 1:
            print(f"Iteration {iteration}, Best Fitness: {best_fitness:.5f}, Best Solution: {best_nest}")

    return best_nest, best_fitness

# Main Function
if __name__ == "__main__":
    n_nests = 25    # Number of nests
    max_iter = 1000 # Maximum iterations
    alpha = 0.1     # Step size
    pa = 0.25       # Probability of abandoning worse nests

    best_solution, best_value = cuckoo_search(
        objective_function, n_nests=n_nests, max_iter=max_iter, alpha=alpha, pa=pa
    )

    print(f"\nBest solution found: x = {best_solution[0]:.5f}, y = {best_solution[1]:.5f}")
    print(f"Best objective function value: {best_value:.5f}")
 

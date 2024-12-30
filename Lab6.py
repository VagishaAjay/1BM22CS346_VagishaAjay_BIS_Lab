import random

# Objective Function
def objective_function(x):
    return -(x ** 2) + 4 * x

# Initialize Parameters
def initialize_parameters():
    grid_size = 10  # Grid size
    num_iterations = 50  # Number of iterations
    lower_bound, upper_bound = -10, 10  # Bounds for the grid values
    return grid_size, num_iterations, lower_bound, upper_bound

# Initialize Population Grid
def initialize_population(grid_size, lower_bound, upper_bound):
    grid = [[random.uniform(lower_bound, upper_bound) for _ in range(grid_size)] for _ in range(grid_size)]
    return grid

# Evaluate Fitness Grid
def evaluate_fitness(grid):
    fitness_grid = [[objective_function(cell) for cell in row] for row in grid]
    return fitness_grid

# Update Grid States Based on Neighbor Averages
def update_states(grid, fitness_grid):
    grid_size = len(grid)
    updated_grid = [[0] * grid_size for _ in range(grid_size)]

    for i in range(grid_size):
        for j in range(grid_size):
            neighbors = []
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < grid_size and 0 <= nj < grid_size:
                        neighbors.append(grid[ni][nj])

            if neighbors:
                updated_grid[i][j] = sum(neighbors) / len(neighbors)
            else:
                updated_grid[i][j] = grid[i][j]

    return updated_grid

# Print Grid State
def print_grid(grid, label="Grid"):
    print(f"{label}")
    for row in grid:
        print([f"{value: .4f}" for value in row])
    print()

# Parallel Cellular Algorithm
def parallel_cellular_algorithm():
    grid_size, num_iterations, lower_bound, upper_bound = initialize_parameters()
    grid = initialize_population(grid_size, lower_bound, upper_bound)

    print_grid(grid, label="Initial Grid")

    best_solution = None
    best_fitness = float('-inf')

    for iteration in range(num_iterations):
        fitness_grid = evaluate_fitness(grid)

        for i in range(grid_size):
            for j in range(grid_size):
                if fitness_grid[i][j] > best_fitness:
                    best_fitness = fitness_grid[i][j]
                    best_solution = grid[i][j]

        # Output progress at multiples of 10 iterations
        if iteration % 10 == 0 or iteration == num_iterations - 1:
            print(f"Iteration {iteration}: Best Solution = {best_solution:.4f}, Best Fitness = {best_fitness:.4f}")

        grid = update_states(grid, fitness_grid)

    return best_solution, best_fitness

# Main Function
if __name__ == "__main__":
    best_solution, best_fitness = parallel_cellular_algorithm()
    print("\nFinal Results:")
    print(f"Best Solution: {best_solution:.4f}")
    print(f"Best Fitness: {best_fitness:.4f}")

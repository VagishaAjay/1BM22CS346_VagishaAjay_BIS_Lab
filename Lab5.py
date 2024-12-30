import random

# Grey Wolf Optimizer Function
def grey_wolf_optimizer(objective_function, lower_bound, upper_bound, dim, num_wolves, max_iter):

    alpha_pos = [0] * dim
    beta_pos = [0] * dim
    delta_pos = [0] * dim

    alpha_score = float('inf')
    beta_score = float('inf')
    delta_score = float('inf')

    wolves = [[random.uniform(lower_bound, upper_bound) for _ in range(dim)] for _ in range(num_wolves)]

    for iteration in range(max_iter):
        for i in range(num_wolves):
            fitness = objective_function(wolves[i])

            if fitness < alpha_score:
                delta_score, delta_pos = beta_score, beta_pos[:]
                beta_score, beta_pos = alpha_score, alpha_pos[:]
                alpha_score, alpha_pos = fitness, wolves[i][:]
            elif fitness < beta_score:
                delta_score, delta_pos = beta_score, beta_pos[:]
                beta_score, beta_pos = fitness, wolves[i][:]
            elif fitness < delta_score:
                delta_score, delta_pos = fitness, wolves[i][:]

        a = 2 - iteration * (2 / max_iter)
        for i in range(num_wolves):
            for j in range(dim):
                r1 = random.random()
                r2 = random.random()
                A1 = a * (2 * r1 - 1)
                C1 = 2 * r2
                D_alpha = abs(C1 * alpha_pos[j] - wolves[i][j])
                X1 = alpha_pos[j] - A1 * D_alpha

                r1 = random.random()
                r2 = random.random()
                A2 = a * (2 * r1 - 1)
                C2 = 2 * r2
                D_beta = abs(C2 * beta_pos[j] - wolves[i][j])
                X2 = beta_pos[j] - A2 * D_beta

                r1 = random.random()
                r2 = random.random()
                A3 = a * (2 * r1 - 1)
                C3 = 2 * r2
                D_delta = abs(C3 * delta_pos[j] - wolves[i][j])
                X3 = delta_pos[j] - A3 * D_delta

                wolves[i][j] = (X1 + X2 + X3) / 3

                if wolves[i][j] < lower_bound:
                    wolves[i][j] = lower_bound
                elif wolves[i][j] > upper_bound:
                    wolves[i][j] = upper_bound

        # Output every 10 iterations
        if iteration % 10 == 0 or iteration == max_iter - 1:
            print(f"Iteration {iteration}: Best Score = {alpha_score:.5f}, Best Position = {alpha_pos}")

    return alpha_pos, alpha_score

# Sphere Function (Objective Function)
def sphere_function(position):
    return sum(x ** 2 for x in position)

# Problem Parameters
lower_bound = -10
upper_bound = 10
dim = 3
num_wolves = 25
max_iter = 50

# Run Grey Wolf Optimizer
best_position, best_score = grey_wolf_optimizer(sphere_function, lower_bound, upper_bound, dim, num_wolves, max_iter)

# Final Output
print("\nFinal Best Position:", best_position)
print("Final Best Score:", best_score)

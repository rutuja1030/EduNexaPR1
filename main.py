import random

# Define a sample population of schedules.
population_size = 10
num_genes = 5  # Number of genes in a schedule
population = []

for _ in range(population_size):
    schedule = [random.randint(0, 23) for _ in range(num_genes)]  # Assume hours of the day for simplicity
    population.append(schedule)

# Define a fitness function to evaluate schedules.
def fitness(schedule):
    # Your custom fitness function to assess the quality of a schedule.
    # You can consider factors like cargo load, flight duration, time windows, etc.

    # For simplicity, we'll calculate the total hours scheduled.
    return sum(schedule)

# Implement the Genetic Algorithm.

generations = 100
for generation in range(generations):
    # Evaluate the fitness of each schedule in the population.
    fitness_scores = [fitness(schedule) for schedule in population]

    # Select schedules for reproduction based on fitness.
    selected_parents = random.choices(population, weights=fitness_scores, k=population_size)

    # Implement crossover and mutation operations to create a new population.
    new_population = []

    for _ in range(population_size):
        parent1, parent2 = random.sample(selected_parents, 2)
        crossover_point = random.randint(1, num_genes - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        mutation_rate = 0.1  # Adjust as needed
        if random.random() < mutation_rate:
            gene_to_mutate = random.randint(0, num_genes - 1)
            child[gene_to_mutate] = random.randint(0, 23)  # Mutate a gene

        new_population.append(child)

    population = new_population
# Select the best schedule from the final population.
best_schedule = max(population, key=fitness)

print("Best Schedule:",best_schedule)
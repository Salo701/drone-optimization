
import random
from utils import calculate_distance, path_crosses_no_fly_zone

def create_random_route(deliveries):
    route = deliveries[:]
    random.shuffle(route)
    return route

def crossover(route1, route2):
    size = len(route1)
    start, end = sorted(random.sample(range(size), 2))
    middle = route1[start:end]
    rest = [d for d in route2 if d not in middle]
    return rest[:start] + middle + rest[start:]

def mutate(route, mutation_rate=0.1):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

def fitness(route, drone, no_fly_zones):
    total_distance = 0
    current_pos = drone.start_pos
    total_weight = 0
    penalty = 0

    for delivery in route:
        if not drone.can_carry(delivery.weight):
            penalty += 1000  # taşıyamıyorsa ceza
            continue

        dist = calculate_distance(current_pos, delivery.pos)

        if path_crosses_no_fly_zone(current_pos, delivery.pos, no_fly_zones, current_time=0):
            penalty += 500  # uçuşa yasak bölgeye girerse ceza

        total_distance += dist
        current_pos = delivery.pos

    energy_penalty = total_distance * 0.1  # örnek enerji tüketim katsayısı
    return -(total_distance + penalty + energy_penalty)  # maximize için negatif toplam

def genetic_algorithm(deliveries, drone, no_fly_zones, pop_size=50, generations=100, mutation_rate=0.1):
    population = [create_random_route(deliveries) for _ in range(pop_size)]

    for _ in range(generations):
        graded = [(fitness(r, drone, no_fly_zones), r) for r in population]
        graded.sort(reverse=True)
        survivors = [r for _, r in graded[:pop_size // 2]]

        children = []
        while len(children) < pop_size:
            parent1 = random.choice(survivors)
            parent2 = random.choice(survivors)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            children.append(child)

        population = children

    best_route = max(population, key=lambda r: fitness(r, drone, no_fly_zones))
    return best_route

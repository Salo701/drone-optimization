import heapq
from utils import euclidean_distance, in_no_fly_zone

def a_star(start_pos, goal_pos, deliveries, no_fly_zones, drone, current_time=0):
    def heuristic(a, b):
        return euclidean_distance(a, b)

    open_set = []
    heapq.heappush(open_set, (0, start_pos))
    
    came_from = {}
    g_score = {start_pos: 0}
    f_score = {start_pos: heuristic(start_pos, goal_pos)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if euclidean_distance(current, goal_pos) < 1.0:  # hedefe çok yakınsa kabul et
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        # Komşu noktaları üret (8 yönlü hareket)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                neighbor = (current[0] + dx, current[1] + dy)

                # Batarya veya ağırlık limitini aştıysa geçme
                weight = sum(d.weight for d in deliveries)
                if not drone.can_carry(weight):
                    continue

                distance = euclidean_distance(current, neighbor)
                estimated_battery = drone.estimate_battery_consumption(distance, weight)
                if estimated_battery > drone.current_battery:
                    continue

                # No-Fly Zone kontrolü
                if in_no_fly_zone(neighbor, no_fly_zones, current_time):
                    continue

                tentative_g_score = g_score[current] + distance
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal_pos)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # Ulaşım yoksa

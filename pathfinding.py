import heapq
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def a_star(start, goal, no_fly_zones, grid_size=1, max_x=100, max_y=100):
    """
    Basit grid tabanlı A* algoritması
    start, goal: (x,y) tuple
    no_fly_zones: NoFlyZone objeleri listesi
    grid_size: Hareket adım boyutu
    max_x, max_y: Alan sınırları
    """

    def neighbors(node):
        x, y = node
        candidates = [
            (x + grid_size, y), (x - grid_size, y),
            (x, y + grid_size), (x, y - grid_size),
            (x + grid_size, y + grid_size), (x - grid_size, y - grid_size),
            (x + grid_size, y - grid_size), (x - grid_size, y + grid_size)
        ]
        valid = []
        for nx, ny in candidates:
            if 0 <= nx <= max_x and 0 <= ny <= max_y:
                # No-Fly Zone kontrolü
                in_no_fly = any(nfz.is_active(0) and nfz.contains_point((nx, ny)) for nfz in no_fly_zones)
                if not in_no_fly:
                    valid.append((nx, ny))
        return valid

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: euclidean_distance(start, goal)}

    log = []

    while open_set:
        current_f, current = heapq.heappop(open_set)
        log.append(f"Visiting node {current} with f={current_f:.2f}")

        if euclidean_distance(current, goal) < grid_size:
            # Hedefe ulaşıldı
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, log

        for neighbor in neighbors(current):
            tentative_g = g_score[current] + euclidean_distance(current, neighbor)
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + euclidean_distance(neighbor, goal)
                f_score[neighbor] = f
                heapq.heappush(open_set, (f, neighbor))
                log.append(f"Added neighbor {neighbor} with f={f:.2f}")

    return None, log  # Yol bulunamadı

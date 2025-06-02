from utils import calculate_distance, path_crosses_no_fly_zone

def select_best_drone(drones, delivery, current_time, no_fly_zones):
    best_drone = None
    best_score = float('inf')

    for drone in drones:
        if drone.can_carry(delivery.weight) and drone.has_battery_for(delivery, no_fly_zones, current_time):
            dist = calculate_distance(drone.current_pos, delivery.pos)
            # No-fly zone kontrolü
            if path_crosses_no_fly_zone(drone.current_pos, delivery.pos, no_fly_zones, current_time):
                continue
            # Öncelik: mesafe ve batarya durumu (basit skor)
            score = dist / drone.speed
            if score < best_score:
                best_score = score
                best_drone = drone
    return best_drone

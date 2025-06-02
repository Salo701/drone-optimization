def optimize_routes(drones, deliveries):
    # Basit öncelik ve mesafeye göre atama
    deliveries_sorted = sorted(deliveries, key=lambda d: (-d.priority, d.time_window[0]))
    for delivery in deliveries_sorted:
        best_drone = None
        best_dist = float('inf')
        for drone in drones:
            if drone.can_carry(delivery.weight):
                dist = ((drone.current_pos[0] - delivery.pos[0])**2 + (drone.current_pos[1] - delivery.pos[1])**2) ** 0.5
                if dist < best_dist:
                    best_dist = dist
                    best_drone = drone
        if best_drone:
            best_drone.load_package(delivery.weight)
            best_drone.move_to(delivery.pos)
            delivery.assigned = True

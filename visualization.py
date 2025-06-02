import matplotlib.pyplot as plt

def plot_map(drones, deliveries, no_fly_zones, assignments):
    plt.figure(figsize=(12, 8))

    # No-Fly Zone'ları çiz
    for i, zone in enumerate(no_fly_zones):
        xs = [p[0] for p in zone.coordinates] + [zone.coordinates[0][0]]
        ys = [p[1] for p in zone.coordinates] + [zone.coordinates[0][1]]
        plt.fill(xs, ys, color='red', alpha=0.3, label='No-Fly Zone' if i == 0 else "")

    # Droneların başlangıç noktaları
    for i, drone in enumerate(drones):
        plt.scatter(*drone.start_pos, marker='^', color='blue', s=100, label='Drone Başlangıç' if i == 0 else "")
        plt.text(drone.start_pos[0], drone.start_pos[1], f"D{drone.id}", color='blue')

    # Teslimat noktaları
    for i, delivery in enumerate(deliveries):
        plt.scatter(*delivery.pos, marker='o', color='green', s=50, label='Teslimat Noktası' if i == 0 else "")
        plt.text(delivery.pos[0], delivery.pos[1], f"L{delivery.id}", color='green')

    # Atamalar ve rotalar
    for drone_id, delivery_list in assignments.items():
        if drone_id == 'unassigned':
            continue
        drone = next(d for d in drones if d.id == drone_id)
        prev_pos = drone.start_pos
        for delivery in delivery_list:
            plt.plot([prev_pos[0], delivery.pos[0]], [prev_pos[1], delivery.pos[1]], 'k--', alpha=0.5)
            prev_pos = delivery.pos
        # Drone başlangıç noktasına dönüş
        plt.plot([prev_pos[0], drone.start_pos[0]], [prev_pos[1], drone.start_pos[1]], 'k--', alpha=0.5)

    plt.title("Drone Teslimat Haritası")
    plt.xlabel("X Koordinatı")
    plt.ylabel("Y Koordinatı")
    plt.legend()
    plt.grid(True)
    plt.show()

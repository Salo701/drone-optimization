import matplotlib.pyplot as plt

def plot_map(drones, deliveries, no_fly_zones, routes=None):
    plt.figure(figsize=(12, 10))

    # Teslimat noktaları
    for i, delivery in enumerate(deliveries):
        plt.scatter(delivery.pos[0], delivery.pos[1], color='blue', s=50, label='Delivery Point' if i == 0 else "")

    # Drone başlangıç pozisyonları
    for i, drone in enumerate(drones):
        plt.scatter(drone.start_pos[0], drone.start_pos[1], color='green', s=80, label='Drone Start' if i == 0 else "")

    # No-fly zone bölgeleri
    for i, no_fly_zone in enumerate(no_fly_zones):
        coords = no_fly_zone.coordinates + [no_fly_zone.coordinates[0]]
        x, y = zip(*coords)
        plt.fill(x, y, color='red', alpha=0.3, label='No-Fly Zone' if i == 0 else "")

    # Rotaları çiz
    if routes:
        for drone in drones:
            drone_id = drone.id
            if drone_id in routes:
                route = routes[drone_id]
                path = [drone.start_pos]
                for delivery_id in route:
                    delivery_obj = next(d for d in deliveries if d.id == delivery_id)
                    path.append(delivery_obj.pos)
                x_path, y_path = zip(*path)
                plt.plot(x_path, y_path, marker='o', label=f'Drone {drone_id} Route')

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Drone Delivery Map with Routes and No-Fly Zones")
    plt.legend()
    plt.grid(True)
    plt.show()

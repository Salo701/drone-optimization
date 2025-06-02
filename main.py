import time
import matplotlib.pyplot as plt
from classes import Delivery, NoFlyZone
from drone import Drone
from noflyzone import select_best_drone
from optimization import optimize_routes
from utils import calculate_distance

# Senaryo verileri
drones_1 = [
    Drone(1, 4.0, 12000, 8.0, (10, 10)),
    Drone(2, 3.5, 10000, 10.0, (20, 30)),
    Drone(3, 5.0, 15000, 7.0, (50, 50)),
    Drone(4, 2.0, 8000, 12.0, (80, 20)),
    Drone(5, 6.0, 20000, 5.0, (40, 70))
]

deliveries_1 = [
    Delivery(1, (15, 25), 1.5, 3, (0, 60)),
    Delivery(2, (30, 40), 2.0, 5, (0, 30)),
    Delivery(3, (70, 80), 3.0, 2, (20, 80)),
    Delivery(4, (90, 10), 1.0, 4, (10, 40)),
    Delivery(5, (45, 60), 4.0, 1, (30, 90)),
    Delivery(6, (25, 15), 2.5, 3, (0, 50)),
    Delivery(7, (60, 30), 1.0, 5, (5, 25)),
    Delivery(8, (85, 90), 3.5, 2, (40, 100)),
    Delivery(9, (10, 80), 2.0, 4, (15, 45)),
    Delivery(10, (95, 50), 1.5, 3, (0, 60)),
    Delivery(11, (55, 20), 0.5, 5, (0, 20)),
    Delivery(12, (35, 75), 2.0, 1, (50, 120)),
    Delivery(13, (75, 40), 3.0, 3, (10, 50)),
    Delivery(14, (20, 90), 1.5, 4, (30, 70)),
    Delivery(15, (65, 65), 4.5, 2, (25, 75)),
    Delivery(16, (40, 10), 2.0, 5, (0, 30)),
    Delivery(17, (5, 50), 1.0, 3, (15, 55)),
    Delivery(18, (50, 85), 3.0, 1, (60, 100)),
    Delivery(19, (80, 70), 2.5, 4, (20, 60)),
    Delivery(20, (30, 55), 1.5, 2, (40, 80))
]

no_fly_zones_1 = [
    NoFlyZone(1, [(40, 30), (60, 30), (60, 50), (40, 50)], (0, 120)),
    NoFlyZone(2, [(70, 10), (90, 10), (90, 30), (70, 30)], (30, 90))
]

def assign_deliveries(drones, deliveries, no_fly_zones, current_time=0):
    assignments = {}
    for delivery in deliveries:
        drone = select_best_drone(drones, delivery, current_time, no_fly_zones)
        if drone:
            drone.load_package(delivery.weight)
            dist = calculate_distance(drone.current_pos, delivery.pos)
            drone.consume_battery(dist, delivery.weight)
            drone.move_to(delivery.pos)
            assignments[delivery.id] = drone.id
        else:
            assignments[delivery.id] = None
    return assignments

def plot_scenario(drones, deliveries, no_fly_zones, assignments, title):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']
    plt.figure(figsize=(10, 8))

    for zone in no_fly_zones:
        poly_x = [p[0] for p in zone.coordinates] + [zone.coordinates[0][0]]
        poly_y = [p[1] for p in zone.coordinates] + [zone.coordinates[0][1]]
        plt.fill(poly_x, poly_y, color='red', alpha=0.3, label='No-Fly Zone' if zone.id == 1 else "")

    for i, drone in enumerate(drones):
        plt.plot(drone.start_pos[0], drone.start_pos[1], marker='^', markersize=12, color=colors[i % len(colors)], label=f'Drone {drone.id} Start')

    for delivery in deliveries:
        dr_id = assignments.get(delivery.id)
        color = 'gray' if dr_id is None else colors[(dr_id - 1) % len(colors)]
        plt.scatter(delivery.pos[0], delivery.pos[1], c=color, s=60, edgecolors='k')
        plt.text(delivery.pos[0] + 1, delivery.pos[1] + 1, f'D{delivery.id}', fontsize=9)

    plt.title(title)
    plt.xlabel('X (metre)')
    plt.ylabel('Y (metre)')
    plt.legend()
    plt.grid(True)
    plt.show()

def run_scenario():
    print("--- Senaryo 1 (5 Drone, 20 Teslimat, 2 No-Fly Zone) Başlıyor ---")
    start = time.time()
    assignments = assign_deliveries(drones_1, deliveries_1, no_fly_zones_1)
    end = time.time()

    for d_id, dr_id in assignments.items():
        print(f"Teslimat {d_id} -> {'Atanmadı' if dr_id is None else 'Drone ' + str(dr_id)}")

    print(f"Senaryo Süresi: {end - start:.2f} saniye\n")
    plot_scenario(drones_1, deliveries_1, no_fly_zones_1, assignments, "Senaryo 1")

if __name__ == "__main__":
    run_scenario()

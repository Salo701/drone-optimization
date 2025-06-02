import time
import random
from drone import Drone
from delivery import Delivery
from noflyzone import NoFlyZone
from optimization import optimize_routes

def generate_random_drones(num):
    drones = []
    for i in range(1, num + 1):
        drones.append(Drone(
            id=i,
            max_weight=random.uniform(5, 10),
            battery=100.0,
            current_battery=100.0,  # Güncelleme: current_battery ekledim
            speed=random.uniform(20, 40),
            start_pos=(random.uniform(0, 100), random.uniform(0, 100))
        ))
    return drones

def generate_random_deliveries(num):
    deliveries = []
    for i in range(1, num + 1):
        start_time = random.randint(0, 50)
        deliveries.append(Delivery(
            id=i,
            pos=(random.uniform(0, 100), random.uniform(0, 100)),
            weight=random.uniform(0.5, 5),
            priority=random.randint(1, 5),
            time_window=(start_time, start_time + random.randint(10, 50))
        ))
    return deliveries

def generate_random_no_fly_zones(num):
    zones = []
    for i in range(1, num + 1):
        x = random.uniform(20, 80)
        y = random.uniform(20, 80)
        size = random.uniform(5, 15)
        coordinates = [
            (x, y),
            (x + size, y),
            (x + size, y + size),
            (x, y + size)
        ]
        active_start = random.randint(0, 40)
        zones.append(NoFlyZone(
            id=i,
            coordinates=coordinates,
            active_time=(active_start, active_start + random.randint(10, 50))
        ))
    return zones

def run_scenario(num_drones, num_deliveries, num_no_fly_zones):
    print(f"\n--- Senaryo: {num_drones} drone, {num_deliveries} teslimat, {num_no_fly_zones} no-fly zone ---")

    drones = generate_random_drones(num_drones)
    deliveries = generate_random_deliveries(num_deliveries)
    no_fly_zones = generate_random_no_fly_zones(num_no_fly_zones)

    start_time = time.time()
    # optimize_routes güncellemesine göre parametreleri düzenledik
    routes = optimize_routes(drones, deliveries, no_fly_zones, verbose=True, current_time=0)
    duration = time.time() - start_time

    total_deliveries = len(deliveries)
    completed_deliveries = sum(len(route[0]) for route in routes.values())
    delivery_percentage = (completed_deliveries / total_deliveries) * 100 if total_deliveries > 0 else 0

    total_energy = 0
    for drone in drones:
        energy_used = drone.battery - drone.current_battery
        total_energy += energy_used
    average_energy = total_energy / len(drones) if drones else 0

    print(f"Tamamlanan teslimat yüzdesi: %{delivery_percentage:.2f}")
    print(f"Ortalama enerji tüketimi (pil kullanımı): {average_energy:.2f}")
    print(f"Algoritma çalışma süresi: {duration:.2f} saniye")

def main():
    run_scenario(5, 20, 2)
    run_scenario(10, 50, 5)

if __name__ == "__main__":
    main()

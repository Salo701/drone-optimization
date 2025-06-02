class Drone:
    def __init__(self, id, max_payload, battery_capacity, speed, start_pos):
        self.id = id
        self.max_payload = max_payload
        self.battery_capacity = battery_capacity  # Wh
        self.speed = speed  # m/s
        self.start_pos = start_pos
        self.current_pos = start_pos
        self.current_payload = 0.0
        self.battery_left = battery_capacity

    def can_carry(self, weight):
        return (self.current_payload + weight) <= self.max_payload

    def load_package(self, weight):
        if self.can_carry(weight):
            self.current_payload += weight
            return True
        return False

    def move_to(self, pos):
        self.current_pos = pos

    def consume_battery(self, distance, weight):
        # Basit enerji tüketimi modeli (mesafe * ağırlık katsayısı)
        consumption = distance * (1 + weight * 0.1)
        if consumption <= self.battery_left:
            self.battery_left -= consumption
            return True
        return False

    def has_battery_for(self, delivery, no_fly_zones, current_time):
        dist = ((self.current_pos[0] - delivery.pos[0])**2 + (self.current_pos[1] - delivery.pos[1])**2) ** 0.5
        consumption = dist * (1 + delivery.weight * 0.1)
        return self.battery_left >= consumption

class Drone:
    def __init__(self, id, max_weight, battery, speed, start_pos):
        self.id = id
        self.max_weight = max_weight
        self.battery = battery
        self.speed = speed
        self.start_pos = start_pos

class Delivery:
    def __init__(self, id, pos, weight, priority, time_window):
        self.id = id
        self.pos = pos
        self.weight = weight
        self.priority = priority
        self.time_window = time_window

class NoFlyZone:
    def __init__(self, id, coordinates, active_time):
        self.id = id
        self.coordinates = coordinates  # [(x1,y1), (x2,y2), ...]
        self.active_time = active_time  # (start_time, end_time)

    def is_active(self, current_time):
        start, end = self.active_time
        return start <= current_time <= end

    def contains_point(self, point):
        # Basit poligon içi test (Ray casting algoritması)
        x, y = point
        coords = self.coordinates
        n = len(coords)
        inside = False
        p1x, p1y = coords[0]
        for i in range(n+1):
            p2x, p2y = coords[i % n]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x <= max(p1x,p2x):
                        if p1y != p2y:
                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

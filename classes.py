class Delivery:
    def __init__(self, id, pos, weight, priority, time_window):
        self.id = id
        self.pos = pos
        self.weight = weight
        self.priority = priority
        self.time_window = time_window
        self.assigned = False

    def is_within_time_window(self, current_time):
        start, end = self.time_window
        return start <= current_time <= end

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority > other.priority
        else:
            return self.time_window[0] < other.time_window[0]

class NoFlyZone:
    def __init__(self, id, coordinates, active_time):
        self.id = id
        self.coordinates = coordinates  # [(x,y), ...]
        self.active_time = active_time  # (start_time, end_time)

    def is_active(self, current_time):
        start, end = self.active_time
        return start <= current_time <= end

    def contains_point(self, point):
        x, y = point
        n = len(self.coordinates)
        inside = False

        p1x, p1y = self.coordinates[0]
        for i in range(n + 1):
            p2x, p2y = self.coordinates[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside

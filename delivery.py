class Delivery:
    def __init__(self, id, pos, weight, priority, time_window):
        self.id = id
        self.pos = pos  # (x, y)
        self.weight = weight
        self.priority = priority  # 1 (düşük) - 5 (yüksek)
        self.time_window = time_window  # (start_time, end_time) dakika cinsinden
        self.assigned = False

    def is_within_time_window(self, current_time, tolerance=3):
        start, end = self.time_window
        return (start - tolerance) <= current_time <= (end + tolerance)

    def __lt__(self, other):
        # Önceliği yüksek olan önce gelir (5 > 1)
        if self.priority != other.priority:
            return self.priority > other.priority
        else:
            return self.time_window[0] < other.time_window[0]

    def __repr__(self):
        return f"Delivery(id={self.id}, priority={self.priority}, time_window={self.time_window})"

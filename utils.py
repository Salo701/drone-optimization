import math

def calculate_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def path_crosses_no_fly_zone(start_pos, end_pos, no_fly_zones, current_time, step=1):
    x1, y1 = start_pos
    x2, y2 = end_pos
    distance = calculate_distance(start_pos, end_pos)
    steps = max(int(distance // step), 1)

    for i in range(steps + 1):
        x = x1 + (x2 - x1) * i / steps
        y = y1 + (y2 - y1) * i / steps
        for zone in no_fly_zones:
            if zone.is_active(current_time) and zone.contains_point((x, y)):
                return True
    return False

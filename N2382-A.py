class Micro:

    def __init__(self, x, y, count, direction, range):
        self.x = x
        self.y = y
        self.count = count
        self.direction = direction
        self.range = range
        self.dead = False

    def change_direction(self):
        if self.direction == 1:
            self.direction = 2
        elif self.direction == 2:
            self.direction = 1
        elif self.direction == 3:
            self.direction = 4
        elif self.direction == 4:
            self.direction = 3

    def cutting_half_micro(self):
        self.count = self.count // 2
        if self.count == 0:
            self.dead = True

    def move(self):
        if self.direction == 1:
            self.x -= 1
        elif self.direction == 2:
            self.x += 1
        elif self.direction == 3:
            self.y -= 1
        elif self.direction == 4:
            self.y += 1

        if self.x == 0 or self.x == self.range - 1 or self.y == 0 or self.y == self.range - 1:
            self.change_direction()
            self.cutting_half_micro()

        return self.x, self.y


def micro_meeting(micros):
    biggest_count = 0
    biggest_micro = micros[0]
    total_micro = 0

    for micro in micros:
        total_micro += micro.count
        if micro.count > biggest_count:
            biggest_count = micro.count
            biggest_micro = micro

    biggest_micro.count = total_micro

    for micro in micros:
        if micro != biggest_micro:
            micro.dead = True


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    micros = []

    for _ in range(K):
        x, y, count, d = list(map(int, input().split()))
        micro = Micro(x, y, count, d, N)
        micros.append(micro)

    hour = 0
    while hour < M:
        hour += 1

        locations = {}

        for micro in micros:
            if not micro.dead:
                coordinate = micro.move()
                if coordinate in locations:
                    locations[coordinate].append(micro)
                else:
                    locations[coordinate] = [micro]

        for coordinate in locations:
            micro_group = locations[coordinate]
            if len(micro_group) >= 2:
                micro_meeting(micro_group)

    total_count = 0
    for micro in micros:
        if not micro.dead:
            total_count += micro.count

    print("#{} {}".format(tc, total_count))
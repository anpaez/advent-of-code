def file_to_array(file_name):
    with open(file_name, 'r') as f:
        file_arr = [[num for num in line.split(' ')] for line in f]
    return file_arr


class Submarine:
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0

    def move_horizontal(self, times):
        self.horizontal_position += times

    def move_vertical(self, times):
        self.depth += times

    def move(self, command):
        method = command[0]
        times = int(command[1])
        if method == 'forward':
            self.move_horizontal(times)
        else:
            if method == 'up':
                times *= -1
            self.move_vertical(times)

    def print_position(self):
        print("Current position (", self.horizontal_position, ", ", self.depth, "). Result: ", self.horizontal_position * self.depth)


commands = file_to_array('test02.txt')
# Part One
submarine = Submarine()
for current in commands:
    submarine.move(current)
submarine.print_position()


class SubmarineWithAim(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def move_horizontal(self, times):
        self.horizontal_position += times
        self.depth += (times * self.aim)

    def move_vertical(self, times):
        self.aim += times

    def move(self, command):
        method = command[0]
        times = int(command[1])
        if method == 'forward':
            self.move_horizontal(times)
        else:
            if method == 'up':
                times *= -1
            self.move_vertical(times)

    def print_position(self):
        print("Current position (", self.horizontal_position, ", ", self.depth, ", ", self.aim, "). Result: ", self.horizontal_position * self.depth)

# Part Two
submarine = SubmarineWithAim()
for current in commands:
    submarine.move(current)
submarine.print_position()

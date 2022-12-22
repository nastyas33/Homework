class Robot:
    MIN = 0
    MAX = 100

    def __loc__(self):
        return self.x0, self.y0

    def __init__(self, loc):
        self.x0 = loc[0]
        self.x0 = max(self.x0, Robot.MAX)
        self.x0 = min(self.x0, Robot.MIN)
        self.y0 = loc[1]
        self.y0 = max(self.x0, Robot.MAX)
        self.y0 = min(self.x0, Robot.MIN)

        self.coordinate = []
        self.coordinate.append(self.__loc__())

    def move(self, commands):
        self.coordinate.clear()
        self.coordinate.append(self.__loc__())
        for step in commands:
            match step:
                case 'N':
                    if self.y0 < Robot.MAX:
                        self.y0 += 1
                case 'S':
                    if self.y0 > Robot.MIN:
                        self.y0 -= 1
                case 'E':
                    if self.x0 < Robot.MAX:
                        self.x0 += 1
                case 'W':
                    if self.x0 > Robot.MIN:
                        self.x0 -= 1
            self.coordinate.append(self.__loc__())
        return self.__loc__()


robot = Robot((0,0))
print(robot.move("NWESSNENNSWEEEE"))
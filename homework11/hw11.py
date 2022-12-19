class Triangle:
    def __init__(self, side_list):
        self.side_list = side_list

    def is_possible(self):
        self.side_list.sort()
        a = self.side_list[0]
        b = self.side_list[1]
        c = self.side_list[2]

        if a + b > c:
            print("Triangle is possible")
        else:
            print("Triangle is not possible")

triangle1 = Triangle([1, 5, 7])

triangle1.is_possible()

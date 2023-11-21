import matplotlib.pyplot as plt


class Drawer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def add_line(self, line):
        self.draw_line(line)

    def add_triangle(self, triangle):
        self.draw_triangle(triangle)

    def add_rectangle(self, rectangle):
        self.draw_rectangle(rectangle)

    def add_point(self, point):
        self.draw_point(point)

    def draw_line(self, line):
        point_a = line.get_a()
        point_b = line.get_b()

        x_values = [point_a.get_x(), point_b.get_x()]
        y_values = [point_a.get_y(), point_b.get_y()]

        self.ax.plot(x_values, y_values, color='black')

    def draw_point(self, point):
        x = point.get_x()
        y = point.get_y()

        self.ax.plot(x, y, 'o', color='black')

    def draw_triangle(self, triangle):
        point_a = triangle.get_a()
        point_b = triangle.get_b()
        point_c = triangle.get_c()

        x_values = [point_a.get_x(), point_b.get_x(), point_c.get_x(), point_a.get_x()]
        y_values = [point_a.get_y(), point_b.get_y(), point_c.get_y(), point_a.get_y()]

        self.ax.plot(x_values, y_values, color='black')

    def draw_rectangle(self, rectangle):
        point_a = rectangle.get_a()
        point_b = rectangle.get_b()
        point_c = rectangle.get_c()
        point_d = rectangle.get_d()

        x_values = [point_a.get_x(), point_b.get_x(), point_c.get_x(), point_d.get_x(), point_a.get_x()]
        y_values = [point_a.get_y(), point_b.get_y(), point_c.get_y(), point_d.get_y(), point_a.get_y()]

        self.ax.plot(x_values, y_values, color='black')

    def show_plot(self):
        plt.show()



from Builder import Builder
from Draw.Drawer import Drawer

def main():
    text = "ПОЗНАЧИТИ ТОЧКУ R, ДЕ R(3, 2);" \
           "ПРОВЕСТИ ПРЯМУ ЧЕРЕЗ ДВІ ТОЧКИ X, Y, ДЕ X(4,8), Y(9,7);" \
           "ПОБУДУВАТИ ТРИКУТНИК ПО 3 ВЕРШИНАМ X, Y, Z, ДЕ X(2,2) Y(5,7), Z(12,2);" \
           "ПОБУДУВАТИ ЧОТИРИКУТНИК З ЧОТИРМА ВЕРШИНАМИ X, Y, Z, R, ДЕ X(2,6), Y, Z(9,2), R"

    inputs = text.split(';')

    for input in inputs:
        drawer = Drawer()
        builder = Builder(drawer)
        builder.parse_input(input)
        drawer.show_plot()
        print()

if __name__ == "__main__":
    main()



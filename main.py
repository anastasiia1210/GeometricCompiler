from Builder import Builder
from Draw.Drawer import Drawer

#https://lucid.app/lucidchart/4d024d15-e619-4479-9438-c902e45604ae/edit?beaconFlowId=951BC25B42639F40&invitationId=inv_631903ae-62fb-4e84-a670-eb64682b67a1&page=0_0#
#https://lucid.app/lucidchart/ca8e5dbe-c114-4841-b933-5c4702bda257/edit?beaconFlowId=BDA68FDC121C6CF6&invitationId=inv_d04b068c-bc7e-4ccb-ab90-b43686763c83&page=0_0#
def main():
    text = "ПОЗНАЧИТИ ТОЧКУ X, ДЕ X(3, 5);" \
           "ПРОВЕСТИ ПРЯМУ ЧЕРЕЗ ДВІ ТОЧКИ X, Y, ДЕ X(1,3), Y(9,7);" \
           "ПОБУДУВАТИ ТРИКУТНИК ПО 3 ВЕРШИНАМ X, Y, Z, ДЕ X(2,2) Y(5,7), Z(12,2);" \
           "ПОБУДУВАТИ ЧОТИРИКУТНИК З ЧОТИРМА ВЕРШИНАМИ X, Y, Z, K, ДЕ X(2,6), Y(11,8), Z(9,2), K(5,0)"

    inputs = text.split(';')

    for input in inputs:
        drawer = Drawer()
        builder = Builder(drawer)
        builder.parse_input(input)
        drawer.show_plot()
        print()

if __name__ == "__main__":
    main()



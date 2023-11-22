from Draw.Drawer import Drawer
from Analyzer.Lexer import Lexer
from Analyzer.Token import Token
from Models.Line import Line
from Models.Line import Point
from Models.Rectangle import Rectangle
from Models.Triangle import Triangle
from typing import List, Optional
import re


class Builder:
    def __init__(self, drawing_panel):
        self.drawing_panel = drawing_panel

    coordinates = {}

    @staticmethod
    def get_tokens(input_tokens):
        tokens = []

        for token in input_tokens:
            if token.strip() != "":
                tokens.append(Lexer.analyze(token.strip()))

        return tokens

    def parse_input(self, input_str):
        input_tokens = re.split(r'(?=[(){}[\];,])|(?<=[(){}[\];,])|\s+', input_str)
        input_tokens = [token for token in input_tokens if token.strip() != ""]

        input_tokens = self.get_tokens(input_tokens)

        if self.contains_token(input_tokens, "ДЕ"):
            if input_tokens[0] is not None and input_tokens[0].get_type() == Lexer.TypeToken.KEYWORD:
                if input_tokens[1] is not None and input_tokens[1].get_type() == Lexer.TypeToken.IDENTIFIER:
                    data_index = next((i for i, token in enumerate(input_tokens) if token.get_value() == "ДЕ"), -1) + 1
                    identifiers = []
                    pattern = re.compile(r'\b[a-zA-Z]+\b')
                    for i in range(data_index):
                        match = pattern.match(input_tokens[i].get_value())
                        if match:
                            identifiers.append(input_tokens[i])

                    switch_case = input_tokens[1].get_value().rstrip(';')
                    if "ПРЯМ" in switch_case:
                        self.build_line(identifiers, input_tokens[data_index:])
                    elif "ТОЧК" in switch_case:
                        self.build_point(identifiers, input_tokens[data_index:])
                    elif "ТРИКУТНИК" in switch_case:
                        self.build_triangle(identifiers, input_tokens[data_index:])
                    elif "ЧОТИРИКУТНИК" in switch_case:
                        self.build_rect(identifiers, input_tokens[data_index:])
                    elif "ПЕРПЕНДИКУЛЯР" in switch_case:
                        self.build_perpendicular(identifiers, input_tokens[data_index:])
                    else:
                        self.print_error_message("Invalid input data: identifier was not found or not valid")
                else:
                    self.print_error_message("Invalid input data order: second value must be an identifier")
            else:
                self.print_error_message("Invalid input data order: first value must be a keyword")
        else:
            self.print_error_message("Invalid data: input doesn't include body for data init (, \"ДЕ\" part)")

    def build_line(self, identifiers, data):
        data_strings = [token.get_value() for token in data]

        for identifier in identifiers:
            if identifier.get_value() not in data_strings:
                self.print_error_message("Invalid input data: data doesn't include enough information to init objects")
                return

        point_a = None
        point_b = None

        for i, token in enumerate(data):
            key_x = identifiers[0].get_value()
            key_y = identifiers[1].get_value()

            if token.get_type() == Lexer.TypeToken.IDENTIFIER:
                if identifiers[0].get_value() == token.get_value():
                    try:
                        x = int(data[i + 2].get_value())
                        y = int(data[i + 4].get_value())
                        point_a = Point(x, y)
                        self.coordinates[key_x] = point_a
                    except:
                        point_a = self.coordinates[key_x]
                elif identifiers[1].get_value() == token.get_value():
                    try:
                        x = int(data[i + 2].get_value())
                        y = int(data[i + 4].get_value())
                        point_b = Point(x, y)
                        self.coordinates[key_y] = point_b
                    except:
                        point_b = self.coordinates[key_y]

        if point_a is not None and point_b is not None:
            line = Line(point_a, point_b)

            self.drawing_panel.add_line(line)

            print(f"Point {identifiers[0].get_value()}: {point_a}")
            print(f"Point {identifiers[1].get_value()}: {point_b}")
            print(f"Line: {line}")
        else:
            print("Points A and B not found in the token array.")

    def build_point(self, identifiers, data):
        data_strings = [token.get_value() for token in data]

        for identifier in identifiers:
            if identifier.get_value() not in data_strings:
                self.print_error_message("Invalid input data: data doesn't include enough information to init objects")
                return

        point_a = None

        for i, token in enumerate(data):
            key_x = identifiers[0].get_value()

        for token in data:
            if token.get_type() == Lexer.TypeToken.IDENTIFIER:
                try:
                    x = int(data[data.index(token) + 2].get_value())
                    y = int(data[data.index(token) + 4].get_value())
                    point_a = Point(x, y)
                    self.coordinates[key_x] = point_a
                except:
                    point_a = self.coordinates[key_x]
                   # self.coordinates[identifiers[0].get_value()] = point_a

                self.drawing_panel.add_point(point_a)

                print(f"Point {identifiers[0].get_value()}: {point_a}")
                break
        else:
            print("Points were not found in the token array.")

    def build_triangle(self, identifiers, data):
        data_strings = [token.get_value() for token in data]

        for identifier in identifiers:
            if identifier.get_value() not in data_strings:
                self.print_error_message("Invalid input data: data doesn't include enough information to init objects")
                return

        point_a = None
        point_b = None
        point_c = None

        for i, token in enumerate(data):
            key_x = identifiers[0].get_value()
            key_y = identifiers[1].get_value()
            key_z = identifiers[2].get_value()

            if token.get_type() == Lexer.TypeToken.IDENTIFIER:
                if identifiers[0].get_value() == token.get_value():
                    raw_x = data[i + 2].get_value()
                    try:
                        x = int(data[i + 2].get_value())
                        y = int(data[i + 4].get_value())
                        point_a = Point(x, y)
                        self.coordinates[key_x] = point_a
                    except:
                        point_a = self.coordinates[key_x]

                elif identifiers[1].get_value() == token.get_value():
                    try:
                        x = int(data[i + 2].get_value())
                        y = int(data[i + 4].get_value())
                        point_b = Point(x, y)
                        self.coordinates[key_y] = point_b
                    except:
                        point_b = self.coordinates[key_y]

                elif identifiers[2].get_value() == token.get_value():
                    try:
                       x = int(data[i + 2].get_value())
                       y = int(data[i + 4].get_value())
                       point_c = Point(x, y)
                       self.coordinates[key_z] = point_c
                    except:
                        point_c = self.coordinates[key_z]

        if point_a is not None and point_b is not None and point_c is not None:
            triangle = Triangle(point_a, point_b, point_c)

            self.drawing_panel.add_triangle(triangle)

            print(f"Point {identifiers[0].get_value()}: {point_a}")
            print(f"Point {identifiers[1].get_value()}: {point_b}")
            print(f"Point {identifiers[2].get_value()}: {point_c}")
            print(f"Triangle: {triangle}")
        else:
            print("Points were not found in the token array.")

    def build_rect(self, identifiers, data):
        data_strings = [token.get_value() for token in data]

        for identifier in identifiers:
            if identifier.get_value() not in data_strings:
                self.print_error_message("Invalid input data: data doesn't include enough information to init objects")
                return

        point_a = None
        point_b = None
        point_c = None
        point_d = None

        for i, token in enumerate(data):
            key_x = identifiers[0].get_value()
            key_y = identifiers[1].get_value()
            key_z = identifiers[2].get_value()
            key_v = identifiers[3].get_value()

        for i, token in enumerate(data):
            if token.get_type() == Lexer.TypeToken.IDENTIFIER:
                if identifiers[0].get_value() == token.get_value():
                    try:
                       x = int(data[i + 2].get_value())
                       y = int(data[i + 4].get_value())
                       point_a = Point(x, y)
                       self.coordinates[key_x] = point_a
                    except:
                       point_a = self.coordinates[key_x]

                elif identifiers[1].get_value() == token.get_value():
                    try:
                       x = int(data[i + 2].get_value())
                       y = int(data[i + 4].get_value())
                       point_b = Point(x, y)
                       self.coordinates[key_y] = point_b
                    except:
                        point_b = self.coordinates[key_y]
                elif identifiers[2].get_value() == token.get_value():
                    try:
                        x = int(data[i + 2].get_value())
                        y = int(data[i + 4].get_value())
                        point_c = Point(x, y)
                        self.coordinates[key_z] = point_c
                    except:
                        point_c = self.coordinates[key_z]
                elif identifiers[3].get_value() == token.get_value():
                    try:
                        x = int(data[i + 2].get_value())
                        y = int(data[i + 4].get_value())
                        point_d = Point(x, y)
                        self.coordinates[key_v] = point_d
                    except:
                        point_d = self.coordinates[key_v]

        if point_a is not None and point_b is not None and point_c is not None and point_d is not None:
            rect = Rectangle(point_a, point_b, point_c, point_d)

            self.drawing_panel.add_rectangle(rect)

            print(f"Point {identifiers[0].get_value()}: {point_a}")
            print(f"Point {identifiers[1].get_value()}: {point_b}")
            print(f"Point {identifiers[2].get_value()}: {point_c}")
            print(f"Point {identifiers[3].get_value()}: {point_d}")
            print(f"Rectangle: {rect}")
        else:
            print("Points were not found in the token array.")

    def build_perpendicular(self, identifiers, data):
        print("Implement buildPerpendicular function")

    @staticmethod
    def contains_token(array, token):
        return any(token == t.get_value() for t in array)

    @staticmethod
    def print_error_message(error_description):
        print(f"Error occurred while processing input\nReason: {error_description}")

#!/usr/bin/python3
"""
Base Module
"""


import json
import csv


class Base:
    """
    Base class implementation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes a base

        Args:
            id (int): not None, assign the public instance attribute id
        """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        file_name = cls.__name__ + ".json"
        objs = []
        if list_objs is not None:
            for i in list_objs:
                objs.append(cls.to_dictionary(i))
        s = cls.to_json_string(objs)
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(s)
        f.close()

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        eturns a list of instances
        """
        s = ""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r', encoding="utf-8") as f:
                s = f.read()
        except Exception:
            pass
        arr = cls.from_json_string(s)
        instances = []
        for i in arr:
            instances.append(cls.create(**i))
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        saves list of objects to csv file
        """
        file_name = cls.__name__ + ".csv"
        data = []
        for obj in list_objs:
            d = []
            d.append(obj.to_dictionary()["id"])
            if "size" in obj.to_dictionary():
                d.append(obj.to_dictionary()["size"])
            else:
                d.append(obj.to_dictionary()["width"])
                d.append(obj.to_dictionary()["height"])
            d.append(obj.to_dictionary()["x"])
            d.append(obj.to_dictionary()["y"])
            data.append(d)
        with open(file_name, 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """
        loads list of objects from csv file
        """
        file_name = cls.__name__ + ".csv"
        data = []
        with open(file_name, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for a in reader:
                d = {}
                d["id"] = int(a[0])
                if len(a) >= 5:
                    d["width"] = int(a[1])
                    d["height"] = int(a[2])
                    d["x"] = int(a[3])
                    d["y"] = int(a[4])
                else:
                    d["size"] = int(a[1])
                    d["x"] = int(a[2])
                    d["y"] = int(a[3])
                data.append(cls.create(**d))
        return data

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        opens a window and draws all the Rectangles and Squares
        """
        import turtle

        max = 0
        turtle.penup()
        turtle.goto(-200, 0)
        turtle.pendown()
        for rect in list_rectangles:
            if max < rect.height:
                max = rect.height
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)
            turtle.penup()
            turtle.forward(rect.width + 20)
            turtle.pendown()
        turtle.penup()
        turtle.goto(-200, max + 20)
        turtle.pendown()
        for square in list_squares:
            turtle.forward(square.size)
            turtle.left(90)
            turtle.forward(square.size)
            turtle.left(90)
            turtle.forward(square.size)
            turtle.left(90)
            turtle.forward(square.size)
            turtle.left(90)
            turtle.penup()
            turtle.forward(square.size + 20)
            turtle.pendown()
        turtle.done()

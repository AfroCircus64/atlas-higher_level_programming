#!/usr/bin/python3

import unittest

import io

import os

import sys

import tempfile

from models.base import Base

from models.rectangle import Rectangle

from models.square import Square


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._instances.clear()

    def test_base_init(self):
        b = Base()
        self.assertIsNotNone(b.id)
        self.assertEqual(len(Base._instances), 1)

    def test_base_passed_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)
        self.assertEqual(len(Base._instances), 1)

    def test_base_to_json(self):
        result = Base.to_json_string(None)
        self.assertIsNone(result)

    def test_base_to_empty_json(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_base_to_json_object(self):
        obj = {'id': 12}
        result = Base.to_json_string([obj])
        expected = '[{"id": 12}]'
        self.assertEqual(result, expected)

    def test_base_from_json(self):
        result = Base.from_json_string(None)
        self.assertIsNone(result)

    def test_base_from_empty_json(self):
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_base_from_json_object(self):
        obj = '[{"id": 89}]'
        result = Base.from_json_string(obj)
        expected = Base(id=89)
        self.assertEqual(type(result[0]), type(expected))
        self.assertEqual(result[0].id, expected.id)

    # Add other Base tests here


class TestRectangle(TestBase):
    def setUp(self):
        Base._instances.clear()

    def test_rectangle_init(self):
        r = Rectangle(width=1, height=2)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_all_parameters(self):
        r = Rectangle(width=1, height=2, x=3, y=4)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_area(self):
        r = Rectangle(width=1, height=2)
        self.assertEqual(r.area(), 2)

    def test_rectangle_display_noxy(self):
        r = Rectangle(width=1, height=2)
        r.display()

    def test_rectangle_update(self):
        r = Rectangle(width=1, height=2, x=3, y=4)
        r.update(x=5, y=6)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_rectangle_str(self):
        r = Rectangle(width=4, height=3, x=2, y=1)
        expected_str = "Rectangle(4, 3, 2, 1)"
        self.assertEqual(str(r), expected_str)

    def test_rectangle_display_without_xy(self):
        r = Rectangle(width=3, height=2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        expected_output = "Displaying rectangle with width=3, height=2, x=0, y=0\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_rectangle_display_without_y(self):
        r = Rectangle(width=3, height=2, x=1)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        expected_output = "Displaying rectangle with width=3, height=2, x=1, y=0\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_rectangle_to_dictionary(self):
        r = Rectangle(width=4, height=3, x=2, y=1)
        r_dict = r.to_dictionary()
        expected_dict = {'id': r.id, 'width': 4, 'height': 3, 'x': 2, 'y': 1}
        self.assertEqual(r_dict, expected_dict)

    def test_rectangle_create_with_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_rectangle_create_with_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_rectangle_create_with_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_create_with_x(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_rectangle_create_with_y(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open('rectangles.json', 'r') as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_rectangle_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open('rectangles.json', 'r') as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_rectangle_save_to_file_objects(self):
        r = Rectangle(width=1, height=2)
        Rectangle.save_to_file([r])
        with open('rectangles.json', 'r') as f:
            content = f.read()
        self.assertIn('"id"', content)
        self.assertIn('"width"', content)
        self.assertIn('"height"', content)

    """def test_rectangle_load_from_file_not_exists(self):
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 0)"""

    def test_rectangle_load_from_file_not_exists(self):
        temp_file_path = tempfile.mktemp()
        r = Rectangle(width=1, height=2)
        Rectangle.save_to_file([r], filename=temp_file_path)
        os.remove(temp_file_path)
        rects = Rectangle.load_from_file(filename=temp_file_path)
        self.assertEqual(len(rects), 0)

    def test_rectangle_load_from_file_exists(self):
        r = Rectangle(width=1, height=2)
        Rectangle.save_to_file([r])
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 1)
        self.assertEqual(rects[0].width, 1)
        self.assertEqual(rects[0].height, 2)

    # Add other Rectangle tests here

class TestSquare(TestRectangle):  # Inherits from TestRectangle to reuse tests
    def setUp(self):
        Base._instances.clear()

    def test_square_init(self):
        s = Square(size=1)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 1)

    def test_square_init_all_parameters(self):
        s = Square(size=1, x=2, y=3)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_updates(self):
        s = Square(size=1, x=2, y=3)
        s.update(size=5, x=6, y=7)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 7)

if __name__ == "__main__":
    unittest.main()

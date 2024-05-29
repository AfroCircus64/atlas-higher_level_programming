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
    """base test class"""
    def setUp(self):
        """setup"""
        Base._instances.clear()

    def test_base_init(self):
        """test init of base"""
        b = Base()
        self.assertIsNotNone(b.id)
        self.assertEqual(len(Base._instances), 1)

    def test_base_passed_id(self):
        """passed id test"""
        b = Base(89)
        self.assertEqual(b.id, 89)
        self.assertEqual(len(Base._instances), 1)

    def test_base_to_json(self):
        """base to json test"""
        result = Base.to_json_string(None)
        self.assertIsNone(result)

    def test_base_to_empty_json(self):
        """base to empty test"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_base_to_json_object(self):
        """base to obj test"""
        obj = {'id': 12}
        result = Base.to_json_string([obj])
        expected = '[{"id": 12}]'
        self.assertEqual(result, expected)

    def test_base_from_json(self):
        """base from json test"""
        result = Base.from_json_string(None)
        self.assertIsNone(result)

    def test_base_from_empty_json(self):
        """base from empty test"""
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_base_from_json_object(self):
        """base from object test"""
        obj = '[{"id": 89}]'
        result = Base.from_json_string(obj)
        expected = Base(id=89)
        self.assertEqual(type(result[0]), type(expected))
        self.assertEqual(result[0].id, expected.id)

    # Add other Base tests here


class TestRectangle(TestBase):
    """test rectangle class"""
    def setUp(self):
        Base._instances.clear()

    def test_rectangle_init(self):
        """rect init test"""
        r = Rectangle(width=1, height=2)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_all_parameters(self):
        """rect all parameters test"""
        r = Rectangle(width=1, height=2, x=3, y=4)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_area(self):
        """area of rect test"""
        r = Rectangle(width=1, height=2)
        self.assertEqual(r.area(), 2)

    def test_rectangle_display_noxy(self):
        """rect display test"""
        r = Rectangle(width=1, height=2)
        r.display()

    def test_rectangle_update(self):
        """rect update test"""
        r = Rectangle(width=1, height=2, x=3, y=4)
        r.update(x=5, y=6)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_rectangle_str(self):
        """rect string test"""
        r = Rectangle(width=4, height=3, x=2, y=1)
        expected_str = "Rectangle(4, 3, 2, 1)"
        self.assertEqual(str(r), expected_str)

    def test_rectangle_display_without_xy(self):
        """rect display w/o xy test"""
        r = Rectangle(width=3, height=2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        expected_output = "Displaying rectangle with width=3, height=2, x=0, y=0\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_rectangle_display_without_y(self):
        """rect display w/o y test"""
        r = Rectangle(width=3, height=2, x=1)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        expected_output = "Displaying rectangle with width=3, height=2, x=1, y=0\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_rectangle_to_dictionary(self):
        """rect to dictionary test"""
        r = Rectangle(width=4, height=3, x=2, y=1)
        r_dict = r.to_dictionary()
        expected_dict = {'id': r.id, 'width': 4, 'height': 3, 'x': 2, 'y': 1}
        self.assertEqual(r_dict, expected_dict)

    def test_rectangle_create_with_id(self):
        """rect create with id test"""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_rectangle_create_with_width(self):
        """rect create with width test"""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_rectangle_create_with_height(self):
        """rect create with height test"""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_create_with_x(self):
        """rect create with x test"""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_rectangle_create_with_y(self):
        """rect create with y test"""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_save_to_file_none(self):
        """rect STF none test"""
        Rectangle.save_to_file(None)
        with open('rectangles.json', 'r') as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_rectangle_save_to_file_empty_list(self):
        """rect STF empty list test"""
        Rectangle.save_to_file([])
        with open('rectangles.json', 'r') as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_rectangle_save_to_file_objects(self):
        """rect STF objects test"""
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
        """rect LFF doesnt exist test"""
        temp_file_path = tempfile.mktemp()
        r = Rectangle(width=1, height=2)
        Rectangle.save_to_file([r], filename=temp_file_path)
        os.remove(temp_file_path)
        rects = Rectangle.load_from_file(filename=temp_file_path)
        self.assertEqual(len(rects), 0)

    def test_rectangle_load_from_file_exists(self):
        """rect LFF exists test"""
        r = Rectangle(width=1, height=2)
        Rectangle.save_to_file([r])
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 1)
        self.assertEqual(rects[0].width, 1)
        self.assertEqual(rects[0].height, 2)

    # Add other Rectangle tests here

class TestSquare(TestRectangle):  # Inherits from TestRectangle to reuse tests
    """test square class"""
    def setUp(self):
        """setup"""
        Base._instances.clear()

    def test_square_init(self):
        """square init test"""
        s = Square(size=1)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 1)

    def test_square_init_all_parameters(self):
        """square all params test"""
        s = Square(size=1, x=2, y=3)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_updates(self):
        """square update test"""
        s = Square(size=1, x=2, y=3)
        s.update(size=5, x=6, y=7)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 7)

    def test_square_str(self):
        """square string test"""
        s = Square(size=4)
        expected_str = "Square(4, 0, 0, 0)"
        self.assertEqual(str(s), expected_str)

    def test_square_to_dictionary(self):
        """sqaure to dict test"""
        s = Square(size=4)
        s_dict = s.to_dictionary()
        expected_dict = {'id': s.id, 'size': 4, 'x': 0, 'y': 0}
        self.assertEqual(s_dict, expected_dict)

    def test_square_create_id_only(self):
        """square create id test"""
        s = Square.create(id=89)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)

    def test_square_create_id_size(self):
        """square create id, size test"""
        s = Square.create(id=89, size=1)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_square_create_id_size_x(self):
        """square crate id, size, x test"""
        s = Square.create(id=89, size=1, x=2)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_square_create_id_size_x_y(self):
        """square create id, size, x, y test"""
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_save_to_file_none(self):
        """square STF none test"""
        Square.save_to_file(None)
        with open('squares.json', 'r') as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_square_save_to_file_empty_list(self):
        """square STF empty list test"""
        Square.save_to_file([])
        with open('squares.json', 'r') as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_square_save_to_file_objects(self):
        """square STF objects test"""
        s = Square(size=1)
        Square.save_to_file([s])
        with open('squares.json', 'r') as f:
            content = f.read()
        self.assertIn('"id"', content)
        self.assertIn('"size"', content)

    def test_square_load_from_file_not_exists(self):
        """square LFF doesnt exist test"""
        temp_file_path = tempfile.mktemp()
        squares = Square.load_from_file(filename=temp_file_path)
        self.assertEqual(len(squares), 0)

    def test_square_load_from_file_exists(self):
        """square LFF exists test"""
        s = Square(size=1)
        Square.save_to_file([s])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0].size, 1)

if __name__ == "__main__":
    unittest.main()

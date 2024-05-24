#!/usr/bin/python3

import unittest

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
        expected = {'id': 89}
        self.assertEqual(result, expected)

    # Add other Base tests here


class TestRectangle(TestBase):
    def setUp(self):
        Base._instances.clear()

    def test_rectangle_init(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_all_parameters(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_area(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)

    def test_rectangle_display_noxy(self):
        r = Rectangle(1, 2)
        r.display()

    def test_rectangle_update(self):
        r = Rectangle(1, 2, 3, 4)
        r.update(x=5, y=6)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    # Add other Rectangle tests here


class TestSquare(TestRectangle):  # Inherits from TestRectangle to reuse tests
    def setUp(self):
        Base._instances.clear()

    def test_square_init(self):
        s = Square(1)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 1)

    def test_square_init_all_parameters(self):
        s = Square(1, 2, 3, 4)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_updates(self):
        s = Square(1, 2, 3, 4)
        s.update(size=5, x=6, y=7)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 7)

if __name__ == "__main__":
    unittest.main()

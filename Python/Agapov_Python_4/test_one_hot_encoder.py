from one_hot_encoder import fit_transform
import unittest
import pytest


class TestFitTransform(unittest.TestCase):
    def test_cities(self):
        actual = fit_transform([
            'Moscow', 'New York', 'Moscow', 'London'
            ])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
            ]
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        self.assertEqual(fit_transform(''), [('', [1])])

    def test_wrong_value(self):
        cities = ['Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 1]),
            ('London', [2, 0]),
            ]

        with self.assertRaises(AssertionError):
            self.assertEqual(fit_transform(cities),
                             exp_transformed_cities)


def test_hello_world():
    assert fit_transform('hello') == [('hello', [1])]


def test_int():
    list_int = [1, 2, 3, 1]
    transformed_list = [
        (1, [0, 0, 1]),
        (2, [0, 1, 0]),
        (3, [1, 0, 0]),
        (1, [0, 0, 1])
    ]
    assert fit_transform(list_int) ==  transformed_list


def test_empty():
    assert fit_transform('') == [('', [1])]


def test_wrong_value():
    cities = ['Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 1]),
        ('London', [2, 0]),
        ]

    with pytest.raises(AssertionError):
        assert fit_transform(cities) == exp_transformed_cities

from unittest import TestCase

from app.mergesort.merge_sort_with_function_annotation import merge


class TestMergeSortWithFunctionAnnotation(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_merge_1(self):
        expected = [27, 38]
        actual = [38, 27]
        merge(actual, 0, 0, 1)
        self.assertListEqual(expected, actual)

    def test_merge_2(self):
        expected = [27]
        actual = [27]
        merge(actual, 0, 0, 0)
        self.assertListEqual(expected, actual)

    def test_merge_3(self):
        expected = [3, 27, 38, 43]
        actual = [27, 38, 3, 43]
        merge(actual, 0, 1, 3)
        self.assertListEqual(expected, actual)

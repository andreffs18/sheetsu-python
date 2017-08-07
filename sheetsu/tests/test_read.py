from unittest import TestCase

from sheetsu import SheetsuClient


class SheetsuApiReadTestCase(TestCase):
    """"""

    def setUp(self):
        pass

    def test_simple_read(self):
        """Ensure that simple READ of a spreadsheet using Sheetsu API
        works properly"""
        client = SheetsuClient("0eec897c6d55")
        response = client.read()

        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'},
            {'id': '3', 'name': 'Meg', 'score': '10'},
            {'id': '4', 'name': 'Chris', 'score': '42'},
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ])

    def test_read_with_limit_parameter(self):
        """Ensure that READing works if limit parameter is given"""
        client = SheetsuClient("0eec897c6d55")
        # test with an invalid values
        for invalid_value in [-1, 0]:
            response = client.read(limit=invalid_value)
            self.assertEqual(response, [
                {'id': '1', 'name': 'Peter', 'score': '42'},
                {'id': '2', 'name': 'Lois', 'score': '89'},
                {'id': '3', 'name': 'Meg', 'score': '10'},
                {'id': '4', 'name': 'Chris', 'score': '42'},
                {'id': '5', 'name': 'Stewie', 'score': '72'}
            ])
        # test with value under the total amount of rows
        response = client.read(limit=2)
        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'}
        ])
        # test with value above the total amount of rows
        response = client.read(limit=10)
        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'},
            {'id': '3', 'name': 'Meg', 'score': '10'},
            {'id': '4', 'name': 'Chris', 'score': '42'},
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ])

    def test_read_with_sheet_parameter(self):
        """Ensure that READing works if sheet parameter is given"""
        client = SheetsuClient("0eec897c6d55")
        response = client.read(sheet="Sheet1")
        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'},
            {'id': '3', 'name': 'Meg', 'score': '10'},
            {'id': '4', 'name': 'Chris', 'score': '42'},
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ])

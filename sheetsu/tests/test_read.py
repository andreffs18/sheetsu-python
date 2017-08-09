import json

from unittest import TestCase
from unittest.mock import MagicMock, patch

from sheetsu import SheetsuClient


class SheetsuApiReadTestCase(TestCase):
    """"""

    def setUp(self):
        super(SheetsuApiReadTestCase, self).setUp()
        self.kwargs = {
            "spreadsheet_id": "<spreadsheet_id>",
            "api_key": "<api_key>",
            "api_secret": "<api_secret>"
        }

    @patch("requests.sessions.Session.request")
    def test_read_fail(self, mock):
        """Ensure that if request fails, that proper response is given"""
        mock.return_value = MagicMock(status_code=400)

        client = SheetsuClient(**self.kwargs)
        response = client.read()
        self.assertIsNone(response)

    @patch("requests.sessions.Session.request")
    def test_simple_read(self, mock):
        """Ensure that simple READ of a spreadsheet using Sheetsu API
        works properly"""
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'},
            {'id': '3', 'name': 'Meg', 'score': '10'},
            {'id': '4', 'name': 'Chris', 'score': '42'},
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ]))

        client = SheetsuClient(**self.kwargs)
        response = client.read()

        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'},
            {'id': '3', 'name': 'Meg', 'score': '10'},
            {'id': '4', 'name': 'Chris', 'score': '42'},
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ])

    @patch("requests.sessions.Session.request")
    def test_read_with_negative_or_zero_limit_parameter(self, mock):
        """Ensure that READing works if limit is negative or zero"""
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'},
            {'id': '3', 'name': 'Meg', 'score': '10'},
            {'id': '4', 'name': 'Chris', 'score': '42'},
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ]))

        client = SheetsuClient(**self.kwargs)
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

    @patch("requests.sessions.Session.request")
    def test_read_with_limit_parameter(self, mock):
        """Ensure that READing works if limit is given"""
        client = SheetsuClient(**self.kwargs)

        # test with value under the total amount of rows
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'},
        ]))
        response = client.read(limit=2)
        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'}
        ])

        # test with value above the total amount of rows
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'},
            {'id': '3', 'name': 'Meg', 'score': '10'},
            {'id': '4', 'name': 'Chris', 'score': '42'},
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ]))
        response = client.read(limit=10)
        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'},
            {'id': '3', 'name': 'Meg', 'score': '10'},
            {'id': '4', 'name': 'Chris', 'score': '42'},
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ])

    @patch("requests.sessions.Session.request")
    def test_read_with_sheet_parameter(self, mock):
        """Ensure that READing works if sheet parameter is given"""
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'},
            {'id': '3', 'name': 'Meg', 'score': '10'},
            {'id': '4', 'name': 'Chris', 'score': '42'},
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ]))

        client = SheetsuClient(**self.kwargs)
        response = client.read(sheet="Sheet1")
        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'},
            {'id': '3', 'name': 'Meg', 'score': '10'},
            {'id': '4', 'name': 'Chris', 'score': '42'},
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ])

    @patch("requests.sessions.Session.request")
    def test_read_with_offset_parameter(self, mock):
        """Ensure that READing works if offset parameter is given"""
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '3', 'name': 'Meg', 'score': '10'},
            {'id': '4', 'name': 'Chris', 'score': '42'},
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ]))

        client = SheetsuClient(**self.kwargs)
        response = client.read(offset=2)
        self.assertEqual(response, [
            {'id': '3', 'name': 'Meg', 'score': '10'},
            {'id': '4', 'name': 'Chris', 'score': '42'},
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ])

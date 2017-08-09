import json

from unittest import TestCase
from unittest.mock import MagicMock, patch

from sheetsu import SheetsuClient


class SheetsuApiCreateTestCase(TestCase):
    """"""

    def setUp(self):
        super(SheetsuApiCreateTestCase, self).setUp()
        self.kwargs = {
            "spreadsheet_id": "<spreadsheet_id>",
            "api_key": "<api_key>",
            "api_secret": "<api_secret>"
        }

    @patch("requests.sessions.Session.request")
    def test_create_one_or_many_fail(self, mock):
        """Ensure that if request fails, that proper response is given"""
        mock.return_value = MagicMock(status_code=400)

        client = SheetsuClient(**self.kwargs)
        response = client.create_one()
        self.assertIsNone(response)
        response = client.create_many()
        self.assertIsNone(response)

    @patch("requests.sessions.Session.request")
    def test_simple_create_one(self, mock):
        """Ensure that simple CREATE one method will add a new row to our
        existing a spreadsheet"""
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'}
        ]))

        client = SheetsuClient(**self.kwargs)
        response = client.create_one(id=2, name="Lois", score=89)

        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'}
        ])

    @patch("requests.sessions.Session.request")
    def test_simple_create_many(self, mock):
        """Ensure that simple CREATE many method will add a new row to our
        existing a spreadsheet"""
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'}
        ]))

        client = SheetsuClient(**self.kwargs)
        response = client.create_many(*[
            dict(id=1, name="Peter", score=42),
            dict(id=2, name="Louis", score=89)
        ])

        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'}
        ])

    @patch("requests.sessions.Session.request")
    def test_simple_create_one_different_sheet(self, mock):
        """Ensure that simple CREATE one method will add a new row to our
        specified sheet"""
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '1', 'name': 'Peter', 'score': '42'},
        ]))

        client = SheetsuClient(**self.kwargs)
        response = client.create_one(sheet="Sheet2", id=1, name="Peter",
                                     score=42)

        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '42'},
        ])

    @patch("requests.sessions.Session.request")
    def test_simple_create_many_different_sheet(self, mock):
        """Ensure that simple CREATE many method will add a new row to our
        specified sheet"""
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'}
        ]))

        client = SheetsuClient(**self.kwargs)
        response = client.create_many(sheet="Sheet2", *[
            dict(id=1, name="Peter", score=42),
            dict(id=2, name="Louis", score=89)
        ])

        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '42'},
            {'id': '2', 'name': 'Lois', 'score': '89'}
        ])

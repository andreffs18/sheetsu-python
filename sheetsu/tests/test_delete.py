import json

from unittest import TestCase
from unittest.mock import MagicMock, patch

from sheetsu import SheetsuClient
from sheetsu.exceptions import UnexpectedResponseCode

class SheetsuApiDeleteTestCase(TestCase):
    """"""

    def setUp(self):
        super(SheetsuApiDeleteTestCase, self).setUp()
        self.kwargs = {
            "spreadsheet_id": "<spreadsheet_id>",
            "api_key": "<api_key>",
            "api_secret": "<api_secret>"
        }

    @patch("requests.sessions.Session.request")
    def test_delete_clear_success(self, mock):
        """Ensure that DELETE works properly in "clear" mode"""
        mock.return_value = MagicMock(status_code=204)
        
        client = SheetsuClient(**self.kwargs)
        response = client.delete(column="name", value="Meg")
        self.assertIsNone(response)

    @patch("requests.sessions.Session.request")
    def test_delete_clear_with_sheet_success(self, mock):
        """Ensure that DELETE works properly in "clear" mode"""
        mock.return_value = MagicMock(status_code=204)
        
        client = SheetsuClient(**self.kwargs)
        response = client.delete(sheet="Sheet1", column="name", value="Meg")
        self.assertIsNone(response)

    @patch("requests.sessions.Session.request")
    def test_delete_destroy_with_sheet_success(self, mock):
        """Ensure that DELETE works properly in "destroy" mode"""
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ]))

        client = SheetsuClient(**self.kwargs)
        response = client.delete(column="name", value="Meg", destroy="true")
        self.assertEqual(response, [
            {'id': '5', 'name': 'Stewie', 'score': '72'}
        ])

    @patch("requests.sessions.Session.request")
    def test_delete_destroy_invalid_with_sheet_success(self, mock):
        """Ensure that DELETE works properly with bad "destroy" parameter"""
        mock.return_value = MagicMock(status_code=204)

        client = SheetsuClient(**self.kwargs)
        response = client.delete(sheet="Sheet1", column="name", value="Meg", destroy="invalid")
        self.assertIsNone(response)

    @patch("requests.sessions.Session.request")
    def test_delete_clear_with_bad_response_fail(self, mock):
        """Ensure that DELETE in clear-mode raises an exception when it doesn't get a 204"""
        mock.return_value = MagicMock(status_code=205)

        client = SheetsuClient(**self.kwargs)
        with self.assertRaises(UnexpectedResponseCode):
            response = client.delete(sheet="Sheet1", column="name", value="Meg")


    

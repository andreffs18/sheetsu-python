import json

from unittest import TestCase
from unittest.mock import MagicMock, patch

from sheetsu import SheetsuClient


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
    def test_delete_success(self, mock):
        """Ensure that DELETE works properlly """
        mock.return_value = MagicMock(status_code=204)
        
        client = SheetsuClient(**self.kwargs)
        response = client.delete(column="name", value="Meg")
        self.assertIsNone(response)

    @patch("requests.sessions.Session.request")
    def test_delete_with_sheet_success(self, mock):
        """Ensure that DELETE works properlly """
        mock.return_value = MagicMock(status_code=204)

        client = SheetsuClient(**self.kwargs)
        response = client.delete(sheet="Sheet1", column="name", value="Meg")
        self.assertIsNone(response)


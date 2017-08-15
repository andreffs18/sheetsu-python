import json

from unittest import TestCase
from unittest.mock import MagicMock, patch

from sheetsu import SheetsuClient


class SheetsuApiSearchTestCase(TestCase):
    """"""

    def setUp(self):
        super(SheetsuApiSearchTestCase, self).setUp()
        self.kwargs = {
            "spreadsheet_id": "<spreadsheet_id>",
            "api_key": "<api_key>",
            "api_secret": "<api_secret>"
        }

    @patch("requests.sessions.Session.request")
    def test_search_success(self, mock):
        """Ensure that DELETE works properlly """
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '1', 'name': 'Peter', 'score': '123'}
        ]))

        client = SheetsuClient(**self.kwargs)
        response = client.search(sheet="Sheet", limit=1, offset=1,
                                 ignore_case=True, name="peter")
        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '123'}
        ])

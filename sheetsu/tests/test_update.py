import json

from unittest import TestCase
from unittest.mock import MagicMock, patch

from sheetsu import SheetsuClient


class SheetsuApiUpdateTestCase(TestCase):
    """"""

    def setUp(self):
        super(SheetsuApiUpdateTestCase, self).setUp()
        self.kwargs = {
            "spreadsheet_id": "<spreadsheet_id>",
            "api_key": "<api_key>",
            "api_secret": "<api_secret>"
        }

    @patch("requests.sessions.Session.request")
    def test_update_success(self, mock):
        """Ensure that DELETE works properlly """
        mock.return_value = MagicMock(status_code=200, content=json.dumps([
            {'id': '1', 'name': 'Peter', 'score': '99'}
        ]))

        client = SheetsuClient(**self.kwargs)
        response = client.update(sheet="Sheet1", column="name", value="Peter",
                                 data={"score": 99})
        self.assertEqual(response, [
            {'id': '1', 'name': 'Peter', 'score': '99'}
        ])

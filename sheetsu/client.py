import json
import logging
import requests
from .exceptions import UnknownRequestMethod

logger = logging.getLogger(__name__)


class SheetsuClient(object):

    def __init__(self, spreadsheet_id, **kwargs):
        self.sheetsu_api_url = "https://sheetsu.com/apis/v1.0/"
        self.ss_id = spreadsheet_id

    def _call(self, url, method="get", data=None):
        """Wrapper around requests
        :param url: end url to concatenate with Sheetsu API url
        :param method: one of the following options:
        :param data: optional, only for 'post' and 'put'
        :return: requests instance"""

        url = "{}{}".format(self.sheetsu_api_url, url)

        if method == 'get':
            func = requests.get
        elif method == 'post':
            func = requests.post
        elif method == 'put':
            func = requests.put
        elif method == 'delete':
            func = requests.delete
        else:
            raise UnknownRequestMethod("Method: {}".format(method))

        kwargs = {'data': data}

        r = func(url, **kwargs)

        logger.debug("--{} ({})-- {} with data {}"
                     "".format(method.upper(), r.status_code, url, data))
        if r.status_code not in [200]:
            logger.error("Error({}): {} for url {}"
                         "".format(r.status_code, r.text, url))
            return

        return json.loads(r.content)

    def read(self, **kwargs):
        """https://docs.sheetsu.com/?shell#read"""
        data = dict()
        if kwargs.get('sheet'):
            data.update({'sheet': kwargs.pop('sheet')})

        if kwargs.get('limit'):
            data.update({'limit': kwargs.pop('limit')})

        return self._call(self.ss_id, method="get", data=data)

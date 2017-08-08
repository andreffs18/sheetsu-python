import json
import requests
from requests.auth import HTTPBasicAuth

from sheetsu.exceptions import UnknownRequestMethod

import logging
logger = logging.getLogger("core" + __name__)


class Resource(object):

    def __init__(self, client):
        """Initialize Sheetsu endpoints common variables"""
        self.sheetsu_api_url = "https://sheetsu.com/apis/v1.0/"
        self.api_key = client.api_key
        self.api_secret = client.api_secret
        self.spreadsheet_id = client.spreadsheet_id

    def __call__(self, *args, **kwargs):
        """Wrapper around requests
        :param url: end url to concatenate with Sheetsu API url
        :param method: one of the following options:
        :param data: optional, only for 'post' and 'put'
        :return: requests instance"""
        url = "{}{}".format(self.sheetsu_api_url, kwargs.pop('url'))

        method = kwargs.pop('method')
        if method == 'get':
            func = requests.get
        elif method == 'post':
            func = requests.post
        elif method == 'patch':
            func = requests.patch
        elif method == 'delete':
            func = requests.delete
        else:
            raise UnknownRequestMethod("Method: {}".format(method))

        kwargs = dict(
            data=kwargs.pop('data', ""),
            headers={"Content-Type": "application/json"}
        )

        if self.api_key and self.api_secret:
            auth = HTTPBasicAuth(self.api_key, self.api_secret)
            kwargs.update(dict(auth=auth))

        r = func(url, **kwargs)

        logger.debug("--{} ({})-- {} with data {}"
                     "".format(method.upper(), r.status_code, url,
                               kwargs.get('data')))

        if r.status_code not in [200]:
            logger.error("Error({}): {} for url {}"
                         "".format(r.status_code, r.text, url))
            return

        return json.loads(r.content)

import sys
import json
import requests
from requests.auth import HTTPBasicAuth

from sheetsu.exceptions import UnknownRequestMethod

import logging
logger = logging.getLogger('sheetsu.' + __name__)
formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
logger.setLevel(logging.ERROR)  # ex: DEBUG ERROR
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


class Resource(object):

    def __init__(self, client):
        """Initialize Sheetsu Resource variables
        :param client: "SheetsuClient" object instance"""
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
        # build url to make request
        url = "{}{}".format(self.sheetsu_api_url, kwargs.pop('url'))
        # decide which HTTP request to make
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
        # build headers and data payload
        kwargs = dict(
            data=kwargs.pop('data', ""),
            headers={"Content-Type": "application/json"}
        )
        # if authentication is required add it to request
        if self.api_key and self.api_secret:
            auth = HTTPBasicAuth(self.api_key, self.api_secret)
            kwargs.update(dict(auth=auth))
        # make HTTP request
        logger.debug("--{}-- {} with data {}"
                     "".format(method.upper(), url, kwargs.get('data')))
        r = func(url, **kwargs)

        if r.status_code not in [200]:
            logger.error("Error({}): {} for url {}"
                         "".format(r.status_code, r.text, url))
            return

        return json.loads(r.content)

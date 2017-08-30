try:
    # for python 3.x
    from urllib.parse import urlencode
except ImportError:
    # for python 2.x
    from urllib import urlencode

from .core import Resource


class ReadResource(Resource):

    def __call__(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        data = dict()
        if kwargs.get('limit'):
            data.update({'limit': kwargs.pop('limit')})

        if kwargs.get('offset'):
            data.update({'offset': kwargs.pop('offset')})

        url = self.spreadsheet_id
        if kwargs.get('sheet'):
            url += "/sheets/" + kwargs.pop('sheet')
        url += "?" + urlencode(data)

        payload = dict(url=url, method="get")
        return super(ReadResource, self).__call__(**payload)


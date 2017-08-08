from urllib.parse import urlencode, quote_plus

from .core import Resource


class ReadResource(Resource):

    def __call__(self, **kwargs):
        """"""
        data = dict()
        if kwargs.get('limit'):
            data.update({'limit': kwargs.pop('limit')})

        if kwargs.get('offset'):
            data.update({'offset': kwargs.pop('offset')})

        url = self.spreadsheet_id
        if kwargs.get('sheet'):
            url += "/sheets/" + kwargs.pop('sheet')
        url += "?" + urlencode(data, quote_via=quote_plus)

        payload = dict(url=url, method="get")
        return super(ReadResource, self).__call__(**payload)


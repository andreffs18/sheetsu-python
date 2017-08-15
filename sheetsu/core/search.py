from urllib.parse import urlencode, quote_plus

from .core import Resource


class SearchResource(Resource):

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

        if kwargs.get('ignore_case'):
            ignore_case = kwargs.pop('ignore_case')
            data.update({'ignore_case': ignore_case in ["True", "true", True]})

        url = self.spreadsheet_id
        if kwargs.get('sheet'):
            url += "/sheets/" + kwargs.pop('sheet')

        url += "/search"
        url += "?" + urlencode(data, quote_via=quote_plus)
        url += "&" + urlencode(kwargs, quote_via=quote_plus)

        payload = dict(url=url, method="get")
        return super(SearchResource, self).__call__(**payload)


from .core import Resource


class UpdateResource(Resource):

    def __call__(self, **kwargs):
        """"""
        url = self.spreadsheet_id
        if kwargs.get('sheet'):
            url += "/sheets/" + kwargs.pop('sheet')

        if kwargs.get('column') and kwargs.get('value'):
            url += "/" + kwargs.pop('column') + "/" + kwargs.pop('value')

        data = kwargs.pop('data', {})
        payload = dict(url=url, method="patch", data=data)
        return super(UpdateResource, self).__call__(**payload)


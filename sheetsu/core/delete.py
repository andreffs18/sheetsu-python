from .core import Resource


class DeleteResource(Resource):

    def __call__(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        url = self.spreadsheet_id
        if kwargs.get('sheet'):
            url += "/sheets/" + kwargs.pop('sheet')

        if kwargs.get('column') and kwargs.get('value'):
            url += "/" + kwargs.pop('column') + "/" + kwargs.pop('value')

        payload = dict(url=url, method="delete")
        return super(DeleteResource, self).__call__(**payload)


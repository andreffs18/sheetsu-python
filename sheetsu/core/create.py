import json

from .core import Resource


class CreateOneResource(Resource):

    def __call__(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        url = self.spreadsheet_id

        if kwargs.get('sheet'):
            url += "/sheets/" + kwargs.pop('sheet')

        data = json.dumps(kwargs)
        payload = dict(url=url, method="post", data=data)
        return super(CreateOneResource, self).__call__(**payload)


class CreateManyResource(Resource):

    def __call__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        url = self.spreadsheet_id

        if kwargs.get('sheet'):
            url += "/sheets/" + kwargs.pop('sheet')

        data = json.dumps({'rows': args})
        payload = dict(url=url, method="post", data=data)
        return super(CreateManyResource, self).__call__(**payload)



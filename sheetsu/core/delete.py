import json

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

        # If destroy=true, the row is removed from the sheet; else the data is
        # cleared but the empty row kept in the sheet.
        if kwargs.get('destroy') and kwargs.pop('destroy') == 'true':
            data = {}
            data[kwargs.pop('column')] = kwargs.pop('value')            
            payload = dict(url=url, method="delete", data=json.dumps(data))
        else:
            if kwargs.get('column') and kwargs.get('value'):
                url += "/" + kwargs.pop('column') + "/" + kwargs.pop('value')
            payload = dict(url=url, method="delete")

        return super(DeleteResource, self).__call__(**payload)

import logging

from sheetsu.core import (
    ReadResource, SearchResource, CreateOneResource,
    CreateManyResource, UpdateResource, DeleteResource)

logger = logging.getLogger(__name__)


class SheetsuClient(object):

    def __init__(self, spreadsheet_id, **kwargs):
        self.spreadsheet_id = spreadsheet_id
        self.api_key = kwargs.pop('api_key', None)
        self.api_secret = kwargs.pop('api_secret', None)

    def read(self, **kwargs):
        """https://docs.sheetsu.com/?shell#read"""
        return ReadResource(self)(**kwargs)

    def search(self, **kwargs):
        """https://docs.sheetsu.com/?shell#search-spreadsheet"""
        return SearchResource(self)(**kwargs)

    def create_one(self, **kwargs):
        """https://docs.sheetsu.com/?shell#create"""
        return CreateOneResource(self)(**kwargs)

    def create_many(self, *args):
        """https://docs.sheetsu.com/?shell#create"""
        return CreateManyResource(self)(*args)

    def update(self, **kwargs):
        """https://docs.sheetsu.com/?shell#update"""
        return UpdateResource(self)(**kwargs)

    def delete(self, **kwargs):
        """https://docs.sheetsu.com/?shell#delete"""
        return DeleteResource(self)(**kwargs)

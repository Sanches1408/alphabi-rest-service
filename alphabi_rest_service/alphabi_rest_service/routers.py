from core.models import AlphaBIData


class AlphaBIRouter(object):

    def db_for_read(self, model, **hints):
        if model == AlphaBIData:
            return 'alphabi'
        return None

    def db_for_write(self, model, **hints):
        if model == AlphaBIData:
            return 'alphabi'
        return None

from core.models import Data


class AlphaBIRouter(object):

    def db_for_read(self, model, **hints):
        if model == Data:
            return 'alphabi'
        return None

    def db_for_write(self, model, **hints):
        if model == Data:
            return 'alphabi'
        return None

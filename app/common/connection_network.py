from .utils import SingletonDecorator


@SingletonDecorator
class ConnectionNetwork:
    """
    This class is used to initialize ConnectionNetwork object which can be used by different services
    of this package in order to get the different types of connections. It has db_session, cache_conn and logger
    variables
    """

    def __init__(self, db_session, logger=None):
        self.db_session = db_session
        self.logger = logger

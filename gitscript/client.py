import asyncio
import logging

log = logging.getLogger(__name__)


class Client:
    def __init__(self, **options):
        self.token = options.get("username", None)
        self.token = options.get("token", None)
        self.httpsession = options.get("httpsession", None)
        if token:
            self.login(username, token=token)

    def __repr__(self):
        if self.session.auth:
            return "<GitHub [{!r}]>".format(self.httpsession.auth)
        return "<Anonymous GitHub at 0x{0:x}>".format(id(self))

    

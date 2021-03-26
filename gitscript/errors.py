# -*- coding: utf-8 -*-


class GitScriptException(Exception):
    pass


class HTTPException(GitScriptException):
    def __init__(self, response, message):
        self.status = response.status
        if isinstance(message, dict):
            self.status = message.get("code", self.status)
            self.error = message.get("message", "GitScriptException")
        else:
            self.error = message
        super().__init__(f"{self.status} {self.error}")


class Unauthorized(HTTPException):
    pass


class Forbidden(HTTPException):
    pass


class NotFound(HTTPException):
    pass

# -*- coding: utf-8 -*-

import asyncio
import json
import logging
import aiohttp
import sys
from urllib.parse import quote as _uriquote

from . import UserAuth

__logs__ = logging.getLogger(__name__)


async def Content_Type(response):
    text = await response.text(encoding="utf-8")
    try:
        if response.headers["content-type"] == "application/json":
            return json.loads(text)
    except KeyError:
        pass
    return text


def requires_2fa(response):
    if (
        response.status == 401
        and "X-GitHub-OTP" in response.headers
        and "required" in response.headers["X-GitHub-OTP"]
    ):
        return True
    return False


class Route:
    BASE = "https://api.github.com"

    def __init__(self, method, path, **parameters):
        self.path = path
        self.method = method
        url = self.BASE + self.path
        if parameters:
            self.url = url.format(
                **{
                    k: _uriquote(v) if isinstance(v, str) else v
                    for k, v in parameters.items()
                }
            )
        else:
            self.url = url

    def __repr__(self):
        return "Route {0}({1})".format(self.path, self.BASE.replace("https://", ""))


class HTTPClient:

    auth = None
    SUCCESS_LOG = "{method} {url} has received {text}"
    REQUEST_LOG = "{method} {url} with {json} has returned {status}"

    def __init__(
        self,
        connector=None,
        default_connect_timeout=4,
        default_read_timeout=10,
        **kwargs
    ):
        self.default_connect_timeout = default_connect_timeout
        self.default_read_timeout = default_read_timeout
        self.connector = connector
        self.two_factor_auth_cb = None
        user_agent = "Gitscript (https://github.com/decave27/gitscript {0}) Python/{1[0]}.{1[1]} aiohttp/{2}"
        self.user_agent = user_agent.format(
            __version__, sys.version_info, aiohttp.__version__
        )
        self.accept_header = "application/vnd.github.v3.full+json"
        self.accept_charset = "utf-8"
        self.content_type = "application/json"
        self.data = kwargs
        self.data["headers"]["Accept"] = self.accept_header
        self.data["headers"]["Accept-Charset"] = self.accept_charset
        self.data["headers"]["Content-Type"] = self.content_type
        self.data["headers"]["User-Agent"] = self.user_agent

    @property
    def timeout(self):
        return (self.default_connect_timeout, self.default_read_timeout)

    def handle_two_factor_auth(self):
        self.data["headers"]["X-GitHub-OTP"] = str(self.two_factor_auth_cb())
        return

    def basic_auth(self, username, password):
        if not (username and password):
            return
        self.auth = UserAuth(username, password)

    def has_auth(self):
        return self.auth or self.data["headers"]

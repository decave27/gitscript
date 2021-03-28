# -*- coding: utf-8 -*-


class BaseUser:
    def __init__(self, *, data):
        self._update(data)

    def _update(self, data):
        self.username = data["login"]
        self.id = data["id"]
        self.node = data["node_id"]
        self.avatar_url = data["avatar_url"]
        self.url = data["html_url"]
        self.name = data["name"]
        

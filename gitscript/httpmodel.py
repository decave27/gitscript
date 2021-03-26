# -*- coding: utf-8 -*-


class TokenAuth:
    header_format_str = "token {}"

    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return "token {}...".format(self.token[:4])

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        return self.token == getattr(other, "token", None)

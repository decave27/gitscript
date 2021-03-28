class Team:
    def __init__(self, *, data):
        self._update(data)
    def _update(self, data):
        self.name = data["login"]
        self.id = data["id"]
        self.avatar_url = data["avatar_url"]
        self.node = data["node_id"]
        self.url = 'https://github.com/' + str(data["login"])
        self.description = data["description"]

class TeamEvent:
    def __init__(self, *, data):
        self._update(data)
    def _update(self, data):
        self.id = data["id"]
        self.action_type = data["type"]
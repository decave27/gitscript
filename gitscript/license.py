class License:
    def __init__(self, *, data):
        self._update(data)
        self.name = data["name"]
    def __repr__(self):
        return f'<License {self.l}>'
    def _update(self, data):
        self.name = data["name"]


        
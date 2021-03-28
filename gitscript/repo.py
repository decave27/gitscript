class Repository:
    def __init__(self, *, data):
        self._update(data)
    def _update(self, data):
        self.name = data["name"]
        self.id = data["id"]
        self.full_name = data["full_name"]
        self.node = data["node_id"]
        if data["private"] == 'false': 
            self.private = False
        elif data["private"] == 'true':
            self.private = True
        else:
            self.private = data["private"]
        self.url = data["html_url"]
        self.description = data["description"]
        if data["fork"] == 'false': 
            self.private = False
        elif data["fork"] == 'true':
            self.private = True
        else:
            self.private = data["fork"]
        self.git = data["git_url"]
        self.ssh = data["ssh_url"]
        self.homepage = data["homepage"]
        self.size = data["size"]
        self.stargazers = data["stargazers_count"]
        self.watchers = data["watchers_count"]
        self.has_issue = data["has_issue"]
        self.has_project = data["has_project"]
        self.has_downloads = data["has_downloads"]
        self.has_wiki = data["has_wiki"]
        self.has_pages = data["has_pages"]
        self.forks_count = data["forks_count"]
        self.language = data["language"]
        self.mirror_url = data["mirror_url"]
        self.archived = data["archived"]
        self.disabled = data["disabled"]
        self.open_issues_count = data["open_issues_count"]
        self.forks = data["forks"]
        self.open_issues = data["open_issues"]
        self.watchers = data["watchers"]
        self.default_branch = data["default_branch"]
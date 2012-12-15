class RoleVO(object):
    username = None
    roles = []

    def __init__(self, username=None, roles=None):
        if username:
            self.username = username
        if roles:
            self.roles = roles



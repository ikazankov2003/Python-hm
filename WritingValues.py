class Note:

    def __init__(self, memo=None, tag=None, id=1, data=None):
        self.memo = memo
        self.tag = tag
        self.id = id
        self.data = data

    def modify(self, id, memo, tag, data):
        if memo:
            self.memo = memo
        if tag:
            self.tag = tag
        self.data = data
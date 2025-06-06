class Account:
    def __init__(self, username, private = False):
        self.username = username
        self.followers = set()
        self.following = set()
        self.blocked = set()
        self.blockedBy = set()
        self.requests = []
        self.private = private

    def setPrivate(self):
        self.private = True

    def setPublic(self):
        self.public = False

    def follow(self, otherAccount):
        if (
            self != otherAccount and
            self not in otherAccount.blocked and
            otherAccount not in self.blocked
        ):
            self.following.add(otherAccount)
            otherAccount.followers.add(self)

    def unfollow(self, otherAccount):
        if self != otherAccount:
            self.following.discard(otherAccount)
            otherAccount.followers.discard(self)  

    def remove(self, otherAccount):
        if self != otherAccount:
            self.following.discard(otherAccount)
            self.followers.discard(otherAccount)
            otherAccount.following.discard(self)
            otherAccount.followers.discard(self)

    def block(self, otherAccount):
        if self != otherAccount:
            self.following.discard(otherAccount)
            self.followers.discard(otherAccount)
            otherAccount.following.discard(self)
            otherAccount.followers.discard(self)
            self.blocked.add(otherAccount)
            otherAccount.blockedBy.add(self)

    def unblock(self, otherAccount):
        if self != otherAccount:
            self.blocked.discard(otherAccount)
            otherAccount.blockedBy.discard(self)

    def mutuals(self, otherAccount):
        return list(self.following & otherAccount.following)

    def reccomendFollowers(self):
        r = set()
        for account in self.following:
            for suggestion in account.following:
                if (
                    suggestion != self and
                    suggestion not in self.following and
                    suggestion not in self.blocked
                ):
                    r.add(suggestion)
        return list(r)

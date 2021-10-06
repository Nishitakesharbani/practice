class other(object):
    def implicit(self):
        print("other implicit")
    def override(self):
        print("other override()")
    def altered(self):
        print("other altered()")


class child(object):
    def __init__(self):
        self.other=other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print("child override()")
    def altered(self):
        print("Child before altered()")
        self.other.altered()
        print("Child after altered")



son=child()


son.implicit()
son.override()
son.altered()
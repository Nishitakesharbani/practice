class parent(object):
    def implicit(self):
        print("Parent implicit")
    def override(self):
        print("Parents override()")
    def altered(self):
        print("Parent altered()")


class child(parent):
    def override(self):
        print("child override()")
    def altered(self):
        print("Child before altered()")
        super(child,self).altered()
        print("Child after altered")


dad=parent()
son=child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
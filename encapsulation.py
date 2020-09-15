class Base(object):
    def __private(self):
        print("this is a private method")
    def _protected(self):
        print("this is a protected method")
    def public(self):
        print("this is a public method")


d = Base()
d.public()

d._Base__private()

d._protected()

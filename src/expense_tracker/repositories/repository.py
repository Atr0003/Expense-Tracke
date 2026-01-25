
class Repository:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def get_all(self):
        return self.data

    def remoeve(self, item):
        self.data.remove(item)

    def modify(self, old_item, new_item):
        index = self.data.index(old_item)
        self.data[index] = new_item

    
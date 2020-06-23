class go_vno:
    def __init__(self, a = None):
        self.a = []
    @property
    def add(self):
        for i in range(0, 10):
            self.a.append(i)
    def __len__(self):
        return len(self.a)
    
a = go_vno()
a.add
print(len(a))
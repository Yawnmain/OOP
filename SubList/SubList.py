class SubList(list):
    def __init__(self, *lst):
        super(SubList, self).__init__(*lst)

    def __sub__(self, other):
        return self.__class__([e for e in self if e not in other])


a = SubList([1, 2, 3])
b = SubList([1, 2 ,5])
c = a - b
print(c)

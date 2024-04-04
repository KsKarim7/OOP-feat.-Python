class home:
    def __init__(self,name,roll) -> None:
        self.name = name
        self.roll = roll
    def setName(self,name):
        self.name = name



lst = []
mst = lst
mst.append(home("khalz",22201091))
mst[0].setName("khal")
mst.remove(mst[0])
print(mst)
# print(mst[0].name)
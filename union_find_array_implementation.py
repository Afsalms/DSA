

class Union:
    def __init__(self, array):
        self.array = [-1 for i in range(len(array))]
        self.map = {item: i for i, item in enumerate(array)}

    def __str__(self):
        return f"array {self.array} map: {self.map}"

    def find(self, item):
        if self.map.get(item) is None:
            print("Not found")
            return None
        value_in_array = self.array[self.map[item]]
        if type(value_in_array) == int and  value_in_array < 0:
            print("Reached root")
            return value_in_array
        return self.find(value_in_array)

    def merge(self, node1, node2):
        node1_value = self.find(node1)
        node2_value = self.find(node2)
        print(node1_value)
        print(node2_value)
        print("++++++++++++++++++++++++++++++++++++++")
        if node1_value is not None and node2_value is not None:
            if node1_value <= node2_value:
                self.array[self.map[node2]] = node1
                self.array[self.map[node1]] = node1_value + node2_value
            else:
                self.array[self.map[node1]] = node2
                self.array[self.map[node2]] = node1_value + node2_value


array = ["a", "b", "c", "d", "e", "f"]



u = Union(array)

print(u)

#print(u.find("a"))
#print(u.find("z"))


u.merge("a", "b")
print(u)
u.merge("a", "c")
print(u)
u.merge("d", "e")
print(u)
u.merge("a", "d")
print(u)

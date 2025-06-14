class BuggyCountedObject:
    num_instances = 0
    def __init__(self):
        self.num_instances += 1

print(BuggyCountedObject().num_instances)
print(BuggyCountedObject().num_instances)
print(BuggyCountedObject().num_instances)

class NormalCountedObject:
    num_instances = 0
    def __init__(self):
        NormalCountedObject.num_instances += 1

print(NormalCountedObject().num_instances)
print(NormalCountedObject().num_instances)
print(NormalCountedObject().num_instances)
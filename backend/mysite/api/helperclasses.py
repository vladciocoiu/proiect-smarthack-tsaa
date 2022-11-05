class Parameter:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def deserializer(self, data):
        self.name = data.get('name')
        self.value = data.get('value')
    def serializer(self):
        return {'name': self.name, 'value': self.value}
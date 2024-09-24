class ModelCompound:

    def __init__(self, id, kind, name):
        self._id = id
        self._kind = kind
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def kind(self):
        return self._kind

    @property
    def name(self):
        return self._name



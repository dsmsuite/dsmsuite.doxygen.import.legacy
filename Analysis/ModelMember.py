class ModelMember:

    def __init__(self, id, kind, name, parent_compound, file):
        self._id = id
        self._kind = kind
        self._name = name
        self._parent_compound = parent_compound
        self._file = file

    @property
    def id(self):
        return self._id

    @property
    def kind(self):
        return self._kind

    @property
    def name(self):
        return self._name

    @property
    def parent_compound(self):
        return self._parent_compound

    @property
    def file(self):
        return self._file

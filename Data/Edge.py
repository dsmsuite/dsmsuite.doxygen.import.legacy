class Edge:

    def __init__(self, index, source, target, kind, strength, description):
        self._index = index
        self._source = source
        self._target = target
        self._kind = kind
        self._strength = strength
        self._description = description

    @property
    def index(self):
        return self._index

    @property
    def source(self):
        return self._source

    @property
    def target(self):
        return self._target

    @property
    def kind(self):
        return self._kind

    @property
    def strength(self):
        return self._strength

    @property
    def description(self):
        return self._description

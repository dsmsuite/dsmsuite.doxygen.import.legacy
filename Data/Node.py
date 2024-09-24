class Node:

    def __init__(self, index, name, kind, description):
        self._index = index
        self._parent = None
        self._name = name
        self._kind = kind
        self._description = description
        self._children = []

        if self._parent is not None:
            self._parent.add_child(self)

    def add_child(self, child):
        self._children.append(child)
        child. parent = self

    @property
    def fullname(self):
        fullname = self.name
        _current_parent = self.parent
        while _current_parent is not None:
            if len(_current_parent.name) > 0:
                fullname = _current_parent.name + '.' + fullname
            _current_parent = _current_parent.parent

        return fullname

    @property
    def index(self):
        return self._index

    @property
    def parent(self):
        return self._parent

    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind

    @property
    def description(self):
        return self._description

    @property
    def children(self):
        return self._children

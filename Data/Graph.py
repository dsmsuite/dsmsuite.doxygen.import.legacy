from Data.Edge import Edge
from Data.Node import Node

class Graph:

    def __init__(self):
        self._node_index = 0
        self._edge_index = 0
        self._root_node = Node(self._node_index, "", "", "")
        self._edges = []

    def create_node(self, name, kind, description):
        #print(‘Create node name={} kind={} description={}'.format(name, kind, description) )
        self._node_index = self. _node_index + 1
        return Node(self._node_index, name, kind, description)

    def add_node_child(self, parent, child):
        if parent is None:
            #print(‘Add child node to root child_name{} child_kind={}‘.format(child.name, child.kind))
            self. _root_node.add_child(child)
        else:
            #print(‘Add child node to parent parent=_name={} parent_kind={} child_name{} child_kind={}'.format(parent.name, parent.kind, ch
            parent.add_child(child)

    def create_edge(self, source, target, kind, strength, description):
        #print(“Create edge source={} target={} kind={} strength={} description={}'.format(source.name, target.name, kind, strength, descrif
        self._edge_index = self._edge_index + 1
        edge = Edge(self._edge_index, source, target, kind, strength, description)
        self._edges.append(edge)
        return edge

    @property
    def root_node(self):
        return self._root_node

    @property
    def edges(self):
        return self._edges


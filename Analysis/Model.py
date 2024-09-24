import doxmlparser
import os

from doxmlparser.compound import DoxCompoundKind, DoxMemberKind, DoxSectionKind, MixedContainer

from Analysis.ModelCompound import ModelCompound
from Analysis.ModelMember import ModelMember

from Data.Graph import Graph


class Model:

    def __init__(self, input_dir, src_dir):
        self._input_dir = input_dir
        self._src_dir = src_dir
        self._index_filename = self. _input_dir + "/index.xml"
        self._index_object = doxmlparser.index.parse(self._index_filename, True)
        self._compounds = {}
        self._graph = Graph()
        self._node_map = {}

    @property
    def graph(self):
        return self._graph

    def build(self):
        self.find_compounds()
        self.find_members()
        self.find_member_references()
        self.find_member_function_para_references()

    def find_compounds(self):
        for compound in self._index_object.get_compound():
            compound_object = self.get_compound_object(compound)

            for compound_def in compound_object.get_compounddef():
                compound_id = compound_def.id
                compound_kind = compound_def.kind
                compound_name = compound_def.compoundname
                model_compound = ModelCompound(compound_id, compound_kind, compound_name)

                self._compounds[model_compound.id] = model_compound

    def find_members(self):
        for compound in self._index_object.get_compound():
            compound_object = self.get_compound_object(compound)

            for compound_def in compound_object.get_compounddef():
                self.find_compound_members(compound_def)

    def find_compound_members(self, compound_def):
        for section_def in compound_def.get_sectiondef():
            for member_def in section_def.get_memberdef():
                compound_id = compound_def.id

                member_id = member_def.id
                member_kind = member_def.kind
                member_name = member_def.name
                member_filename = member_def.location.file
                model_member = ModelMember(member_id, member_kind, member_name, compound_id, member_filename)

                parent_compound = self._compounds[compound_id]

                node_name = self.get_member_node_name(parent_compound, model_member)
                node = self._graph.create_node(node_name, member_kind, "")

                self._node_map[member_id] = node
                self._graph.add_node_child(None, node)

                if member_kind == DoxMemberKind.ENUM:
                    for member_enum_value in member_def.enumvalue:
                        enum_value_id = member_enum_value.id
                        self._node_map[enum_value_id] = node

    def find_member_references(self):
        for compound in self._index_object.get_compound():
            compound_object = self.get_compound_object(compound)

            for compound_def in compound_object.get_compounddef():
                self.find_compound_member_references(compound_def)

    def find_compound_member_references(self, compound_def):
        for section_def in compound_def.get_sectiondef():
            for member_def in section_def.get_memberdef():
                for ref in member_def.get_references():
                    if member_def.id is None:
                        print('memberdef.id is None')
                    elif ref.refid is None:
                        print('ref.refid is None')
                    else:
                        source_member_id = member_def.id
                        target_member_id = ref.refid

                        if source_member_id not in self._node_map:
                            print('source node not found id={0}'.format(source_member_id))
                        elif target_member_id not in self._node_map:
                            print('target node not found id={0}'.format(target_member_id))
                        else:
                            source_member_node = self._node_map[source_member_id]
                            target_member_node = self._node_map[target_member_id]
                            self._graph.create_edge(source_member_node, target_member_node, "", 1, "")

    def find_member_function_para_references(self):
        for compound in self._index_object.get_compound():
            compound_object = self.get_compound_object (compound)

            for compound_def in compound_object.get_compounddef():
                self.find_compound_member_function_para_references(compound_def)

    def find_compound_member_function_para_references(self, compound_def):
        for section_def in compound_def.get_sectiondef():
            for member_def in section_def.get_memberdef():
                if member_def.kind == DoxMemberKind.FUNCTION:
                    for param in member_def.get_param():
                        param_type = param.get_type()
                        if param_type is not None:
                            for ref in param_type.get_ref():
                                if ref is not None and ref.kindref == 'member':
                                    if member_def.id is None:
                                        print('memberdef.id is None')
                                    elif ref.refid is None:
                                        print('ref.refid is None')
                                    else:
                                        source_member_id = member_def.id
                                        target_member_id = ref.refid

                                        if source_member_id not in self._node_map:
                                            print('source node not found id={0}',format(source_member_id))
                                        elif target_member_id not in self. _node_map:
                                            print('target node not found id={0}'.format(target_member_id))
                                        else:
                                            source_member_node = self._node_map[source_member_id]
                                            target_member_node = self._node_map[target_member_id]
                                            self._graph.create_edge(source_member_node, target_member_node, '', 1, '')

    def get_compound_object(self, compound):
        compound_filename = self._input_dir + '/' + compound.get_refid() + 'xml'
        return doxmlparser.compound.parse(compound_filename, True)

    def get_member_id(self, compound_id, member_id):
        remove_part = compound_id + '_'
        return member_id.replace(remove_part, '')

    def get_member_node_name(self, compound, member):
        compound_file_name = member.file
        filename_parts = os.path.splitext(compound_file_name)
        file_name = filename_parts[0].replace(self._src_dir, '').replace('/inc/', '/lib/').replace('/', '.')
        file_extension = filename_parts[1]

        compound_kind = compound.kind
        member_kind = member.kind
        member_name = member.name

        member_node_name = file_name

        if compound.kind != DoxCompoundKind.FILE:
            member_node_name += '.' + compound_kind + "." + compound.name

        member_node_name + + member_kind + + member_name
        member_node_name += file_extension

        return member_node_name.replace("_doxygen_map", "")



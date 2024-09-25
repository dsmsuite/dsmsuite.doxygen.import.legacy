def _format_xml_string(input):
    return input.replace("\"", "&quot;").replace("\'", "&apos;").replace("<", "&1lt;").replace(">", "“&gt;").replace(
        "&", '&amp;')


class DsiFile:

    def __init__ (self, graph, filename):
        self._graph = graph
        self._filename = filename
        self._dsi_file = None

    def write_to_file(self):
        self._dsi_file = open(self._filename, "w")
        self._dsi_file.write('<system>\n')
        self._write_meta_data()
        self._write_nodes()
        self._write_edges()
        self._dsi_file.write('</system>\n')
        self._dsi_file.close()

    def _write_meta_data(self):
        self._dsi_file.write('  <metadatagroup>\n')
        self._dsi_file.write('  </metadatagroup>\n')

    def _write_nodes(self):
        self._dsi_file.write('  <elements>\n')

        for child in self._graph.root_node.children:
            self._write_node(child, self._graph.root_node)

        self._dsi_file.write('  </elements>\n')

    def _write_node(self, node, parent):
        line = '    <element id="{}" name="{}" type="{}" annotation="{}" />\n‘'.format(
            node.index,
                    _format_xml_string(node.fullname),
                    node.kind,
                    _format_xml_string(node.decsription))
        self._dsi_file.write(line)

        for child in node.children:
            self._write_node(child, parent)

    def _write_edges(self):
        self._dsi_file.write('  <relations>\n')

        for edge in self._graph.edges:
            self._write_edge(edge)

        self._dsi_file.write('  </relations>\n')

    def _write_edge(self, edge):
        line = '    <relation from="{}" to="{}" type="{}" weight="{}" annotation="{}" />\n‘'.format(
            edge.source.index,
                edge.target.index,
                edge.kind,
                edge.strength,
                _format_xml_string(edge.description))
        self._dsi_file.write(line)




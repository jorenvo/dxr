from dxr.lines import Ref
from dxr.utils import search_url


class _PythonPluginAttr(object):
    plugin = 'python'


class ClassRef(Ref, _PythonPluginAttr):
    """A reference attached to a class definition"""

    def menu_items(self):
        qualname = self.menu_data
        yield {'html': 'Find subclasses',
               'title': 'Find subclasses of this class',
               'href': search_url(self.tree.name, '+derived:' + qualname),
               'icon': 'type'}
        yield {'html': 'Find base classes',
               'title': 'Find base classes of this class',
               'href': search_url(self.tree.name, '+bases:' + qualname),
               'icon': 'type'}
        # yield {'html': 'Find Odoo models that inherit from this',
        #        'title': 'Find Odoo models that inherit from this',
        #        'href': search_url(self.tree.name, '+odoo_inherit:' + qualname),
        #        'icon': 'type'}


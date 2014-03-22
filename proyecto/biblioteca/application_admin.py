
from camelot.view.art import Icon
from camelot.admin.application_admin import ApplicationAdmin
from camelot.admin.section import Section
from camelot.core.utils import ugettext_lazy as _
from biblioteca.model import Libro, Ejemplar, Prestamo, Usuario

class MyApplicationAdmin(ApplicationAdmin):
  
    name = 'Biblioteca'
    application_url = 'http://www.python-camelot.com'
    help_url = 'http://www.python-camelot.com/docs.html'
    author = 'Ivan Mtz.'
    domain = 'mydomain.com'
    
    def get_sections(self):
        from camelot.model.memento import Memento
        from camelot.model.i18n import Translation
        return [ Section( _('Biblioteca'),
                          self,
                          Icon('tango/22x22/apps/system-users.png'),
                          items = [ Libro, Ejemplar, Prestamo, Usuario ] ),
                 Section( _('Configuration'),
                          self,
                          Icon('tango/22x22/categories/preferences-system.png'),
                          items = [Memento, Translation] )
                ]
    
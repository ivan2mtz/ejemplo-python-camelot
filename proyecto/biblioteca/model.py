# begin basic imports
from camelot.core.orm import Entity
from camelot.admin.entity_admin import EntityAdmin

from sqlalchemy import sql
from sqlalchemy.schema import Column
import sqlalchemy.types
# end basic imports

import camelot.types
from camelot.core.sql import metadata
from camelot.core.orm import Entity, Field, ManyToOne, OneToMany, \
                             ManyToMany, using_options, ColumnProperty, ManyToOne
from camelot.admin.action import Action
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.utils import ugettext_lazy as _
from camelot.model.party import Person
from camelot.view import action_steps
from camelot.view.forms import Form, TabForm, WidgetOnlyForm, HBoxForm, Stretch
from camelot.view.controls import delegates
from camelot.view.filters import ComboBoxFilter
from camelot.view.art import ColorScheme
from sqlalchemy.types import Unicode, Date, Integer
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

from camelot_example.change_rating import ChangeRatingAction
from camelot_example.drag_and_drop import DropAction


class Libro( Entity ):

    __tablename__ = 'libro'

    titulo = Column( Unicode(60), nullable = False )
    autor = Column( Unicode(60) )
    editorial = Column( Unicode(30) )

    def __unicode__( self ):
        return self.titulo or 'Sin titulo'

    class Admin( EntityAdmin ):
        verbose_name = 'Libro'
        list_display = ['titulo', 'autor', 'editorial' ]
        form_display = list_display + ['ejemplares']

class Ejemplar( Entity ):

    __tablename__ = 'ejemplar'

    clave = Column( Unicode(10), nullable = False )
    estado = Column( Unicode(30) )

    libro_id = Column( Integer, ForeignKey('libro.id') )
    libro = relationship( 'Libro',
                             backref = 'ejemplares' )

    def __unicode__( self ):
        return self.libro.titulo + ' - ' + self.clave or 'Sin Numero de Ejemplar'

    class Admin( EntityAdmin ):
        verbose_name = 'Ejemplar'
        list_display = [ 'libro', 'clave', 'estado' ]
        form_display = list_display + ['prestamos']

class Prestamo( Entity ):

    __tablename__ = 'prestamo'

    numero = Column( Unicode(4), nullable = False  )
    fecha_prestamo = Column( sqlalchemy.types.Date() )
    fecha_entrega = Column( sqlalchemy.types.Date() )
    fecha_devolucion = Column( sqlalchemy.types.Date() )

    ejemplar_id = Column( Integer, ForeignKey('ejemplar.id') )
    ejemplar = relationship( 'Ejemplar',
                             backref = 'prestamos' )

    usuario_id = Column( Integer, ForeignKey('usuario.id') )
    usuario = relationship( 'Usuario',
                             backref = 'prestamos' )

    def __unicode__( self ):
        return self.numero or 'Sin Num. de prestamo'

    class Admin( EntityAdmin ):
        verbose_name = 'Prestamo'
        list_display = ['numero', 'fecha_prestamo', 'fecha_entrega', 'fecha_devolucion', 'ejemplar', 'usuario' ]

class Usuario( Entity ):

    __tablename__ = 'usuario'

    nombre = Column( Unicode(60), nullable = False )
    direccion = Column( Unicode(60) )
    email = Column( Unicode(30) )
    telefono = Column( Unicode(15) )

    def __unicode__( self ):
        return self.nombre or 'Sin nombre'

    class Admin( EntityAdmin ):
        verbose_name = 'Usuario'
        list_display = ['nombre', 'direccion', 'email', 'telefono' ]
        form_display = list_display + ['prestamos']
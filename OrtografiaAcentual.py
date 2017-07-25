import random
import gi
import logging
from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import (ActivityToolbarButton, StopButton)

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
logger = logging.getLogger(__name__)

class OrtografiaAcentual(activity.Activity):
	def __init__(self, handle):
		activity.Activity.__init__(self, handle)
		self.primeriano = 1
		self.mensaje = '<b> Bienvenido Seas a la Ortografia Acentual<b>'
		self.agregar_toolbar()
		self.agregar_canvas()
		self.agregar_style()

	def agregar_toolbar(self):
		toolbar_box = ToolbarBox()
		aplicacion_toolbar_boton = ActivityToolbarButton(self)
		aplicacion_stop_boton = StopButton(self)
		toolbar_box.toolbar.insert(aplicacion_toolbar_boton, 0)
		aplicacion_toolbar_boton.show()
		toolbar_box.toolbar.insert(aplicacion_stop_boton, -1)
		aplicacion_stop_boton.show()

		self.set_toolbar_box(toolbar_box)
		toolbar_box.show()

	def agregar_canvas(self):
		pass

	def agregar_style(self):
		pass



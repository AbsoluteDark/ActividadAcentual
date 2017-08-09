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
		self.canvas = Gtk.Grid()
		play = Gtk.Button('Jugar')
		self.canvas.attach(play, 0, 0, 1, 1)
		
		play.connect('clicked', self.jugar)
		imagen = Gtk.Image.new_from_file('buho.png')
		buf_image = imagen.get_pixbuf()
		
		nueva_img = Gtk.Image()
		nuevo_pixbuf = buf_image.scale_simple(500,500,GdkPixbuf.InterpType.BILINEAR )
		nueva_img.set_from_pixbuf(nuevo_pixbuf)
		self.canvas.attach_next_to(nueva_img, play, Gtk.PositionType.BOTTOM, 1,  1)
		self.canvas.show_all()

	def jugar(self, btn):
		for widget in self.canvas:
			self.canvas.remove(widget)

		label = Gtk.Label('Nueva Pantalla')
		self.canvas.attach(label, 1, 1, 1, 1)
		self.canvas.show_all()

		Boton2 = Gtk.Button('Oprimir Respuesta correcta')
		self.canvas.attach(Boton2, 0, 0, 3, 1)
		self.canvas.show_all()
		Boton2.connect('clicked', self.jugar)


	def agregar_style(self):
		pass

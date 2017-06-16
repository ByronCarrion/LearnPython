import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

windows = Gtk.Window()
windows.set_title("Datos personales")
windows.connect("delete-event", Gtk.main_quit)
windows.show()


#age= Gtk.Label("18")
#age.show()
#windows.add(age)

#carnet= Gtk.Label("numero de carnet: 15011650")
#carnet.show()
#windows.add(carnet)


#nivel= Gtk.Label("estudiante de informatica educativa")
#nivel.show()
#windows.add(nivel)

box= Gtk.Box()
box.show()
windows.add(box)


name= Gtk.Label("byron mejia")
name.show()
box.pack_start(name, True, True,0)

def evento(widget):
    exit()


boton=Gtk.Button("salir")
boton.connect("clicked" , evento)
boton.show()
box.pack_start(boton,True,True,0)

#def evento2(widget):
 #   print "hola mundo"

#boton2=Gtk.Button("haz click")
#boton2.connect("clicked" , evento)
#boton2.show()
#caja.add(boton)

Gtk.main()

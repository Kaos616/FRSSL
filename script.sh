#!/bin/bash

# Carga el sistema de mensajes D-Bus
# Especificamos que nos comunique eventos del ScreenSaver de Gnome

# Con un booleano comunicara
# cuando la pantalla este bloqueada (true)
# o cuando este desbloqueada (false)

dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver'" |
  while read x; do
    case "$x" in
	# En el caso true (pantalla bloqueada) ejecuta el programa
	*"boolean true"*) cd / && /home/ka0sd/.lockscreen/face_reco_lockscreen.py;;
	# En el caso false (pantalla desbloqueada) no hace nada
    esac
  done

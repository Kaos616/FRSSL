#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:30:06 2022

@author: ka0sd
"""

### LIBRERIAS ###

from subprocess import call

import face_recognition
import cv2
import numpy as np

### /LIBRERIAS ###

### LOCK SCREEN ###

argumento = {
    True: 'lock-session',
    False: 'unlock-session'
}

def bloqueo(parametro):
    call(('loginctl', argumento[parametro]))

### /LOCK SCREEN ###

### FACE RECO ###

# Referencia a la webcam
capturar_video = cv2.VideoCapture(0)

# Carga una imagen y la codifica
foto_user = face_recognition.load_image_file("/home/ka0sd/.lockscreen/user.jpg")
cara_codificada_user = face_recognition.face_encodings(foto_user)[0]

# Crear array de imagenes con nombres
caras_conocidas = [cara_codificada_user]
nombres_caras_conocidas = ["Nicolas G"]

### /FACE RECO ###

### VARIABLES ###

# Arrays
ubicaciones_caras = []
codificaciones_caras = []
nombres_caras = []

# Booleanos
procesar_frame = True
cerrar = False

### /VARIABLES ###

### PROGRAMA ###

while True:
    # Guarda, para utilizar, el frame actual que esta capturando la cam
    ret, frame = capturar_video.read()

    # Cambia tamano del frame a 1/4 del original para procesar mas rapido
    frame_chico = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convierte la imagen de BGR (de OpenCV) a RGB (para face_recognition)
    frame_chico_rgb = frame_chico[:, :, ::-1]

    # Procesa el frame
    if procesar_frame:
        # Encontrar caras y sus codificaciones en el frame actual
        ubicaciones_caras = face_recognition.face_locations(frame_chico_rgb)
        codificaciones_caras = face_recognition.face_encodings(frame_chico_rgb, ubicaciones_caras)

        for cara_codificada in codificaciones_caras:
            # Ver si la cara detectada coincide con alguna de las conocidas
            coincide = face_recognition.compare_faces(caras_conocidas, cara_codificada)

            # Si encuentra alguna coincidencia en caras_conocidas desbloqueara la computadora
            if True in coincide:
                cerrar = True
                bloqueo(False) #Desbloquea la pantalla
                break

    procesar_frame = not procesar_frame

    if cerrar:
        break

### /PROGRAMA ###

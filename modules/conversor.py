import subprocess

import os

def convert(archivo,tipo):
    input_file = archivo
    nombre_completo = os.path.basename(archivo)   # ej: "buble.m4a"
    nombre, _ = os.path.splitext(nombre_completo)
    output_file = nombre + tipo

    if tipo==".ogg":
        formato="libvorbis"
    elif tipo==".mp3":
        formato="libmp3lame"
    elif tipo==".wav":
        formato="pcm_s16le"

   


    # Comando FFmpeg con codec libvorbis y bitrate fijo
    command = [
        "ffmpeg",
        "-i", input_file,
        "-c:a", formato,  # Codec para OGG
        "-b:a", "192k",       # Bitrate fijo 192 kbps
        output_file
    ]

    # Ejecutar el comando
    subprocess.run(command, check=True)

    print("¡Conversión completa con bitrate de 192 kbps!")
    return True
   


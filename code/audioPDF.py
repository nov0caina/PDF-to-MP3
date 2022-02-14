from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pdftotext
from gtts import gTTS

Tk().withdraw()  # no queremos una GUI completa, así que evita que aparezca la ventana raíz
filelocation = askopenfilename()  # abre el cuadro de diálogo GUI para seleccionar el PDF que queremos convertir a MP3

with open(filelocation, "rb") as f:  # abre el archivo en modo lectura (rb) y llámalo f
    pdf = pdftotext.PDF(f) # almacenar una versión de texto del archivo pdf f en la variable pdf

string_of_text = ''

for text in pdf:
    string_of_text += text

# almacenar archivo en variable
final_file = gTTS(text=string_of_text, lang='es') #currently the language is set to 'es' wich means spanish, if you want to change it to english just use 'en' instead
final_file.save("AudioPDF.mp3")  # guardar archivo en la computadora

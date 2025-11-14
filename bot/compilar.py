import PyInstaller.__main__
import os
import shutil

def compilar_chatbot():
    # Configuración de PyInstaller
    PyInstaller.__main__.run([
        'main.py',
        '--name=ChatbotIA',
        '--onefile',           # Un solo archivo ejecutable
        '--windowed',          # Sin consola (solo ventana)
        '--icon=icon.ico',     # Icono personalizado (opcional)
        '--add-data=title_bar.py;.',
        '--add-data=nltk_processor.py;.',
        '--add-data=chatbot_core.py;.',
        '--add-data=ui_components.py;.',
        '--hidden-import=nltk',
        '--hidden-import=nltk.tokenize',
        '--hidden-import=nltk.corpus',
        '--hidden-import=nltk.stem',
        '--hidden-import=nltk.tag',
        '--hidden-import=tkinter',
        '--hidden-import=datetime',
        '--hidden-import=random',
        '--clean',             # Limpiar archivos temporales
    ])

if __name__ == "__main__":
    compilar_chatbot()
    print("✅ Compilación completada! El ejecutable está en la carpeta 'dist'")
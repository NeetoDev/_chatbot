import tkinter as tk
from tkinter import messagebox

class TitleBar:
    def __init__(self, parent, root_window, title_text):
        self.root_window = root_window
        # Simplemente establecer el título de la ventana
        self.root_window.title(title_text)

    def close_window(self):
        """Cierra la ventana"""
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir del chatbot?"):
            self.root_window.quit()
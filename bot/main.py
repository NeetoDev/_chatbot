import tkinter as tk
import datetime
from title_bar import TitleBar
from nltk_processor import NLTKProcessor
from chatbot_core import ChatbotCore
from ui_components import UIComponents

class ChatbotIA:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot de IA - Trabajo Práctico")
        self.root.geometry("900x650")
        
        # Sistema de temas
        self.modo_oscuro = False
        self.colores_claro = {
            'bg_principal': '#ebf3fb',
            'bg_secundario': '#0054ae',
            'bg_chat': 'white',
            'bg_input': 'white',  # Campo de entrada siempre claro
            'texto_principal': '#2c3e50',
            'texto_secundario': '#0054ae',
            'texto_chat_usuario': '#0054ae',
            'texto_chat_bot': '#2d7d2d',
            'texto_input': '#2c3e50',  # Texto del input
            'borde': '#cccccc'
        }
        self.colores_oscuro = {
            'bg_principal': '#2c3e50',
            'bg_secundario': '#34495e',
            'bg_chat': '#1a1a1a',
            'bg_input': 'white',  # ✅ Campo de entrada MANTIENE fondo blanco
            'texto_principal': '#ecf0f1',
            'texto_secundario': '#3498db',
            'texto_chat_usuario': '#3498db',
            'texto_chat_bot': '#27ae60',
            'texto_input': '#2c3e50',  # ✅ Texto oscuro para contraste con fondo blanco
            'borde': '#7f8c8d'
        }
        
        self.colores_actuales = self.colores_claro
        self.root.configure(bg=self.colores_actuales['bg_principal'])
        
        # Centrar la ventana
        self.center_window()
        
        # Inicializar componentes
        self.nltk_processor = NLTKProcessor()
        self.chatbot_core = ChatbotCore(self.nltk_processor)
        self.ui_components = UIComponents()
        
        # Variables de la UI
        self.chat_area = None
        self.entry = None
        self.entry_var = tk.StringVar()
        self.title_bar = None
        self.main_border = None
        self.main_frame = None
        self.content_frame = None
        
        self.setup_ui()
        self.mostrar_mensaje_bienvenida()
    
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = 900
        height = 650
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def toggle_tema(self):
        """Cambia entre modo claro y oscuro"""
        self.modo_oscuro = not self.modo_oscuro
        
        if self.modo_oscuro:
            self.colores_actuales = self.colores_oscuro
            print("🌙 Modo oscuro activado - Campo de entrada MANTIENE fondo blanco")
        else:
            self.colores_actuales = self.colores_claro
            print("☀️ Modo claro activado")
        
        self.aplicar_tema()
    
    def aplicar_tema(self):
        """Aplica los colores del tema actual a toda la interfaz"""
        # Actualizar ventana principal
        self.root.configure(bg=self.colores_actuales['bg_principal'])
        
        # Actualizar frames principales
        if self.main_border:
            self.main_border.configure(bg=self.colores_actuales['bg_secundario'])
        if self.main_frame:
            self.main_frame.configure(bg=self.colores_actuales['bg_principal'])
        if self.content_frame:
            self.content_frame.configure(bg=self.colores_actuales['bg_principal'])
        
        # Actualizar área de chat
        if self.chat_area:
            self.chat_area.configure(
                bg=self.colores_actuales['bg_chat'],
                fg=self.colores_actuales['texto_principal']
            )
            
            # Actualizar tags del chat
            self.chat_area.tag_config('usuario', foreground=self.colores_actuales['texto_chat_usuario'])
            self.chat_area.tag_config('bot', foreground=self.colores_actuales['texto_chat_bot'])
            self.chat_area.tag_config('sistema', foreground='#e74c3c')
            self.chat_area.tag_config('info', foreground='#f39c12')
            self.chat_area.tag_config('nltk', foreground='#9b59b6')
        
        # ✅ ACTUALIZAR CAMPO DE ENTRADA - FONDO SIEMPRE BLANCO, TEXTO OSCURO
        if self.entry:
            self.entry.configure(
                bg=self.colores_actuales['bg_input'],  # Siempre fondo blanco
                fg=self.colores_actuales['texto_input'],  # Texto oscuro para buen contraste
                insertbackground=self.colores_actuales['texto_input']  # Cursor oscuro
            )
    
    def setup_ui(self):
        """Configura la interfaz gráfica"""
        # Frame principal con borde
        self.main_border = tk.Frame(self.root, bg=self.colores_actuales['bg_secundario'], relief='raised', bd=1)
        self.main_border.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
        
        # Frame principal interno
        self.main_frame = tk.Frame(self.main_border, bg=self.colores_actuales['bg_principal'])
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Barra de título por defecto de Windows
        self.title_bar = TitleBar(self.main_frame, self.root, "Chatbot de IA - Trabajo Práctico")
        
        # Área de contenido principal
        self.content_frame = tk.Frame(self.main_frame, bg=self.colores_actuales['bg_principal'])
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        
        # Header estilo Windows 7
        self.setup_header(self.content_frame)
        
        # Área de conversación
        self.setup_chat_area(self.content_frame)
        
        # Panel de control inferior
        self.setup_control_panel(self.content_frame)
    
    def setup_header(self, parent):
        """Configura el encabezado"""
        header_frame = tk.Frame(parent, bg=self.colores_actuales['bg_principal'])
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Icono y título principal
        icon_frame = tk.Frame(header_frame, bg=self.colores_actuales['bg_principal'])
        icon_frame.pack(fill=tk.X)
        
        tk.Label(
            icon_frame,
            text="🤖",
            font=('Arial', 24),
            bg=self.colores_actuales['bg_principal'],
            fg=self.colores_actuales['texto_secundario']
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        title_frame = tk.Frame(icon_frame, bg=self.colores_actuales['bg_principal'])
        title_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Label(
            title_frame,
            text="CHATBOT DE INTELIGENCIA ARTIFICIAL",
            font=('Segoe UI', 16, 'bold'),
            bg=self.colores_actuales['bg_principal'],
            fg=self.colores_actuales['texto_secundario']
        ).pack(anchor='w')
        
        tk.Label(
            title_frame,
            text="Trabajo Práctico - Prácticas Profesionalizantes II",
            font=('Segoe UI', 10),
            bg=self.colores_actuales['bg_principal'],
            fg=self.colores_actuales['texto_principal']
        ).pack(anchor='w')
        
        # Separador
        from tkinter import ttk
        separator = ttk.Separator(header_frame, orient='horizontal')
        separator.pack(fill=tk.X, pady=5)
    
    def setup_chat_area(self, parent):
        """Configura el área de chat"""
        chat_container = tk.Frame(parent, bg=self.colores_actuales['bg_principal'])
        chat_container.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Etiqueta del área de chat
        chat_label = tk.Label(
            chat_container,
            text="Conversación:",
            font=('Segoe UI', 9, 'bold'),
            bg=self.colores_actuales['bg_principal'],
            fg=self.colores_actuales['texto_secundario']
        )
        chat_label.pack(anchor='w')
        
        # Frame del área de chat con borde
        chat_frame = tk.Frame(chat_container, bg=self.colores_actuales['borde'], relief='sunken', bd=1)
        chat_frame.pack(fill=tk.BOTH, expand=True, pady=(2, 0))
        
        # Área de texto scrollable
        self.chat_area = tk.scrolledtext.ScrolledText(
            chat_frame, 
            wrap=tk.WORD, 
            width=80, 
            height=20,
            font=('Segoe UI', 9),
            bg=self.colores_actuales['bg_chat'],
            fg=self.colores_actuales['texto_principal'],
            relief='flat',
            bd=0,
            padx=5,
            pady=5,
            state=tk.DISABLED
        )
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
        
        # Configurar tags para diferentes tipos de mensajes
        self.chat_area.tag_config('usuario', foreground=self.colores_actuales['texto_chat_usuario'], justify='right')
        self.chat_area.tag_config('bot', foreground=self.colores_actuales['texto_chat_bot'], justify='left')
        self.chat_area.tag_config('sistema', foreground='#e74c3c', justify='center')
        self.chat_area.tag_config('info', foreground='#f39c12', justify='left')
        self.chat_area.tag_config('nltk', foreground='#9b59b6', justify='left')
        
        return self.chat_area, chat_container
    
    def setup_control_panel(self, parent):
        """Configura el panel de control"""
        button_commands = {
            'temas_ia': self.mostrar_temas_ia,
            'estadisticas': self.mostrar_estadisticas,
            'analisis_nltk': self.mostrar_analisis_nltk,
            'limpiar_chat': self.limpiar_chat,
            'ayuda': self.mostrar_ayuda,
            'enviar_mensaje': self.enviar_mensaje,
            'cambiar_tema': self.toggle_tema,
            'salir': self.cerrar_aplicacion
        }
        
        # Frame de entrada
        input_frame = tk.Frame(parent, bg=self.colores_actuales['bg_principal'])
        input_frame.pack(fill=tk.X, pady=(5, 0))
        
        tk.Label(
            input_frame,
            text="Tu mensaje:",
            font=('Segoe UI', 9, 'bold'),
            bg=self.colores_actuales['bg_principal'],
            fg=self.colores_actuales['texto_secundario']
        ).pack(anchor='w')
        
        # ✅ CAMPO DE ENTRADA - SIEMPRE CON FONDO BLANCO Y TEXTO OSCURO
        entry_frame = tk.Frame(input_frame, bg=self.colores_actuales['borde'], relief='sunken', bd=1)
        entry_frame.pack(fill=tk.X, pady=(2, 5))
        
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(
            entry_frame, 
            textvariable=self.entry_var,
            font=('Segoe UI', 10),
            bg=self.colores_actuales['bg_input'],  # ✅ Siempre fondo blanco
            fg=self.colores_actuales['texto_input'],  # ✅ Siempre texto oscuro
            relief='flat',
            bd=0,
            insertbackground=self.colores_actuales['texto_input']  # ✅ Cursor oscuro
        )
        self.entry.pack(fill=tk.X, padx=1, pady=1)
        self.entry.bind('<Return>', self.enviar_mensaje)
        
        # Frame de botones
        buttons_frame = tk.Frame(parent, bg=self.colores_actuales['bg_principal'])
        buttons_frame.pack(fill=tk.X)
        
        # Botones estilo Windows 7
        self.crear_boton(buttons_frame, "📋 Temas IA", button_commands['temas_ia']).pack(side=tk.LEFT, padx=(0, 5))
        self.crear_boton(buttons_frame, "📊 Stats", button_commands['estadisticas']).pack(side=tk.LEFT, padx=(0, 5))
        self.crear_boton(buttons_frame, "🔍 NLTK", button_commands['analisis_nltk']).pack(side=tk.LEFT, padx=(0, 5))
        self.crear_boton(buttons_frame, "🎨 Tema", button_commands['cambiar_tema'], '#9b59b6').pack(side=tk.LEFT, padx=(0, 5))
        self.crear_boton(buttons_frame, "🧹 Limpiar", button_commands['limpiar_chat']).pack(side=tk.LEFT, padx=(0, 5))
        self.crear_boton(buttons_frame, "ℹ️ Ayuda", button_commands['ayuda']).pack(side=tk.LEFT, padx=(0, 5))
        
        # Botón enviar a la derecha
        self.crear_boton(buttons_frame, "➤ Enviar", button_commands['enviar_mensaje'], '#2d7d2d').pack(side=tk.RIGHT, padx=(0, 5))
        
        # Botón salir
        self.crear_boton(buttons_frame, "🚪 Salir", button_commands['salir'], '#e74c3c').pack(side=tk.RIGHT)
    
    def crear_boton(self, parent, text, command, color='#0054ae'):
        """Crea un botón con estilo"""
        return tk.Button(
            parent,
            text=text,
            command=command,
            font=('Segoe UI', 9),
            bg=color,
            fg='white',
            activebackground=self.oscurecer_color(color),
            activeforeground='white',
            relief='raised',
            bd=1,
            padx=12,
            pady=6
        )
    
    def oscurecer_color(self, color):
        """Oscurece un color hexadecimal"""
        rgb = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
        darkened = tuple(max(0, c - 30) for c in rgb)
        return f'#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}'
    
    def cerrar_aplicacion(self):
        """Cierra la aplicación desde el botón salir"""
        from tkinter import messagebox
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir del chatbot?"):
            self.root.quit()
    
    def mostrar_mensaje_bienvenida(self):
        """Muestra mensaje de bienvenida"""
        welcome_text = f"""
🤖 {self.chatbot_core.nombre} - Versión {self.chatbot_core.version}

¡Bienvenido al Chatbot de Inteligencia Artificial!
Ahora con capacidades avanzadas de NLP usando NLTK.

Características NLTK incluidas:
• Tokenización y análisis gramatical
• Análisis de sentimiento avanzado
• Extracción de palabras clave
• Procesamiento de lenguaje natural en español

💡 **Nueva función**: Usa el botón "🎨 Tema" para cambiar entre modo claro y oscuro

Puedes preguntarme sobre:
• Inteligencia Artificial en general
• Aprendizaje automático
• Redes neuronales
• Procesamiento de lenguaje natural
• Y muchos temas más...

Escribe tu pregunta abajo y presiona Enter o el botón Enviar.
        """
        self.agregar_mensaje_chat(welcome_text, 'sistema')
    
    def agregar_mensaje_chat(self, mensaje, tipo='bot'):
        """Agrega un mensaje al área de chat"""
        if self.chat_area is None:
            return
            
        self.chat_area.config(state=tk.NORMAL)
        
        # Agregar timestamp
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        if tipo == 'usuario':
            self.chat_area.insert(tk.END, f"\n[{timestamp}] Tú:\n", 'usuario')
            self.chat_area.insert(tk.END, f"{mensaje}\n", 'usuario')
        elif tipo == 'bot':
            self.chat_area.insert(tk.END, f"\n[{timestamp}] {self.chatbot_core.nombre}:\n", 'bot')
            self.chat_area.insert(tk.END, f"{mensaje}\n", 'bot')
        elif tipo == 'sistema':
            self.chat_area.insert(tk.END, f"\n{'='*50}\n", 'sistema')
            self.chat_area.insert(tk.END, f"{mensaje}\n", 'sistema')
            self.chat_area.insert(tk.END, f"{'='*50}\n", 'sistema')
        elif tipo == 'info':
            self.chat_area.insert(tk.END, f"\n💡 {mensaje}\n", 'info')
        elif tipo == 'nltk':
            self.chat_area.insert(tk.END, f"\n🔍 {mensaje}\n", 'nltk')
        
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)
    
    def enviar_mensaje(self, event=None):
        """Envía el mensaje del usuario y procesa la respuesta"""
        mensaje = self.entry_var.get().strip()
        
        if not mensaje:
            return
        
        # Limpiar campo de entrada
        self.entry_var.set("")
        
        # Mostrar mensaje del usuario
        self.agregar_mensaje_chat(mensaje, 'usuario')
        
        # Procesar y mostrar respuesta (con pequeña demora para simular pensamiento)
        self.root.after(500, self.procesar_y_mostrar_respuesta, mensaje)
    
    def procesar_y_mostrar_respuesta(self, mensaje):
        """Procesa el mensaje y muestra la respuesta"""
        try:
            respuesta = self.chatbot_core.procesar_mensaje(mensaje)
            self.agregar_mensaje_chat(respuesta, 'bot')
        except Exception as e:
            error_msg = f"Lo siento, hubo un error procesando tu mensaje. El chatbot funciona en modo básico.\n\nError técnico: {str(e)}"
            # Respuesta de fallback
            fallback_responses = [
                "Hola! Soy tu asistente de IA. ¿En qué puedo ayudarte?",
                "Interesante pregunta. ¿Podrías reformularla?",
                "Estoy aquí para ayudarte con temas de Inteligencia Artificial.",
                "¿Te gustaría aprender sobre machine learning, redes neuronales o otros temas de IA?"
            ]
            import random
            fallback = random.choice(fallback_responses)
            self.agregar_mensaje_chat(fallback, 'bot')
    
    def mostrar_temas_ia(self):
        """Muestra los temas de IA disponibles"""
        temas = self.chatbot_core.obtener_temas_ia()
        temas_texto = "🎯 **TEMAS DE IA DISPONIBLES:**\n\n"
        for i, tema in enumerate(temas, 1):
            temas_texto += f"{i}. {tema.title()}\n"
        
        temas_texto += "\nPregunta sobre cualquiera de estos temas para obtener información detallada."
        self.agregar_mensaje_chat(temas_texto, 'info')
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas de la conversación"""
        stats = self.chatbot_core.obtener_estadisticas()
        
        stats_text = f"""
📊 **ESTADÍSTICAS DE LA CONVERSACIÓN**

• Mensajes intercambiados: {stats['total_mensajes']}
• Hora actual: {stats['hora_actual']}
• Versión del chatbot: {stats['version']}
• Temas de IA disponibles: {stats['temas_disponibles']}
• Tema actual: {'🌙 Oscuro' if self.modo_oscuro else '☀️ Claro'}
• Capacidades NLTK: Tokenización, Análisis de Sentimiento, POS Tagging

💡 **Consejo:** Usa el botón '🎨 Tema' para cambiar el color del fondo
        """
        self.agregar_mensaje_chat(stats_text, 'info')
    
    def mostrar_analisis_nltk(self):
        """Muestra un análisis NLTK del último mensaje"""
        if not self.chatbot_core.historial or not any(m.startswith("Usuario:") for m in self.chatbot_core.historial):
            self.agregar_mensaje_chat("No hay mensajes recientes para analizar. Escribe algo primero.", 'info')
            return
        
        # Obtener el último mensaje del usuario
        ultimo_mensaje = None
        for mensaje in reversed(self.chatbot_core.historial):
            if mensaje.startswith("Usuario:"):
                ultimo_mensaje = mensaje.replace("Usuario: ", "")
                break
        
        if ultimo_mensaje:
            # Análisis completo con NLTK
            analisis_completo = self.generar_analisis_completo(ultimo_mensaje)
            self.agregar_mensaje_chat(analisis_completo, 'nltk')
        else:
            self.agregar_mensaje_chat("No se encontraron mensajes para analizar.", 'info')
    
    def generar_analisis_completo(self, texto):
        """Genera análisis completo NLTK"""
        try:
            estructura = self.nltk_processor.analizar_estructura_detallada(texto)
            sentimiento = self.nltk_processor.analizar_sentimiento_detallado(texto)
            palabras_clave = self.nltk_processor.analizar_palabras_clave_detallado(texto)
            metricas = self.nltk_processor.analizar_metricas_generales(texto)
            
            return f"""
🔍 **ANÁLISIS NLTK COMPLETO - ÚLTIMO MENSAJE**

📝 **Texto analizado:** "{texto}"

📊 **Análisis de Estructura:**
• Oraciones: {estructura['oraciones']}
• Tokens/Palabras: {estructura['tokens']}
• Sustantivos: {estructura['sustantivos']}
• Verbos: {estructura['verbos']}
• Adjetivos: {estructura['adjetivos']}

🎭 **Análisis de Sentimiento:**
• Sentimiento general: {sentimiento['sentimiento'].upper()}
• Palabras positivas: {sentimiento['positivas']} ({sentimiento['porcentaje_positivo']:.1f}%)
• Palabras negativas: {sentimiento['negativas']} ({sentimiento['porcentaje_negativo']:.1f}%)
• Total palabras con sentimiento: {sentimiento['total']}

🔑 **Palabras Clave:**
• Palabras clave identificadas: {', '.join(palabras_clave['palabras_clave']) if palabras_clave['palabras_clave'] else 'No identificadas'}
• Total de palabras únicas: {palabras_clave['total_palabras_unicas']}

📈 **Métricas Generales:**
• Longitud del texto: {metricas['longitud_texto']} caracteres
• Palabras después de limpieza: {metricas['palabras_limpias']}
• Densidad léxica: {metricas['densidad_lexica']:.1f}%
            """
        except Exception as e:
            return f"Error en el análisis NLTK: {str(e)}"
    
    def limpiar_chat(self):
        """Limpia el área de chat"""
        if self.chat_area:
            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.delete(1.0, tk.END)
            self.chat_area.config(state=tk.DISABLED)
            self.chatbot_core.limpiar_historial()
            self.mostrar_mensaje_bienvenida()
    
    def mostrar_ayuda(self):
        """Muestra ayuda para usar el chatbot"""
        ayuda_texto = f"""
🆘 **AYUDA - CÓMO USAR EL CHATBOT**

**Comandos disponibles:**
• Escribe normalmente para conversar sobre IA
• Usa los botones inferiores para funciones especiales
• Presiona Enter para enviar mensajes rápidamente

**Nuevas características:**
• 🎨 **Cambio de tema**: Usa el botón "Tema" para cambiar entre modo claro y oscuro
• 🔍 **Análisis NLTK**: Análisis avanzado de texto
• 📊 **Estadísticas**: Información de la conversación

**Temas que puedo explicar:**
• Fundamentos de Inteligencia Artificial
• Aprendizaje automático y deep learning
• Redes neuronales y PLN
• Aplicaciones prácticas de IA

**Controles de ventana:**
• Usa los controles estándar de Windows
• Botón "🎨 Tema" para cambiar colores
• Botón "🚪 Salir" para cerrar la aplicación

**Tema actual:** {'🌙 Modo oscuro' if self.modo_oscuro else '☀️ Modo claro'}
        """
        self.agregar_mensaje_chat(ayuda_texto, 'info')

def main():
    """Función principal"""
    try:
        root = tk.Tk()
        app = ChatbotIA(root)
        root.mainloop()
    except Exception as e:
        print(f"Error iniciando la aplicación: {e}")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()
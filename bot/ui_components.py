import tkinter as tk
from tkinter import ttk, scrolledtext

class UIComponents:
    def __init__(self):
        pass
    
    @staticmethod
    def create_button(parent, text, command, color='#0054ae'):
        """Crea un botón con estilo Windows 7"""
        return tk.Button(
            parent,
            text=text,
            command=command,
            font=('Segoe UI', 9),
            bg=color,
            fg='white',
            activebackground=UIComponents.darken_color(color),
            activeforeground='white',
            relief='raised',
            bd=1,
            padx=12,
            pady=6
        )
    
    @staticmethod
    def darken_color(color):
        """Oscurece un color hexadecimal"""
        rgb = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
        darkened = tuple(max(0, c - 30) for c in rgb)
        return f'#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}'
    
    @staticmethod
    def setup_chat_area(parent):
        """Configura el área de chat estilo Windows 7"""
        chat_container = tk.Frame(parent, bg='#ebf3fb')
        chat_container.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Etiqueta del área de chat
        chat_label = tk.Label(
            chat_container,
            text="Conversación:",
            font=('Segoe UI', 9, 'bold'),
            bg='#ebf3fb',
            fg='#0054ae'
        )
        chat_label.pack(anchor='w')
        
        # Frame del área de chat con borde
        chat_frame = tk.Frame(chat_container, bg='#cccccc', relief='sunken', bd=1)
        chat_frame.pack(fill=tk.BOTH, expand=True, pady=(2, 0))
        
        # Área de texto scrollable
        chat_area = scrolledtext.ScrolledText(
            chat_frame, 
            wrap=tk.WORD, 
            width=80, 
            height=20,
            font=('Segoe UI', 9),
            bg='white',
            fg='#2c3e50',
            relief='flat',
            bd=0,
            padx=5,
            pady=5,
            state=tk.DISABLED
        )
        chat_area.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
        
        # Configurar tags para diferentes tipos de mensajes
        chat_area.tag_config('usuario', foreground='#0054ae', justify='right')
        chat_area.tag_config('bot', foreground='#2d7d2d', justify='left')
        chat_area.tag_config('sistema', foreground='#d0453e', justify='center')
        chat_area.tag_config('info', foreground='#e67e22', justify='left')
        chat_area.tag_config('nltk', foreground='#8e44ad', justify='left')
        
        return chat_area, chat_container
    
    @staticmethod
    def setup_header(parent):
        """Configura el encabezado estilo Windows 7"""
        header_frame = tk.Frame(parent, bg='#ebf3fb')
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Icono y título principal
        icon_frame = tk.Frame(header_frame, bg='#ebf3fb')
        icon_frame.pack(fill=tk.X)
        
        tk.Label(
            icon_frame,
            text="🤖",
            font=('Arial', 24),
            bg='#ebf3fb',
            fg='#0054ae'
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        title_frame = tk.Frame(icon_frame, bg='#ebf3fb')
        title_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Label(
            title_frame,
            text="CHATBOT DE INTELIGENCIA ARTIFICIAL",
            font=('Segoe UI', 16, 'bold'),
            bg='#ebf3fb',
            fg='#0054ae'
        ).pack(anchor='w')
        
        tk.Label(
            title_frame,
            text="Trabajo Práctico - Prácticas Profesionalizantes II",
            font=('Segoe UI', 10),
            bg='#ebf3fb',
            fg='#666666'
        ).pack(anchor='w')
        
        # Separador estilo Windows 7
        separator = ttk.Separator(header_frame, orient='horizontal')
        separator.pack(fill=tk.X, pady=5)
        
        return header_frame
    
    @staticmethod
    def setup_control_panel(parent, button_commands):
        """Configura el panel de control inferior"""
        # Frame de entrada
        input_frame = tk.Frame(parent, bg='#ebf3fb')
        input_frame.pack(fill=tk.X, pady=(5, 0))
        
        tk.Label(
            input_frame,
            text="Tu mensaje:",
            font=('Segoe UI', 9, 'bold'),
            bg='#ebf3fb',
            fg='#0054ae'
        ).pack(anchor='w')
        
        # Campo de entrada con estilo Windows 7
        entry_frame = tk.Frame(input_frame, bg='#cccccc', relief='sunken', bd=1)
        entry_frame.pack(fill=tk.X, pady=(2, 5))
        
        entry_var = tk.StringVar()
        entry = tk.Entry(
            entry_frame, 
            textvariable=entry_var,
            font=('Segoe UI', 10),
            bg='white',
            fg='#2c3e50',
            relief='flat',
            bd=0,
            insertbackground='#2c3e50'
        )
        entry.pack(fill=tk.X, padx=1, pady=1)
        
        # Frame de botones
        buttons_frame = tk.Frame(parent, bg='#ebf3fb')
        buttons_frame.pack(fill=tk.X)
        
        # Botones estilo Windows 7
        UIComponents.create_windows7_button(
            buttons_frame, 
            "📋 Temas de IA", 
            button_commands['temas_ia']
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        UIComponents.create_windows7_button(
            buttons_frame, 
            "📊 Estadísticas", 
            button_commands['estadisticas']
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        UIComponents.create_windows7_button(
            buttons_frame, 
            "🔍 Análisis NLTK", 
            button_commands['analisis_nltk']
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        UIComponents.create_windows7_button(
            buttons_frame, 
            "🧹 Limpiar Chat", 
            button_commands['limpiar_chat']
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        UIComponents.create_windows7_button(
            buttons_frame, 
            "ℹ️ Ayuda", 
            button_commands['ayuda']
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        # Botón enviar a la derecha
        UIComponents.create_windows7_button(
            buttons_frame, 
            "➤ Enviar Mensaje", 
            button_commands['enviar_mensaje'],
            '#2d7d2d'
        ).pack(side=tk.RIGHT, padx=(0, 5))
        
        # Botón salir
        UIComponents.create_windows7_button(
            buttons_frame, 
            "🚪 Salir", 
            button_commands['salir'],
            '#d0453e'
        ).pack(side=tk.RIGHT)
        
        return entry, entry_var, buttons_frame
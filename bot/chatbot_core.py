import random
import datetime

class ChatbotCore:
    def __init__(self, nltk_processor):
        self.nltk_processor = nltk_processor
        self.nombre = "NEET"
        self.creador = "Martín Cruz Vince"
        self.version = "0.8.1c"
        self.historial = []
        
        # Temas de IA en español e inglés - ORDENADOS POR PRIORIDAD
        self.temas_ia = [
            "machine learning",  # PRIMERO los términos en inglés
            "deep learning",
            "artificial intelligence", 
            "neural networks",
            "natural language processing",
            "computer vision",
            "robotics",
            "expert systems",
            "genetic algorithms",
            "aprendizaje automático",  # LUEGO los términos en español
            "redes neuronales",
            "procesamiento de lenguaje natural",
            "visión computerizada", 
            "robótica",
            "sistemas expertos",
            "algoritmos genéticos",
            "inteligencia artificial"
        ]
        
        # Mapeo de términos en inglés a español
        self.mapeo_terminos = {
            "machine learning": "machine learning",  # Mantener en inglés para respuestas
            "deep learning": "deep learning",
            "computer vision": "computer vision",
            "natural language processing": "natural language processing",
            "neural networks": "neural networks",
            "artificial intelligence": "artificial intelligence",
            "robotics": "robotics",
            "expert systems": "expert systems",
            "genetic algorithms": "genetic algorithms"
        }
        
        # Términos relacionados y sinónimos - MÁS ESPECÍFICOS
        self.terminos_relacionados = {
            "ml": "machine learning",
            "ia": "artificial intelligence", 
            "ai": "artificial intelligence",
            "pln": "natural language processing",
            "nlp": "natural language processing", 
            "cv": "computer vision",
            "dl": "deep learning",
            "nn": "neural networks",
            "red neuronal": "neural networks",
            "redes neurales": "neural networks",
            "automático": "machine learning",
            "automática": "machine learning",
            "aprendizaje maquina": "machine learning",
            "aprendizaje de máquinas": "machine learning",
            "mlp": "machine learning"
        }
        
        # Respuestas predefinidas
        self.respuestas_ia = {
            "aprendizaje automático": [
                "El **aprendizaje automático** (Machine Learning) es una rama de la IA que permite a las computadoras aprender sin ser programadas explícitamente. Se basa en algoritmos que identifican patrones en datos.",
                "El **Machine Learning** usa datos para entrenar modelos que pueden hacer predicciones. Existen tres tipos principales:\n• **Supervisado**: Con datos etiquetados\n• **No supervisado**: Sin etiquetas  \n• **Por refuerzo**: Basado en recompensas",
                "El **aprendizaje automático** incluye técnicas como:\n• Regresión lineal\n• Árboles de decisión\n• SVM (Máquinas de Vectores de Soporte)\n• Redes neuronales artificiales\n• Clustering"
            ],
            "machine learning": [
                "**Machine Learning** es el corazón de la IA moderna. Permite a los sistemas mejorar automáticamente con la experiencia mediante algoritmos que aprenden de datos.",
                "Los algoritmos de **ML** pueden clasificar datos, hacer predicciones y encontrar patrones ocultos en grandes conjuntos de datos. Es fundamental para:\n• Sistemas de recomendación\n• Detección de fraudes\n• Vehículos autónomos\n• Asistentes virtuales",
                "**Machine Learning** se divide en:\n🔹 **Aprendizaje supervisado**: Con ejemplos etiquetados\n🔹 **Aprendizaje no supervisado**: Descubriendo patrones\n🔹 **Aprendizaje por refuerzo**: Aprendiendo por prueba y error"
            ],
            "redes neuronales": [
                "Las **redes neuronales artificiales** imitan el funcionamiento del cerebro humano. Están compuestas de neuronas artificiales interconectadas organizadas en capas.",
                "El **aprendizaje profundo** (Deep Learning) usa redes neuronales con muchas capas ocultas para resolver problemas complejos como reconocimiento de imágenes y lenguaje natural.",
                "Las **redes neuronales** tienen:\n• **Capa de entrada**: Recibe los datos\n• **Capas ocultas**: Procesan la información\n• **Capa de salida**: Produce el resultado\n• **Funciones de activación**: Como ReLU o sigmoid"
            ],
            "neural networks": [
                "**Neural Networks** are computing systems inspired by the human brain. They consist of interconnected nodes (neurons) organized in layers.",
                "**Deep Learning** uses neural networks with many hidden layers to solve complex problems like image recognition and natural language processing.",
                "Key components of **neural networks**:\n• Input layer\n• Hidden layers  \n• Output layer\n• Activation functions\n• Weights and biases"
            ],
            "deep learning": [
                "El **deep learning** es un subcampo del machine learning que utiliza redes neuronales profundas con múltiples capas.",
                "Es especialmente efectivo para tareas complejas como:\n• Reconocimiento de imágenes (CNN)\n• Procesamiento de lenguaje (RNN, Transformers)\n• Juegos (AlphaGo)\n• Vehículos autónomos",
                "El **aprendizaje profundo** requiere:\n• Grandes cantidades de datos\n• Potencia computacional\n• Arquitecturas especializadas como CNN, RNN, GAN"
            ],
            "procesamiento de lenguaje natural": [
                "El **PLN** permite a las computadoras entender, interpretar y generar lenguaje humano. ¡Es la tecnología que me permite conversar contigo!",
                "**ChatGPT**, los asistentes virtuales y los traductores automáticos son ejemplos de aplicaciones de PLN.",
                "Técnicas de **PLN** incluyen:\n• Tokenización\n• Análisis de sentimientos\n• Reconocimiento de entidades\n• Traducción automática\n• Generación de texto"
            ],
            "natural language processing": [
                "**NLP** (Natural Language Processing) enables computers to understand, interpret, and generate human language.",
                "**ChatGPT**, virtual assistants, and machine translators are examples of NLP applications.",
                "**NLP** techniques include:\n• Tokenization\n• Sentiment analysis\n• Named entity recognition\n• Machine translation\n• Text generation"
            ],
            "visión computerizada": [
                "La **visión computerizada** permite a las máquinas 'ver' e interpretar imágenes y videos.",
                "Se usa en:\n• Diagnóstico médico\n• Vehículos autónomos\n• Reconocimiento facial\n• Control de calidad industrial",
                "Las **redes neuronales convolucionales (CNN)** son especialmente efectivas para tareas de visión por computadora."
            ],
            "computer vision": [
                "**Computer Vision** enables machines to 'see' and interpret images and videos.",
                "Used in:\n• Medical diagnosis\n• Autonomous vehicles\n• Facial recognition\n• Industrial quality control",
                "**Convolutional Neural Networks (CNNs)** are particularly effective for computer vision tasks."
            ],
            "inteligencia artificial": [
                "La **IA** es el campo de la informática que crea sistemas capaces de realizar tareas que normalmente requieren inteligencia humana.",
                "La **IA** incluye:\n• Aprendizaje automático\n• Razonamiento\n• Planificación\n• Percepción\n• Comprensión del lenguaje natural",
                "Áreas de la **IA**:\n• Machine Learning\n• Robótica\n• Procesamiento de lenguaje natural\n• Visión por computadora\n• Sistemas expertos"
            ],
            "artificial intelligence": [
                "**AI** is the field of computer science that creates systems capable of performing tasks that normally require human intelligence.",
                "**AI** includes:\n• Machine Learning\n• Reasoning\n• Planning\n• Perception\n• Natural language understanding",
                "**AI** subfields:\n• Machine Learning\n• Robotics\n• Natural Language Processing\n• Computer Vision\n• Expert Systems"
            ],
            "robótica": [
                "La **robótica** combina IA con ingeniería para crear robots que pueden realizar tareas autónomamente.",
                "Los robots modernos usan IA para:\n• Navegación\n• Manipulación de objetos\n• Toma de decisiones\n• Interacción humana",
                "Aplicaciones de **robótica** con IA:\n• Robots industriales\n• Robots de servicio\n• Drones autónomos\n• Robots médicos"
            ],
            "robotics": [
                "**Robotics** combines AI with engineering to create robots that can perform tasks autonomously.",
                "Modern robots use AI for:\n• Navigation\n• Object manipulation\n• Decision-making\n• Human interaction",
                "**AI** applications in robotics:\n• Industrial robots\n• Service robots\n• Autonomous drones\n• Medical robots"
            ],
            "sistemas expertos": [
                "Los **sistemas expertos** son programas de IA que imitan la capacidad de decisión de un experto humano en un dominio específico.",
                "Usan:\n• Bases de conocimiento\n• Reglas de inferencia\n• Motor de inferencia",
                "Ejemplos de **sistemas expertos**:\n• Diagnóstico médico\n• Análisis financiero\n• Soporte técnico\n• Planificación de proyectos"
            ],
            "expert systems": [
                "**Expert systems** are AI programs that mimic the decision-making ability of a human expert in a specific domain.",
                "They use:\n• Knowledge bases\n• Inference rules\n• Inference engine",
                "Examples of **expert systems**:\n• Medical diagnosis\n• Financial analysis\n• Technical support\n• Project planning"
            ],
            "algoritmos genéticos": [
                "Los **algoritmos genéticos** son técnicas de optimización inspiradas en la evolución natural.",
                "Usan conceptos de:\n• Selección natural\n• Cruce (crossover)\n• Mutación\n• Fitness function",
                "Aplicaciones de **algoritmos genéticos**:\n• Optimización de rutas\n• Diseño de circuitos\n• Aprendizaje automático\n• Planificación de horarios"
            ],
            "genetic algorithms": [
                "**Genetic algorithms** are optimization techniques inspired by natural evolution.",
                "They use concepts of:\n• Natural selection\n• Crossover\n• Mutation\n• Fitness function",
                "**Genetic algorithms** applications:\n• Route optimization\n• Circuit design\n• Machine learning\n• Scheduling problems"
            ]
        }
    
    def normalizar_tema(self, tema):
        """Normaliza el tema manteniendo el idioma original"""
        tema_lower = tema.lower().strip()
        
        # Primero verificar si está en el mapeo directo
        if tema_lower in self.mapeo_terminos:
            return self.mapeo_terminos[tema_lower]
        
        # Verificar términos relacionados
        if tema_lower in self.terminos_relacionados:
            return self.terminos_relacionados[tema_lower]
        
        return tema_lower
    
    def reconocer_tema_ia(self, texto):
        """Identifica si el texto menciona temas de IA - MÁS ROBUSTO"""
        texto_min = texto.lower()
        
        print(f"🔍 Analizando: '{texto}'")  # Debug para ver qué está llegando
        
        # 1. Búsqueda DIRECTA y EXACTA primero
        for tema in self.temas_ia:
            # Buscar el tema como palabra completa (case insensitive)
            if tema in texto_min:
                print(f"✅ Tema detectado: {tema}")
                return self.normalizar_tema(tema)
        
        # 2. Búsqueda de términos relacionados
        for termino, tema_mapeado in self.terminos_relacionados.items():
            if termino in texto_min:
                print(f"✅ Término relacionado: {termino} -> {tema_mapeado}")
                return self.normalizar_tema(tema_mapeado)
        
        print("❌ No se detectó tema específico")
        return None
    
    def generar_respuesta_ia(self, tema):
        """Genera respuestas informativas sobre IA"""
        tema_normalizado = self.normalizar_tema(tema)
        print(f"🎯 Generando respuesta para: {tema_normalizado}")
        
        if tema_normalizado in self.respuestas_ia:
            return random.choice(self.respuestas_ia[tema_normalizado])
        elif tema in self.respuestas_ia:
            return random.choice(self.respuestas_ia[tema])
        else:
            return f"🤖 **{tema.title()}**\n\nEs un área fascinante de la Inteligencia Artificial. ¿Qué aspecto específico te interesa conocer más?\n\nPuedo explicarte:\n• Conceptos fundamentales\n• Aplicaciones prácticas\n• Tecnologías relacionadas\n• Casos de uso reales"
    
    def procesar_mensaje(self, mensaje):
        """Procesa el mensaje del usuario - ORDEN CORREGIDO"""
        mensaje_lower = mensaje.lower().strip()
        
        print(f"\n📨 Mensaje recibido: '{mensaje}'")  # Debug
        
        # Guardar en historial
        self.historial.append(f"Usuario: {mensaje}")
        
        # 1. PRIMERO: Detección de temas específicos de IA (ANTES de saludos)
        tema_ia = self.reconocer_tema_ia(mensaje)
        if tema_ia:
            print(f"🎯 Tema identificado: {tema_ia}")
            # Análisis de sentimiento para personalizar respuesta
            sentimiento, positivas, negativas = self.nltk_processor.analizar_sentimiento_avanzado(mensaje)
            respuesta_ia = self.generar_respuesta_ia(tema_ia)
            
            if sentimiento == "positivo":
                return f"¡Excelente pregunta sobre **{tema_ia}**! 😊\n\n{respuesta_ia}"
            elif sentimiento == "negativo":
                return f"Entiendo que **{tema_ia}** puede parecer complejo. Te explico:\n\n{respuesta_ia}"
            else:
                return f"**Sobre {tema_ia}**:\n\n{respuesta_ia}"
        
        # 2. LUEGO: Detección de saludos (SOLO si no se detectó tema)
        saludos = ['hola','buenos dias', 'buenos días', 'buenas tardes', 'buenas noches', 'hey', 'hi', 'hello', 'buen día', 'buen dia', 'good morning', 'good afternoon']
        if any(saludo in mensaje_lower for saludo in saludos):
            return random.choice([
                "¡Hola! Soy tu asistente de IA especializado. ¿En qué tema de Inteligencia Artificial te puedo ayudar? 🤖",
                "¡Buen día! Estoy aquí para ayudarte con Machine Learning, Redes Neuronales y otros temas de IA.",
                "¡Hola! ¿Listo para explorar el fascinante mundo de la IA? Puedo explicarte sobre machine learning, deep learning y más."
            ])
        
        # 3. Detección de despedida
        despedidas = ['adiós', 'adios', 'chau', 'hasta luego', 'nos vemos', 'salir', 'bye', 'hasta pronto', 'goodbye', 'exit', 'quit']
        if any(despedida in mensaje_lower for despedida in despedidas):
            return "¡Ha sido un gusto conversar contigo! Espero haberte ayudado con tu investigación sobre IA. ¡Éxito con tu trabajo práctico! 🎓"
        
        # 4. Preguntas específicas sobre IA
        if 'qué es machine learning' in mensaje_lower or 'que es machine learning' in mensaje_lower:
            return self.generar_respuesta_ia("machine learning")
            
        if 'qué es ia' in mensaje_lower or 'qué es la inteligencia artificial' in mensaje_lower or 'que es la ia' in mensaje_lower  or 'what is ai' in mensaje_lower:
            return "La **Inteligencia Artificial** es el campo de la informática que desarrolla sistemas capaces de realizar tareas que normalmente requieren inteligencia humana: aprendizaje, razonamiento, percepción y toma de decisiones."
        
        if 'tipos de ia' in mensaje_lower or 'types of ai' in mensaje_lower:
            return "Existen principalmente **tres tipos de IA**:\n\n🔹 **IA Débil**: Especializada en tareas específicas (como yo)\n🔹 **IA Fuerte**: Hipotética, con inteligencia general comparable a humanos\n🔹 **IA Superinteligente**: Concepto futurista que superaría todas las capacidades humanas"
        
        if 'ejemplos de ia' in mensaje_lower or 'aplicaciones de ia' in mensaje_lower or 'examples of ai' in mensaje_lower:
            return "**Ejemplos prácticos de IA**:\n\n• 🤖 Asistentes virtuales (Siri, Alexa, yo mismo)\n• 🚗 Vehículos autónomos (Tesla)\n• 🎬 Sistemas de recomendación (Netflix, Spotify)\n• 🏥 Diagnóstico médico asistido\n• 🌐 Traductores automáticos (Google Translate)\n• 💳 Detección de fraudes bancarios\n• 📸 Reconocimiento facial"
        
        # 5. Pregunta sobre NLTK
        if 'nltk' in mensaje_lower or 'procesamiento' in mensaje_lower or 'lenguaje natural' in mensaje_lower:
            return "¡Sí! Uso NLTK (Natural Language Toolkit) para procesar tu lenguaje. Puedo:\n• Analizar estructura de oraciones\n• Identificar sentimientos\n• Extraer palabras clave\n• Hacer análisis gramatical\n\n¿Quieres ver un análisis detallado de algún texto?"
        
        # 6. Pregunta sobre el chatbot
        if 'quién eres' in mensaje_lower or 'quien eres' in mensaje_lower or 'qué eres' in mensaje_lower or 'que eres' in mensaje_lower or 'who are you' in mensaje_lower:
            return f"Soy un chatbot educativo especializado en IA, con capacidades NLTK. Creado por {(self.creador)} para el trabajo práctico de IA. Mi propósito es demostrar aplicaciones prácticas de PLN y sistemas basados en reglas."
        
        if 'cómo estás' in mensaje_lower or 'como estas' in mensaje_lower or 'how are you' in mensaje_lower:
            sentimiento, positivas, negativas = self.nltk_processor.analizar_sentimiento_avanzado(mensaje)
            return f"¡Analizando texto con NLTK perfectamente! Detecté que tu mensaje tiene sentimiento {sentimiento}. ¿En qué más puedo ayudarte?"
        
        # 7. Pregunta sobre el trabajo práctico
        if 'trabajo práctico' in mensaje_lower or 'trabajo practico' in mensaje_lower or 'práctica' in mensaje_lower or 'proyecto' in mensaje_lower or 'practical work' in mensaje_lower:
            return """**Para tu trabajo práctico**, te sugiero esta estructura:

📋 **Estructura recomendada**:
1. **Introducción**: Definición y evolución de la IA
2. **Fundamentos teóricos**: Historia, tipos y tecnologías
3. **Parte práctica**: Esta demostración con el chatbot + NLTK
4. **Impacto social**: Ventajas, desafíos y futuro
5. **Conclusión**: Reflexiones personales

¿Te ayudo con alguna sección específica?"""
        
        # 8. FINALMENTE: Respuesta por defecto
        sentimiento, positivas, negativas = self.nltk_processor.analizar_sentimiento_avanzado(mensaje)
        palabras_clave = self.nltk_processor.extraer_palabras_clave(mensaje)
        estructura = self.nltk_processor.analizar_estructura(mensaje)
        
        return self.generar_respuesta_por_defecto(sentimiento, positivas, negativas, palabras_clave, estructura)
    
    def generar_respuesta_por_defecto(self, sentimiento, positivas, negativas, palabras_clave, estructura):
        """Genera respuesta por defecto"""
        respuestas = [
            f"¿Te interesa aprender sobre **Machine Learning**, **Redes Neuronales** u otros temas de **Inteligencia Artificial**? Puedo explicarte conceptos fundamentales, aplicaciones prácticas y casos de uso reales.",
            f"Detecté palabras clave como: **{', '.join(palabras_clave) if palabras_clave else 'IA y tecnología'}**. ¿En qué tema específico de Inteligencia Artificial te puedo ayudar?",
            f"Como especialista en IA, puedo explicarte sobre:\n\n• 🤖 **Machine Learning** y sus aplicaciones\n• 🧠 **Redes Neuronales** y Deep Learning\n• 💬 **Procesamiento de Lenguaje Natural** (NLP)\n• 👁️ **Visión por Computadora**\n• 🏥 **IA en medicina** y otros campos\n\n¿Cuál te interesa más?",
            f"Parece que buscas información sobre **Inteligencia Artificial**. ¿Te gustaría que te explique algún concepto específico como Machine Learning, Redes Neuronales o alguna aplicación práctica?"
        ]
        
        return random.choice(respuestas)
    
    def obtener_estadisticas(self):
        """Obtiene estadísticas de la conversación"""
        total_mensajes = len([m for m in self.historial if m.startswith("Usuario")])
        tiempo_actual = datetime.datetime.now().strftime("%H:%M:%S")
        
        return {
            'total_mensajes': total_mensajes,
            'hora_actual': tiempo_actual,
            'version': self.version,
            'temas_disponibles': len(self.temas_ia)
        }
    
    def obtener_temas_ia(self):
        """Retorna la lista de temas de IA disponibles"""
        temas_principales = [
            "Machine Learning (Aprendizaje Automático)",
            "Redes Neuronales (Neural Networks)", 
            "Deep Learning (Aprendizaje Profundo)",
            "Procesamiento de Lenguaje Natural (NLP)",
            "Visión por Computadora (Computer Vision)",
            "Inteligencia Artificial (AI)"
        ]
        return temas_principales
    
    def limpiar_historial(self):
        """Limpia el historial de conversación"""
        self.historial.clear()
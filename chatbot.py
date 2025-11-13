import nltk
import random
import datetime
import json

class Chatbot:
    def __init__(self):
        self.nombre = "ChatBotIA"
        self.conversaciones = []
        self.aprendizaje = {}
        
        # Base de conocimiento expandida
        self.base_conocimiento = {
            "ia": "La Inteligencia Artificial permite a las máquinas aprender y tomar decisiones.",
            "python": "Python es un lenguaje de programación muy usado en IA por su simplicidad.",
            "aprendizaje": "Machine Learning es cuando las computadoras aprenden de datos sin programación explícita.",
            "clima": "No tengo acceso en tiempo real al clima, pero puedo ayudarte con otras cosas."
        }
    
    def procesar_mensaje(self, mensaje):
        mensaje = mensaje.lower()
        
        # Guardar conversación
        self.conversaciones.append(("usuario", mensaje))
        
        # Detectar intención
        if any(palabra in mensaje for palabra in ["hola", "buenos días", "buenas tardes"]):
            return self.saludar()
        elif "hora" in mensaje:
            return self.decir_hora()
        elif "fecha" in mensaje or "día" in mensaje:
            return self.decir_fecha()
        elif "chiste" in mensaje:
            return self.contar_chiste()
        elif "que es" in mensaje:
            return self.explicar_concepto(mensaje)
        elif "gracias" in mensaje:
            return "¡De nada! Estoy aquí para ayudarte 😊"
        elif "adios" in mensaje or "chao" in mensaje:
            return "¡Hasta luego! Fue un gusto conversar contigo."
        else:
            return self.respuesta_generica()
    
    def saludar(self):
        saludos = [
            f"¡Hola! Soy {self.nombre}, ¿en qué puedo ayudarte?",
            "¡Buen día! ¿Cómo estás hoy?",
            "¡Hola! Encantado de conocerte 😊"
        ]
        return random.choice(saludos)
    
    def decir_hora(self):
        ahora = datetime.datetime.now()
        return f"Son las {ahora.strftime('%H:%M')}"
    
    def decir_fecha(self):
        ahora = datetime.datetime.now()
        return f"Hoy es {ahora.strftime('%A %d de %B de %Y')}"
    
    def contar_chiste(self):
        chistes = [
            "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
            "¿Qué hace un perro con un taladro? ¡Taladrando!",
            "¿Qué hace un pez? Nada."
        ]
        return random.choice(chistes)
    
    def explicar_concepto(self, mensaje):
        for concepto, explicacion in self.base_conocimiento.items():
            if concepto in mensaje:
                return f"{concepto.upper()}: {explicacion}"
        return "No tengo información sobre ese concepto específico. ¿Podrías preguntarme sobre IA, Python o aprendizaje automático?"
    
    def respuesta_generica(self):
        respuestas = [
            "Interesante, ¿puedes contarme más?",
            "No estoy seguro de entender completamente. ¿Podrías reformular?",
            "Eso suena fascinante. ¿Qué más te gustaría saber?",
            "Voy aprendiendo cada día. ¿Podrías explicarme más sobre eso?"
        ]
        return random.choice(respuestas)
    
    def iniciar_chat(self):
        print("=" * 50)
        print(f"¡Bienvenido al {self.nombre}!")
        print("Puedes: preguntar la hora/fecha, pedir un chiste,")
        print("preguntar sobre IA, o simplemente conversar.")
        print("Escribe 'adios' para salir.")
        print("=" * 50)
        
        while True:
            try:
                usuario_input = input("\nTú: ").strip()
                
                if not usuario_input:
                    continue
                
                if usuario_input.lower() in ['adios', 'chao', 'salir']:
                    print(f"\n{self.nombre}: ¡Hasta pronto! Fue un gusto ayudarte.")
                    break
                
                respuesta = self.procesar_mensaje(usuario_input)
                print(f"{self.nombre}: {respuesta}")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.nombre}: ¡Hasta luego! Espero verte pronto.")
                break
            except Exception as e:
                print(f"{self.nombre}: Ocurrió un error. Por favor, intenta de nuevo.")

# Ejecutar el chatbot mejorado
if __name__ == "__main__":
    bot = Chatbot()
    bot.iniciar_chat()
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk import pos_tag
import string
import os

class NLTKProcessor:
    def __init__(self):
        # Descargar recursos de NLTK
        self.download_nltk_resources()
        
        # Inicializar componentes de NLTK
        try:
            self.stop_words_spanish = set(stopwords.words('spanish'))
            self.stemmer_spanish = SnowballStemmer('spanish')
            self.nltk_ready = True
        except Exception as e:
            print(f"Error inicializando NLTK: {e}")
            self.nltk_ready = False
    
    def download_nltk_resources(self):
        """Descarga los recursos necesarios de NLTK"""
        resources = [
            'punkt',
            'punkt_tab',
            'stopwords',
            'averaged_perceptron_tagger',
            'maxent_ne_chunker',
            'words'
        ]
        
        print("Verificando recursos NLTK...")
        for resource in resources:
            try:
                if resource == 'punkt':
                    nltk.data.find('tokenizers/punkt')
                elif resource == 'punkt_tab':
                    # Intentar encontrar punkt_tab, si no existe usar punkt normal
                    try:
                        nltk.data.find('tokenizers/punkt_tab')
                    except LookupError:
                        print("punkt_tab no encontrado, usando punkt estándar...")
                        nltk.download('punkt', quiet=True)
                elif resource == 'stopwords':
                    nltk.data.find('corpora/stopwords')
                elif resource == 'averaged_perceptron_tagger':
                    nltk.data.find('taggers/averaged_perceptron_tagger')
                elif resource == 'maxent_ne_chunker':
                    nltk.data.find('chunkers/maxent_ne_chunker')
                elif resource == 'words':
                    nltk.data.find('corpora/words')
                print(f"✓ {resource} disponible")
            except LookupError:
                print(f"Descargando {resource}...")
                try:
                    nltk.download(resource, quiet=True)
                    print(f"✓ {resource} descargado exitosamente")
                except Exception as e:
                    print(f"✗ Error descargando {resource}: {e}")
    
    def safe_tokenize(self, texto, language='spanish'):
        """Tokenización segura con fallback"""
        try:
            # Intentar con punkt_tab primero
            return word_tokenize(texto, language=language)
        except LookupError:
            try:
                # Fallback a tokenización básica en inglés
                print("Usando tokenización en inglés como fallback...")
                return word_tokenize(texto)
            except:
                # Último fallback: tokenización simple
                print("Usando tokenización simple...")
                return texto.split()
    
    def safe_sent_tokenize(self, texto, language='spanish'):
        """Tokenización de oraciones segura con fallback"""
        try:
            return sent_tokenize(texto, language=language)
        except LookupError:
            try:
                return sent_tokenize(texto)
            except:
                return [texto]
    
    def preprocesar_texto(self, texto):
        """Preprocesa el texto usando NLTK con manejo de errores"""
        if not self.nltk_ready:
            return self.preprocesar_texto_basico(texto)
        
        try:
            # Tokenización segura
            tokens = self.safe_tokenize(texto.lower())
            
            # Eliminar puntuación y stopwords
            tokens_limpios = [
                token for token in tokens 
                if token not in string.punctuation and token not in self.stop_words_spanish
            ]
            
            # Stemming
            stems = [self.stemmer_spanish.stem(token) for token in tokens_limpios]
            
            return {
                'tokens_originales': tokens,
                'tokens_limpios': tokens_limpios,
                'stems': stems,
                'num_palabras': len(tokens_limpios),
                'nltk_funcional': True
            }
        except Exception as e:
            print(f"Error en preprocesamiento NLTK: {e}")
            return self.preprocesar_texto_basico(texto)
    
    def preprocesar_texto_basico(self, texto):
        """Preprocesamiento básico sin NLTK"""
        # Tokenización simple
        tokens = texto.lower().split()
        
        # Lista básica de stopwords en español
        stopwords_basicas = {
            'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para', 
            'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 
            'este', 'sí', 'porque', 'esta', 'entre', 'cuando', 'muy', 'sin', 'sobre', 'también', 
            'me', 'hasta', 'hay', 'donde', 'quien', 'desde', 'todo', 'nos', 'durante', 'todos', 
            'uno', 'les', 'ni', 'contra', 'otros', 'ese', 'eso', 'ante', 'ellos', 'e', 'esto', 'mí',
            'antes', 'algunos', 'qué', 'unos', 'yo', 'otro', 'otras', 'otra', 'él', 'tanto', 'esa',
            'estos', 'mucho', 'quienes', 'nada', 'muchos', 'cual', 'poco', 'ella', 'estar', 'estas',
            'algunas', 'algo', 'nosotros', 'mi', 'mis', 'tú', 'te', 'ti', 'tu', 'tus', 'ellas',
            'nosotras', 'vosotros', 'vosotras', 'os', 'mío', 'mía', 'míos', 'mías', 'tuyo', 'tuya',
            'tuyos', 'tuyas', 'suyo', 'suya', 'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros',
            'nuestras', 'vuestro', 'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy',
            'estás', 'está', 'estamos', 'estáis', 'están', 'esté', 'estés', 'estemos', 'estéis',
            'estén', 'estaré', 'estarás', 'estará', 'estaremos', 'estaréis', 'estarán', 'estaría',
            'estarías', 'estaríamos', 'estaríais', 'estarían', 'estaba', 'estabas', 'estábamos',
            'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis',
            'estuvieron', 'estuviera', 'estuvieras', 'estuviéramos', 'estuvierais', 'estuvieran',
            'estuviese', 'estuvieses', 'estuviésemos', 'estuvieseis', 'estuviesen', 'estando',
            'estado', 'estada', 'estados', 'estadas', 'estad', 'he', 'has', 'ha', 'hemos', 'habéis',
            'han', 'haya', 'hayas', 'hayamos', 'hayáis', 'hayan', 'habré', 'habrás', 'habrá',
            'habremos', 'habréis', 'habrán', 'habría', 'habrías', 'habríamos', 'habríais', 'habrían',
            'había', 'habías', 'habíamos', 'habíais', 'habían', 'hube', 'hubiste', 'hubo', 'hubimos',
            'hubisteis', 'hubieron', 'hubiera', 'hubieras', 'hubiéramos', 'hubierais', 'hubieran',
            'hubiese', 'hubieses', 'hubiésemos', 'hubieseis', 'hubiesen', 'habiendo', 'habido',
            'habida', 'habidos', 'habidas', 'soy', 'eres', 'es', 'somos', 'sois', 'son', 'sea',
            'seas', 'seamos', 'seáis', 'sean', 'seré', 'serás', 'será', 'seremos', 'seréis', 'serán',
            'sería', 'serías', 'seríamos', 'seríais', 'serían', 'era', 'eras', 'éramos', 'erais',
            'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera', 'fueras',
            'fuéramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fuésemos', 'fueseis', 'fuesen',
            'sintiendo', 'sentido', 'tengo', 'tienes', 'tiene', 'tenemos', 'tenéis', 'tienen',
            'tenga', 'tengas', 'tengamos', 'tengáis', 'tengan', 'tendré', 'tendrás', 'tendrá',
            'tendremos', 'tendréis', 'tendrán', 'tendría', 'tendrías', 'tendríamos', 'tendríais',
            'tendrían', 'tenía', 'tenías', 'teníamos', 'teníais', 'tenían', 'tuve', 'tuviste',
            'tuvo', 'tuvimos', 'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuviéramos',
            'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuviésemos', 'tuvieseis', 'tuviesen',
            'teniendo', 'tenido', 'tenida', 'tenidos', 'tenidas', 'tened'
        }
        
        tokens_limpios = [token for token in tokens if token not in stopwords_basicas]
        
        return {
            'tokens_originales': tokens,
            'tokens_limpios': tokens_limpios,
            'stems': tokens_limpios,  # Sin stemming en versión básica
            'num_palabras': len(tokens_limpios),
            'nltk_funcional': False
        }
    
    def analizar_estructura(self, texto):
        """Analiza la estructura del texto usando NLTK con fallback"""
        if not self.nltk_ready:
            return self.analizar_estructura_basica(texto)
        
        try:
            oraciones = self.safe_sent_tokenize(texto)
            tokens = self.safe_tokenize(texto)
            
            # Etiquetado gramatical básico (puede fallar sin los recursos)
            pos_tags = []
            try:
                pos_tags = pos_tag(tokens)
            except:
                pos_tags = [(token, 'UNK') for token in tokens]
            
            return {
                'num_oraciones': len(oraciones),
                'num_tokens': len(tokens),
                'pos_tags': pos_tags,
                'oraciones': oraciones
            }
        except Exception as e:
            print(f"Error en análisis de estructura: {e}")
            return self.analizar_estructura_basica(texto)
    
    def analizar_estructura_basica(self, texto):
        """Análisis básico de estructura sin NLTK"""
        oraciones = texto.split('.')
        tokens = texto.split()
        
        return {
            'num_oraciones': len([o for o in oraciones if o.strip()]),
            'num_tokens': len(tokens),
            'pos_tags': [(token, 'UNK') for token in tokens],
            'oraciones': [o.strip() for o in oraciones if o.strip()]
        }
    
    def analizar_sentimiento_avanzado(self, texto):
        """Análisis de sentimiento mejorado con manejo de errores"""
        analisis = self.preprocesar_texto(texto)
        stems = analisis['stems']
        
        # Diccionario de sentimientos en español
        palabras_positivas = {
            'bien', 'excelent', 'genial', 'maravill', 'fantast', 'perfect', 
            'feliz', 'content', 'alegr', 'satisf', 'encant', 'gust', 'bonit',
            'buen', 'geni', 'brill', 'estupend', 'magnif', 'fabul', 'increíbl',
            'formidabl', 'extraordinari', 'espectacul', 'fantástic', 'perfect',
            'divin', 'hermos', 'precios', 'ador', 'amor', 'sonris', 'ris',
            'goz', 'dich', 'ventur', 'afortun', 'suerte', 'éxit', 'triunf',
            'victori', 'gan', 'premi', 'celebr', 'fiest', 'alegr', 'júbil'
        }
        
        palabras_negativas = {
            'mal', 'terribl', 'horribl', 'fatal', 'trist', 'enoj', 'molest',
            'difícil', 'complic', 'problem', 'error', 'fall', 'decepcion',
            'pésim', 'horror', 'asqu', 'desagrad', 'fe', 'cans', 'aburr',
            'frustr', 'ira', 'rabi', 'enfad', 'disgust', 'desgrac', 'desastr',
            'catastrof', 'traged', 'dolor', 'sufrimient', 'pen', 'lástim',
            'desesper', 'desesper', 'angusti', 'preocup', 'mied', 'terror',
            'pánic', 'nervi', 'ansied', 'estrés', 'presió', 'confus', 'perdid',
            'fracas', 'derrot', 'hundimient', 'caíd', 'ruin', 'bancarrot'
        }
        
        positivas = sum(1 for stem in stems if stem in palabras_positivas)
        negativas = sum(1 for stem in stems if stem in palabras_negativas)
        
        if positivas > negativas:
            return "positivo", positivas, negativas
        elif negativas > positivas:
            return "negativo", positivas, negativas
        else:
            return "neutral", positivas, negativas
    
    def extraer_palabras_clave(self, texto):
        """Extrae palabras clave con manejo de errores"""
        try:
            analisis = self.preprocesar_texto(texto)
            tokens_limpios = analisis['tokens_limpios']
            
            if not analisis['nltk_funcional']:
                # Versión básica sin POS tagging
                palabras_clave = [token for token in tokens_limpios if len(token) > 3]
                return list(set(palabras_clave))[:5]
            
            # Filtrar palabras relevantes (sustantivos, adjetivos, verbos)
            try:
                pos_tags = pos_tag(tokens_limpios)
                palabras_clave = [
                    palabra for palabra, pos in pos_tags
                    if pos.startswith(('NN', 'JJ', 'VB')) and len(palabra) > 3
                ]
                return list(set(palabras_clave))[:5]
            except:
                # Fallback si el POS tagging falla
                palabras_clave = [token for token in tokens_limpios if len(token) > 3]
                return list(set(palabras_clave))[:5]
                
        except Exception as e:
            print(f"Error extrayendo palabras clave: {e}")
            return []
    
    def analizar_estructura_detallada(self, texto):
        """Análisis detallado de estructura con fallback"""
        estructura = self.analizar_estructura(texto)
        
        # Contar tipos de palabras (versión básica si no hay POS tagging)
        sustantivos = 0
        verbos = 0
        adjetivos = 0
        
        for _, pos in estructura['pos_tags']:
            if pos.startswith('NN'):
                sustantivos += 1
            elif pos.startswith('VB'):
                verbos += 1
            elif pos.startswith('JJ'):
                adjetivos += 1
        
        return {
            'oraciones': estructura['num_oraciones'],
            'tokens': estructura['num_tokens'],
            'sustantivos': sustantivos,
            'verbos': verbos,
            'adjetivos': adjetivos
        }
    
    def analizar_sentimiento_detallado(self, texto):
        """Análisis detallado de sentimiento"""
        sentimiento, positivas, negativas = self.analizar_sentimiento_avanzado(texto)
        total = positivas + negativas
        porcentaje_positivo = (positivas / total * 100) if total > 0 else 0
        porcentaje_negativo = (negativas / total * 100) if total > 0 else 0
        
        return {
            'sentimiento': sentimiento,
            'positivas': positivas,
            'negativas': negativas,
            'total': total,
            'porcentaje_positivo': porcentaje_positivo,
            'porcentaje_negativo': porcentaje_negativo
        }
    
    def analizar_palabras_clave_detallado(self, texto):
        """Análisis detallado de palabras clave"""
        palabras_clave = self.extraer_palabras_clave(texto)
        preprocesado = self.preprocesar_texto(texto)
        
        return {
            'palabras_clave': palabras_clave,
            'total_palabras_unicas': len(set(preprocesado['tokens_limpios']))
        }
    
    def analizar_metricas_generales(self, texto):
        """Análisis de métricas generales"""
        estructura = self.analizar_estructura(texto)
        preprocesado = self.preprocesar_texto(texto)
        
        densidad_lexica = (len(set(preprocesado['tokens_limpios'])) / preprocesado['num_palabras'] * 100) if preprocesado['num_palabras'] > 0 else 0
        
        return {
            'longitud_texto': len(texto),
            'palabras_limpias': preprocesado['num_palabras'],
            'densidad_lexica': densidad_lexica
        }
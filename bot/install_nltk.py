import nltk
import sys

def download_all_resources():
    """Descarga todos los recursos necesarios de NLTK"""
    resources = [
        'punkt',
        'punkt_tab',
        'stopwords',
        'averaged_perceptron_tagger',
        'maxent_ne_chunker',
        'words'
    ]
    
    print("=" * 50)
    print("INSTALADOR DE RECURSOS NLTK")
    print("=" * 50)
    
    for resource in resources:
        print(f"\n📦 Procesando: {resource}")
        try:
            nltk.download(resource, quiet=False)
            print(f"✅ {resource} instalado correctamente")
        except Exception as e:
            print(f"❌ Error instalando {resource}: {e}")
    
    print("\n" + "=" * 50)
    print("INSTALACIÓN COMPLETADA")
    print("=" * 50)
    print("\nAhora puedes ejecutar el chatbot:")
    print("python main.py")

if __name__ == "__main__":
    # Verificar si NLTK está instalado
    try:
        import nltk
        print("✅ NLTK está instalado")
    except ImportError:
        print("❌ NLTK no está instalado. Instálalo con:")
        print("pip install nltk")
        sys.exit(1)
    
    # Descargar recursos
    download_all_resources()
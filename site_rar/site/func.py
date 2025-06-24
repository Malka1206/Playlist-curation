# filepath: c:\Users\user\p104site\func.py
import sys
import os

def analyze_audio(file_path):
    # Exemple d'analyse : retourne la taille du fichier
    if not os.path.exists(file_path):
        return "Fichier introuvable."
    file_size = os.path.getsize(file_path)
    return f"Le fichier audio a une taille de {file_size} octets."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Aucun fichier fourni.", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    result = analyze_audio(file_path)
    print(result)
# filepath: c:\Users\user\p104site\func.py
import sys
import os
from prediction import predire_genre

def analyze_audio(file_path):
    # Exemple d'analyse : retourne la taille du fichier
    if not os.path.exists(file_path):
        return "Fichier introuvable."
    file_genre = predire_genre(file_path)
    return f"{file_genre}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Aucun fichier fourni.", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    result = analyze_audio(file_path)
    print(result)
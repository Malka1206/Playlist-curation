import sys

def fx(audio_path):
    return f"Traitement effectué sur le fichier : {audio_path}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        result = fx(sys.argv[1])
        print(result)
    else:
        print("Erreur : Chemin du fichier non fourni")

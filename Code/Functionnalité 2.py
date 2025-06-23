import prediction as pred
import os

def analyze_musics(musics):
    L=[]
    for i in musics:
        L.append(pred.predire_genre(i))
    playlists={}
    for i in range (len(L)):
        if L[i] not in playlists.keys():
            playlists[L[i]]=[musics[i]]
        else:
            playlists[L[i]].append(musics[i])
    return playlists

def tolist_music(path):
    chemin_musics=[]
    for fichier in os.listdir(path):
        chemin_fichier = os.path.join(path, fichier)
        chemin_musics.append(chemin_fichier)
    return chemin_musics

basepath= "C:\\Users\\Administrateur\\Downloads\\musics"
musics=tolist_music(basepath)
playlists=analyze_musics(musics)

prefix = r'C:\\Users\\Administrateur\\Downloads\\musics\\'

for genre, tracks in playlists.items():
    print(f"\n Genre: {genre}")
    for track in tracks:
        rel_path = os.path.relpath(track, prefix)
        print(f"  - {rel_path}")
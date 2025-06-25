import joblib
import matplotlib.pyplot as plt

# Charger le modèle
model = joblib.load(r"C:\\Users\\Administrateur\\Documents\\projet Artishow\\playlist-curation\\Code\\xgb_multi.pkl")
booster = model.get_booster()

# Récupérer les importances par 'gain'
importances = booster.get_score(importance_type='gain')

# Trier les features par importance décroissante
sorted_items = sorted(importances.items(), key=lambda x: x[1], reverse=True)

Liste=["MFCC_var0","MFCC_var1","MFCC_var2","MFCC_var3","MFCC_var4",
       "MFCC_mean0","MFCC_mean1","MFCC_mean2","MFCC_mean3","MFCC_mean4",
       "SpectralCentroid_var","SpectralCentroid_mean","SpectRollof_var","SpectRollof_mean",
       "SpectFlux_var","SpectFlux_mean","Passage_par_0_var","Passage_par_0_mean","LowEnergy",
        "BH_rel_amp0", "BH_rel_amp1", "BH_ratio_amp", "BH_pos_pic0", "BH_pos_pic1", "BH_somme_pics",
        "FPH_amp_pic_max", "FPH_pos_pic_max", "pitch_intervalle", "UPH_period_pic/octave", "PH_sum_pics"]

# Séparer les noms et les scores
features = [Liste[int(item[0][-1])] for item in sorted_items]
scores = [item[1] for item in sorted_items]

# Tracer le barplot horizontal
plt.figure(figsize=(8, 6))
plt.barh(features, scores, color='skyblue')
plt.xlabel("Gain")
plt.ylabel("Features")
plt.title("Feature importance")
plt.gca().invert_yaxis()  # Pour afficher la plus importante en haut
plt.tight_layout()
plt.show()

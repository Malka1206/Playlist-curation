document.addEventListener('DOMContentLoaded', function () {
    // Créer la zone de dépôt
    var dropZone = document.createElement('div');
    dropZone.id = 'drop-zone';
    dropZone.innerHTML = 'Déposez votre fichier .au ici';
    document.body.appendChild(dropZone);
    // Ajouter les styles pour la zone de dépôt
    dropZone.style.width = '300px';
    dropZone.style.height = '200px';
    dropZone.style.border = '2px dashed #ccc';
    dropZone.style.borderRadius = '4px';
    dropZone.style.display = 'flex';
    dropZone.style.alignItems = 'center';
    dropZone.style.justifyContent = 'center';
    dropZone.style.margin = '20px auto';
    dropZone.style.cursor = 'pointer';
    // Gérer les événements de drag & drop
    dropZone.addEventListener('dragover', function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropZone.style.backgroundColor = '#f0f0f0';
    });
    dropZone.addEventListener('dragleave', function (e) {
        e.preventDefault();
        e.stopPropagation();
        dropZone.style.backgroundColor = 'transparent';
    });
    dropZone.addEventListener('drop', function (e) {
        var _a;
        e.preventDefault();
        e.stopPropagation();
        dropZone.style.backgroundColor = 'transparent';
        var files = (_a = e.dataTransfer) === null || _a === void 0 ? void 0 : _a.files;
        if (files && files.length > 0) {
            var file = files[0];
            if (file.name.endsWith('.au')) {
                handleAudioFile(file);
            }
            else {
                alert('Veuillez déposer un fichier .au');
            }
        }
    });
    // Fonction pour gérer le fichier audio
    function handleAudioFile(file) {
        console.log('Fichier .au reçu:', file.name);
        // Ici vous pouvez ajouter le code pour traiter le fichier
        dropZone.innerHTML = "Fichier re\u00E7u : ".concat(file.name);
    }
});

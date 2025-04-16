document.addEventListener('DOMContentLoaded', () => {
    // Création de la zone de dépôt
    const dropZone = document.createElement('div');
    dropZone.id = 'drop-zone';
    dropZone.textContent = 'Déposez votre fichier .au ici';
    document.body.appendChild(dropZone);

    // Style simple
    dropZone.style.width = '300px';
    dropZone.style.height = '150px';
    dropZone.style.border = '2px dashed #888';
    dropZone.style.borderRadius = '8px';
    dropZone.style.display = 'flex';
    dropZone.style.alignItems = 'center';
    dropZone.style.justifyContent = 'center';
    dropZone.style.margin = '40px auto';
    dropZone.style.fontSize = '1.2em';
    dropZone.style.background = '#fafafa';

    // Drag over
    dropZone.addEventListener('dragover', (e: DragEvent) => {
        e.preventDefault();
        dropZone.style.background = '#e0e0e0';
    });

    // Drag leave
    dropZone.addEventListener('dragleave', (e: DragEvent) => {
        e.preventDefault();
        dropZone.style.background = '#fafafa';
    });

    // Drop
    dropZone.addEventListener('drop', (e: DragEvent) => {
        e.preventDefault();
        dropZone.style.background = '#fafafa';
        const files = e.dataTransfer?.files;
        if (files && files.length > 0) {
            const file = files[0];
            if (file.name.toLowerCase().endsWith('.au')) {
                dropZone.textContent = `Fichier reçu : ${file.name}`;
            } else {
                dropZone.textContent = 'Seuls les fichiers .au sont acceptés.';
            }
        }
    });
});
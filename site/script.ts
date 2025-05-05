document.addEventListener('DOMContentLoaded', () => {
    // Create container
    const container = document.createElement('div');
    container.style.maxWidth = '600px';
    container.style.margin = '20px auto';
    document.body.appendChild(container);

    // Create title
    const title = document.createElement('h1');
    title.textContent = 'Traitement de fichiers .au';
    title.style.textAlign = 'center';
    title.style.color = '#333';
    container.appendChild(title);

    // Create drop zone with instructions
    const dropZone = document.createElement('div');
    dropZone.id = 'drop-zone';
    dropZone.innerHTML = `
        <div>Déposez votre fichier .au ici</div>
        <div style="font-size: 0.8em; color: #666; margin-top: 10px;">
            La fonction fx sera appliquée au fichier
        </div>
    `;
    container.appendChild(dropZone);

    // Styles for drop zone
    dropZone.style.width = '300px';
    dropZone.style.height = '150px';
    dropZone.style.border = '2px dashed #888';
    dropZone.style.borderRadius = '8px';
    dropZone.style.display = 'flex';
    dropZone.style.flexDirection = 'column';
    dropZone.style.alignItems = 'center';
    dropZone.style.justifyContent = 'center';
    dropZone.style.margin = '20px auto';
    dropZone.style.fontSize = '1.2em';
    dropZone.style.background = '#fafafa';
    dropZone.style.transition = 'all 0.3s ease';

    let uploadedFile: File | null = null;

    // Drag & drop event handlers
    dropZone.addEventListener('dragover', (e: DragEvent) => {
        e.preventDefault();
        dropZone.style.background = '#e0e0e0';
        dropZone.style.borderColor = '#666';
    });

    dropZone.addEventListener('dragleave', (e: DragEvent) => {
        e.preventDefault();
        dropZone.style.background = '#fafafa';
        dropZone.style.borderColor = '#888';
    });

    dropZone.addEventListener('drop', (e: DragEvent) => {
        e.preventDefault();
        dropZone.style.background = '#fafafa';
        dropZone.style.borderColor = '#888';
        
        const files = e.dataTransfer?.files;
        if (files && files.length > 0) {
            const file = files[0];
            if (file.name.toLowerCase().endsWith('.au')) {
                uploadedFile = file;
                dropZone.innerHTML = `
                    <div>Fichier reçu : ${file.name}</div>
                    <div style="font-size: 0.8em; color: #666; margin-top: 10px;">
                        Cliquez sur le bouton pour traiter le fichier
                    </div>
                `;
                processButton.disabled = false;
                processButton.style.opacity = '1';
            } else {
                dropZone.innerHTML = `
                    <div style="color: #d43f3f;">Seuls les fichiers .au sont acceptés</div>
                    <div style="font-size: 0.8em; color: #666; margin-top: 10px;">
                        Veuillez réessayer avec un fichier .au
                    </div>
                `;
                processButton.disabled = true;
                processButton.style.opacity = '0.5';
            }
        }
    });

    // Create process button
    const processButton = document.createElement('button');
    processButton.textContent = 'Traiter le fichier';
    processButton.style.display = 'block';
    processButton.style.margin = '20px auto';
    processButton.style.padding = '10px 20px';
    processButton.style.fontSize = '1em';
    processButton.style.backgroundColor = '#4CAF50';
    processButton.style.color = 'white';
    processButton.style.border = 'none';
    processButton.style.borderRadius = '4px';
    processButton.style.cursor = 'pointer';
    processButton.disabled = true;
    processButton.style.opacity = '0.5';
    processButton.style.transition = 'all 0.3s ease';
    container.appendChild(processButton);

    // Create result area
    const resultArea = document.createElement('div');
    resultArea.style.margin = '20px auto';
    resultArea.style.padding = '15px';
    resultArea.style.border = '1px solid #ccc';
    resultArea.style.borderRadius = '4px';
    resultArea.style.minHeight = '50px';
    resultArea.style.background = '#f9f9f9';
    resultArea.innerHTML = `
        <div style="color: #666; text-align: center;">
            Le résultat du traitement s'affichera ici
        </div>
    `;
    container.appendChild(resultArea);

    // Handle button click
    processButton.addEventListener('click', async () => {
        if (!uploadedFile) {
            resultArea.innerHTML = `
                <div style="color: #d43f3f; text-align: center;">
                    Veuillez d'abord déposer un fichier .au
                </div>
            `;
            return;
        }

        // Show loading state
        processButton.disabled = true;
        processButton.textContent = 'Traitement en cours...';
        resultArea.innerHTML = `
            <div style="color: #666; text-align: center;">
                Traitement du fichier en cours...
            </div>
        `;

        const formData = new FormData();
        formData.append('file', uploadedFile);

        try {
            const response = await fetch('http://localhost:3000/process', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                const result = await response.text();
                resultArea.innerHTML = `
                    <div style="color: #4CAF50; text-align: center;">
                        ${result}
                    </div>
                `;
            } else {
                resultArea.innerHTML = `
                    <div style="color: #d43f3f; text-align: center;">
                        Erreur lors du traitement du fichier
                    </div>
                `;
            }
        } catch (error) {
            resultArea.innerHTML = `
                <div style="color: #d43f3f; text-align: center;">
                    Erreur de connexion au serveur
                </div>
            `;
            console.error(error);
        } finally {
            processButton.disabled = false;
            processButton.textContent = 'Traiter le fichier';
        }
    });
});
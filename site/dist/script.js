"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
document.addEventListener('DOMContentLoaded', () => __awaiter(void 0, void 0, void 0, function* () {
    // Vérifier si le serveur Flask est prêt
    const checkServerReady = () => __awaiter(void 0, void 0, void 0, function* () {
        try {
            const response = yield fetch('http://localhost:5000');
            return response.ok;
        }
        catch (_a) {
            return false;
        }
    });
    // Attendre que le serveur Flask soit prêt
    const waitForServer = () => __awaiter(void 0, void 0, void 0, function* () {
        let ready = false;
        while (!ready) {
            ready = yield checkServerReady();
            if (!ready) {
                console.log('En attente du serveur Flask...');
                yield new Promise((resolve) => setTimeout(resolve, 1000));
            }
        }
        console.log('Serveur Flask prêt.');
    });
    // Appeler la fonction pour attendre le serveur
    yield waitForServer();
    // Reste du code pour gérer la zone de dépôt, le bouton et l'exécution
    const container = document.createElement('div');
    container.style.maxWidth = '600px';
    container.style.margin = '20px auto';
    document.body.appendChild(container);
    // Create drop zone
    const dropZone = document.createElement('div');
    dropZone.id = 'drop-zone';
    dropZone.textContent = 'Déposez votre fichier .au ici';
    container.appendChild(dropZone);
    // Styles for drop zone
    dropZone.style.width = '300px';
    dropZone.style.height = '150px';
    dropZone.style.border = '2px dashed #888';
    dropZone.style.borderRadius = '8px';
    dropZone.style.display = 'flex';
    dropZone.style.alignItems = 'center';
    dropZone.style.justifyContent = 'center';
    dropZone.style.margin = '20px auto';
    dropZone.style.fontSize = '1.2em';
    dropZone.style.background = '#fafafa';
    let uploadedFile = null;
    // Drag over
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.style.background = '#e0e0e0';
    });
    // Drag leave
    dropZone.addEventListener('dragleave', (e) => {
        e.preventDefault();
        dropZone.style.background = '#fafafa';
    });
    // Drop
    dropZone.addEventListener('drop', (e) => {
        var _a;
        e.preventDefault();
        dropZone.style.background = '#fafafa';
        const files = (_a = e.dataTransfer) === null || _a === void 0 ? void 0 : _a.files;
        if (files && files.length > 0) {
            const file = files[0];
            if (file.name.toLowerCase().endsWith('.au')) {
                uploadedFile = file;
                dropZone.textContent = `Fichier reçu : ${file.name}`;
            }
            else {
                dropZone.textContent = 'Seuls les fichiers .au sont acceptés.';
            }
        }
    });
    // Create button to execute Python function
    const executeButton = document.createElement('button');
    executeButton.textContent = 'Exécuter la fonction Python';
    executeButton.style.display = 'block';
    executeButton.style.margin = '20px auto';
    executeButton.style.padding = '10px 20px';
    executeButton.style.fontSize = '1em';
    container.appendChild(executeButton);
    // Create output area
    const outputArea = document.createElement('div');
    outputArea.style.margin = '20px auto';
    outputArea.style.padding = '10px';
    outputArea.style.border = '1px solid #ccc';
    outputArea.style.borderRadius = '4px';
    outputArea.style.background = '#f9f9f9';
    outputArea.style.width = '80%';
    outputArea.style.minHeight = '50px';
    outputArea.textContent = 'Résultat :';
    container.appendChild(outputArea);
    // Handle button click
    executeButton.addEventListener('click', () => __awaiter(void 0, void 0, void 0, function* () {
        if (!uploadedFile) {
            outputArea.textContent = 'Veuillez déposer un fichier .au avant de continuer.';
            return;
        }
        // Fixed Python file path and function name
        const pythonFilePath = 'C:\\Users\\user\\Desktop\\proj104\\site\\func.py';
        const pythonFunctionName = 'fx';
        // Simulate sending the file and parameters to a Python backend
        const formData = new FormData();
        formData.append('file', uploadedFile);
        formData.append('pythonFilePath', pythonFilePath);
        formData.append('pythonFunctionName', pythonFunctionName);
        try {
            const response = yield fetch('http://localhost:5000/execute', {
                method: 'POST',
                body: formData,
            });
            if (response.ok) {
                const result = yield response.text();
                outputArea.textContent = `Résultat : ${result}`;
            }
            else {
                outputArea.textContent = `Erreur : ${response.statusText}`;
            }
        }
        catch (error) {
            outputArea.textContent = `Erreur lors de l'exécution : ${error}`;
        }
    }));
}));

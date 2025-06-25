// filepath: c:\Users\user\p104site\server.js
const express = require('express');
const multer = require('multer');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');
const path = require('path');

const app = express();
const upload = multer({ dest: 'uploads/' }); // Dossier temporaire pour les fichiers uploadés

app.use(bodyParser.json());

// Endpoint pour analyser le fichier audio
app.post('/api/analyze', upload.single('audio'), (req, res) => {
    if (!req.file) {
        return res.status(400).json({ error: 'Aucun fichier fourni.' });
    }

    // Chemin du fichier uploadé
    const filePath = path.resolve(req.file.path);

    // Appeler le script Python
    const pythonProcess = spawn('python', ['../func.py', filePath]);

    let result = '';
    pythonProcess.stdout.on('data', (data) => {
        result += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Erreur Python : ${data}`);
    });

    pythonProcess.on('close', (code) => {
        if (code === 0) {
            res.json({ result });
        } else {
            res.status(500).json({ error: 'Erreur lors de l\'analyse.' });
        }
    });
});

// Démarrer le serveur
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Serveur démarré sur http://localhost:${PORT}`);
});
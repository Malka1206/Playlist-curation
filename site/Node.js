const express = require('express');
const multer = require('multer');
const { spawn } = require('child_process');
const cors = require('cors');
const path = require('path');

const app = express();
app.use(cors());

// Configuration de multer pour gérer les fichiers
const storage = multer.diskStorage({
    destination: 'uploads/',
    filename: (req, file, cb) => {
        cb(null, file.originalname);
    }
});
const upload = multer({ storage: storage });

// Route pour traiter le fichier
app.post('/process', upload.single('file'), (req, res) => {
    if (!req.file) {
        return res.status(400).send('Aucun fichier reçu');
    }

    const pythonProcess = spawn('python', [
        path.join(__dirname, 'func.py'),
        path.join(__dirname, 'uploads', req.file.filename)
    ]);

    let result = '';
    pythonProcess.stdout.on('data', (data) => {
        result += data.toString();
    });

    pythonProcess.on('close', (code) => {
        res.send(result);
    });
});

app.listen(3000, () => {
    console.log('Serveur démarré sur http://localhost:3000');
});
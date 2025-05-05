const { spawn } = require('child_process');
const path = require('path');

// Fonction pour exécuter le script Python
function executePython(filePath, callback) {
    const pythonFilePath = path.resolve('C:\\Users\\user\\Desktop\\proj104\\site\\func.py');

    // Exécuter le script Python avec Node.js
    const pythonProcess = spawn('python', [pythonFilePath, filePath]);

    let result = '';
    let error = '';

    pythonProcess.stdout.on('data', (data) => {
        result += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        error += data.toString();
    });

    pythonProcess.on('close', (code) => {
        if (code === 0) {
            callback(null, result.trim());
        } else {
            callback(error.trim(), null);
        }
    });
}

// Exporter la fonction pour l'utiliser dans d'autres fichiers
module.exports = executePython;
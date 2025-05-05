var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var _this = this;
document.addEventListener('DOMContentLoaded', function () {
    // Create container
    var container = document.createElement('div');
    container.style.maxWidth = '600px';
    container.style.margin = '20px auto';
    document.body.appendChild(container);
    // Create title
    var title = document.createElement('h1');
    title.textContent = 'Traitement de fichiers .au';
    title.style.textAlign = 'center';
    title.style.color = '#333';
    container.appendChild(title);
    // Create drop zone with instructions
    var dropZone = document.createElement('div');
    dropZone.id = 'drop-zone';
    dropZone.innerHTML = "\n        <div>D\u00E9posez votre fichier .au ici</div>\n        <div style=\"font-size: 0.8em; color: #666; margin-top: 10px;\">\n            La fonction fx sera appliqu\u00E9e au fichier\n        </div>\n    ";
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
    var uploadedFile = null;
    // Drag & drop event handlers
    dropZone.addEventListener('dragover', function (e) {
        e.preventDefault();
        dropZone.style.background = '#e0e0e0';
        dropZone.style.borderColor = '#666';
    });
    dropZone.addEventListener('dragleave', function (e) {
        e.preventDefault();
        dropZone.style.background = '#fafafa';
        dropZone.style.borderColor = '#888';
    });
    dropZone.addEventListener('drop', function (e) {
        var _a;
        e.preventDefault();
        dropZone.style.background = '#fafafa';
        dropZone.style.borderColor = '#888';
        var files = (_a = e.dataTransfer) === null || _a === void 0 ? void 0 : _a.files;
        if (files && files.length > 0) {
            var file = files[0];
            if (file.name.toLowerCase().endsWith('.au')) {
                uploadedFile = file;
                dropZone.innerHTML = "\n                    <div>Fichier re\u00E7u : ".concat(file.name, "</div>\n                    <div style=\"font-size: 0.8em; color: #666; margin-top: 10px;\">\n                        Cliquez sur le bouton pour traiter le fichier\n                    </div>\n                ");
                processButton.disabled = false;
                processButton.style.opacity = '1';
            }
            else {
                dropZone.innerHTML = "\n                    <div style=\"color: #d43f3f;\">Seuls les fichiers .au sont accept\u00E9s</div>\n                    <div style=\"font-size: 0.8em; color: #666; margin-top: 10px;\">\n                        Veuillez r\u00E9essayer avec un fichier .au\n                    </div>\n                ";
                processButton.disabled = true;
                processButton.style.opacity = '0.5';
            }
        }
    });
    // Create process button
    var processButton = document.createElement('button');
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
    var resultArea = document.createElement('div');
    resultArea.style.margin = '20px auto';
    resultArea.style.padding = '15px';
    resultArea.style.border = '1px solid #ccc';
    resultArea.style.borderRadius = '4px';
    resultArea.style.minHeight = '50px';
    resultArea.style.background = '#f9f9f9';
    resultArea.innerHTML = "\n        <div style=\"color: #666; text-align: center;\">\n            Le r\u00E9sultat du traitement s'affichera ici\n        </div>\n    ";
    container.appendChild(resultArea);
    // Handle button click
    processButton.addEventListener('click', function () { return __awaiter(_this, void 0, void 0, function () {
        var formData, response, result, error_1;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    if (!uploadedFile) {
                        resultArea.innerHTML = "\n                <div style=\"color: #d43f3f; text-align: center;\">\n                    Veuillez d'abord d\u00E9poser un fichier .au\n                </div>\n            ";
                        return [2 /*return*/];
                    }
                    // Show loading state
                    processButton.disabled = true;
                    processButton.textContent = 'Traitement en cours...';
                    resultArea.innerHTML = "\n            <div style=\"color: #666; text-align: center;\">\n                Traitement du fichier en cours...\n            </div>\n        ";
                    formData = new FormData();
                    formData.append('file', uploadedFile);
                    _a.label = 1;
                case 1:
                    _a.trys.push([1, 6, 7, 8]);
                    return [4 /*yield*/, fetch('http://localhost:3000/process', {
                            method: 'POST',
                            body: formData
                        })];
                case 2:
                    response = _a.sent();
                    if (!response.ok) return [3 /*break*/, 4];
                    return [4 /*yield*/, response.text()];
                case 3:
                    result = _a.sent();
                    resultArea.innerHTML = "\n                    <div style=\"color: #4CAF50; text-align: center;\">\n                        ".concat(result, "\n                    </div>\n                ");
                    return [3 /*break*/, 5];
                case 4:
                    resultArea.innerHTML = "\n                    <div style=\"color: #d43f3f; text-align: center;\">\n                        Erreur lors du traitement du fichier\n                    </div>\n                ";
                    _a.label = 5;
                case 5: return [3 /*break*/, 8];
                case 6:
                    error_1 = _a.sent();
                    resultArea.innerHTML = "\n                <div style=\"color: #d43f3f; text-align: center;\">\n                    Erreur de connexion au serveur\n                </div>\n            ";
                    console.error(error_1);
                    return [3 /*break*/, 8];
                case 7:
                    processButton.disabled = false;
                    processButton.textContent = 'Traiter le fichier';
                    return [7 /*endfinally*/];
                case 8: return [2 /*return*/];
            }
        });
    }); });
});

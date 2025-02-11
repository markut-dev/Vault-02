import hashlib
import json
import os

# 📌 Lista de archivos requeridos
required_files = [
  "Assets/Prefabs/Client.unity",
  "Assets/Scenes/FrontEnd.unity",
  "Assets/Scenes/Avatar Editor.unity",
  "Assets/Scenes/InitGame.unity",
  "Assets/Scripts/Firebase/FirebaseAuthManager.cs",
  "Assets/Scripts/Firebase/AvatarCustomManager.cs",
  "Assets/Scripts/Firebase/AgentNameDisplayManager.cs",
  "Assets/Scripts/GitHub/ClientVersionChecker.cs"
  "Assets/AssetBundles"
]

# 📌 Ruta donde se guardará el archivo JSON
game_data_path = "game_data.json"

# 📌 Nueva versión del juego (cambia esto en cada actualización)
new_version = "1.0.0"

def calculate_hash(file_path):
    """Calcula el hash SHA-256 de un archivo."""
    try:
        with open(file_path, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        return file_hash
    except FileNotFoundError:
        print(f"⚠️ Archivo no encontrado: {file_path}")
        return None

def generate_game_data():
    """Genera el JSON con la versión y los hashes de los archivos."""
    game_data = {"game_version": new_version, "required_files": {}}

    for file in required_files:
        file_hash = calculate_hash(file)
        if file_hash:
            game_data["required_files"][file] = file_hash

    # 📌 Guardar el JSON
    with open(game_data_path, "w") as json_file:
        json.dump(game_data, json_file, indent=4)

    print(f"✅ Archivo '{game_data_path}' actualizado con la nueva versión: {new_version}")

if __name__ == "__main__":
    generate_game_data()

import os
import json
import subprocess

# Конфигурационные данные
CONFIG = {
    "env_file": {
        "TRANSPORT_API_KEY": "ваш_ключ_из_env",  # Замените ключом из файла env.txt
        "TECHNOLOGY_API_KEY": "ваш_ключ_из_env",
        "TRANSPORT_API_URL": "https://api.transport.local/data",
        "LOGS_PATH": "./logs/system_logs.log",
        "UPDATE_FREQUENCY": "15"
    },
    "git_config": {
        "repo_url": "https://github.com/your-repo/project.git",
        "branch": "main"
    },
    "dependencies": [
        "axios",
        "cheerio",
        "pandas",
        "numpy",
        "dotenv",
        "express",
        "react",
        "typescript"
    ],
    "test_files": {
        "test_cases.json": {
            "description": "Сценарии тестирования API",
            "content": [
                {
                    "test_name": "API Transport Check",
                    "expected_result": "Valid Transport Data"
                },
                {
                    "test_name": "JSON Parsing",
                    "expected_result": "Correct Structure"
                }
            ]
        },
        "response_template.json": {
            "columns": [
                "Номер рейса", "Место отправления", "Вид транспорта", 
                "Статус с места отправления", "Фактическое время отправления", 
                "Количество пассажиров", "Запланированное время прибытия", 
                "Время прибытия с учётом опозданий", "Фактическое время прибытия", 
                "Статус прибытия"
            ]
        }
    }
}

# Функция для создания .env файла
def create_env_file():
    print("[INFO] Создаю .env файл...")
    with open(".env", "w") as env_file:
        for key, value in CONFIG["env_file"].items():
            env_file.write(f"{key}={value}\n")
    print("[SUCCESS] .env файл создан.")

# Функция для клонирования репозитория
def clone_repo():
    print("[INFO] Клонирую репозиторий...")
    try:
        subprocess.run(["git", "clone", CONFIG["git_config"]["repo_url"]], check=True)
        repo_name = CONFIG["git_config"]["repo_url"].split("/")[-1].replace(".git", "")
        os.chdir(repo_name)
        subprocess.run(["git", "checkout", CONFIG["git_config"]["branch"]], check=True)
        print("[SUCCESS] Репозиторий успешно клонирован.")
    except Exception as e:
        print(f"[ERROR] Ошибка клонирования репозитория: {e}")

# Функция для установки зависимостей
def install_dependencies():
    print("[INFO] Устанавливаю зависимости...")
    try:
        subprocess.run(["npm", "install"] + CONFIG["dependencies"], check=True)
        print("[SUCCESS] Все зависимости установлены.")
    except Exception as e:
        print(f"[ERROR] Ошибка установки зависимостей: {e}")

# Функция для создания тестовых файлов
def create_test_files():
    print("[INFO] Создаю тестовые файлы...")
    os.makedirs("tests", exist_ok=True)
    for filename, content in CONFIG["test_files"].items():
        with open(f"./tests/{filename}", "w") as test_file:
            json.dump(content, test_file, indent=4, ensure_ascii=False)
    print("[SUCCESS] Тестовые файлы успешно созданы.")

# Функция для запуска сервера
def start_server():
    print("[INFO] Запускаю сервер...")
    try:
        subprocess.run(["npm", "start"], check=True)
        print("[SUCCESS] Сервер успешно запущен.")
    except Exception as e:
        print(f"[ERROR] Ошибка запуска сервера: {e}")

# Основной процесс настройки
def setup_project():
    print("[START] Начало настройки проекта...")
    create_env_file()
    clone_repo()
    install_dependencies()
    create_test_files()
    start_server()
    print("[FINISH] Настройка завершена.")

if __name__ == "__main__":
    setup_project()

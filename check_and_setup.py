import os
import subprocess
import sys

# Проверка наличия программы в системе
def check_program(program_name, install_command):
    print(f"[INFO] Проверяю наличие {program_name}...")
    try:
        subprocess.run([program_name, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(f"[SUCCESS] {program_name} установлен.")
    except FileNotFoundError:
        print(f"[WARNING] {program_name} не найден. Устанавливаю...")
        try:
            subprocess.run(install_command, check=True, shell=True)
            print(f"[SUCCESS] {program_name} успешно установлен.")
        except Exception as e:
            print(f"[ERROR] Не удалось установить {program_name}: {e}")
            sys.exit(1)

# Установка зависимостей проекта через npm
def install_npm_dependencies():
    print("[INFO] Устанавливаю зависимости через npm...")
    try:
        subprocess.run(["npm", "install"], check=True)
        print("[SUCCESS] Все npm-зависимости установлены.")
    except Exception as e:
        print(f"[ERROR] Ошибка установки npm-зависимостей: {e}")
        sys.exit(1)

# Создание файла .env с конфигурацией
def create_env_file():
    print("[INFO] Создаю .env файл...")
    env_content = """
TRANSPORT_API_KEY=ваш_ключ
TECHNOLOGY_API_KEY=ваш_ключ
TRANSPORT_API_URL=https://api.transport.local/data
LOGS_PATH=./logs/system_logs.log
UPDATE_FREQUENCY=15
"""
    try:
        with open(".env", "w") as env_file:
            env_file.write(env_content.strip())
        print("[SUCCESS] Файл .env создан.")
    except Exception as e:
        print(f"[ERROR] Ошибка создания .env файла: {e}")
        sys.exit(1)

# Основной процесс проверки и установки
def setup_environment():
    print("[START] Запуск проверки и установки необходимых компонентов...")

    # Проверка Python
    check_program("python3", "sudo apt-get install -y python3" if sys.platform == "linux" else "brew install python3")

    # Проверка Node.js и npm
    check_program("node", "sudo apt-get install -y nodejs npm" if sys.platform == "linux" else "brew install node")

    # Проверка Git
    check_program("git", "sudo apt-get install -y git" if sys.platform == "linux" else "brew install git")

    # Установка зависимостей через npm
    install_npm_dependencies()

    # Создание файла .env
    create_env_file()

    print("[FINISH] Проверка и установка завершены. Среда готова к работе.")

# Запуск скрипта
if __name__ == "__main__":
    setup_environment()

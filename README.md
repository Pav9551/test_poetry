# Проект Домашнее задание "Продвинутый Git"
## Описание: Виджет банковских операций клиента. Позволяет извлекать выбранные данные из приложения и отображает их на экране
### Установка poetry:
1. cd C:\Users\user\AppData\Local\Programs\Python\Python313
2. python -m ensurepip
3. python -m pip install --upgrade certifi
4. (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
5. poetry --version

6. The installer installs the poetry tool to Poetry's bin directory. This location depends on your system:
$HOME/.local/bin for Unix
%APPDATA%\Python\Scripts on Windows
7. ~/AppData/Roaming/pypoetry/venv/Scripts/poetry.exe
### Установка
1. Клонируйте репозиторий:
git clone https://github.com/Pav9551/test_poetry
2. Перейдите в директорию проекта:
cd test_poetry
3. Установите необходимые зависимости:
- poetry add --dev pytest 
- poetry add --dev pytest coverage
## Использование
1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами
### Тестирование
Проект покрыт тестами. Для их запуска выполните команду:
poetry run pytest tests
Поктытие:
poetry run coverage run -m pytest
poetry run coverage html


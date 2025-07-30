# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код в контейнер
COPY ./src .

# Создаем директорию для данных, если используется SQLite
RUN mkdir -p /app/data

# Команда для запуска бота
CMD ["python", "main.py"]

FROM python:3.9

# Встановлення залежностей для pygame
RUN apt-get update && apt-get install -y \
    libasound2 \
    libasound2-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Створення робочої директорії
WORKDIR /app

# Копіюємо файли
COPY main.py .
COPY Try.mp3 .

# Встановлюємо бібліотеки
RUN pip install flask pygame

# Відкриваємо порт
EXPOSE 8000

# Команда запуску
CMD ["python", "main.py"]
# Установка
## 1. Клонирование репозитория
```bash
git clone https://github.com/kirillysz/aqa_python_junior.git
```
## 2. Билд и запуск Docker контейнера
```bash
mkdir -p ./allure-results

docker build -t automation-tests .
docker run --rm \
  -v $(pwd)/allure-results:/app/allure-results \
  automation-tests
```
## 3. Завершение
Результаты всех тестов можно посмотреть
```bash
ls -la allure-results/
```
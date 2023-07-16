# REST API сервис по расчёту стоимости страхования в зависимости от типа груза и объявленной стоимости.  

## Технологии
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=19&pause=1000&color=000000&background=D97FFF5A&multiline=true&width=630&height=40&lines=Python+%F0%9F%90%8D+FastAPI+%E2%9A%A1%EF%B8%8F+PostgreSQL+%F0%9F%90%98+Tortoise+%F0%9F%90%A2+Docker+%F0%9F%90%B3)](https://git.io/typing-svg)

## Чтобы протестировать его работу Вам необходимо:  
### Клонировать репозиторий  
```bash
git clone https://github.com/fulliam/insurance_calculator.git
```

#### Перейти в папку репозитория  
```bash
cd /insurance_calculator 
```

### Создать в корневом каталоге репозитория файл .env  
**Содержимое файла:**  
```bash
DB_USER = admin_insurance
DB_PASS = password
DB_HOST = db
DB_PORT = 5432
DB_NAME = insurance_db
```

### Запустить сборку контейнеров  
```bash
docker-compose up --build
```

## Открыть документацию Swagger или воспользоваться curl-запросами  
http://0.0.0.0:5050/docs  

# Вы превосходны! ✨

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from tortoise import run_async, Tortoise

# Функция для создания таблицы по модели
async def create_tables():
    await Tortoise.init(
        db_url=f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()


if __name__ == '__main__':
    run_async(create_tables())
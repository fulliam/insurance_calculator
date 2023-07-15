from fastapi import FastAPI
from models import InsuranceRate
from migrations import create_tables
from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

# Создание экземпляра FastAPI
app = FastAPI(
    title='Insurance calculator',
    version='1.0.0'
)

@app.on_event('startup')
async def startup_event():
    # Создание таблицы InsuranceRate
    await create_tables()
    # Создание тестовых записей
    data = [
        {
            'date': '2023-07-14',
            'cargo_type': 'Past',
            'rate': 0.01
        },
        {
            'date': '2023-07-15',
            'cargo_type': 'Present',
            'rate': 0.02
        },
        {
            'date': '2023-07-16',
            'cargo_type': 'Future',
            'rate': 0.03
        }
    ]
    # Вставка данных в таблицу InsuranceRate
    await InsuranceRate.bulk_create([InsuranceRate(**item) for item in data])

@app.get('/insurance/calculate', tags=["Insurance"])
async def calculate_insurance(date: str, cargo_type: str, declared_value: float):
    '''
    ## Маршрут для рассчёта стоимости страхования по тарифному плану

    **Пример ввода запроса:**
    - **date**: 2023-07-15 
    - **cargo_type**: Present 
    - **declared_value**: 230715 
    '''
    try:
        # Ищем соответствующий тариф с помощью фильтрации по дате и типу груза
        insurance_rate = await InsuranceRate.filter(date=date, cargo_type=cargo_type).first()
        if not insurance_rate:
            return {'error': 'Insurance rate not found', 'Совет': 'Выберите другой тариф'}
    except Exception as e:
        return {'error': str(e), 'Совет': 'Проверьте правильность ввода'}
    # Вычисляем стоимость страхования, умножая заявленную стоимость на тариф
    rate = float(insurance_rate.rate)
    insurance_cost = declared_value * rate
    # Возвращаем стоимость страхования
    return {'insurance_cost': insurance_cost}
# Запуск сервера
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        'API:app', port=5050, host='0.0.0.0',
        reload=True)

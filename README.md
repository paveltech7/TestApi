# TestApi
Должна быть установлена база данных mongodb
Для начала надо скачать работу и перейдя в директорию, установить зависимости командами
```bash
git clone https://github.com/paveltech7/TestApi.git
cd TestApi
pip install -r requirements.txt
```
Запуск происходит при помощи команды в главной директории
```bash
python app.py
```
Можно также написать python3 вместо python

Настройка выбора коллекции находится в файле app.py и изменение в 
```python
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/users'
} #где "users" ваша коллекция в БД
```
Также в файле resources/apiuser.py есть закоментированные методы для автозаполнения таблицы и удаления всех элементов элементами по модели в файле database/model.py
Инициализация базы данных в файле database/db.py

# Инструкция по использованию скрипта

1. Необходимо сохранить данный файл в директории вашего проекта Django, где находится manage.py
2. Запустить Django shell командой:
```python
python manage.py shell
```
3. Импортировать функции

Пример использования:
```python
from utils import get_schoolkid_by_full_name, fix_marks, remove_chastisements, create_commendation
fix_marks('ФИО ученика')
remove_chastisements('ФИО ученика')
create_commendation('ФИО ученика', 'Предмет')
```
- `fix_marks` - исправление оценок 2 и 3 на оценку 5
- `remove_chastisements` - удаление замечаний
- `create_commendation` - создание похвалы по определенному предмету

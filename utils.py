import random
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
from django.core.exceptions import MultipleObjectsReturned

PRAISES = [
    "Молодец, так держать!",
    "Отличная работа!",
    "Умница, продолжай в том же духе!",
    "Твои успехи радуют, так держать!"
]


def get_schoolkid_by_full_name(full_name):
    try:
        return Schoolkid.objects.get(full_name__contains=full_name)
    except Schoolkid.DoesNotExist:
        print(f"Ученик {full_name} не найден.")
        return None
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем {full_name}. Уточните запрос.")
        return None


def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid_by_full_name(schoolkid_name)
    if schoolkid:
        Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)
        print(f"Оценки исправлены для {schoolkid_name}.")


def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid_by_full_name(schoolkid_name)
    if schoolkid:
        Chastisement.objects.filter(schoolkid=schoolkid).delete()
        print(f"Замечания удалены для {schoolkid_name}.")


def create_commendation(full_name, subject_title):
    schoolkid = get_schoolkid_by_full_name(full_name)
    if schoolkid:
        last_lesson = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject_title
        ).order_by('-date').first()

        if last_lesson:
            praise_text = random.choice(PRAISES)
            Commendation.objects.create(
                text=praise_text,
                created=last_lesson.date,
                schoolkid=schoolkid,
                subject=last_lesson.subject,
                teacher=last_lesson.teacher
            )
            print("Похвала успешно добавлена.")
        else:
            print("Не найден урок по заданному предмету.")

import csv
from datetime import datetime
from pathlib import Path
import operator as op
from functools import partial


# task 2
def get_spendings_by_daterange(path, start_date, end_date):
    """
    Функция читает файл CSV по пути path и выводит сумму запланированых расходов между датами start_date и end_date

    Чтобы прочитать дату из текста нужно воспользоватся функцией datetime.strptime(s, '%Y-%m-%d')

    задачу решить двумя способами с помощью map и reduce

    :param path: путь к файлу
    :param start_date:
    :param end_date:
    :return:

    >>> get_spendings_by_daterange('mlt_budget.csv', datetime(2020, 2, 1), datetime(2020, 10, 1))
    Decimal('621980232.95')

    >>> get_spendings_by_daterange('mlt_budget.csv', datetime(2024, 2, 1), datetime(2020, 10, 1))
    0

    >>> get_spendings_by_daterange('mlt_budget.csv', datetime(2020, 4, 1), datetime(2020, 4, 1))
    Decimal('100415681.82')
    """

    cur = pathlib.Path.cwd()
    work_file: pathlib.Path = cur / './mlt_budget.csv'
    with open(work_file) as f:
        reader = csv.reader(f)

        # я так розумію, що ф-ція map повинна перебрати всі рядки і для необхідного
        # діапазона дат просумувати поле 'plan_s'.
        # map i reduce тут в принципі виконують одну й ту ж функцію (суму)

        data_more = filter(partial(op.gt, start_date), reader)        # отримує дати більші за стартову дату
        data_finally = filter(partial(op.lt, end_date), data_more)    # з попередніх вибирає менші за кінцеву дату
        data = sum(map(op.itemgetter('plan_s'), data_finally))
        data = reduce(lambda x: x + op.itemgetter('plan_s'), data_finally)

    return data



# task 3
def get_groupby_report(path, property):
    """
    Функция возвращает словарь вида
    {
        id критерия группировки: [
            {
                'name': название критерия
                'code': код критерия
                'date': дата отчетного периода,
                'plan': сумма запланированых расходов
                'fact': сумма фактических расходов
            }
        ],
    }

    Решить двумя способами (с использованием map и reduce)

    :param path: путь к файлу
    :param property: свойство для группировки: 1 - budget, 2 - fond, 3 - source
    :return:
    ===

    >>> report = get_groupby_report(Path(__file__).parent / 'mlt_budget.csv', 1)
    >>> sum(map(lambda x: Decimal(x['plan']), report['e1915daa-b06d-11e4-8068-000c29123d1d']))
    Decimal('1148563604.00')

    >>> report = get_groupby_report(Path(__file__).parent / 'mlt_budget.csv', 2)
    >>> sum(map(lambda x: Decimal(x['fact']), report['58eaf96b-780a-4376-a762-deb41e32be0c']))
    Decimal('0.00')

    >>> report = get_groupby_report(Path(__file__).parent / 'mlt_budget.csv', 2)
    >>> sum(map(lambda x: Decimal(x['plan']), report['58eaf96b-780a-4376-a762-deb41e32be0c']))
    Decimal('7500000.00')
    """
    cur = pathlib.Path.cwd()
    work_file: pathlib.Path = cur / './mlt_budget.csv'
    with open(work_file) as f:
        reader = csv.reader(f)

       ''' id критерия группировки: [{
                'name': название критерия --- ~65 source_name
                'code': код критерия
                'date': дата отчетного периода,
                'plan': сумма запланированых расходов ---- sum_plan
                'fact': сумма фактических расходов}],}
        1 - budget (budget__code), 2 - fond (fond__code), 3 - source (source__code)
        1 - budget (budget_id), 2 - fond (fond_id), 3 - source (source_id)
        ++++++dict(zip())
        '''
    sel = {1:'budget', 2:'fond', 3:'source'}
    for row in reader:
        sum_plan = sum(map(lambda))
        

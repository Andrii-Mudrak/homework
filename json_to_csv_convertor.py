import pathlib
import json
import csv


test_str = """date,budget_id,budget__name,budget__code,fond_id,fond__code,fond__name,source_id,source__code,source__name,plan_s,fact_s
2020-01-01,e1915daa-b06d-11e4-8068-000c29123d1d,"м.Мелітополь, Запорiзька область",013,e490836c-bfac-43c6-8507-a5206ef13ae8,1 ,Загальний фонд,7a075f16-b0fe-11e4-8068-000c29123d1d,11010100,"Податок на доходи фізичних осіб, що сплачується податковими агентами, із доходів платника податку у вигляді заробітної плати",25000000.00,25572777.68
2020-01-01,e1915daa-b06d-11e4-8068-000c29123d1d,"м.Мелітополь, Запорiзька область",013,a791ab20-d55a-4f18-9bf5-5ac10053bbbf,2 ,2. Плата за послуги бюджетних установ,7a0760a3-b0fe-11e4-8068-000c29123d1d,25010100,"Плата за послуги, що надаються бюджетними установами згідно з їх основною діяльністю",24503236.00,1600204.08
2020-01-01,e1915daa-b06d-11e4-8068-000c29123d1d,"м.Мелітополь, Запорiзька область",013,e490836c-bfac-43c6-8507-a5206ef13ae8,1 ,Загальний фонд,7a0760f8-b0fe-11e4-8068-000c29123d1d,41033900,Освітня субвенція з державного бюджету місцевим бюджетам,12447900.00,12447900.00
"""


def convertor(path, out_path):
    """
    Написать программу что преобразует файл mlt_budget.json в csv таблицу

    json читается командой json.dumps(text)

    :param path: путь к json-файлу
    :param out_path: путь для сохранения таблицы

    ===
    >>> convertor(pathlib.Path(__file__).parent / 'mlt_budget.json', pathlib.Path(__file__).parent / 'mlt_budget.csv')
    >>> content = pathlib.Path(__file__).parent.joinpath('mlt_budget.csv').read_text().splitlines(keepends=True)[:4]
    >>> assert_str = ''.join(content)
    >>> test_str == assert_str
    True
    """

    with open(path) as json_file:
        data = json.load(json_file)
    print(path, out_path)
    f = csv.writer(open(out_path, "w", newline=''))
    f.writerow(list(data[0]))                               # csv headers
    for data in data:
        '''f.writerow([data['date'],
                    data['budget_id'],
                    data['budget__name'],
                    data['budget__code'],
                    data['fond_id'],
                    data['fond__code'],
                    data['fond__name'],
                    data['source_id'],
                    data['source__code'],
                    data['source__name'],
                    data['plan_s'],
                    data['fact_s']]
                   )'''
        f.writerow(*row.value())



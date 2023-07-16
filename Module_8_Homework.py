from datetime import datetime, timedelta
from collections import defaultdict


employees = [{"name": "Пабло Пікассо", "birthday": datetime(1990, 12, 29)},
            {"name": "Антуанетта Кабаненко", "birthday": "30.12.2000"},
            {"name": "Ієронім Шевченко", "birthday": "30.12.2000"},
            {"name": "Арчібальд Панасенко", "birthday": datetime(1985, 12, 30)},
            {"name": "Сигізмунд Перевертайло", "birthday": datetime(1985, 12, 31)},
            {"name": "Salvador Domingo Felipe Jacinto Dalí i Domènech, Marqués de Dalíy de Púbol",
            "birthday": "31.12.2000"},
            {"name": "Vincent Willem van Gogh", "birthday": datetime(1985, 12, 31)},
            {"name": "Річард Гоголь", "birthday": datetime(1965, 1, 1)},
            {"name": "Карл Гайдай", "birthday": datetime(1985, 1, 1)},
            {"name": "鈴木 陽一", "birthday": datetime(1985, 1, 1)},
            {"name": "Марио Пушкар", "birthday": datetime(1970, 1, 2)},
            {"name": "Leonardo di ser Piero da Vinci", "birthday": datetime(2000, 1, 2)},
            {"name": "中津川 春香", "birthday": datetime(2000, 1, 3)},
            {"name": "Michelangelo di Lodovico di Leonardo di Buonarroti Simoni",
            "birthday": datetime(1985, 1, 3)},
            {"name": "山田 桃子", "birthday": datetime(1950, 1, 4)},
            {"name": "Прохір Зінченко", "birthday": datetime(2000, 1, 4)},
            {"name": "Ада Шевченко", "birthday": datetime(1980, 1, 4)},
            {"name": "Rembrandt Harmenszoon van Rijn", "birthday": datetime(1985, 1, 5)},
            {"name": "Edward Hopper", "birthday": datetime(1986, 1, 5)},
            {"name": "Leslie Moreno", "birthday": datetime(1987, 1, 5)},
            {"name": "Marcantonio Galuppi", "birthday": datetime(1985, 1, 6)},
            {"name": "Martha Davis", "birthday": datetime(1985, 1, 7)},
            {"name": "Jan Vermeer van Delft", "birthday": datetime(1985, 1, 8)}]

current_date = datetime(2023, 12, 25)

def get_period() -> tuple[datetime.date, datetime.date]:
    start_period = current_date + timedelta(days=5-current_date.weekday())
    return start_period.date(), (start_period + timedelta(6)).date()
        

def check_epl(list_of_emp: list) -> None:
    result = defaultdict(list)
    current_year = current_date.year
    start, end = get_period()
    for employee in list_of_emp:
        bd = employee["birthday"]
        if isinstance(bd, datetime):
            bd = bd.date()
        else:
            bd = datetime.strptime(bd, "%d.%m.%Y").date()
        
        # обробка дат поблизу нового року
        if start.year < end.year:
            if bd.month == 12:
                bd = bd.replace(year=current_year)
            else:
                bd = bd.replace(year=(current_year + 1))
        else:
            bd = bd.replace(year=current_year)

        if start <= bd <= end:
            if bd.weekday() in (5, 6):
                result[start + timedelta(days=2)].append(employee["name"])
            else:
                result[bd].append(employee["name"])
    
    result_for_print = []
    
    for bd in result:
        result_for_print.append(f'{bd.strftime("%A")}: {", ".join(result[bd])}')
    
    return result_for_print
            

if __name__ == "__main__":
    birthdays_to_print = check_epl(employees)
    for bd in birthdays_to_print:
        print(bd)
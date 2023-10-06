import calendar
from collections import deque

class Calendar:
    def __init__(self, monthes: list[str], days: list[int]):
        self.days_in_monthes = dict(zip(monthes, days))
        self.days = deque()
        for month in monthes:
            self.days.extend([f'{i} {month}' for i in range(1, self.days_in_monthes[month] + 1)])

    def __iter__(self):
        return self

    def __next__(self):
        if self.days:
            return self.days.popleft()
        else:
            raise StopIteration

monthes_names = list(calendar.month_name)[1:]
days_in_monthes = list([calendar.monthrange(2023, month)[1] for month in range(1, 13)])

c = Calendar(monthes_names, days_in_monthes)



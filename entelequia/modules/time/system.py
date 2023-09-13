from datetime import datetime
from entelequia.system.system import GenericSystem


class TimeSystem(GenericSystem):
    def now(self):
        return datetime.now()

    def today(self):
        return datetime.now().date()

    def time_of_day(self):
        return datetime.now().time()

from datetime import date, time, datetime, timedelta

from entelequia.modules.time.system import TimeSystem
from entelequia.modules.time.interface import TimeSystemInterface


def test_time_system_accessing(app):
    assert isinstance(app.time_system, TimeSystem)

def test_time_system_implements(app):
    assert app.implements(TimeSystemInterface) == app.time_system

def test_time_system_date(app):
    assert isinstance(app.time_system.today(), date)
    today = datetime.now().date()
    assert app.time_system.today() == today

def test_time_system_time_of_day(app):
    assert isinstance(app.time_system.time_of_day(), time)
    time_of_day = datetime.now().time()
    assert datetime.combine(date.min, app.time_system.time_of_day()) - datetime.combine(date.min, time_of_day) < timedelta(seconds=2)

def test_time_system_date_and_time(app):
    assert isinstance(app.time_system.now(), datetime)
    now = datetime.now()
    assert app.time_system.now() - now < timedelta(seconds=2)

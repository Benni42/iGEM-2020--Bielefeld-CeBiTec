from period_calender_entry import PeriodCalenderEntry,Hormone
from datetime import datetime, timedelta
import random
from kivy.storage.jsonstore import JsonStore
class PeriodCalenderRepository:

    #entries = []

    def __init__(self):
        self.store = JsonStore('entry.json')

    def save(self, entry):
        existing_entry = self.findByDate(entry.date)
        if existing_entry != None:
            self.store.delete(entry.date.strftime("%Y-%m-%d"))
            #self.entries.remove(existing_entry)
        self.store.put(entry.date.strftime("%Y-%m-%d"), emotionalstate=entry.emotionalState,
                       hormone_concentration=entry.hormone_concentration, blood=entry.blood)
        #self.entries.append(entry)

    def findAll(self):
        result = []
        for key in self.store:
            value = self.store.get(key)
            result.append(PeriodCalenderEntry(datetime.strptime(key, "%Y-%m-%d"), value['emotionalstate'], value['hormone_concentration'],
                                              value['blood']))
        return result

    def findByDate(self, date):
        for entry in self.findAll():
            if entry.date.date() == date.date():
                return entry
        return None

    def findAfterDate(self, date):
        found_entries = []
        for entry in self.findAll():
            if entry.date.date() >= date.date():
                found_entries.append(entry)
        return found_entries

    def create_test_data(self):
        for i in range(40):
            date = datetime.now() - timedelta(days = i)
            emotionalState = random.randint(1, 5)
            hormone = {
                Hormone.LH: random.randint(10, 20),
                Hormone.ESTRADIOL: random.randint(10, 20),
                Hormone.PROGESTERONE: random.randint(10, 20),
            }
            self.save(PeriodCalenderEntry(date, emotionalState, hormone, False))

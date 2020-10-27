class PeriodCalenderEntry:

    def __init__(self, date, emotional_state, hormone_concentration, blood):
        self.date = date
        self.emotionalState = emotional_state
        self.hormone_concentration = hormone_concentration
        self.blood = blood

    def __str__(self):
        hormones = ""
        for hormone, value in self.hormone_concentration.items():
            hormones += "{}={}".format(str(hormone), str(value)) + ", "
        return self.date.strftime("%m/%d/%Y, %H:%M:%S") + ": emotionalState=" + str(self.emotionalState) + ", hormone_concentration=" + hormones + "blood=" + str(self.blood)

class Hormone:
    LH = str(1)
    ESTRADIOL = str(2)
    PROGESTERONE = str(3)

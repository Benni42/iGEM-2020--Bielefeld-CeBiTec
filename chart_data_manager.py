from datetime import datetime,timedelta

class ChartDataManager:

    def __init__(self, repository):
        self.repository = repository

    # IN shown graphs
    # OUT last 30 days in 2D array of values of hormones
    #
    # e.g. IN: LH, PROGESTERONE
    #      OUT: DATE        LH       PROGESTERONE
    #           [[1,2,4,5], [1,2,3], [4,5,6]]
    def getChartData(self, shown_hormones, show_mood):
        result = []
        for i in range(len(shown_hormones) + 1 + show_mood):
            result.append([])
        start_date = datetime.now() - timedelta(days=30)
        days = {}
        for i in range(31):
            entry = self.repository.findByDate(start_date + timedelta(days=i))
            if entry != None:
                days[i] = entry
        for day,entry in days.items():
            result[0].append(day) # add day to first array
            if show_mood:
                result[1].append(entry.emotionalState)
            for graphIndex in range(len(shown_hormones)):
                hormoneId = shown_hormones[graphIndex]
                result[graphIndex + 1 + show_mood].append(entry.hormone_concentration[hormoneId])
        return result

from kivy_garden.graph import Graph, MeshLinePlot, SmoothLinePlot
from kivy.graphics import Color
from kivy.uix.boxlayout import BoxLayout
import chart_data_manager
from period_calender_entry import PeriodCalenderEntry, Hormone
from period_calender_repository import PeriodCalenderRepository
from chart_data_manager import ChartDataManager
from datetime import datetime, timedelta

repository = PeriodCalenderRepository()
repository.create_test_data()
chartData = ChartDataManager(repository)


def create_graph(values, shown, color, show_mood):
    plot = None

    graph = Graph(ylabel='Concentration', x_ticks_major=1, y_ticks_minor=1, y_ticks_major=1, y_grid_label='True',
                  x_grid_label='True', xlabel='Day relative to today.', padding=5, x_grid=True, y_grid=True, xmin=-30, xmax=2, ymin=0, ymax=30)

    if (len(shown) + show_mood > 0):
        for i in range(0, len(shown) + show_mood):
            plot = SmoothLinePlot(color=color[i])

            plot.points = [(i-30, j) for i, j in zip(values[0], values[i + 1])]

            graph.add_plot(plot)
    return graph



class Dataset(BoxLayout):
    def __init__(self, **kwargs):
        super(Dataset, self).__init__(**kwargs)
        self.size_hint = (1, 3)
        self.orientation = 'horizontal'
        self.all_hormones = [Hormone.LH, Hormone.ESTRADIOL, Hormone.PROGESTERONE]
        self.shown_hormones = [Hormone.LH, Hormone.ESTRADIOL, Hormone.PROGESTERONE]
        self.color_hormone = [[1, 1, 0, 1], [0, 1, 1, 1], [1, 0.5, 0.5, 1], [0.5, 0, 1, 1]]
        self.show_mood = True
        self.values = chart_data_manager.ChartDataManager.getChartData(chartData, self.shown_hormones, True)

        graph = create_graph(self.values, self.shown_hormones, self.color_hormone, self.show_mood)

        self.add_widget(graph)

    def add_hormone(self,name):
        self.shown_hormones.append(name)

    def remove_hormone(self,name):
        self.shown_hormones.remove(name)

    def state_show_horone(self, boolean):
        self.show_mood = boolean
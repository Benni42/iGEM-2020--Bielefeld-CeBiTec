from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
import graphmacro
from period_calender_entry import Hormone
from period_calender_entry import PeriodCalenderEntry
from datetime import datetime


def on_checkbox_active(checkbox, value):
    if value:
        print('The checkbox', checkbox, 'is active')
    else:
        print('The checkbox', checkbox, 'is inactive')


class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        self.add_widget(HomeBorder())
    pass


class HomeBorder(GridLayout):
    def __init__(self, **kwargs):
        super(HomeBorder, self).__init__(**kwargs)
        self.rows = 8
        self.row_default_height = 10
        #self.add_widget(HomeOben())
        self.add_widget(Label(text="How is your emotional state today?"))
        self.add_widget(Smileys())
        self.add_widget(Period())

        self.add_widget(TodayInfoEs())
        self.add_widget(TodayInfoFertile())
        self.add_widget(TodayInfoBlood())
        self.add_widget(TodayInfoConcentration())
        #self.add_widget(TodayOutput()


        #self.add_widget(HomeMitte())
        self.add_widget(HomeUnten())
    pass


class HomeOben(GridLayout):
    def __init__(self, **kwargs):
        super(HomeOben, self).__init__(**kwargs)
        self.cols = 5
        self.add_widget(Button())
        self.add_widget(Button())
        self.add_widget(Button())
        self.add_widget(Button())
        self.add_widget(Button())
    pass


class HomeMitte(GridLayout):
    def __init__(self, **kwargs):
        super(HomeMitte, self).__init__(**kwargs)
        self.size_hint = (1, 5)
        self.rows = 4
    pass

#In Mitte-----------------------------------------------------------------


class Smileys(GridLayout):
    def __init__(self, **kwargs):
        super(Smileys, self).__init__(**kwargs)
        self.cols = 5
        self.add_widget(SmileyButton1())
        self.add_widget(SmileyButton2())
        self.add_widget(SmileyButton3())
        self.add_widget(SmileyButton4())
        self.add_widget(SmileyButton5())
    pass
#--------------------------------Sminley Buttons--------------------------------------


class SmileyButton1(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(SmileyButton1, self).__init__(**kwargs)
        self.source = 'resources/02.png'
        self.group = "Smileys"

    def on_press(self):
        entry = graphmacro.repository.findByDate(datetime.now())
        if entry is not None:
            entry.emotionalState = 5
        else:
            entry = PeriodCalenderEntry(datetime.now(), 5, {}, False)
        graphmacro.repository.save(entry)

    def on_state(self, widget, value):
        if value == 'down':
            self.source = 'resources/2.png'
        else:
            self.source = 'resources/02.png'
    pass


class SmileyButton2(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(SmileyButton2, self).__init__(**kwargs)
        self.source = 'resources/01.png'
        self.group = "Smileys"

    def on_press(self):
        entry = graphmacro.repository.findByDate(datetime.now())
        if entry is not None:
            entry.emotionalState = 4
        else:
            entry = PeriodCalenderEntry(datetime.now(), 4, {}, False)
        graphmacro.repository.save(entry)

    def on_state(self, widget, value):
        if value == 'down':
            self.source = 'resources/1.png'
        else:
            self.source = 'resources/01.png'
    pass


class SmileyButton3(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(SmileyButton3, self).__init__(**kwargs)
        self.source = 'resources/00.png'
        self.group = "Smileys"

    def on_press(self):
        entry = graphmacro.repository.findByDate(datetime.now())
        if entry is not None:
            entry.emotionalState = 3
        else:
            entry = PeriodCalenderEntry(datetime.now(), 3, {}, False)
        graphmacro.repository.save(entry)

    def on_state(self, widget, value):
        if value == 'down':
            self.source = 'resources/0.png'
        else:
            self.source = 'resources/00.png'
    pass


class SmileyButton4(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(SmileyButton4, self).__init__(**kwargs)
        self.source = 'resources/0-1.png'
        self.group = "Smileys"

    def on_press(self):
        entry = graphmacro.repository.findByDate(datetime.now())
        if entry is not None:
            entry.emotionalState = 2
        else:
            entry = PeriodCalenderEntry(datetime.now(), 2, {}, False)
        graphmacro.repository.save(entry)

    def on_state(self, widget, value):
        if value == 'down':
            self.source = 'resources/-1.png'
        else:
            self.source = 'resources/0-1.png'
    pass


class SmileyButton5(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(SmileyButton5, self).__init__(**kwargs)
        self.source = 'resources/0-2.png'
        self.group = "Smileys"

    def on_press(self):
        entry = graphmacro.repository.findByDate(datetime.now())
        if entry is not None:
            entry.emotionalState = 1
        else:
            entry = PeriodCalenderEntry(datetime.now(), 1, {}, False)
        graphmacro.repository.save(entry)

    def on_state(self, widget, value):
        if value == 'down':
            self.source = 'resources/-2.png'
        else:
            self.source = 'resources/0-2.png'
    pass

#--------------------------------------------------------------------------------------

class Period(GridLayout):
    def __init__(self, **kwargs):
        super(Period, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Are you on your period?"))
        self.add_widget(Periodbutton())
    pass

class Periodbutton(CheckBox):
    def __init__(self, **kwargs):
        super(Periodbutton, self).__init__(**kwargs)
        self.active =on_checkbox_active
        self.state = 'normal'

    def on_press(self):
        entry = graphmacro.repository.findByDate(datetime.now())
        if entry is not None:
            entry.blood = self.state == 'down'
        else:
            entry = PeriodCalenderEntry(datetime.now(), 3, {}, self.state == 'down')
        graphmacro.repository.save(entry)



#--------Todays Output------------
class TodayOutput(GridLayout):
    def __init__(self, **kwargs):
        super(TodayOutput, self).__init__(**kwargs)
        self.rows = 3
    pass


#------------------------------
class TodayInfoEs(Label):
    def __init__(self, **kwargs):
        super(TodayInfoEs, self).__init__(**kwargs)
        if True:
            self.text = "Your hormones could have a negative impact on your mood."
        elif True:
            self.text = "Your hormones will have no impact on your mood."
        else:
            self.text = "Your hormaones could have a positive impact on your mood."


class TodayInfoFertile(Label):
    def __init__(self, **kwargs):
        super(TodayInfoFertile, self).__init__(**kwargs)
        if 20 > graphmacro.repository.findByDate(datetime.today()).hormone_concentration[Hormone.PROGESTERONE]:
        # and LH and Estradiol are decending
            self.text = "It´s likly that you you are fertile today."
        else:
            self.text = "It´s unlikly that you get you are fertile today."



class TodayInfoBlood(Label):
    def __init__(self, **kwargs):
        super(TodayInfoBlood, self).__init__(**kwargs)
        if not graphmacro.repository.findByDate(datetime.today()).blood:
            self.text = "It´s unlikly that you get your period today."
        else:
            self.text = "It´s likly that you get your period today."


class TodayInfoConcentration(GridLayout):
    def __init__(self, **kwargs):
        super(TodayInfoConcentration, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 2
        self.add_widget(Label(text="Progesteron concentration: " + str(graphmacro.repository.findByDate(datetime.today()).hormone_concentration["3"])))
        self.add_widget(Label(text="Estradiol concentration: " + str(graphmacro.repository.findByDate(datetime.today()).hormone_concentration["2"])))
        self.add_widget(Label(text="LH concentration: " + str(graphmacro.repository.findByDate(datetime.today()).hormone_concentration["1"])))
        self.add_widget(Label(text="MoodValue: " + str(graphmacro.repository.findByDate(datetime.today()).emotionalState)))



#-------------------------------------------------------------------------
def go_to_graphs(_a):
    sm.transition.direction = "left"
    sm.current = "Graphs"


def go_to_home(_a):
    sm.transition.direction = "right"
    sm.current = "Home"


InPutStream = [10, 15, 20]


#Bluetooth Input would go here



def sync_f(_a):
    #perform Bluetooth sync

    hormone = {
        Hormone.LH: InPutStream[0],
        Hormone.ESTRADIOL: InPutStream[1],
        Hormone.PROGESTERONE: InPutStream[2],
    }
    entry = graphmacro.repository.findByDate(datetime.now())
    if entry is not None:
        entry.hormone_concentration = hormone
    else:
        entry = PeriodCalenderEntry(datetime.now(), 3, hormone, False)
    graphmacro.repository.save(entry)
    print(graphmacro.repository.findByDate(datetime.now()))


class HomeUnten(GridLayout):
    def __init__(self, **kwargs):
        super(HomeUnten, self).__init__(**kwargs)
        self.size_hint = (1, 0.5)
        self.cols = 2
        self.sync_button = Button(text="Sync")
        self.sync_button.bind(on_press=sync_f)
        self.add_widget(self.sync_button)
        self.to_graphs_button = Button(text="Graphs")
        self.to_graphs_button.bind(on_press=go_to_graphs)
        self.add_widget(self.to_graphs_button)
    pass
#Home Ende-----------------------------------------------------------------


#Graphs Page Anfaang--------------------------------------------------------
class Graphs(Screen):
    def __init__(self, **kwargs):
        super(Graphs, self).__init__(**kwargs)
        self.add_widget(GraphsBorder())
    pass



class GraphsBorder(GridLayout):
    def __init__(self, **kwargs):
        super(GraphsBorder, self).__init__(**kwargs)
        self.rows = 5
        graf_von_erhobenen_daten = graphmacro.Dataset()
        self.add_widget(graf_von_erhobenen_daten)
        #self.add_widget(GrapsMitte())
        #self.add_widget(GrapsUnten())
        self.add_widget(GrapsGanzunten())
    pass

#-------------------------------In Grpahs-------------------------


class GrapsGanzoben(GridLayout):
    def __init__(self, **kwargs):
        super(GrapsGanzoben, self).__init__(**kwargs)
        self.add_widget(Label(text="Graphs"))
    pass



def toggle_graph(_a):
    graphmacro.shown_hormones.append(Hormone.PROGESTERONE)
    print("bla")
    #if _a.id ==  'mood':
    #if _a.state == 'down':




class GrapsMitte(GridLayout):
    def __init__(self, **kwargs):
        super(GrapsMitte, self).__init__(**kwargs)
        self.cols = 4

        self.show_mood_button = ToggleButton(text="mood", id = "mood")
        self.show_mood_button.bind(on_press=toggle_graph)
        self.add_widget(self.show_mood_button)

        self.add_widget(Button(text="i"))

        self.show_progesteron_button = ToggleButton(text="progesteron", id="progesteron")
        self.show_progesteron_button.bind(on_press=toggle_graph)
        self.add_widget(self.show_progesteron_button)

        self.add_widget(Button(text="i"))
    pass


class GrapsUnten(GridLayout):
    def __init__(self, **kwargs):
        super(GrapsUnten, self).__init__(**kwargs)
        self.cols = 4

        self.show_lh_button = ToggleButton(text="lh", id="lh")
        self.show_lh_button.bind(on_press=toggle_graph)
        self.add_widget(self.show_lh_button)

        self.add_widget(Button(text="i"))

        self.show_estradiol_button = ToggleButton(text="estradiol", id="estradiol")
        self.show_estradiol_button.bind(on_press=toggle_graph)
        self.add_widget(self.show_estradiol_button)

        self.add_widget(Button(text="i"))
    pass


class Info(Screen):
    def go_to_graphs(self):
        sm.transition.direction = "right"
        sm.current = "Graphs"
    pass


def go_to_info(_a):
    #view = ModalView(size_hint=(0.9, 0.9))
    #view.add_widget(Label(markup=True, pos=(100, 100),
#                          text="[b][u]About the WavySense project[/u][/b] \n Women all over the world wish to abstain from taking the pill because it causes a lot of side effects. Not taking the pill means the female body is undergoing its natural cycle in which there are fertile and non fertile days. Knowing this cycle a women is able to predict if she can get pregnant or not. The concentration of the sex hormones estradiol, progesterone, LH and FSH proved to be indicators for the respective cycle phase. Therefore a device measuring the concentration of these hormones and evaluating them could give women a potent alternative to artificial hormonal contraception. For measuring low level concentrations high sensitivity methods such as Surface acoustic wave technology (SAW) are needed. SAW is a method by which a wave is generated inside a piezoelectric crystal. In the center of this crystal a gold layer is applied, on which antibodies or their derivatives are immobilized. These antibodies bind the target specifically. The antibody – antigen interaction results in a mass shift inducing a phase shift in the crystal. This phase shift is recognized by the associated electronics and evaluated by this app.", ))

    #view.add_widget(TextHolder())
    sm.current = "Info"


class TextHolder(GridLayout):
    def __init__(self, **kwargs):
        super(TextHolder, self).__init__(**kwargs)
        #self.rows = 2
        self.add_widget(Label(text_size= self.size, markup=True, valign="middle", halign="justify", text="[b][u]About the WavySense project[/u][/b] \n Women all over the world wish to abstain from taking the pill because it causes a lot of side effects. Not taking the pill means the female body is undergoing its natural cycle in which there are fertile and non fertile days. Knowing this cycle a women is able to predict if she can get pregnant or not. The concentration of the sex hormones estradiol, progesterone, LH and FSH proved to be indicators for the respective cycle phase. Therefore a device measuring the concentration of these hormones and evaluating them could give women a potent alternative to artificial hormonal contraception. For measuring low level concentrations high sensitivity methods such as Surface acoustic wave technology (SAW) are needed. SAW is a method by which a wave is generated inside a piezoelectric crystal. In the center of this crystal a gold layer is applied, on which antibodies or their derivatives are immobilized. These antibodies bind the target specifically. The antibody – antigen interaction results in a mass shift inducing a phase shift in the crystal. This phase shift is recognized by the associated electronics and evaluated by this app.",))
        #self.add_widget(Label(markup=True, text= "[b][u]About the hormones[/u][/b] \n [b]Estradiol[/b] \n Estradiol is an estrogen steroid hormone and the major female sex hormone. It is involved in the regulation of the estrous and menstrual female reproductive cycles. \n [b]Progesterone[/b] \n Progesterone is an endogenous steroid and progestogen sex hormone involved in the menstrual cycle, pregnancy, and embryogenesis of humans and other species. It belongs to a group of steroid hormones called the progestogens, and is the major progestogen in the body. Progesterone has a variety of important functions in the body.\n [b]LH and FSH[/b] \n In females, an acute rise of LH (Luteinizing hormone) triggers ovulation and development of the corpus luteum. FSH (Follicle-stimulating hormone) regulates the development, growth, pubertal maturation, and reproductive processes of the body. FSH and LH work together in the reproductive system.",font_size= '16sp'))
    pass


class TextWidget1(Label):
    def __init__(self, **kwargs):
        super(TextWidget1, self).__init__(**kwargs)

    pass


class TextWidget2(Label):
    def __init__(self, **kwargs):
        super(TextWidget2, self).__init__(**kwargs)
        self.add_widget(Label(markup=True, text= "[b][u]About the hormones[/u][/b] \n [b]Estradiol[/b] \n Estradiol is an estrogen steroid hormone and the major female sex hormone. It is involved in the regulation of the estrous and menstrual female reproductive cycles. \n [b]Progesterone[/b] \n Progesterone is an endogenous steroid and progestogen sex hormone involved in the menstrual cycle, pregnancy, and embryogenesis of humans and other species. It belongs to a group of steroid hormones called the progestogens, and is the major progestogen in the body. Progesterone has a variety of important functions in the body.\n [b]LH and FSH[/b] \n In females, an acute rise of LH (Luteinizing hormone) triggers ovulation and development of the corpus luteum. FSH (Follicle-stimulating hormone) regulates the development, growth, pubertal maturation, and reproductive processes of the body. FSH and LH work together in the reproductive system.",font_size= '16sp'))
    pass


class GrapsGanzunten(GridLayout):
    def __init__(self, **kwargs):
        super(GrapsGanzunten, self).__init__(**kwargs)
        self.size_hint=(1, 0.85)
        self.rows =3
        self.cols = 2
        self.add_widget(Label(text="Progesteron", color=(0.5, 0, 1, 1)))
        self.add_widget(Label(text="Estradiol", color=(1, 0.5, 0.5, 1)))
        self.add_widget(Label(text="LH", color=(0, 1, 1, 1)))
        self.add_widget(Label(text="Mood", color=(1, 1, 0, 1)))

        self.to_home_button = Button(text="Homescreen")
        self.to_home_button.bind(on_press=go_to_home)
        self.add_widget(self.to_home_button)

        self.to_info_button = Button(text="more information")
        self.to_info_button.bind(on_press=go_to_info)
        self.add_widget(self.to_info_button)
    pass


#--------------------------------Ende Graphs----------------------



#Graphs Ende Anfaang--------------------------------------------------------
class Manager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
sm = Manager()

screens = [Home(name="Home"), Graphs(name="Graphs"), Info(name="Info")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "Home"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
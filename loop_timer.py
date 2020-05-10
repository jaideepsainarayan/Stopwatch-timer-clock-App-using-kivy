import kivy 
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
import kivy.uix.image 
from kivy.config import Config 
Config.set('graphics', 'resizable', 1) 
from kivy.lang import Builder
from kivy.lang import Builder
from kivy.clock import Clock
import time
from time import strftime

sec=0
mi=0
hr=0

tr = Builder.load_string('''
<NGrid>:
    rows:2
    padding:2
    PageLayout:
        Label:
            id: timer
            font_size: 25
            text:"0:0:0"
            
        Label:
            id:clk
            font_size: 25
            text:" "
            color:(0,0.1,0.2,1)
            canvas.before:
                Rectangle:
                    pos: self.pos
                    size: self.size
                    source: "clock.jpg"
    BoxLayout:
        ToggleButton:
            id: ko
            markup: True
            text: "start"
            on_press: self.text ="start" if(ko.state == "normal") else("Pause")
        Button:
            id:ok
            text: "reset"
            on_press: root.rest()

''')
class NGrid(GridLayout):
    
    def rest(self):
        global mi
        global hr
        global sec
        sec=0 
        hr=0
        mi=0
        self.ids.timer.text='0:0:0'
    

class Timer(App):

    def on_start(self):
        Clock.schedule_interval(self.tim,1)
        Clock.schedule_interval(self.time,1)


    def time(self,*args):
        self.root.ids.clk.text= str(strftime("%b %d %Y %H:%M:%S"))

    def tim(self,*args):
        global sec
        global mi
        global hr
        ii=1
        if self.root.ids.ko.text == "Pause":
            ii-=1 
            sec +=1 
            if sec== 59:
                sec =0
                mi +=1
            if mi ==60:
                mi =0
                hr+=1
            self.root.ids.timer.text = str(str(hr)+':'+str(mi)+':'+str(sec))

    def build(self):
        return NGrid()
Timer().run()


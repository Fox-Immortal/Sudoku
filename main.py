import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder 
from solve import grid
from kivy.clock import Clock
from kivy.uix.button import Button
from functools import partial
kivy.require("1.10.1")

kvfile = Builder.load_file("file.kv")
#grid[3][3][3][3]
#31701256022
class Grid(BoxLayout):
    def __init__(self, **kwagrs):
        super().__init__(**kwagrs)
        self.can = False
        self.grid = BoxLayout(orientation='vertical')
        self.grid.spacing = 4
        for j in range(3):
            self.big_cols = BoxLayout(orientation='vertical')
            for l in range(3):
                self.row = BoxLayout(orientation='horizontal')
                self.row.spacing = 4
                for i in range(3):
                    self.col = BoxLayout(orientation='horizontal')
                    for k in range(3):
                        self.cube = self.create_cube(grid[j][l][i][k])
                        self.col.add_widget(self.cube)
                    self.row.add_widget(self.col)
                self.big_cols.add_widget(self.row)
            self.grid.add_widget(self.big_cols)
        self.orientation = 'vertical'
        self.footer = BoxLayout(orientation='horizontal')
        self.btn_solve = Button(text="Solve")
        self.btn_solve.bind(on_press=self.gui_solve)
        self.footer.add_widget(self.btn_solve)
        self.counter = Button(text="Your mistakes are : 0")
        self.counter.bind(on_press=self.gui_solve)
        self.counter.mistakes = 0
        self.footer.add_widget(self.counter)
        self.grid.add_widget(self.footer)
        self.add_widget(self.grid)
        for i in range(1,4):
            for j in range(3):
                for k in range(3):
                    print("[ ", end="")
                    for l in range(3):
                        self.grid.children[i].children[j].children[k].children[l].data = (i, j, k, l)
                        grid[i][j][k][l] = int(self.grid.children[i].children[j].children[k].children[l].text)
                        print(self.grid.children[i].children[j].children[k].children[l].text, end=" , ")
                    print("],", end="")
                print()
    def happen(self, *args):
        print(args)
        print("***************************")
        return args
    def color(self, colors, instance, *args):
        instance.background_color = colors
    def clean(self, instance, *args):
        for i in range(1, 4):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        ins = self.grid.children[i].children[j].children[k].children[l]
                        if(instance != None and ins == instance):
                            continue
                        if(instance == None and ins.text == "0"):
                            continue
                        Clock.schedule_once(partial(self.color, (1, 1, 1, 1), ins), (i*0.09 + j*0.01 + k*0.01 + l*0.01) + 0.01)
    def lightup(self, instance, value):
        Clock.schedule_once(partial(self.happen, 1, 2, 3), 0.5)
        self.clean(instance)
        instance.background_color = (0.5,0.5,1,1)
    def validate(self, position, *args):
        big_row = position[0] 
        small_row = position[1]
        small_col = position[2]
        cell = position[3]
        number = self.grid.children[big_row].children[small_row].children[small_col].children[cell].text
        self.currx = self.grid.children[big_row].children[small_row].children[small_col].children[cell]
        can = True
        for i in range(3):
            for j in range(3):
                self.curr = self.grid.children[big_row].children[small_row].children[i].children[j]
                ins = self.curr
                if i == small_col and j == cell:
                    continue 
                if self.curr.text == str(number):
                    Clock.schedule_once(partial(self.color, (1, 0, 0, 1), ins), (big_row*0.09 + small_row*0.05 + i*0.05 + j*0.05) + 0.01)
                    can = False
                else:
                    Clock.schedule_once(partial(self.color, (0.2, 1.2, 0.2, 1), ins), (big_row*0.09 + small_row*0.05 + i*0.05 + j*0.05) + 0.01)
        for i in range(3):
            for j in range(3):
                self.curr = self.grid.children[i + 1].children[j].children[small_col].children[cell]
                ins = self.curr
                if i + 1 == big_row and j == small_row:
                    continue
                if self.curr.text == str(number):
                    Clock.schedule_once(partial(self.color, (1, 0, 0, 1), ins), (i*0.09 + j*0.05 + small_col*0.05 + cell*0.05) + 0.01)
                    can = False
                else:
                    Clock.schedule_once(partial(self.color, (0.2, 1.2, 0.2, 1), ins), (i*0.09 + j*0.05 + small_col*0.05 + cell*0.05) + 0.01)
        for i in range(3):
            for j in range(3):
                self.curr = self.grid.children[big_row].children[i].children[small_col].children[j]
                ins = self.curr
                if i == small_row and j == cell:
                    continue
                if self.curr.text == str(number):
                    Clock.schedule_once(partial(self.color, (1, 0, 0, 1), ins), (big_row*0.09 + i*0.05 + small_col*0.05 + j*0.05) + 0.01)
                    can = False
                else:
                    Clock.schedule_once(partial(self.color, (0.2, 1.2, 0.2, 1), ins), (big_row*0.09 + i*0.05 + small_col*0.05 + j*0.05) + 0.01)
        if(not can):
            return False
        return True
    def valid(self, instance, value):
        if value == '0' or value == "":
            self.clean(instance)
        elif(not value.isnumeric() or len(value) > 1):
            instance.text = ""
        else:
            v = self.validate(instance.data)
            if(not v and not self.can):
                self.counter.mistakes += 1
                self.counter.text= f"Your mistakes are : {self.counter.mistakes}"
    def create_cube(self, number):      
        self.cube = TextInput(multiline=False, text=str(number))
        self.cube.padding = self.cube.width/8
        self.cube.bind(text=self.valid)
        self.cube.bind(focus=self.lightup)
        return self.cube
    def find_empty(self):
        for i in range(1, 4):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        if self.grid.children[i].children[j].children[k].children[l].text == '0':
                            return (i, j, k, l)
        return None
    def gui_find(self, *args):
        self.zeros = []
        for i in range(1, 4):
            for j in range(3):
                timing = i*0.09 + j*0.09 + 0.1
                for k in range(3):
                    for l in range(3):
                        ins = self.grid.children[i].children[j].children[k].children[l]
                        Clock.schedule_once(partial(self.color, (1, 1, 0, 1), ins), timing)
                        if ins.text == '0':
                            self.zeros.append([i, j, k, l])
                            Clock.schedule_once(partial(self.color, (1.2, 0.1, 0.1, 1), ins), timing)
        return self.zeros
    def gui_solve(self, *args):
        to_valid = self.gui_find()
        Clock.schedule_once(partial(self.clean, None), 1.2)
        for c in to_valid:
            Clock.schedule_once(partial(self.validate, c), 1.6)
        Clock.schedule_once(partial(self.clean, None), 2)
        Clock.schedule_once(partial(self.solve), 2.1)
    def solve(self, *args):
        self.can = True
        found = self.find_empty()
        if not found:
            Clock.schedule_once(partial(self.clean, None), 1.5) 
            self.can = False
            return True
        i, j, k, l = found
        for num in range(1, 10):
            self.grid.children[i].children[j].children[k].children[l].text = str(num)
            if(self.validate(found)):
                if(self.solve() == True):
                    return True
            self.grid.children[i].children[j].children[k].children[l].text = '0'
        return False
    



class MainPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.grid = Grid()
        self.add_widget(self.grid)


class EpicApp(App):
    def build(self):
        self.main_page = MainPage()
        return self.main_page

if __name__ == "__main__":
    # Window.fullscreen = 'auto'
    Window.size = (700, 600)
    EpicApp().run()

import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder 
from kivy.uix.splitter import Splitter
from solve import board

kivy.require("1.10.1")

kvfile = Builder.load_file("file.kv")
#grid[3][3][3][3]
#31701256022
class Grid(BoxLayout):
    def __init__(self, **kwagrs):
        super().__init__(**kwagrs)
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
                        self.cube = self.create_cube(board[j][l][i][k])
                        self.cube.data = (j, l, i, k)
                        self.col.add_widget(self.cube)
                    self.row.add_widget(self.col)
                self.big_cols.add_widget(self.row)
            self.grid.add_widget(self.big_cols)
        self.orientation = 'vertical'
        self.footer = Label(text="hey there")
        self.grid.add_widget(self.footer)
        self.add_widget(self.grid)
        for i in range(1,3):
            for j in range(3):
                for k in range(3):
                    print("[ ", end="")
                    for l in range(3):
                        print(self.grid.children[i].children[j].children[k].children[l].text, end=" , ")
                    print("],", end="")
                print()
    def lightup(self, instance, value):
        if(value):
            instance.background_color = (0.5,0.5,1,1)
        else:
            instance.background_color = (1,1,1,1)
    def validate(self, board, number, position):
        for i in range(3):
            for j in range(3):
                if board.children[position[0] + 1].children[position[1]].children[i].children[j].text == str(number) and i != position[2] and j != position[3]:
                    return False
        for i in range(1, 3):
            for j in range(3):
                if board.children[i].children[j].children[position[2]].children[position[3]].text == str(number) and i != position[0] + 1 and j != position[1]:
                    return False        
        box_row = position[0] + 1
        box_col = position[2]
        for i in range(3):
            for j in range(3):
                if board.children[box_row].children[i].children[box_col].children[j] == str(number) and i != position[1] and j != position[3]:
                    return False
        return True
    def valid(self, instance, value):
        if(not value.isnumeric() or len(value) > 1):
            instance.text = ""
        else:
            val = self.validate(self.grid, int(value), instance.data)
            print(val)
    def create_cube(self, number):        
        self.cube = TextInput(multiline=False, text=str(number))
        self.cube.padding = self.cube.width/8
        self.cube.bind(text=self.valid)
        self.cube.bind(focus=self.lightup)
        return self.cube
    
    

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

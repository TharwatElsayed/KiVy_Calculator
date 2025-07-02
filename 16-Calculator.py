import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

Window.size=(500,700)

Builder.load_file("my.kv")

class LoginScreen(Widget):
   def clear(self):
      self.ids.calc_input.text="0"

   def percentage(self):
      pr = self.ids.calc_input.text
      answer = float(pr)/100
      self.ids.calc_input.text=str(answer)

   def remove(self):
      pr=self.ids.calc_input.text
      pr=pr[0:-1]
      self.ids.calc_input.text=pr

   def min_neg(self):
      pr=self.ids.calc_input.text
      if "-" in pr:
         self.ids.calc_input.text=f'{pr.replace("-","")}'
      else:
         self.ids.calc_input.text=f"-{pr}"

   def dot(self):
      pr=self.ids.calc_input.text
      num = pr.split("+")
      if "+" in pr and "." not in num[0:-1]:
         pr=f'{pr}.'
         self.ids.calc_input.text=str(pr)
      elif '.' in pr:
         pass
      else:
         pr = f'{pr}.'
         self.ids.calc_input.text = pr

   def btn_press(self,btn):
      pr=self.ids.calc_input.text
      if "Error" in pr:
         pr=""
      if pr=="0":
         self.ids.calc_input.text=""
         self.ids.calc_input.text=f'{btn}'
      else:
         self.ids.calc_input.text=f'{pr}{btn}'

   def add(self,sign):
      pr=self.ids.calc_input.text
      self.ids.calc_input.text=f'{pr}{sign}'

   def equals(self):
      pr=self.ids.calc_input.text
      try:
         answer=eval(pr)
         self.ids.calc_input.text = str(answer)
      except:
         self.ids.calc_input.text ="Error"
   
    
class Calc(App):
    def build(self):
       #Window.clearcolor=(0.4,0.6,1,1)
       return LoginScreen()
if __name__=='__main__':
    Calc().run()

from bank import *
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window

joe = Bank("Joe", 23, "23459876")

class HomeWindow(Screen):
    accountNo = joe.account
    balance = joe.balance
    pass


class NewPantWindow(Screen):
    code = ObjectProperty(None)
    pass


class ConfirmationWindow(Screen):
    pass


class TransferWindow(Screen):
    account = ObjectProperty(None)
    withdraw = ObjectProperty(None)

    def details(self):
        print("Account", self.account.text, "Withdraw", self.withdraw.text)
        self.account.text = ""
        self.withdraw.text = ""
    pass


class SuccessfulTransfer(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

class GreenSavingsApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return kv
        # return MyGrid()


if __name__ == "__main__":
    GreenSavingsApp().run()

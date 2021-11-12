# Joe = Bank("Joe", 23, "Current")
#
# class MyGrid(GridLayout):
#     def __init__(self, **kwargs):
#         super(MyGrid, self).__init__(**kwargs)
#         self.cols = 1
#
#         self.inside = GridLayout()
#         self.inside.cols = 2
#
#         self.inside.add_widget(Label(text=" First Name: "))
#         self.name = TextInput(multiline=False)
#         self.inside.add_widget(self.name)
#
#         self.inside.add_widget(Label(text="Last Name: "))
#         self.lastname = TextInput(multiline=False)
#         self.inside.add_widget(self.lastname)
#
#         self.inside.add_widget(Label(text="Account type: "))
#         self.account = TextInput(multiline=False)
#         self.inside.add_widget(self.account)
#
#         self.add_widget(self.inside)
#
#         self.checkbalance = Button(text="Check Balance", font_size=20)
#         self.checkbalance.bind(on_press=self.balance)
#         self.add_widget(self.checkbalance)
#
#         self.newpant = Button(text="Add new pant", font_size=20)
#         self.newpant.bind(on_press=self.pressedN)
#         self.add_widget(self.newpant)
#
#         self.transferpant = Button(text="Transfer pant to account", font_size=20)
#         self.transferpant.bind(on_press=self.pressedT)
#         self.add_widget(self.transferpant)
#
#     def pressedT(self, instance):
#         print("Transfer page")
#
#     def pressedN(self, instance):
#         print("Pant Page")
#
#     def balance(self, instance):
#         print(Joe.balance)

# canvas.before:
#                     Color:
#                         rgba: self.background_color
#                     Rectangle:
#                         size: self.size
#                         pos: self.pos

# class MyGrid(Widget):
#     pass


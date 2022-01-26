from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBody
from kivymd.uix.button import MDIconButton
from kivy.lang.builder import  Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivy.core.window import Window

Window.size = (320, 600)

dictionary = {
'instagram': 'giphy.gif',
'twitter' : 'twitter.gif'



}

class ContentNavigationDrawer(BoxLayout):
    pass



class RightButton(IRightBody, MDIconButton):
    """ The only usefull part is IRightBody.
    Needed to align 'minus' icon button to the right
    in SearchResultItem 
    """
    pass
class SearchResultItem(TwoLineAvatarIconListItem):
    """Need to redefine ___init___ method in order to pass (stick) an extra param - user_id"""
    def __init__(self, user_id, **kwargs):
        super(SearchResultItem, self).__init__(**kwargs)
        self.user_id = user_id
    def delete_phone(self, user_id):
        if User.delete_by_id(user_id):
            self.parent.remove_widget(self)


class MainWindow(MDBoxLayout):
    pass

class PhoneBookApp(MDApp):


    def get_info_for_button(self, instance, text):
        pass



    def on_start(self):
        for item in dictionary:
            self.root.ids.images.add_widget(Image(size_hint_y=None, source = dictionary[item], height = 180))
            self.root.ids.images.add_widget(Button(size_hint_y=None, text = item, height = 10))

        



    def build(self):
        self.title = 'Мега телефонная книга'
        self.theme_cls.primary_palette = "BlueGray"  # "Purple", "Red"
        self.icon = 'Mobile-icon.png'
        return MainWindow()

if __name__ == '__main__':
    PhoneBookApp().run()
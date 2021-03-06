
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.effects.scroll import ScrollEffect

from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivy.uix.scrollview import ScrollView
from kivymd.font_definitions import fonts


from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

from kivy.uix.button import Button
from kivymd.icon_definitions import md_icons

class Template(BoxLayout):
    pass

class Tab(MDFloatLayout, MDTabsBase):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class TestNavigationDrawer(MDApp):

    icons = list(md_icons.keys())[1:3]

    def about_as(self, instance, text):
        print(text)

    def inurl_get(self, instance):
        print(instance.text)



    def build(self):
        return Builder.load_file('main.kv')



    def on_start(self):
        icons_item = {
            "theme-light-dark": "Theme",
            "star": "Favorites",
        }
        # for icon_name in icons_item.keys():
        #     self.root.ids.content_drawer.ids.md_list.add_widget(
        #         ItemDrawer(icon=icon_name, text=icons_item[icon_name])
        #     )

        for name_tab in self.icons:
            self.root.ids.tabs.add_widget(
                Tab(
                    text=f"[ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons['close']}[/font][/ref]  {name_tab}"
                )
            )




        

TestNavigationDrawer().run()

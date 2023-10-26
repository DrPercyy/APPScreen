from kivymd.app import MDApp
import os
from kaki.app import App
from kivy.factory import Factory
from kivy.core.window import Window #You must import this
Window.size = (640, 920)

class LiveApp(MDApp, App):
    
    DEBUG = 1  # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "APP\Screens\screenmanager.kv"),
        os.path.join(os.getcwd(), "APP\Screens\loginscreen\loginscreen.kv"),
        }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "Screens.screenmanager",
        "LoginScreen": "Screens.loginscreen.loginscreen",
        }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
        ]

    def build_app(self):
        return Factory.MainScreenManager()


if __name__ == "__main__":
    LiveApp().run()

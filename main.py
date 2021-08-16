from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class WallpaperProgramApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, WallpaperProgram", halign="center")


WallpaperProgramApp().run()
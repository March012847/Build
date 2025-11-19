from kivy.app import App
from kivy.uix.label import Label

class FastBuildApp(App):
    def build(self):
        return Label(text="Hello Buildozer!")

if __name__ == "__main__":
    FastBuildApp().run()

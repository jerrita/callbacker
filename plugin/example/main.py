from model import BasePlugin

class Plugin(BasePlugin):
    def run(self, param) -> str:
        print('Hello world from python!')
        return 'Hello world'

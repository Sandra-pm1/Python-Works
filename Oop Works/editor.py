class Editor:

    def __init__(self,name,vendor):
        self.name=name
        self.vendor=vendor

    def open(self):
        print(f"{self.name} Open")

    def execute(self):
        print(f"{self.name} execute")

class Vscode(Editor):

    def __init__(self,name,vendor):
        super().__init__(name,vendor)

class PyCharm(Editor):

    def __init__(self,name,vendor):
        super().__init__(name,vendor)


pycharm_instance=PyCharm("PyCharm","jetbrains")
pycharm_instance.open()
vscode_instance=Vscode("Visual basic code","vscvendor")
vscode_instance.open()
from main_page import *


class Application(QApplication):
    def __init__(self) -> None:
        super().__init__([])

        self.win = AnalyticsDashoard()
        # self.win = QColorDialog()
        self.win.show()

        self.setStyleSheet(STYLE_QSS)


app = Application()

app.exec()

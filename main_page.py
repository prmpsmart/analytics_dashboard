from side_panel import *
from body import Body


class AnalyticsDashoard(QFrame):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Analytics Dashboard")
        self.setFixedSize(CODING_WIDTH, CODING_HEIGHT)

        # setup widgets

        main_lay = QHBoxLayout(self)

        self.side_panel = SidePanel()
        main_lay.addWidget(self.side_panel)

        self.body = Body()
        main_lay.addWidget(self.body)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        return QApplication.instance().quit()

    def showEvent(self, event: QShowEvent) -> None:

        return super().showEvent(event)


if __name__ == "__main__":
    import os

    os.system("python main.py")

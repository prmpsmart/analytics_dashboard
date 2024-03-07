from commons import *


class HLine(QFrame):
    def __init__(self):
        super().__init__()

        self.setFrameShape(self.Shape.HLine)


class ScrollableFrame(QScrollArea):
    def __init__(
        self,
        hbar: bool = False,
        vbar: bool = True,
        is_vertical: bool = True,
    ):
        QScrollArea.__init__(self)

        self.frame: QFrame = QFrame()
        self.frame.setObjectName("frame")

        self.setWidget(self.frame)
        self.setWidgetResizable(True)

        if is_vertical:
            QVBoxLayout(self.frame)
        else:
            QHBoxLayout(self.frame)

        if hbar:
            self.show_hbar()
        else:
            self.hide_hbar()

        if vbar:
            self.show_vbar()
        else:
            self.hide_vbar()

    def frameLayout(self) -> QBoxLayout:
        return self.frame.layout()

    def hide_hbar(self):
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def hide_vbar(self):
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def hide_bars(self):
        self.hide_hbar()
        self.hide_vbar()

    def show_hbar(self):
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def show_vbar(self):
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

    def show_bars(self):
        self.show_hbar()
        self.show_vbar()

    def scroll_down(self, minimum, maximum):
        self.verticalScrollBar().setSliderPosition(maximum)

    def disable_hbar(self):
        self.horizontalScrollBar().setDisabled(True)

    def disable_vbar(self):
        self.verticalScrollBar().setDisabled(True)

    def enable_hbar(self):
        self.horizontalScrollBar().setEnabled(True)
        self.horizontalScrollBar()

    def enable_vbar(self):
        self.verticalScrollBar().setEnabled(True)

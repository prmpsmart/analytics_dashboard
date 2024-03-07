from commons import *

try:
    from buttons import DropdownButton
except:
    ...


class DropdownDialog(QDialog):
    submit = Signal(str)

    def __init__(self):
        super().__init__()

        lay = QVBoxLayout(self)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Popup)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)

        self.dropdown_button: DropdownButton = None

        self.widget = QWidget()
        self.widget_lay = QVBoxLayout(self.widget)
        self.widget.setObjectName("widget")
        lay.addWidget(self.widget)

        # effect = QGraphicsDropShadowEffect()
        # effect.setOffset(15)
        # # self.setGraphicsEffect(effect)


class TimeFrameDialog(DropdownDialog):

    def __init__(self, items: list[str]):
        super().__init__()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        return self.hide()

    def closeEvent(self, arg__1: QCloseEvent) -> None:
        if self.dropdown_button:
            self.dropdown_button.setChecked(False)
            # self.dropdown_button.toggledEvent(False)

    def hideEvent(self, event: QHideEvent) -> None:
        return self.closeEvent(event)

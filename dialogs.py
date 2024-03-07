from frames import *

try:
    from buttons import DropdownButton
except:
    ...


class DropdownDialog(QWidget):
    submit = Signal(str)

    def __init__(self):
        super().__init__()

        lay = QVBoxLayout(self)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)

        self.dropdown_button: DropdownButton = None

        self.widget = QWidget()
        self.widget_lay = QVBoxLayout(self.widget)
        self.widget.setObjectName("widget")
        lay.addWidget(self.widget)

        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(5)
        effect.setXOffset(15)
        effect.setYOffset(15)
        effect.setColor("black")
        self.widget.setGraphicsEffect(effect)
        self.setGraphicsEffect(effect)


class TimeFrameDialog(DropdownDialog):

    def __init__(self):
        super().__init__()

        top_lay = QHBoxLayout()
        top_lay.setContentsMargins(5, 0, 5, 0)

        self.widget_lay.addLayout(top_lay)

        label = QLabel("Timeframe:")
        label.setObjectName("label")
        top_lay.addWidget(label)

        self.text = QLabel()
        self.text.setObjectName("text")
        top_lay.addWidget(self.text)

        top_lay.addStretch()

        self._icon = QLabel()
        self._icon.setPixmap(QPixmap("./svgs/arrow_full_up.svg"))
        top_lay.addWidget(self._icon)

        self.widget_lay.addWidget(HLine())

        for text in ("Last 7 Days", "This Month", "This Year", "Custom"):
            button = QPushButton(text)
            self.widget_lay.addWidget(button)

    def on_selected(self):
        button: QPushButton = self.sender()
        text = button.text()

        self.text.setText(text)
        self.submit.emit(text)
        self.hide()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        return self.hide()

    def showEvent(self, event: QShowEvent) -> None:
        button_pos = self.dropdown_button.pos()
        from_parent = self.dropdown_button.mapToGlobal(button_pos)

        self.move(from_parent.x() - 20, from_parent.y() - 15)
        self.setFixedWidth(self.dropdown_button.width() + 22)

    def closeEvent(self, arg__1: QCloseEvent) -> None:
        if self.dropdown_button:
            self.dropdown_button.setChecked(False)
            # self.dropdown_button.toggledEvent(False)

    def hideEvent(self, event: QHideEvent) -> None:
        return self.closeEvent(event)


if __name__ == "__main__":
    import os

    os.system("python main.py")

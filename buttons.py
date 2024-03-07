from dialogs import *


class SidePanelButton(QPushButton):

    def __init__(self, svg: str, text: str, toggled: bool = False):
        super().__init__()

        hlay = QHBoxLayout(self)
        hlay.setContentsMargins(24, 0, 0, 0)
        hlay.setSpacing(10)

        self.svg = svg

        self._icon = QLabel()
        self._icon.setObjectName("icon")
        hlay.addWidget(self._icon)

        self.label = QLabel(text.title())
        hlay.addWidget(self.label)

        self.setAutoExclusive(True)
        self.setCheckable(True)

        self.setChecked(toggled)
        self.toggledEvent(toggled)

        self.toggled.connect(self.toggledEvent)

    def toggledEvent(self, toggled: bool):
        color = "#1B59F8" if toggled else "#4c4c4c"
        self._icon.setPixmap(QSvgPixmap(self.svg, color=color))
        self.label.setObjectName("selected" if toggled else "non_selected")

        self.window().setStyleSheet(STYLE_QSS)


class DropdownButton(QPushButton):
    def __init__(self, label: str, text: str, dialog: DropdownDialog = None):
        super().__init__()

        self.dialog = dialog
        if self.dialog:
            self.dialog.submit.connect(self.on_submit)

        lay = QHBoxLayout(self)
        lay.setContentsMargins(15, 0, 15, 0)

        self.label = QLabel(label)
        self.label.setObjectName("label")
        lay.addWidget(self.label)

        self._text = QLabel(text)
        self._text.setObjectName("text")
        lay.addWidget(self._text)

        lay.addStretch()

        self._icon = QLabel()
        self._icon.setObjectName("icon")
        lay.addWidget(self._icon)

        for w in (self.label, self._text, self._icon):
            w.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.setCheckable(True)
        self.setChecked(False)
        self.toggledEvent(False)

        self.toggled.connect(self.toggledEvent)

    def toggledEvent(self, toggled: bool):
        position = "up" if toggled else "down"
        self._icon.setPixmap(
            QSvgPixmap(
                f"./svgs/arrow_full_{position}.svg",
                color="black",
            )
        )

        if self.dialog:
            self.dialog.setVisible(toggled)

    def on_submit(self, text: str):
        self._text.setText(text)

    def showEvent(self, event: QShowEvent) -> None:
        if self.dialog:
            self.dialog.dropdown_button = self

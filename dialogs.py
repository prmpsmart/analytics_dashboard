from frames import *
from buttons import *


class DropdownDialog(QWidget):
    submit = Signal(str)

    def __init__(self):
        super().__init__()

        self._lay = QVBoxLayout(self)
        # lay.setContentsMargins(0, 0, 0, 0)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)

        self.dropdown_button: DropdownButton = None

        self.widget = QWidget()
        self.widget_lay = QVBoxLayout(self.widget)
        self.widget.setObjectName("widget")
        self._lay.addWidget(self.widget)

    def event(self, event):
        if event.type() == QEvent.Type.WindowDeactivate:
            self.hide()
        return super().event(event)

    def closeEvent(self, arg__1: QCloseEvent) -> None:
        if self.dropdown_button:
            self.dropdown_button.setChecked(False)

    def hideEvent(self, event: QHideEvent) -> None:
        return self.closeEvent(event)


class TimeFrameDialog(DropdownDialog):
    def __init__(self):
        super().__init__()

        top_lay = QHBoxLayout()
        top_lay.setContentsMargins(5, 0, 5, 0)

        self.widget_lay.addLayout(top_lay)

        label = QLabel("Timeframe:")
        label.setObjectName("label")
        top_lay.addWidget(label)

        self.text = QLabel("This Month")
        self.text.setObjectName("text")
        top_lay.addWidget(self.text)

        top_lay.addStretch()

        self._icon = QLabel()
        self._icon.setPixmap(QPixmap("./svgs/arrow_full_up.svg"))
        top_lay.addWidget(self._icon)

        self.widget_lay.addWidget(HLine())

        for index, text in enumerate(
            ("Last 7 Days", "This Month", "This Year", "Custom")
        ):
            button = QPushButton(text)
            button.setCheckable(True)
            button.setAutoExclusive(True)
            button.clicked.connect(self.on_selected)
            self.widget_lay.addWidget(button)

            if index == 2:
                button.setChecked(True)

    def on_selected(self):
        button: QPushButton = self.sender()
        text = button.text()

        self.text.setText(text)
        self.submit.emit(text)
        self.hide()

    def showEvent(self, event: QShowEvent) -> None:
        from_parent = self.dropdown_button.mapToGlobal(self.dropdown_button.pos())
        self.move(from_parent.x() - 20, from_parent.y() - 15)
        self.setFixedWidth(self.dropdown_button.width() + 22)


class PeopleFrameDialog(DropdownDialog):
    def __init__(self):
        super().__init__()

        top_lay = QHBoxLayout()
        top_lay.setContentsMargins(5, 0, 5, 0)

        self.widget_lay.addLayout(top_lay)

        label = QLabel("People:")
        label.setObjectName("label")
        top_lay.addWidget(label)

        self.text = QLabel("Multiple Selected")
        self.text.setObjectName("text")
        top_lay.addWidget(self.text)

        top_lay.addStretch()

        clear = QPushButton("Clear")
        clear.setObjectName("clear")
        clear.clicked.connect(self.on_clear)
        top_lay.addWidget(clear)

        self.widget_lay.addWidget(HLine())

        hlay = QHBoxLayout()
        self.widget_lay.addLayout(hlay)
        hlay.setSpacing(10)

        self.group_item = ItemButton("Managers")
        self.group_item.clicked.connect(self.deselect_group)
        hlay.addWidget(self.group_item)

        self.user_item = ItemButton("Adrian Lu")
        self.user_item.clicked.connect(self.deselect_user)
        hlay.addWidget(self.user_item)

        hlay.addStretch()

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search")
        icon = QIcon("./svgs/search.svg")
        self.search.addAction(icon, QLineEdit.ActionPosition.LeadingPosition)
        self.search.setClearButtonEnabled(True)
        self.widget_lay.addWidget(self.search)

        groups_box = QGroupBox("GROUPS")
        self.widget_lay.addWidget(groups_box)

        groups_box_lay = QVBoxLayout(groups_box)

        self.groups: dict[str, QPushButton] = {}
        for text in ("All Users", "Managers", "Trainers"):
            button = QRadioButton(text)
            self.groups[text] = button
            button.setAutoExclusive(False)
            button.toggled.connect(self.on_group_selected)
            groups_box_lay.addWidget(button)

        users_box = QGroupBox("USERS")
        self.widget_lay.addWidget(users_box)

        users_box_lay = QVBoxLayout(users_box)

        self.users: dict[str, QRadioButton] = {}
        for text in ("Adrian Lu", "Evelyn Hamilton"):
            button = QRadioButton(text)
            self.users[text] = button
            button.toggled.connect(self.on_user_selected)
            users_box_lay.addWidget(button)

    def on_clear(self):
        for button in [*self.groups.values(), *self.users.values()]:
            button.setChecked(False)

        self.group_item.hide()
        self.user_item.hide()
        self.text.setText("")

    def deselect_group(self):
        self.group_item.hide()
        self.groups[self.group_item.text()].setChecked(False)

        self.text.setText(self.user_item.text() if self.user_item.isVisible() else "")

    def deselect_user(self):
        self.user_item.hide()
        self.users[self.user_item.text()].setChecked(False)

        self.text.setText(self.group_item.text() if self.group_item.isVisible() else "")

    def on_group_selected(self):
        for button in [*self.groups.values()]:
            button.setAutoExclusive(False)

        button = self.sender()
        self.group_item.setText(button.text())
        self.group_item.show()

        self.text.setText(
            "Multiple Selected"
            if self.user_item.isVisible()
            else self.group_item.text()
        )

    def on_user_selected(self):
        for button in [*self.users.values()]:
            button.setAutoExclusive(False)

        button = self.sender()
        self.user_item.setText(button.text())
        self.user_item.show()

        self.text.setText(
            "Multiple Selected"
            if self.group_item.isVisible()
            else self.user_item.text()
        )

    def on_selected(self):
        button: QPushButton = self.sender()
        text = button.text()

        self.text.setText(text)
        self.submit.emit(text)
        self.hide()

    def showEvent(self, event: QShowEvent) -> None:
        button_pos = self.dropdown_button.pos()
        from_parent = self.dropdown_button.mapToGlobal(button_pos)

        self.move(
            from_parent.x() - 26 - self.dropdown_button.width(), from_parent.y() - 15
        )
        self.setFixedWidth(self.dropdown_button.width() + 22)


if __name__ == "__main__":
    import os

    os.system("python main.py")

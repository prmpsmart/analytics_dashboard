from commons import *


class Card(QFrame):
    def __init__(self):
        super().__init__()

        addShadow(self)

class SmallCard(Card):
    def __init__(
        self,
        title: str,
        value: str,
        default_value_style: bool = True,
        have_graph: bool = False,
    ):
        super().__init__()

        lay = QVBoxLayout(self)

        title = QLabel(title)
        title.setObjectName("title")
        lay.addWidget(title)

        lay.addSpacing(24)

        value = QLabel(value)
        value.setObjectName("value" if default_value_style else "")
        lay.addWidget(value)

        if have_graph:
            graph = QLabel()
            graph.setPixmap(QPixmap("./svgs/graph.svg"))
            lay.addWidget(graph)

        lay.addStretch()


class ActivityCard(Card): ...


if __name__ == "__main__":
    import os

    os.system("python main.py")

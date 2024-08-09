from enum import Enum

try:
    # if PySide6 if what you have installed
    from PySide6.QtCore import *
    from PySide6.QtGui import *
    from PySide6.QtWidgets import *
except:  # if PyQt6 is what you have installed
    from PyQt6.QtCore import *  # type: ignore
    from PyQt6.QtGui import *  # type: ignore
    from PyQt6.QtWidgets import *  # type: ignore

DESIGN_WIDTH = 1440
DESIGN_HEIGHT = 1162

CODING_WIDTH = 1540
CODING_HEIGHT = 900

STYLE_QSS = ""
STYLE_QSS = open("style.qss").read()


def scale_width(width: int):
    return CODING_WIDTH * width / DESIGN_WIDTH


def scale_height(height: int):
    return CODING_HEIGHT * height / DESIGN_HEIGHT


class SvgCompositions(Enum):
    Overlay = QPainter.CompositionMode_Overlay
    SourceIn = QPainter.CompositionMode_SourceIn
    SourceOut = QPainter.CompositionMode_SourceOut
    SourceAtop = QPainter.CompositionMode_SourceAtop


def QSvgPixmap(
    pixmap: QPixmap = None,
    color: QColor = Qt.black,
    composition: SvgCompositions = SvgCompositions.SourceIn,
) -> QPixmap:
    assert composition in SvgCompositions
    o = pixmap
    if not isinstance(pixmap, QPixmap):
        pixmap = QPixmap(pixmap)

    if pixmap.isNull():
        print(o)

    painter = QPainter(pixmap)
    painter.setCompositionMode(composition.value)
    painter.fillRect(pixmap.rect(), QColor(color))
    painter.end()
    return pixmap


def QSvgIcon(
    icon: str = "",
    size: QSize = None,
    color: QColor = Qt.black,
    composition: SvgCompositions = SvgCompositions.SourceIn,
) -> QIcon:
    if isinstance(icon, QIcon):
        icon = icon.pixmap(size)

    pixmap = QSvgPixmap(pixmap=icon, color=color, composition=composition)
    return QIcon(pixmap)


def addShadow(self):

    self.___effect = QGraphicsDropShadowEffect()
    # self.___effect.setBlurRadius(2)
    self.___effect.setOffset(4)
    self.___effect.setColor(QColor(0, 0, 0, 30))
    self.setGraphicsEffect(self.___effect)

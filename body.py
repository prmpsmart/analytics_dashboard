from buttons import *
from frames import *


class BodyContentFrame(ScrollableFrame):
    def __init__(self):
        super().__init__()

        main_lay = self.frameLayout()

        top_lay = QHBoxLayout()
        main_lay.addLayout(top_lay)

        time_frame_dialog = TimeFrameDialog([])
        time_frame_dropdown = DropdownButton(
            "Timeframe:",
            "All-time",
            dialog=time_frame_dialog,
        )
        time_frame_dialog.dropdown_button = time_frame_dropdown
        top_lay.addWidget(time_frame_dropdown)

        people_dropdown = DropdownButton("People:", "All")
        top_lay.addWidget(people_dropdown)

        topic_dropdown = DropdownButton("Topic:", "Al")
        top_lay.addWidget(topic_dropdown)

        main_lay.addStretch()


class Body(QFrame):
    def __init__(self):
        super().__init__()

        main_lay = QVBoxLayout(self)

        top_lay = QHBoxLayout()
        main_lay.addLayout(top_lay)

        reports = QLabel("Reports")
        reports.setObjectName("reports")
        top_lay.addWidget(reports)

        top_lay.addStretch()

        download_pixmap = QLabel()
        download_pixmap.setPixmap(
            QSvgPixmap(
                "./svgs/download.svg",
                color="#4c4c4c",
            )
        )
        download_pixmap.setObjectName("download_pixmap")
        top_lay.addWidget(download_pixmap)

        download = QLabel("Download")
        download.setObjectName("download")
        top_lay.addWidget(download)

        main_lay.addSpacing(37)

        top_hline = HLine()
        main_lay.addWidget(top_hline)

        main_lay.addSpacing(28)

        body_content_frame = BodyContentFrame()
        main_lay.addWidget(body_content_frame)

        main_lay.addStretch()


if __name__ == "__main__":
    import os

    os.system("python main.py")

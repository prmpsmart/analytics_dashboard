from dialogs import *
from cards import *


class BodyContentFrame(ScrollableFrame):
    def __init__(self):
        super().__init__()

        main_lay = self.frameLayout()
        main_lay.setSpacing(21)

        top_lay = QHBoxLayout()
        main_lay.addLayout(top_lay)

        time_frame_dropdown = DropdownButton(
            "Timeframe:",
            "This Month",
            dialog_class=TimeFrameDialog,
        )
        top_lay.addWidget(time_frame_dropdown)

        people_dropdown = DropdownButton(
            "People:",
            "All",
            dialog_class=PeopleFrameDialog,
        )
        top_lay.addWidget(people_dropdown)

        topic_dropdown = DropdownButton(
            "Topic:",
            "All",
        )
        top_lay.addWidget(topic_dropdown)

        content_lay = QGridLayout()
        content_lay.setSpacing(24)
        main_lay.addLayout(content_lay)

        small_cards_lay = QVBoxLayout()
        small_cards_lay.setSpacing(17)
        content_lay.addLayout(small_cards_lay, 0, 0)

        small_card_details = (
            dict(
                title="Active Users",
                # value="27/80",
                value="<a style='font-size: 26px; font-weight: bold;'>27</a><a style='font-size: 19px; font-weight: 700; color: rgba(0, 0, 0, .5);'>/80</a>",
                default_value_style=False,
            ),
            dict(
                title="Questions Answered",
                value="3,298",
            ),
            dict(
                title="Av. Session Length",
                value="2m 34s",
            ),
            dict(
                title="Starting Knowledge",
                value="64%",
                have_graph=True,
            ),
            dict(
                title="Current Knowledge",
                value="86%",
                have_graph=True,
            ),
            dict(
                title="Knowledge Gain",
                value="+34%",
                have_graph=True,
            ),
        )

        row, col = 0, 0
        for index, small_card_detail in enumerate(small_card_details):
            if index and not index % 3:
                row += 1
                col = 0

            if not col:
                _small_cards_lay = QHBoxLayout()
                small_cards_lay.addLayout(_small_cards_lay)

            small_card = SmallCard(**small_card_detail)
            _small_cards_lay.addWidget(small_card)

            col += 1

        activity_card = ActivityCard()
        content_lay.addWidget(activity_card, 0, 1)

        main_lay.addStretch()
        # self.setMinimumHeight(900)


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
        main_lay.addWidget(body_content_frame, 1)

        main_lay.addStretch()


if __name__ == "__main__":
    import os

    os.system("python main.py")

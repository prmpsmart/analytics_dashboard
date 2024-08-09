from buttons import *
from cards import *


class SidePanel(Card):
    def __init__(self):
        super().__init__()

        main_lay = QVBoxLayout(self)

        tesla_pixmap = QSvgPixmap(
            "./svgs/tesla.svg",
            color=QColor("#E51837"),
        )

        tesla_label = QLabel()
        tesla_label.setObjectName("tesla_label")
        tesla_label.setPixmap(tesla_pixmap)
        main_lay.addWidget(tesla_label)

        main_lay.addSpacing(43)

        reports_button = SidePanelButton(
            "./svgs/reports.svg",
            "reports",
            toggled=True,
        )
        main_lay.addWidget(reports_button)

        library_button = SidePanelButton(
            "./svgs/library.svg",
            "library",
        )
        main_lay.addWidget(library_button)

        people_button = SidePanelButton(
            "./svgs/people.svg",
            "people",
        )
        main_lay.addWidget(people_button)

        activities_button = SidePanelButton(
            "./svgs/activities.svg",
            "activities",
        )
        main_lay.addWidget(activities_button)

        main_lay.addSpacing(60)

        supported = QLabel("Supported")
        supported.setObjectName("supported")
        main_lay.addWidget(supported)

        main_lay.addSpacing(28)

        get_started_button = SidePanelButton(
            "./svgs/get_started.svg",
            "get started",
        )
        main_lay.addWidget(get_started_button)

        settings_button = SidePanelButton(
            "./svgs/settings.svg",
            "settings",
        )
        main_lay.addWidget(settings_button)

        main_lay.addStretch()


if __name__ == "__main__":
    import os

    os.system("python main.py")

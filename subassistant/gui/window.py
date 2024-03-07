import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTabWidget, QWidget, QVBoxLayout
from subassistant.gui.tab import CommentTab, RemoveCommentTab, AboutTab

class SubAssistantWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SubAssistant")
        self.setWindowIcon(QIcon("./resources/curly_braces_icon.png"))
        self.setFixedSize(550, 350)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.West)

        self.tab_widget.addTab(CommentTab(), QIcon("./resources/curly_braces.png"), "")
        self.tab_widget.addTab(RemoveCommentTab(), QIcon("./resources/no_curly_braces.png"), "")
        self.tab_widget.addTab(AboutTab(), QIcon("./resources/about.png"), "")


        self.tab_widget.setStyleSheet("QTabBar::tab { height: 60px; width: 100px;}")
        layout.addWidget(self.tab_widget)

        self.setLayout(layout)

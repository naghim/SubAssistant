from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QTabWidget, QWidget, QVBoxLayout
from subassistant.globals import RESOURCES_DIR
from subassistant.gui.tab import CommentTab, RemoveCommentTab, AboutTab
from subassistant.gui import util
import os

class SubAssistantWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SubAssistant")
        self.setWindowIcon(QIcon(os.path.join(RESOURCES_DIR, 'curly_braces_icon.png')))
        self.setFixedSize(550, 350)
        util.apply_background_color(self, QColor(240, 240, 240))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.West)

        self.tab_widget.addTab(CommentTab(), QIcon(os.path.join(RESOURCES_DIR, 'curly_braces.png')), "")
        self.tab_widget.addTab(RemoveCommentTab(), QIcon(os.path.join(RESOURCES_DIR, 'no_curly_braces.png')), "")
        self.tab_widget.addTab(AboutTab(), QIcon(os.path.join(RESOURCES_DIR, 'about.png')), "")

        self.tab_widget.setObjectName("TabWidget")
        self.tab_widget.setStyleSheet("QTabBar::tab { height: 60px; width: 100px; background-color: #f3f3f3; border: 1px solid #e8e8e8; padding-top: -22px; padding-bottom: 22px; } QTabBar::tab:selected { background-color: #f9f9f9; }")
        layout.addWidget(self.tab_widget)

        self.setLayout(layout)

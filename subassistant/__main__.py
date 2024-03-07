import sys
from PySide6.QtWidgets import QApplication
from subassistant.globals import RESOURCES_DIR
from subassistant.gui.window import SubAssistantWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open(f'{RESOURCES_DIR}/styles.css', "r") as f:
        app.setStyleSheet(f.read())

    window = SubAssistantWindow()
    window.show()
    sys.exit(app.exec())

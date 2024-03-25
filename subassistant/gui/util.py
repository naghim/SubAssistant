from PySide6.QtGui import QPalette

def apply_background_color(widget, color):
    palette = QPalette()
    palette.setColor(QPalette.Window, color)
    widget.setAutoFillBackground(True)
    widget.setPalette(palette)
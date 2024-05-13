from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QHBoxLayout, QLineEdit, QScrollArea, QMessageBox, QTableWidget, QHeaderView, QTableWidgetItem, QCheckBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from subassistant.logic.logic import RemoveComments, CommentDialogue
from subassistant.gui import util
from subassistant.logic.fonts import copy, font, subtitle, windows
import os

class BaseSubtitleUI(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.window_title = QLabel(self.TAB_TITLE)
        self.window_title.setObjectName("Label_txt_bold")
        self.layout.addWidget(self.window_title)

        self.input_file_label = QLabel("Select Input File:")
        self.input_file_label.setObjectName("Label_txt")
        self.layout.addWidget(self.input_file_label)

        self.input_file_line_edit = QLineEdit()
        self.input_file_line_edit.setReadOnly(True)
        self.input_file_line_edit.setObjectName("LineEdit")

        self.input_btn = QPushButton("Browse", clicked=self.get_file)
        self.input_btn.setObjectName("FileChooserButton")

        input_file_layout = QHBoxLayout()
        input_file_layout.addWidget(self.input_file_line_edit)
        input_file_layout.addWidget(self.input_btn)

        self.layout.addLayout(input_file_layout)

        self.output_label = QLabel("Output Folder:")
        self.output_label.setObjectName("Label_txt")
        self.layout.addWidget(self.output_label)

        self.output_file_line_edit = QLineEdit()
        self.output_file_line_edit.setObjectName("LineEdit")
        output_file_layout = QHBoxLayout()
        output_file_layout.addWidget(self.output_file_line_edit)

        self.output_btn = QPushButton("Browse", clicked=self.get_output_folder)
        self.output_btn.setObjectName("FileChooserButton")
        output_file_layout.addWidget(self.output_btn)

        self.layout.addLayout(output_file_layout)

        self.action_button = QPushButton(self.ACTION)
        self.action_button.setObjectName("Action_btn")
        self.action_button.clicked.connect(lambda: self.process_file(self.ACTION_CLASS))

        util.apply_background_color(self, QColor(249, 249, 249))
        self.layout.addWidget(self.action_button)
        self.setLayout(self.layout)

    def get_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select File", filter="Subtitles (*.ass)")
        if filename:
            self.input_file_line_edit.setText(filename)
            self.output_file_line_edit.setText(self.get_output_file(self.output_file_line_edit.text()))

    def get_output_folder(self):
        output_folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if output_folder:
            self.output_file_line_edit.setText(self.get_output_file(output_folder))

    def get_output_file(self, folder):
        input_file = self.input_file_line_edit.text()

        if input_file:
            input_filename, input_ext = os.path.splitext(os.path.basename(input_file))

            if not folder:
                folder = os.path.dirname(input_file)
            if folder.endswith(".ass"):
                folder = os.path.dirname(folder)
            output_filename = f'{input_filename}_modified{input_ext}'
            output_file = os.path.join(folder, output_filename)
        else:
            output_file = folder

        output_file = output_file.replace(os.sep, '/')
        return output_file

    def process_file(self, action_class):
        input_file = self.input_file_line_edit.text()
        output_folder = self.output_file_line_edit.text()

        if not input_file:
            QMessageBox.warning(self, "Warning", "Please select a file to process.")
            return

        if not output_folder:
            QMessageBox.warning(self, "Warning", "Please select an output folder.")
            return

        output_file = self.get_output_file(output_folder)

        try:
            action_class(input_file, output_file).process_file()
            QMessageBox.information(self, "Success", f'File processed successfully.\nOutput file: {output_file}')
        except Exception as e:
            QMessageBox.critical(self, "Error", f'An error occurred while processing the file.\nError: {e}')

class CommentTab(BaseSubtitleUI):
    ACTION = "Comment Dialogue"
    TAB_TITLE = "Comment Subtitle Text"
    ACTION_CLASS = CommentDialogue


class RemoveCommentTab(BaseSubtitleUI):
    ACTION = "Delete Comments"
    TAB_TITLE = "Delete Commented Dialogue"
    ACTION_CLASS = RemoveComments



class FontCheckerTab(QWidget):
    TAB_TITLE = "Font Checker"

    def __init__(self):
        super().__init__()
        self.subtitle_filename = None

        self.layout = QVBoxLayout()
        self.window_title = QLabel(self.TAB_TITLE)
        self.window_title.setObjectName("Label_txt_bold")
        self.layout.addWidget(self.window_title)

        self.subtitle_label = QLabel("Select subtitle:")
        self.subtitle_label.setObjectName("Label_txt")
        self.layout.addWidget(self.subtitle_label)

        self.subtitle_line_edit = QLineEdit()
        self.subtitle_line_edit.setReadOnly(True)
        self.subtitle_line_edit.setObjectName("LineEdit")

        self.input_btn = QPushButton("Browse", clicked=self.get_subtitle)
        self.input_btn.setObjectName("FileChooserButton")

        self.subtitle_layout = QHBoxLayout()
        self.subtitle_layout.addWidget(self.subtitle_line_edit)
        self.subtitle_layout.addWidget(self.input_btn)

        self.layout.addLayout(self.subtitle_layout)

        
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Font", "Installed", "Location"])
        self.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table_widget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table_widget.setObjectName("TableWidget")
        self.table_widget.setStyleSheet("QTableWidget#TableWidget {"
            "border: 1px solid #dcdcdc;"
            "border-radius: 5px;"
        "}")
        self.layout.addWidget(self.table_widget)

        self.button_widget = QWidget()
        self.button_widget.setContentsMargins(0, 0, 0, 0)

        self.button_layout = QHBoxLayout(self.button_widget)
        self.button_layout.setContentsMargins(0, 0, 0, 0)

        self.check_button = QPushButton("Check Fonts in System")
        self.check_button.setObjectName("Action_btn")
        self.check_button.clicked.connect(lambda: self.check_fonts())
        self.check_button.setEnabled(False)

        self.export_button = QPushButton("Export Fonts to Folder")
        self.export_button.setObjectName("Action_btn")
        self.export_button.clicked.connect(lambda: self.export_fonts())
        self.export_button.setDisabled(True)

        self.button_layout.addWidget(self.check_button)
        self.button_layout.addWidget(self.export_button)

        util.apply_background_color(self, QColor(249, 249, 249))
        self.layout.addWidget(self.button_widget)
        self.setLayout(self.layout)

    def get_subtitle(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select Subtitle", filter="Subtitles (*.ass)")

        if not filename:
            return
        
        self.subtitle_line_edit.setText(os.path.basename(filename))
        self.subtitle_filename = filename
        self.check_button.setEnabled(True)

    def add_fonts(self, fonts, installed):
        for font, font_filename in fonts:
            self.table_widget.insertRow(self.table_widget.rowCount())
            row = self.table_widget.rowCount() - 1

            font_item = QTableWidgetItem(font)

            cell_widget = QWidget()
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.Checked if installed else Qt.Unchecked)
            checkbox.setEnabled(False)
            checkbox_layout = QHBoxLayout(cell_widget)
            checkbox_layout.addWidget(checkbox)
            checkbox_layout.setAlignment(Qt.AlignCenter)
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            cell_widget.setLayout(checkbox_layout)
            
            filename_item = QTableWidgetItem(font_filename)
            filename_item.setToolTip(font_filename)

            self.table_widget.setItem(row, 0, font_item)
            self.table_widget.setCellWidget(row, 1, cell_widget)
            self.table_widget.setItem(row, 2, filename_item)
            self.table_widget.setWordWrap(False)

    def check_fonts(self):
        if not self.subtitle_filename:
            return

        self.check_button.setEnabled(False)

        # First, find all installed fonts...
        installed_font_ttfs = windows.find_installed_ttfs()

        # Second, find the font names of all installed fonts...
        installed_fonts = {}
        font.parse_font_names(installed_font_ttfs, installed_fonts)

        # Third, find the fonts in the subtitle...
        subtitle_fonts = subtitle.find_fonts_in_subtitle(self.subtitle_filename)

        # Fourth, check which fonts are installed...
        subtitle_fonts = [(font, installed_fonts.get(font, 'N/A')) for font in subtitle_fonts]
        self.all_installed_fonts = [font for font in subtitle_fonts if font[0] in installed_fonts]
        all_unavailable_fonts = [font for font in subtitle_fonts if font[0] not in installed_fonts]

        # Fifth, update the table...
        self.table_widget.setRowCount(0)

        self.add_fonts(all_unavailable_fonts, False)
        self.add_fonts(self.all_installed_fonts, True)

        # Sixth, enable the export button if there are fonts to export...
        self.export_button.setEnabled(not all_unavailable_fonts)
        self.check_button.setEnabled(True)

    def export_fonts(self):
        output_folder = QFileDialog.getExistingDirectory(self, "Select Folder to save fonts in")

        if not output_folder:
            return

        try:
            copy.copy_fonts(output_folder, self.all_installed_fonts)
            QMessageBox.information(self, "Success", "Fonts exported successfully.")
        except:
            QMessageBox.critical(self, "Error", "An error occurred while exporting fonts.")

class AboutTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.content_widget)
        util.apply_background_color(self.content_widget, QColor(249, 249, 249))
        self.layout.addWidget(scroll_area)


        self.text_logo = QLabel("<html><head/><body><h3 align='center'>Sub<span style=\"color: #d9073f\">Assistant</span></h3></body></html>"
        )

        self.text = QLabel("<html><head/><body><p align='justify'><b> 👀 What is this?</b> SubAssistant is a specialized desktop application designed to simplify the translation process for subtitle files, specifically for the .ass (Advanced SubStation Alpha) format. Tailored for translators, SubAssistant facilitates seamless collaboration by allowing users to comment out the original dialogue text, write their translations alongside it, and enable proofreaders or quality checkers to review both versions within the same file. Users also have the possibilitiy to delete the commented out texts, by doing so the application enhances the efficiency and accuracy of subtitle translation workflows.<br/> SubAssistant also aids in recognizing  fonts from an .ass subtitle file that are not installed on your machine, also giving the opportunity to export all fonts used in a subtitle.</p></body></html>"
        )

        self.text_how_to = QLabel("<html><head/><body><p align='justify'><b> 👀 How to use?</b> Choose the action you wish to take from the side menu—whether to comment out text or delete comments. Use the \"Select File\" button to open the .ass file. The program will automatically propose an output filename within the same folder. If you prefer a different folder or wish to rename the output, utilize the \"Browse\" button or directly edit the output path. Upon clicking the button, the selected operation will be executed.<br/> To pinpoint missing fonts, begin by selecting the subtitle, then click the \"Check Fonts in System\" button. The application will display a list of fonts from the subtitle, indicating installed fonts along with their locations on your machine.  If all fonts are installed, you can also export them into a folder by clicking the \"Export Fonts to Folder\" button.</p></body></html>"
        )

        self.text_slogan = QLabel("<html><head/><body><p align='center'>Made with 50% 💕 and 50% ☕ <br/> by <a style=\"color: #d9073f\" href=\"https://github.com/naghim\">naghim @ GitHub</a></p></body></html>"
        )

        self.text_slogan.setOpenExternalLinks(True)
        self.text.setWordWrap(True)
        self.text_how_to.setWordWrap(True)
        self.text.setObjectName("About_txt")
        self.text_how_to.setObjectName("About_txt")
        self.text_slogan.setObjectName("Label_txt_bold_mini")
        self.text_logo.setObjectName("Label_txt_bold")
        self.content_widget.setStyleSheet("background-color: #f0f0f0")
        self.content_layout.addWidget(self.text_logo)
        self.content_layout.addWidget(self.text_how_to)
        self.content_layout.addWidget(self.text)
        self.content_layout.addWidget(self.text_slogan)
        self.content_widget.setLayout(self.content_layout)

        util.apply_background_color(self, QColor(249, 249, 249))
        self.setLayout(self.layout)

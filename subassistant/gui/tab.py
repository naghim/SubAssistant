from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QHBoxLayout, QLineEdit, QScrollArea, QMessageBox
from subassistant.logic.logic import RemoveComments, CommentDialogue
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
        
        self.layout.addWidget(scroll_area)


        self.text_logo = QLabel("<html><head/><body><p align='center'>Sub<span style=\"color: #d9073f\">Assistant</span></p></body></html>"
        )

        self.text = QLabel("<html><head/><body><p align='justify'><b> 👀 What is this?</b> This is a specialized desktop application designed to simplify the translation process for subtitle files, specifically .ass (Advanced SubStation Alpha) format. Tailored for translators, CommentOut facilitates seamless collaboration by allowing users to comment out the original English dialogue text, write their translations alongside it, and enable proofreaders or quality checkers to review both versions within the same file. By providing a unified platform for bilingual text management, this application enhances the efficiency and accuracy of subtitle translation workflows.</p></body></html>"
        )

        self.text_how_to = QLabel("<html><head/><body><p align='justify'><b> 👀 How to use?</b> Choose the action you wish to take from the side menu—whether to comment out text or delete comments. Use the \"Select File\" button to open the .ass file. The program will automatically propose an output filename within the same folder. If you prefer a different folder or wish to rename the output, utilize the \"Browse\" button or directly edit the output path. Upon clicking the button, the selected operation will be executed.</p></body></html>"
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
        self.content_layout.addWidget(self.text_logo)
        self.content_layout.addWidget(self.text_how_to)
        self.content_layout.addWidget(self.text)
        self.content_layout.addWidget(self.text_slogan)
        self.content_widget.setLayout(self.content_layout)
        
        self.setLayout(self.layout)

<p align="center">
  <img width="500" src="https://i.imgur.com/ocW7Hse.png"" alt="SubAssistant screenshot"/>
</p>

<p align='justify'>This is a specialized desktop application designed to simplify the translation process for subtitle files, specifically for the <code>.ass</code> (Advanced SubStation Alpha) format. Tailored for translators, SubAssistant facilitates seamless collaboration by allowing users to comment out the original dialogue text, write their translations alongside it, and enable proofreaders or quality checkers to review both versions within the same file. Users also have the possibilitiy to delete the commented out texts, by doing so the application enhances the efficiency and accuracy of subtitle translation workflows. SubAssistant also aids in recognizing  fonts from an <code>.ass</code> subtitle file that are not installed on your machine, also giving the opportunity to export all fonts used in a subtitle.</p>

<p align="center">
  <img width="500" src="https://i.imgur.com/Kpbfsmj.png"" alt="SubAssistant screenshot"/>
</p>

## Installation

### Windows

1. Download the latest release from the [Releases](https://github.com/naghim/SubAssistant/releases) page.
2. Double-click the downloaded `.exe` file to launch the application.

### Linux and macOS

Currently, there is no standalone executable for Linux and macOS. You can still run SubAssistant using Python as described below.

### Using Python

#### Pre-requisites

- Ensure you have Python 3.12 installed on your system.
- Make sure `pip` is installed. You can check by running `pip --version` in your terminal.

#### Installation Steps

1. Clone this repository to your local machine:

```bash
git clone https://github.com/naghim/SubAssistant.git
```

2. Navigate to the project directory:

```bash
cd SubAssistant
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python -m subassistant
```

## FAQ

<p align='justify'><b> 👀 How to use SubAssistant?</b> </br>  Using SubAssistant is a piece of cake! Choose the action you wish to take from the side menu—whether to comment out text or delete comments. Use the "Select File" button to open the .ass file. The program will automatically propose an output filename within the same folder. If you prefer a different folder or wish to rename the output, utilize the "Browse" button or directly edit the output path. Upon clicking the button, the selected operation will be executed. To pinpoint missing fonts, begin by selecting the subtitle, then click the "Check Fonts in System" button. The application will display a list of fonts from the subtitle, indicating installed fonts along with their locations on your machine.  If all fonts are installed, you can also export them into a folder by clicking the "Export Fonts to Folder" button.</p>

<p align='justify'><b> 👀 Can SubAssistant mess up my subtitles?</b> </br> No, SubAssistant will always generate a new file with the modifications, does not do any editing in the input file, so your subtitles are safe!</p>

<p align='justify'><b> 👀 Can SubAssistant handle <code>.srt</code> files?</b></br> No, currently SubAssistant does not support <code>.srt</code> files. </p>

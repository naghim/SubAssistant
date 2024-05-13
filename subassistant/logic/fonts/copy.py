import shutil
import os

def copy_fonts(font_folder, subtitle_fonts):
    # Create the folder if it does not exist
    if not os.path.exists(font_folder):
        os.makedirs(font_folder)

    # Make sure not to copy fonts twice
    fonts_copied = set()

    for font, installed_ttf in subtitle_fonts:
        if installed_ttf in fonts_copied:
            # This font was already copied
            continue

        extension = os.path.splitext(installed_ttf)[-1]
        font_file = os.path.join(font_folder, f'{font}{extension}')

        if os.path.exists(font_file):
            # This font already exists in the folder
            continue

        # Copy the font into the folder
        shutil.copyfile(installed_ttf, font_file)
        fonts_copied.add(installed_ttf)
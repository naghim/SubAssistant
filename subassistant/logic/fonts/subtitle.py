import ass
import re

def find_fonts_in_subtitle(subtitle_filename):
    # Now let's parse the subtitles
    with open(subtitle_filename, 'r', encoding='utf-8-sig') as f:
        doc = ass.parse(f)

    # These are the fonts that are used in the subtitle
    fonts = set()

    # First, the fonts used in all styles...
    for style in doc.styles:
        font_name = style.fontname
        fonts.add(font_name)

    # Second, the fonts that are manually specified in each dialogue
    # Format: \fnFontName\
    pattern = re.compile(r'\\fn([^\\}]+)(\\|})')

    for event in doc.events:
        fonts_found = pattern.findall(event.text)

        # Add all fonts that are found
        for font in fonts_found:
            # The first match is the font name itself
            # The second match is the delimiter
            fonts.add(font[0])

    # Sort the fonts
    fonts = list(fonts)
    fonts = sorted(fonts)
    return fonts
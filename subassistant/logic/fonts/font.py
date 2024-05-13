from fontTools import ttLib
from fontTools.ttLib import TTLibError

def parse_font_name(ttf, installed_fonts):
    # Some fonts are collections
    # For these fonts, we have to query each font separately
    fontNumber = 0

    while True:
        try:
            font = ttLib.TTFont(ttf, fontNumber=fontNumber)
        except TTLibError as e:
            # Maybe this isn't a TrueType font?
            if 'Not a TrueType' in str(e):
                print(ttf, 'is not a TrueType font')
                break

        # Let's check all names.
        for name in font['name'].names:
            # https://learn.microsoft.com/en-us/typography/opentype/spec/name#name-ids
            # Only check names that are font names
            if name.nameID in [1, 4]:
                # For some reason, names are in UTF-16-BE
                try:
                    name = name.string.decode('utf-16-be')
                except:
                    name = name.string.decode('utf-8')

                installed_fonts[name] = ttf
    
        if font.sfntVersion != b'ttcf':
            # Not a collection, so let's not check the rest of the fonts
            break

        # Check the next font if this is a collection
        fontNumber += 1

def parse_font_names(ttfs, installed_fonts):
    # Read all font files and see which are installed
    for ttf in ttfs:
        parse_font_name(ttf, installed_fonts)
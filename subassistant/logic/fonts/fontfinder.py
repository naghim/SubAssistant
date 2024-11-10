import os

def find_installed_ttfs():
    installed_font_ttfs = []

    if os.name == 'nt':  # Windows
        # Find all installed font TTFs
        # There are two places to check:
        # - System fonts (Windows)
        # - User installed fonts (AppData)

        import winreg
        for registry_hive in [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]:
            reg = winreg.ConnectRegistry(None, registry_hive)
            key = winreg.OpenKey(reg, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts', 0, winreg.KEY_READ)

            for i in range(0, winreg.QueryInfoKey(key)[1]):
                ttf = winreg.EnumValue(key, i)[1]

                if '\\' not in ttf:
                    ttf = os.path.join(os.environ['WINDIR'], 'Fonts', ttf)

                installed_font_ttfs.append(ttf)
    elif os.name == 'posix':  # Linux
        # Common directories where fonts are installed on Linux
        font_dirs = [
            '/usr/share/fonts',
            '/usr/local/share/fonts',
            os.path.expanduser('~/.fonts'),
            os.path.expanduser('~/.local/share/fonts')
        ]

        for font_dir in font_dirs:
            for root, _, files in os.walk(font_dir):
                for file in files:
                    if file.lower().endswith('.ttf'):
                        installed_font_ttfs.append(os.path.join(root, file))

    return installed_font_ttfs
import os
import winreg

def find_installed_ttfs():
    installed_font_ttfs = []

    # Find all installed font TTFs
    # There are two places to check:
    # - System fonts (Windows)
    # - User installed fonts (AppData)
    for registry_hive in [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]:
        reg = winreg.ConnectRegistry(None, registry_hive)
        key = winreg.OpenKey(reg, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts', 0, winreg.KEY_READ)

        for i in range(0, winreg.QueryInfoKey(key)[1]):
            ttf = winreg.EnumValue(key, i)[1]

            if '\\' not in ttf:
                ttf = os.path.join(os.environ['WINDIR'], 'Fonts', ttf)

            installed_font_ttfs.append(ttf)
    
    return installed_font_ttfs
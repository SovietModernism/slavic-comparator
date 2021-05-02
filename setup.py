from cx_Freeze import setup, Executable
import sys

# скрываем окно консоли при выполнении программы
base = None
if (sys.platform == "win32"):
    base = "Win32GUI"
    
elif (sys.platform == "win64"):
    base = "Win64GUI"


executables = [Executable("SlavicComparatorGUI.py", base=base)]

# лишние модули
excludes = ['xml', 'lib2to3', 'asyncio', 'html', 'logging', 'unittest',
            'test', 'pydoc_data', 'bz2', 'lzma',
            'distutils', ]


# настройки
options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
    }
}


# основная информация
setup(
    name="Slavic Comparator",
    description='description',
    version='1.0',
    executables = executables,
    options = options
)
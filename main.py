from functions import user_interface


def main():
    user_interface()


if __name__ == '__main__':
    main()

"""
HOW TO generate .exe with nuitka? Use command:
python -m nuitka --onefile --include-data-dir=imgs=imgs --windows-icon-from-ico=imgs\_icon.ico main.py
"""
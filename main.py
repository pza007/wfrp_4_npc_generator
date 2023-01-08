from functions import user_interface


def main():
    user_interface()


if __name__ == '__main__':
    main()

# TODO
# - continue advancing after reaching career lvl 4?
# - age=6, career lvl 4? possible??

# To generate .exe using nuitka, use command:
#   python -m nuitka --onefile --include-data-dir=imgs=imgs --windows-icon-from-ico=imgs\_icon.ico main.py
from pathlib import Path
from clean_folder.main import main


def start():
    folder_for_scan = input('Enter a scan folder: ')
    try:
        if folder_for_scan:
            folder_for_scan = Path(folder_for_scan)
            print(f'Start in folder {folder_for_scan.resolve()}')
            main(folder_for_scan.resolve())
    except:
        print('Directory name not found or not entered')

# -*- coding: utf-8 -*-
"""
Created on Sun May  1 16:48:09 2022

@author: admin
"""
from pathlib import Path
import shutil
import sys
import clean_folder.collections_file as collection
from clean_folder.normalize import normalize


def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path):
    # Создаем папку для архивов
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / \
                      normalize(filename.name.replace(filename.suffix, ''))

    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Обман - это не архив {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Не удалось удалить папку {folder}')


def main(folder: Path):
    collection.scan(folder)

    for file in collection.IMAGES:
        handle_media(file, folder / 'images')
    for file in collection.AUDIOS:
        handle_media(file, folder / 'audio')
    for file in collection.DOCUMENTS:
        handle_media(file, folder / 'documets')
    for file in collection.VIDEOS:
        handle_media(file, folder / 'video')
    for file in collection.UNKNOWS:
        handle_media(file, folder / 'unknows')

    for file in collection.ARCHIVES:
        handle_archive(file, folder / 'archives')

    for folder in collection.FOLDERS[::-1]:
        handle_folder(folder)


if __name__ == '__main__':
    folder_for_scan = input('Enter a scan folder: ')
    if folder_for_scan:
        folder_for_scan = Path(folder_for_scan)
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())

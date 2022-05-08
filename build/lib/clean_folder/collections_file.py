# -*- coding: utf-8 -*-
"""
Created on Sun May  1 15:16:43 2022

@author: admin
"""
import sys
from pathlib import Path

IMAGES = []
AUDIOS = []
VIDEOS = []
DOCUMENTS = []
ARCHIVES = []
UNKNOWS = []

REGISTER_EXTENSIONS = {
    'JPEG': IMAGES,
    'PNG': IMAGES,
    'JPG': IMAGES,
    'SVG': IMAGES,
    
    'MP3': AUDIOS,
    'OGG': AUDIOS,
    'WAV': AUDIOS,
    'AMR': AUDIOS,
    
    'DOC': DOCUMENTS,
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'PDF': DOCUMENTS,    
    'XLSX': DOCUMENTS,
    'PPTX': DOCUMENTS,  
    
    'AVI': VIDEOS,
    'MP4': VIDEOS,
    'MOV': VIDEOS,
    'MKV': VIDEOS,

    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ['archives', 'video', 'audio', 'documents', 'images', 'unknowns']:
                FOLDERS.append(item)
                scan(item)
                
        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:  
            UNKNOWS.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                UNKNOWS.append(fullname)
                
                

if __name__ == '__main__':
    #folder_for_scan = sys.argv[1]
    folder_for_scan = input('Enter a scan folder: ')
    print(f'Start in folder {folder_for_scan}')
    scan(Path(folder_for_scan))
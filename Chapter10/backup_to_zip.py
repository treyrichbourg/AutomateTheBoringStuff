#! /usr/bin/env python3
# backup_to_zip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backup_to_zip(folder):
    #Back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)   #make sure folder is absolute

    #Figure out the filename this code should use based on
    #what files already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    #Create the ZIP file.
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    #TODO: Walk the entire folder tree and compress the files in each folder.
    print('Done.')

backup_to_zip()


#! python3
# backupToZip.py - copies entire folder and its content
# into a ZIP file whose filename increments (ver)

import os
import zipfile

def backupToZip(folder):
    # backs up entire contenr of folder into a ZIP file.
    # get absolute path of an input folder
    # folder = os.path.abspath(folder)
    print(folder)
    ver = 1
    # loop increments archive names until gets a non-taken one
    while 1:
        zipFilename = os.path.basename(folder) + '_' + str(ver) + '.zip'
        if not os.path.exists(zipFilename):
            break
        ver += 1
    
    # creating ZIP archive
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    # walking the folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files to {foldername}...')
        # save main folder in archive
        backupZip.write(foldername)
        # add all files in main folder to archive
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            # don't archive previous archives
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    # close archive
    backupZip.close()
    print('Done.')


# run the function
backupToZip('C:\\skryptyPython')

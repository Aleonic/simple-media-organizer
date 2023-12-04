import os
from pathlib import Path

def prepareNewFileName(file): # Will rename a file until there is no overlapping file

    complete = False
    counter = 1
    fileParts = os.path.splitext(file)
    newFilePath = ""
    while not complete:
        fileName = fileParts[0] + "_" + f'{counter}'
        newFilePath = fileName + fileParts[1]

        if(os.path.exists(newFilePath)):
            counter += 1
        else:
            complete = True
    
    return newFilePath


def fileTransfer(filePath, fileNames, newFolderName):
    
    # Create a folder to move files to if the folder does not already exist
    folderPath = filePath / newFolderName
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

    # Move files to new destination (Avoiding overwriting any existing files)
    for fileToMove in fileNames:
        previousPath = filePath / fileToMove
        newPath = folderPath / fileToMove

        if(os.path.exists(newPath)):
                newPath = prepareNewFileName(newPath)
        
        previousPath.rename(newPath)



if __name__ == "__main__":

    fpath = input("Enter file path of the directory to be sorted: ")
    fpath = Path(fpath)

    dir_list = os.listdir(fpath)

    # Collects the file names based on the type of file extension
    images = []
    videos = []
    gifs = []
    for file in dir_list:
        extension = os.path.splitext(file)[1]
        if (extension in ('.png','.jpg','.jpeg', '.webp')):
            images.append(file)
        elif(extension in ('.gif',)):
            gifs.append(file)
        elif(extension in ('.mp4','.mov', '.webm')):
            videos.append(file)
    
    fileTransfer(fpath, images, "Images")
    fileTransfer(fpath, videos, "Videos")
    fileTransfer(fpath, gifs, "Gifs")
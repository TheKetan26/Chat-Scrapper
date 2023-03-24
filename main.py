from os.path import isfile, isdir

from fileManager import FileFolder


status = isfile('data.json')

if __name__ == '__main__':
    if status:
        print('File exists!')
        pass

    else:
        print("Json file not found!\nEnter following details to create new.")
        user = input("Enter complete username: ").lower()
        while not isdir(user):
            print('Folder not found!')
            user = input("Enter complete username: ").lower()
        target = input("Enter complete target username: ").lower()
        while not isdir(f'{user}\messages\inbox\{target}'):
            print('Folder not found!')
            target = input("Enter complete username: ").lower()
        file = FileFolder(user, target)
        try:
            file.create_json()
        except:
            print('An unknown error occured!')
        else:
            print("File created! Start the app again to continue.")
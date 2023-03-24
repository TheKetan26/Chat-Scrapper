from os.path import isfile, isdir

from fileManager import FileFolder, File


status = isfile('data.json')

if __name__ == '__main__':
    file = File()

    if status:
        names = file.names()
        print(f"You are in chat of {names[0]} and {names[1]}")

        while 1:
            print("1. Word list and count")
            print("2. Number of the word")
            print("0. Exit")
            ch = int(input("Select an option: "))

            match ch:
                case 1:
                    print('1.', names[0])
                    print('2.', names[1])
                    name = int(input("Select an option: "))
                    file.list(names[name-1])

                case 2:
                    word = input("Enter word: ")
                    file.count(word)

                case 4:
                    break

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
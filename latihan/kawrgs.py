def printData(**kwargs):
    for key, value in kwargs.items():
        print(key + " - " + value)

printData(name = 'Rony', age = '21', hobby = 'Coding')
from read import readUserAge


def main():
    userAge = readUserAge()
    if userAge < 16:
        print("He is a child")
    elif userAge < 18:
        print("Trâm là con chó")
    else:
        print("He is a man")
    message = "man" if userAge > 16 else "child"
    print("He is a" + message)


if __name__ == '__main__':
    main()

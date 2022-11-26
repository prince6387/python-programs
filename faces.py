def main():
    x = input()

    result = convert(x)

    print(result)


def convert(x):

    y = x.replace(":)","🙂").replace(":(","🙁")

    return y

main()

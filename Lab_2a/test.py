def main():
    print(f'To be {True},', end=' ')
    print(f'or not to be {False},', end=' ')
    print(f'{None} - that is the question. Wait... What?')

    data = ['1 {0}', 2, '3 {0}', 4, '5 {0}', 6, '7 {0}']
    print(
        list(
            filter(lambda val: isinstance(val, int), data)
        )
    )

    """
                        ＜(⬤‿⬤)＞
        "This mess because I can, I did" - Master Yoda.
    """

    print(
        tuple(
            string.format("is a string") for string in data if isinstance(string, str)
        )
    )

    print('I Like ', float('\t3.14\n'), 'zza', sep='')

    try:
        x = [[x for x in range(5)] for x in range(3)]
        for i in range(5):
            for j in range(4):
                x[i][j] = "x"
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        with open("parrot-abstract.jpg", 'rb') as file:
            data = file.read()
            with open("parrot-abstract-copy.jpg", "wb") as copy:
                copy.write(data)


if __name__ == "__main__":
    main()

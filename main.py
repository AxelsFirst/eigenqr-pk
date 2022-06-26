# from eigenqr.matrix import Matrix


if __name__ == "__main__":

    while True:
        lang = input('Choose language / Wybierz język [EN/pl]: ').lower()
        if lang == 'en' or lang == '':
            import cli.en as en
        elif lang == 'pl':
            import cli.pl as pl
        else:
            print('Wrong input! Try again:')

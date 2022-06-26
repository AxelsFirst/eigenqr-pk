if __name__ == "__main__":

    print('\nPre-launch settings / Ustawienia uruchomienia aplikacji')
    print('\nChoose language / Wybierz język')
    print('\nTo choose english, type "en".')
    print('Aby wybrać język polski, napisz "pl".')

    while True:
        lang = input('Type here / Wpisz tutaj [EN/pl]: ').lower()
        if lang == 'en' or lang == '':
            import cli.en as app
            break

        elif lang == 'pl':
            import cli.pl as app
            break

        else:
            print('\nWrong input! Try again.')

    cli = app.Cli_app()

    cli.intro()

    cli.help()

    n = 3

    while True:
        user_command = cli.user_input()

        if user_command == 'matrix':
            cli.input_matrix()

        elif user_command == 'deco':
            cli.qr_decomposition(n)

        elif user_command == 'algo':
            cli.qr_algorithm(n)

        elif user_command == 'prec':
            n = cli.precision()

        elif user_command == 'intro':
            cli.intro()

        elif user_command == 'help':
            cli.help()

        elif user_command == 'end':
            break

        else:
            cli.wrong_input()

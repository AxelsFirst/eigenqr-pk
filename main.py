if __name__ == "__main__":

    while True:
        lang = input('Choose language / Wybierz język [EN/pl]: ').lower()
        if lang == 'en' or lang == '':
            import cli.en as app
            break

        elif lang == 'pl':
            import cli.pl as app
            break

        else:
            print('Wrong input! Try again:')

    cli = app.Cli_app()

    cli.intro()

    cli.help()

    while True:
        user_command = cli.user_input()

        if user_command == 'matrix':
            cli.input_matrix()

        elif user_command == 'qr_decomposition':
            cli.qr_decomposition()

        elif user_command == 'qr_algorithm':
            cli.qr_algorithm()

        elif user_command == 'intro':
            cli.intro()

        elif user_command == 'help':
            cli.help()

        elif user_command == 'break':
            break

        else:
            cli.wrong_input()

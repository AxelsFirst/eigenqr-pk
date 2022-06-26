from eigenqr.matrix import Matrix


class Cli_app():
    """

    Class for a CLI app.

    """

    def __init__(self):
        """

        Atributes will be set by methods.

        """

        self.matrix = None

        self.Q = None
        self.R = None

        self.eigenvalues = None
        self.old_n_max = None
        self.old_eps = None

    def intro(self):
        """

        Function will display basic informations about our project.

        """

        print('\nEigenQR-PK')

        print('\nPrzedstawiony przez:')
        print('Julia Bugaj, Dawid Kapcia, Alex Gibała, Szymon Forysiuk')

        print("Celem naszego projektu jest zaimplementowanie algorytmu QR do obliczania" + "wartości własnych macierzy.")

    def help(self):
        """

        Function will display list of possible commands.

        """

        print('\n   Lista możliwych komend:')

        print('\nmatrix: wprowadź macierz')
        print('deco: QR rozkład')
        print('algo: QR algorytm')
        print('intro: informacja')
        print('help: lista komend')
        print('end: zamkniecie aplikacji')


        print('\nNa przykład, aby użyć polecenia "matrix", wpisz "matrix".')

    def wrong_input(self):
        """

        Note that user inputed wrong command.

        """

        print('\nNieprawidłowa komenda!')
        print('Aby sprawdzić, jakie polecenia są możliwe, wpisz polecenie "help".')

    def user_input(self):
        """

        Take user's input as a command.

        """

        user_command = input('\nWpisz tutaj: ')

        return user_command

    def input_matrix(self):
        """

        Input a matrix to the app.

        """

        self.Matrix = None
        self.qr_deco = None
        self.qr_algo = None

        while True:
            print('\nJaki będzie wymiar macierzy?')
            print('Pamiętaj, że zalecamy używanie macierzy o '
                  + ' wymiarze większym niż 4.')
            try:
                dimension = int(input('Wpisz tutaj: '))

                if dimension > 4:
                    break

                else:
                    print('\nWprowadź dodatnią liczbę całkowitą większą od 4!')

            except ValueError:
                print('\nWprowadź liczbę całkowitą!')

        print('\nJakie będą wartości macierzy?')
        print('Pamiętaj o dzieleniu liczb za pomocą spacji.')
        print('Napisz wartości złożone, na przykład 2+3j.')

        matrix = []

        for row_i in range(dimension):
            while True:
                print('\nWprowadź wartości dla ' + str(row_i+1) + '-tego wiersza.')
                row = input('Wpisz tutaj: ').split(' ')

                if row[-1] == '':
                    row.pop(-1)

                if len(row) < dimension:
                    print('\nZa mało wprowadzonych zmiennych!')

                elif len(row) > dimension:
                    print('\nZa dużo wprowadzonych zmiennych!')

                else:
                    try:
                        for col_i in range(dimension):
                            row[col_i] = complex(row[col_i])

                        matrix.append(row)
                        break

                    except ValueError:
                        print('\nWprowadź liczby złożone!')

        self.matrix = Matrix(matrix)

        print('\Macierz została zapisywana.')

    def qr_decomposition(self):
        """

        Calculates QR decomposition of a previously inputed matrix.

        """

        if self.matrix is None:
            print('\nMusisz wprowadzić macierz!')
            print('Aby wprowadzić macierz, należy użyć polecenia "matrix".')

        else:
            if self.Q is not None and self.R is not None:
                print('\nMacierz ortogonalna Q:')
                print(self.Q.matrix)

                print('\nMacierz górno trójkątna R:')
                print(self.R.matrix)

            else:
                Q, R = self.matrix.qr_decomposition()

                self.Q = Q
                self.R = R

                print('\nMacierz ortogonalna Q:')
                print(Q.matrix)

                print('\nMacierz górno trójkątna R:')
                print(R.matrix)

    def qr_algorithm(self):
        """

        Calculates eigenvalues of a matrix using the QR algorithm

        Parameters:
        -----------
        n_max: an integer.
        eps: a float.

        """

        if self.matrix is None:
            print('\nMusisz wprowadzić macierz!')
            print('Użyj polecenia "matrix".')

        else:
            while True:
                print('\nJaka będzie górna granica'
                      + ' możliwych iteracji rozkładów QR'
                      + ' w algorytmie QR?')
                try:
                    n_max = int(input('Wpisz tutaj: '))

                    if n_max > 0:
                        break

                    else:
                        print('\nWprowadź dodatnią liczbę całkowitą!')

                except ValueError:
                    print('\nWprowadź liczbę całkowitą!')

            while True:
                print('\nJaka będzie tolerancja wartości?')
                try:
                    eps = float(input('Wpisz tutaj: '))

                    if eps > 0:
                        break

                    else:
                        print('\nWprowadź dodatnią liczbe wymierną!')

                except ValueError:
                    print('\nWprowadź liczbe wymierną!')

            is_new = not self.old_n_max == n_max or not self.old_eps == eps

            if is_new or self.eigenvalues is None:
                self.eigenvalues = self.matrix.qr_algorithm(n_max, eps)
                self.old_n_max = n_max
                self.old_eps = eps

                values = ''
                for eigenvalue in self.eigenvalues:
                    values = values + ' ' + str(eigenvalue)

                print('\nWartości własne macierzy:')
                print(values)

            else:
                values = ''
                for eigenvalue in self.eigenvalues:
                    values = values + ' ' + str(eigenvalue)

                print('\nWartości własne macierzy:')
                print(values)

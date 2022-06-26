from eigenqr.matrix import Matrix
import numpy as np


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

        print('\nAutorstwa:')
        print('Julia Bugaj, Dawid Kapcia, Alex Gibała, Szymon Forysiuk')

        print("\nNaszym celem jest zaprogramowanie aplikacji do obliczania"
              + " wartości własnych macierzy za pomocą algorytmu QR.")

    def help(self):
        """

        Function will display list of possible commands.

        """

        print('\n   Lista możliwych komend:')

        print('\nmatrix: wprowadź macierz,')
        print('deco:   dokonać rozkładu QR,')
        print('algo:   dokonać algorytmu QR,')
        print('prec:   ustawienie dokładności wyświetlania w deco,')
        print('intro:  wprowadzenie do aplikacji,')
        print('help:   lista komend,')
        print('end:    wyjście z aplikacji,')

        print('\nPrzykładowo w celu wprowadzenia macierzy wpisz'
              + ' w wiersz polecenia komendę "matrix".')

    def wrong_input(self):
        """

        Note that user inputed wrong command.

        """

        print('\nNieprawidłowa komenda!')
        print('Aby sprawdzić jakie komendy są możliwe, wpisz komendę "help".')

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
            print('\nJaki jest wymiar macierzy?')
            print('Pamiętaj, że zalecamy używanie macierzy o'
                  + ' wymiarze większym niż 4.')
            try:
                dimension = int(input('Wpisz tutaj: '))

                if dimension > 4:
                    break

                else:
                    print('\nProsimy wprowadzić dodatnią liczbę'
                          + ' całkowitą większą od 4!')

            except ValueError:
                print('\nProsimy wprowadzić liczbę całkowitą!')

        print('\nJakie są wartości macierzy?')
        print('Pamiętaj o umieszczaniu przerw pomiędzy liczbami'
              + ' za pomocją spacji.')
        print('Można wprowadzać liczbę zespoloną za pomocą wzoru a+bj,'
              + ' gdzie a to część rzeczywista, a b zespolona.'
              + ' Przykładem jest liczba 3+2j.')

        matrix = []

        for row_i in range(dimension):
            while True:
                print('\nWprowadź wiersz numer ' + str(row_i+1) + '.')
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
                        print('\nProsimy wprowadzać liczby złożone!')

        self.matrix = Matrix(matrix)

        print('\nMacierz została zapisana.')

    def qr_decomposition(self, n):
        """

        Calculates QR decomposition of a previously inputed matrix.

        Parameters:
        -----------
        n: an integer.

        """

        if self.matrix is None:
            print('\nMusisz najpierw wprowadzić macierz!')
            print('Aby wprowadzić macierz należy użyć komendy "matrix".')

        else:
            if self.Q is not None and self.R is not None:
                print('Wiersze są posegregowane za pomocą'
                      + ' nawiasów kwadratowych.')

                np.set_printoptions(threshold=np.inf)
                np.set_printoptions(precision=n)

                print('\nMacierz unitarna Q:')
                print(self.Q.matrix)

                np.set_printoptions(threshold=np.inf)
                np.set_printoptions(precision=n)

                print('\nMacierz górnotrójkątna R:')
                print(self.R.matrix)

            else:
                Q, R = self.matrix.qr_decomposition()

                self.Q = Q
                self.R = R

                print('Wiersze są posegregowane za pomocą'
                      + ' nawiasów kwadratowych.')

                np.set_printoptions(threshold=np.inf)
                np.set_printoptions(precision=n)

                print('\nMacierz unitarna Q:')
                print(Q.matrix)

                np.set_printoptions(threshold=np.inf)
                np.set_printoptions(precision=n)

                print('\nMacierz górnotrójkątna R:')
                print(R.matrix)

    def qr_algorithm(self, n):
        """

        Calculates eigenvalues of a matrix using the QR algorithm

        Parameters:
        -----------
        n: an integer.

        """

        if self.matrix is None:
            print('\nMusisz najpierw wprowadzić macierz!')
            print('Aby wprowadzić macierz należy użyć komendy "matrix".')

        else:
            while True:
                print('\nJakie jest maksymalnie ograniczenie liczby'
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
                print('\nJaka jest maksymalna tolerancja wartości?')
                try:
                    eps = float(input('Wpisz tutaj: '))

                    if eps > 0 and eps < 1:
                        break

                    elif eps < 1:
                        print('\nWprowadź liczbę wymierną mniejszą od 1!')

                    else:
                        print('\nWprowadź dodatnią liczbę wymierną!')

                except ValueError:
                    print('\nWprowadź liczbę wymierną!')

            is_new = not self.old_n_max == n_max or not self.old_eps == eps

            if is_new or self.eigenvalues is None:
                self.eigenvalues = self.matrix.qr_algorithm(n_max, eps)
                self.old_n_max = n_max
                self.old_eps = eps

                values = ''
                for eigenvalue in self.eigenvalues:
                    values = values + ' ' + str(eigenvalue)

                np.set_printoptions(threshold=np.inf)
                np.set_printoptions(precision=n)

                print('\nWartości własne macierzy:')
                print(values)

            else:
                values = ''
                for eigenvalue in self.eigenvalues:
                    values = values + ' ' + str(eigenvalue)

                np.set_printoptions(threshold=np.inf)
                np.set_printoptions(precision=n)

                print('\nWartości własne macierzy:')
                print(values)

    def precision(self):
        """

        Set precision of printing

        Parameters:
        -----------
        n: an integer.

        """

        while True:
            print('\nJaka jest maksymalna tolerancja wartości?')
            try:
                n = float(input('Type here: '))

                if n > 0 and n < 1:
                    break

                elif n < 1:
                    print('\nWprowadź liczbę wymierną mniejszą od 1!')

                else:
                    print('\nWprowadź dodatnią liczbę wymierną!')

            except ValueError:
                print('\nWprowadź liczbę wymierną!')

        np.set_printoptions(precision=n)

        return n

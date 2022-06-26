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

        print('\nBrought by:')
        print('Julia Bugaj, Dawid Kapcia, Alex Gibała, Szymon Forysiuk')

        print("\nThe aim of our project is to implement a QR algorithm to"
              + " calculate eigenvalues of a matrix.")

    def help(self):
        """

        Function will display list of possible commands.

        """

        print('\n   List of possible commands:')

        print('\nmatrix: input a matrix')
        print('deco: QR decomposition')
        print('algo: QR algorithm')
        print('intro: info')
        print('help: list of commands')
        print('end: close the app')

        print('\nFor example, to use command "matrix", type "matrix".')

    def wrong_input(self):
        """

        Note that user inputed wrong command.

        """

        print('\nWrong command!')
        print('To check what commands are possible, type "help".')

    def user_input(self):
        """

        Take user's input as a command.

        """

        user_command = input('\nType here: ')

        return user_command

    def input_matrix(self):
        """

        Input a matrix to the app.

        """

        self.Matrix = None
        self.qr_deco = None
        self.qr_algo = None

        while True:
            print('\nWhat will be the dimension of the matrix?')
            print('Please remember, that we recommend using a matrix of a'
                  + ' dimension greater than 4.')
            try:
                dimension = int(input('Type here: '))

                if dimension > 4:
                    break

                else:
                    print('\nPlease input a positive integer greater than 4!')

            except ValueError:
                print('\nPlease input an integer!')

        print('\nWhat will be the values of a matrix?')
        print('Please remember to split numbers using space.')
        print('Write complex values for example as 2+3j.')

        matrix = []

        for row_i in range(dimension):
            while True:
                print('\nInput the values of the ' + str(row_i+1) + '-th row.')
                row = input('Type here: ').split(' ')

                if row[-1] == '':
                    row.pop(-1)

                if len(row) < dimension:
                    print('\nNot enough inputed variables!')

                elif len(row) > dimension:
                    print('\nToo many inputed variables!')

                else:
                    try:
                        for col_i in range(dimension):
                            row[col_i] = complex(row[col_i])

                        matrix.append(row)
                        break

                    except ValueError:
                        print('\nPlease input complex numbers!')

        self.matrix = Matrix(matrix)

        print('\nMatrix is saved.')

    def qr_decomposition(self):
        """

        Calculates QR decomposition of a previously inputed matrix.

        """

        if self.matrix is None:
            print('\nYou need to input a matrix!')
            print('Please use command "matrix" to input a matrix.')

        else:
            if self.Q is not None and self.R is not None:
                print('\nOrthogonal matrix Q:')
                print(self.Q.matrix)

                print('\nUpper triangular matrix R:')
                print(self.R.matrix)

            else:
                Q, R = self.matrix.qr_decomposition()

                self.Q = Q
                self.R = R

                print('\nOrthogonal matrix Q:')
                print(Q.matrix)

                print('\nUpper triangular matrix R:')
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
            print('\nYou need to input a matrix!')
            print('Please use command "matrix".')

        else:
            while True:
                print('\nWhat will be the upper limit of the number of'
                      + ' possible iterations of the QR decompositions'
                      + ' during QR algorithm?')
                try:
                    n_max = int(input('Type here: '))

                    if n_max > 0:
                        break

                    else:
                        print('\nPlease input a positive integer!')

                except ValueError:
                    print('\nPlease input an integer!')

            while True:
                print('\nWhat will be the tolerance of the values?')
                try:
                    eps = float(input('Type here: '))

                    if eps > 0:
                        break

                    else:
                        print('\nPlease input a positive float!')

                except ValueError:
                    print('\nPlease input an float!')

            is_new = not self.old_n_max == n_max or not self.old_eps == eps

            if is_new or self.eigenvalues is None:
                self.eigenvalues = self.matrix.qr_algorithm(n_max, eps)
                self.old_n_max = n_max
                self.old_eps = eps

                values = ''
                for eigenvalue in self.eigenvalues:
                    values = values + ' ' + str(eigenvalue)

                print('\nEigenvalues of a matrix:')
                print(values)

            else:
                values = ''
                for eigenvalue in self.eigenvalues:
                    values = values + ' ' + str(eigenvalue)

                print('\nEigenvalues of a matrix:')
                print(values)
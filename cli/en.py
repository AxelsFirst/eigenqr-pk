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
        self.R

        self.qr_algo = None
        self.old_n_max = None
        self.old_eps = None

    def intro(self):
        """

        Function will display basic informations about our project.

        """

        print('EigenQR-PK')

        print('Brought by:')
        print('Julia Bugaj, Dawid Kapcia, Alex Gibała, Szymon Forysiuk')

        print("The aim of our project is to implement a QR algorithm to"
              + " calculate eigenvalues of a matrix.")

    def help(self):
        """

        Function will display list of possible commands.

        """

        print('List of commands:')

        print('matrix: input a matrix')
        print('deco: QR decomposition')
        print('algo: QR algorithm')
        print('intro: info')
        print('help: list of commands')
        print('end: close the app')

    def input_matrix(self):
        """

        Input a matrix to the app.

        """

        self.Matrix = None
        self.qr_deco = None
        self.qr_algo = None

        while True:
            print('What will be the dimension of the matrix?')
            try:
                dimension = int(input('Type here: '))

                if dimension > 0:
                    break

                else:
                    print('Please input a positive integer!')

            except ValueError:
                print('Please input an integer!')

        print('What will be the values of a matrix?')
        print('Please remember to split numbers using space.')
        print('Write complex values for example as 2+3j.')

        matrix = []

        for row_i in range(dimension):
            while True:
                print('Input the values of the ' + row_i + '-th row.')
                row = input('Type here: ').split(' ')

                if row[-1] == '':
                    row.pop(-1)

                if len(row) < dimension:
                    print('Not enough inputed variables!')

                elif len(row) > dimension:
                    print('Too many inputed variables!')

                try:
                    for col_i in range(dimension):
                        row[col_i] = complex(row[col_i])

                    matrix.append(row)
                    break

                except ValueError:
                    print('Please input complex numbers!')

        self.matrix = Matrix(matrix)

    def qr_decomposition(self):
        """

        Calculates QR decomposition of a previously inputed matrix.

        """

        if self.Q is not None and self.R is not None:
            print('Orthogonal matrix Q:')
            print(self.Q)

            print('Upper triangular matrix R:')
            print(self.R)

        else:
            Q, R = self.matrix.qr_decomposition()

            self.Q = Q
            self.R = R

            print('Orthogonal matrix Q:')
            print(Q.matrix)

            print('Upper triangular matrix R:')
            print(R.matrix)

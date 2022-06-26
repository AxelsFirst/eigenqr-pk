def intro():
    print('EigenQR-PK')
    print('Przedstawiony przez')
    print('Julia Bugaj, Dawid Kapcia, Alex Gibała, Szymon Forysiuk')
    print(" Celem naszego projektu jest zaimplementowanie algorytmu QR do obliczania" + "wartości własnych macierzy.")

def help():
    print('Lista komend:')

    print('matrix: wprowadź macierz')
    print('deco: QR rozkład')
    print('algo: QR algorithm')
    print('intro: informacja')
    print('help: lista komend')
    print('end: zamkniecie aplikacji')

def input_matrix():



    while True:
        print('Jaki będzie wymiar macierzy?')
        try:
            dimension = int(input('Wpisz tutaj'))

            if dimension >0:
                break
            
            else:
                print('Wprowadź dodatnią liczbę całkowitą!')

        except ValueError:
            print('Proszę wprowadzić liczbę całkowitą!')

    print('Jakie będą wartości macierzy')
    for row_index in range(dimension):
        while True:
            print('Zapisz wartości dla' + i + '-tego wiersza.')
            print('Prosze pamiętać o dzieleniu liczb spacją.')



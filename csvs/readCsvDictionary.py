import timeit
import csv


def extract_csv(paths):
    """Leer varios csvs y unirlos todos en el mismo diccionario con la id como clave y las demás columnas
        como valor en una misma lista"""

    with open(paths[0], newline='') as csvfile:
        file = csv.reader(csvfile, delimiter=',', quotechar='\"')
        next(file)
        response = {}
        for row in file:
            response[row[0]] = row[1:]

    for path in paths[1:]:
        with open(path, newline='') as csvfile:
            file = csv.reader(csvfile, delimiter=',', quotechar='\"')
            next(file)
            for row in file:
                response[row[0]].extend(row[1:])

    return response


def calc_extract_csv(path):
    return timeit.Timer(lambda: extract_csv(path)).timeit(number=3)


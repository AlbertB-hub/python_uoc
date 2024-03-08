import timeit
import pandas as pd
from datetime import datetime


def extract_csv(paths):
    """Lee diferentes csvs y los une en el mismo DataFrame por ID"""
    dfs = []
    for path in paths:
        dfs.append(pd.read_csv(path))

    merged_df = pd.merge(dfs[0], dfs[1], on='id')
    merged_df = pd.merge(merged_df, dfs[2], on='id')

    return merged_df


def calc_extract_csv(path):
    """Calcula el tiempo de ejecución de la creación del dataframe"""
    return timeit.Timer(lambda: extract_csv(path)).timeit(number=3)


def add_air_days_column(row):
    """Añadir columna de días de emisión de cada programa"""
    if not isinstance(row['last_air_date'], str) or not isinstance(row['first_air_date'], str):
        return 0

    return abs(int((datetime.strptime(row['last_air_date'], "%Y-%m-%d") - datetime.strptime(row['first_air_date'],
                                                                                            "%Y-%m-%d")).days))


def create_poster_dict(df):
    """Crear un diccionario con la url de las portadas de cada programa si existe"""
    poster_dict = {}
    for key, row in df.iterrows():
        if row['homepage'] == 'NaN' or row['homepage'] == '' or row['poster_path'] == 'NaN' or row['poster_path'] == '' or not isinstance(row['homepage'], str) or not isinstance(row['poster_path'], str):
            poster_dict[row['name']] = 'NOT AVAILABLE'
            continue

        poster_dict[row['name']] = row['homepage'] + row['poster_path']

    return poster_dict

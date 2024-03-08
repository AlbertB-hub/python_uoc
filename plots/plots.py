import pandas as pd
import matplotlib.pyplot as plt


def bar_plot_year(df):
    """Crear gráfico de barras de nuevas series emitidas agrupadas por año de estreno"""
    df2 = df.copy()
    df2['first_air_date'] = pd.to_datetime(df['first_air_date']).dt.year
    df2 = df2['first_air_date'].dropna()

    years_dict = {}
    for row in df2:
        years_dict[int(row)] = years_dict.get(row, 0) + 1

    lists = sorted(years_dict.items())

    x, y = zip(*lists)
    plt.bar(x, y)
    plt.show()


def line_plot_types_decade(df):
    """Gráfica de líneas de los programas agrupados por año y género"""
    df2 = df.copy()
    df2['first_air_date'] = pd.to_datetime(df['first_air_date']).dt.year
    df2 = df2[['first_air_date', 'type']].dropna()
    decades_dict = {}

    for key, row in df2.iterrows():
        decade = int(row['first_air_date']) // 10 * 10
        decades_dict[decade] = decades_dict.get(decade, {})
        decades_dict[decade][row['type']] = decades_dict[decade].get(row['type'], 0) + 1

    df2 = pd.DataFrame.from_dict(decades_dict, orient='index').sort_index()
    df2 = df2[df2.index >= 1940]
    df2.plot.line()

    plt.show()


def pie_chart_genres(df):
    """Gráfico de sectores para mostrar los porcentajes de cada género respecto al total y agrupando los que
        sean menores de 1% en el valor Other"""
    df = df[['genres']].dropna()
    genres_dict = {}
    df_len = len(df.index)

    for key, row in df.iterrows():
        for genre in row['genres'].split(','):
            genres_dict[genre.strip()] = genres_dict.get(genre.strip(), 0) + 1

    genres = ['Others']
    totals = [0]
    for key, value in genres_dict.items():
        pct = value / df_len * 100
        if pct >= 1:
            genres.append(key)
            totals.append(pct)
        else:
            totals[0] += pct
    plt.pie(totals, labels=genres, autopct='%1.1f%%')

    plt.show()

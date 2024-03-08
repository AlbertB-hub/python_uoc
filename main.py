from filemanager import extractfiles as filemanager
from csvs import readCsvPandas as csvpd, readCsvDictionary as csvdict
from plots import plots

if __name__ == '__main__':
    # 1.1
    filemanager.extract_zip('./TMDB.zip')
    csvs = [
        '/home/datasci/PycharmProjects/PEC4/TMDB_distribution.csv',
        '/home/datasci/PycharmProjects/PEC4/TMDB_info.csv',
        '/home/datasci/PycharmProjects/PEC4/TMDB_overview.csv'
    ]

    # 1.2 y 1.3
    csv_df = csvpd.extract_csv(csvs)
    csv_dict = csvdict.extract_csv(csvs)

    print('El tiempo de ejecución con pandas es')
    print(csvpd.calc_extract_csv(csvs))
    print('El tiempo de ejecución con csv reader es')
    print(csvdict.calc_extract_csv(csvs))

    # 2.1
    csv_df['air_days'] = csv_df.apply(csvpd.add_air_days_column, axis=1)
    print('Las emisiones más duraderas son:')
    print(csv_df.sort_values(['air_days'], ascending=False)[:10])

    # 2.2
    poster_dict = csvpd.create_poster_dict(csv_df)

    print(list(poster_dict.items())[:5])

    # 3.1
    filter_lang_topic = csv_df[
        ((csv_df['original_language'] == 'en')
         &
         (csv_df['overview'].str.contains('mystery', case=False)
          | csv_df['overview'].str.contains('crime', case=False)))
    ]

    # 3.2
    filter_2023_canceled = csv_df[
        (csv_df['first_air_date'].str.contains('2023', na=False))
        &
        (csv_df['status'].str.contains('canceled', case=False))
    ]

    # 3.3
    filter_japanese = csv_df[
        (csv_df['languages'].str.contains('ja', na=False))
        &
        csv_df['original_language'].str.contains('ja', na=False)
        ][['name', 'original_name', 'networks', 'production_companies']]

    print('Las veinte primeras series disponibles en japonés son:')
    print(filter_japanese[:20])

    # 4.1
    plots.bar_plot_year(csv_df)
    # 4.2
    plots.line_plot_types_decade(csv_df)
    # 4.3
    plots.pie_chart_genres(csv_df)

    print('hola')

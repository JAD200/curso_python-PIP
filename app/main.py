import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('./data.csv')
#?  Second CHallenge
    data = list(filter(lambda x: x['Continent'] == 'South America', data))
#*  First CHallenge
    country = input('Type country => ').title()
    print(country)

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country'], labels, values)

#?  Second CHallenge
    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)


if __name__ == '__main__':
    run()

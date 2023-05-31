import pandas as pd
from data.load_data import load_data
from data.clear_data import clear_data
from stats.calc_stats import show_stats, sum
from plots.plots import show_plots

if __name__ == "__main__":
    urodzenia = load_data("https://statisticstimes.com/demographics/countries-by-birth-rate.php", ['Kraj', 'Narodziny na rok',
                        'Narodziny na dzień', 'Wspołczynnik urodzeń', 'Kontynent'])
    smierci = load_data("https://statisticstimes.com/demographics/countries-by-death-rate.php",
                        ['Kraj', 'Śmierci na rok', 'Śmierci na dzień', 'Wspołczynnik śmierci', 'Kontynent'])
    
    data = clear_data(urodzenia, smierci, ['Kraj'])

    with pd.option_context('display.width', 250, 'display.max_columns', 10):
        print(data)

    show_stats(data)

    totalSumBirthCountry = sum(data, 'Kraj','Narodziny na rok')
    totalSumBirthContinent = sum(data, 'Kontynent','Narodziny na rok')
    totalSumDeathCountry = sum(data, 'Kraj', 'Śmierci na rok')
    totalSumDeathContinent = sum(data, 'Kontynent','Śmierci na rok')

    print(totalSumBirthCountry)
    print(totalSumBirthContinent)
    print(totalSumDeathCountry)
    print(totalSumDeathContinent)

    show_plots(data, totalSumBirthContinent, totalSumDeathContinent)
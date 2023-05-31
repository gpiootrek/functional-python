
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from helpers.format import millions
from stats.calc_stats import mediana


def plot_sums(X_axis, totalSumBirthContinent, totalSumDeathContinent):
    plt.figure(figsize=(10, 6))

    plt.bar(X_axis - 0.2, totalSumBirthContinent['Narodziny na rok'], 0.4, label='Suma narodzin na rok')
    plt.bar(X_axis + 0.2, totalSumDeathContinent['Śmierci na rok'], 0.4, label='Suma śmierci na rok')

    plt.gca().yaxis.set_major_formatter(mpl.ticker.FuncFormatter(millions))


def plot_with_errors(data, X_axis, totalSumBirthContinent, totalSumDeathContinent):
    std_births_continent = data.groupby('Kontynent')['Narodziny na rok'].std()
    std_deaths_continent = data.groupby('Kontynent')['Śmierci na rok'].std()
    
    plt.errorbar(X_axis - 0.2, totalSumBirthContinent['Narodziny na rok'], yerr=std_births_continent, fmt='none', color='black', capsize=5)
    plt.errorbar(X_axis + 0.2, totalSumDeathContinent['Śmierci na rok'], yerr=std_deaths_continent, fmt='none', color='black', capsize=5)

    plt.xticks(X_axis, totalSumBirthContinent.index)
    plt.xlabel('Kontynent')
    plt.ylabel('Suma')
    plt.title('Porównanie liczby narodzin a śmierci według kontynentów')
    plt.legend()
    plt.show()


def plot_medians(data, X_axis, totalSumBirthContinent):
    plt.figure(figsize=(10, 6))

    plt.bar(X_axis - 0.2, mediana(data, 'Kontynent', 'Narodziny na rok')['Narodziny na rok'], 0.4, label='Mediana narodzin na rok')
    plt.bar(X_axis + 0.2, mediana(data, 'Kontynent', 'Śmierci na rok')['Śmierci na rok'], 0.4, label='Mediana śmierci na rok')

    plt.xticks(X_axis, totalSumBirthContinent.index)
    plt.xlabel('Kontynent')
    plt.ylabel('Mediana')
    plt.title('Mediana liczby narodzin i zgonów według kontynentów')
    plt.legend()
    plt.show()


def plot_violins(data):
    plt.figure(figsize=(10, 6))

    sns.violinplot(x='Kontynent', y='Wspołczynnik urodzeń', data=data)

    plt.xlabel('Kontynent')
    plt.ylabel('Wspołczynnik urodzeń')
    plt.title('Rozkład liczby zgonów na rok dla każdego kontynentu')
    plt.show()


    plt.figure(figsize=(10, 6))

    sns.violinplot(x='Kontynent', y='Wspołczynnik śmierci', data=data)

    plt.xlabel('Kontynent')
    plt.ylabel('Wspołczynnik śmierci')
    plt.title('Rozkład liczby narodzin na rok dla każdego kontynentu')
    plt.show()


def plot_corr(data):
    plt.figure(figsize=(10, 10))

    sns.scatterplot(data=data, x='Wspołczynnik urodzeń', y='Wspołczynnik śmierci', hue='Kontynent', s=60)

    plt.legend(title='Kontynent')
    plt.xlabel('Wspołczynnik urodzeń')
    plt.ylabel('Wspołczynnik śmierci')
    plt.title('Korelacja pomiędzy współczynnikiem urodzeń a śmierci')

    plt.show()

    plot_distribution_by_continent(data, 'Kraj', 'Narodziny na rok')


def plot_distribution_by_continent(data, x_column, y_column):
    continents = data['Kontynent'].unique()

    for continent in continents:
        continent_data = data[data['Kontynent'] == continent]
        sorted_data = continent_data.sort_values(y_column)[-10::]
        
        plt.figure(figsize=(12, 8))
        sns.barplot(x=x_column, y=y_column, data=sorted_data)
        plt.gca().yaxis.set_major_formatter(mpl.ticker.FuncFormatter(millions))

        plt.xlabel('Kraj')
        plt.ylabel('Liczba narodzin na rok')
        plt.title(f'Liczba narodzin w 10 krajach o najwyższych wartościach na kontynencie: {continent}')
        plt.xticks(rotation=90)
        plt.legend()

        plt.tight_layout()
        plt.show()


def show_plots(data, totalSumBirthContinent, totalSumDeathContinent):
    X_axis = np.arange(len(totalSumBirthContinent.index))


    plot_sums(X_axis, totalSumBirthContinent, totalSumDeathContinent)

    plot_with_errors(data, X_axis, totalSumBirthContinent, totalSumDeathContinent)

    plot_medians(data, X_axis, totalSumBirthContinent)

    plot_violins(data)

    plot_corr(data)

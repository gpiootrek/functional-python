import numpy as np

def sum(data, grupa, column):
    return data.groupby(grupa).agg({
        column:'sum'
    })
    
def std_deviation(data, dane):
    return np.std(data[dane])

def std(data, grupa, column):
    return data.groupby(grupa).agg({
        column:'std'
    })
    
def mediana(data, grupa,column):
    return data.groupby(grupa).agg({
        column:'median'
    })
    
def show_stats(data):
    print("Odchylenie standardowe liczby narodzin i zgonów:")
    print(std_deviation(data, 'Wspołczynnik urodzeń'))
    print(std_deviation(data, 'Wspołczynnik śmierci'))
    print(std(data, 'Kontynent','Narodziny na rok'))  


    print("Mediana liczby narodzin i zgonów dla każdego kontynentu")
    print(mediana(data, 'Kontynent','Narodziny na rok'))
    print(mediana(data, 'Kontynent','Śmierci na rok'))


    print("Korelacja między wskaźnikami urodzeń a wskaźnikami zgonów dla każdego kontynentu:")
    corr = data.groupby('Kontynent')[
        ['Wspołczynnik urodzeń', 'Wspołczynnik śmierci']].corr().iloc[0::2, -1]
    print(corr)


    var_urodzen = data.groupby('Kontynent')['Wspołczynnik urodzeń'].var()
    var_smierci = data.groupby('Kontynent')['Wspołczynnik śmierci'].var()
    print("Wariancja wskaźnika zgonów dla każdego kontynentu:")
    print(var_smierci)
    print("Wariancja wskaźnika urodzeń dla każdego kontynentu:")
    print(var_urodzen)
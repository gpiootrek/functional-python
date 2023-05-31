import pandas as pd

def clear_data(frame1, frame2, colName):
    result = pd.merge(frame1, frame2, on=colName)
    result.rename(columns={'Kontynent_y':'Kontynent'}, inplace=True)
    result.drop('Kontynent_x',axis=1, inplace=True)
    result.dropna(inplace=True)

    result['Wspołczynnik urodzeń'] = result['Wspołczynnik urodzeń'].str.replace(',', '').astype(float)
    result['Wspołczynnik śmierci'] = result['Wspołczynnik śmierci'].str.replace(',', '').astype(float)
    result['Narodziny na rok'] = result['Narodziny na rok'].str.replace(',', '').astype(float)
    result['Śmierci na rok'] = result['Śmierci na rok'].str.replace(',', '').astype(float)

    return result
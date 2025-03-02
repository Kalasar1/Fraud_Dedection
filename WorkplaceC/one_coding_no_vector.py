import pandas as pd

def one_coding_no_vec(df):
    # Kategorik sütunları bul
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    # Her kategorik sütun için benzersiz değerleri alıp 1 ve 0 ile kodla
    for col in categorical_cols:
        unique_values = df[col].unique()  # Benzersiz değerleri al
        
        # Her benzersiz değer için yeni sütun oluştur
        for value in unique_values:
            # Yeni sütunu oluştur, '1' değerini sadece o değeri içeren satırlarda koy
            df[f'is_{col}_{value}'] = (df[col] == value).astype(int)
        
        # Orijinal kategorik sütunu çıkar
        df = df.drop(col, axis=1)
    
    return df

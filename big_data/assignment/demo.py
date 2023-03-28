def normalize(df):
    # select numerical columns
    num_cols = df.select_dtypes(include=[np.number]).copy()
    num_cols.drop('price', axis='columns', inplace=True)
    df_norm = ((num_cols - num_cols.min()) / (num_cols.max() - num_cols.min()))
    return df_norm

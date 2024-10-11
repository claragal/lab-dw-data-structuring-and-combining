import pandas as pd

def clean_column_names(df):
    df.columns = (df.columns
                  .str.replace('ST', 'state', regex=False)
                  .str.replace(' ', '_')
                  .str.lower())
    return df

def clean_invalid_values(df):
    df['gender'] = df['gender'].replace({
        'F': 'F', 'M': 'M', 'Female': 'F', 'male': 'M', 'Male': 'M', 'Femal': 'F'})
    state_name = {'AZ': 'Arizona', 'Cali': 'California', 'WA': 'Washington'}
    df['state'] = df['state'].replace(state_name)
    df['education'] = df['education'].replace({'Bachelors': 'Bachelor'})
    #df['customer_lifetime_value'] = df['customer_lifetime_value'].str.replace('%', '').str.strip()
    df['customer_lifetime_value'] = df['customer_lifetime_value'].astype(float)
    df['vehicle_class'] = df['vehicle_class'].replace({
        'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'})
    return df

def formatting_data_types(df):
    df['customer_lifetime_value'] = pd.to_numeric(df['customer_lifetime_value'], errors='coerce')
    df['number_of_open_complaints'] = df['number_of_open_complaints'].apply(
        lambda x: int(x.split('/')[1]) if isinstance(x, str) else x)
    return df

def fill_missing_values(df):
    numerical_cols = df.select_dtypes(include=['float64', 'int']).columns
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].median())
    return df

def convert_numeric_to_integers(df):
    numerical_cols = df.select_dtypes(include=['float64', 'int']).columns
    df[numerical_cols] = df[numerical_cols].astype(int)
    return df

def clean_data(df):
    """
    Apply all the cleaning and formatting steps on the dataset.
    """
    df = clean_column_names(df)
    df = clean_invalid_values(df)
    df = formatting_data_types(df)
    df = fill_missing_values(df)
    df = convert_numeric_to_integers(df)
    return df
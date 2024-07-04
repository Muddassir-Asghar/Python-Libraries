import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer


try:
    df = pd.read_csv('WHO-COVID-19-global-data.csv')
except FileNotFoundError:
    print("The specified file was not found.")
    exit()

# Drop unnecessary columns and rename remaining columns
df.drop(['Country_code', 'WHO_region', 'Cumulative_cases', 'Cumulative_deaths'], axis=1, inplace=True)
df = df.rename(columns={'Date_reported': 'Date', 'New_cases': 'Cases', 'New_deaths': 'Deaths'})

try:
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
except ValueError as e:
    print("Date format mismatch. Please check the date format in your CSV file.")
    print(e)
    exit()

# Handle missing values using SimpleImputer with constant strategy
imputer = SimpleImputer(strategy='constant')
df = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Convert columns to numeric where applicable and drop rows with NaN values
df['Cases'] = pd.to_numeric(df['Cases'], errors='coerce')
df['Recovered'] = pd.to_numeric(df['Recovered'], errors='coerce')
df['Deaths'] = pd.to_numeric(df['Deaths'], errors='coerce')
df.dropna(subset=['Cases', 'Recovered', 'Deaths'], inplace=True)

# Plot indivdual country COVID-19 trends
# countries = df['Country'].unique()
# for i in range(len(countries)):
    # C = df[df['Country'] == countries[i]].reset_index()
    # plt.plot(C['Date'], C['Cases'], color='yellow', label='Confirmed Cases')
    # plt.plot(C['Date'], C['Recovered'], color='green', label='Recovered Cases')
    # plt.plot(C['Date'], C['Deaths'], color='red', label='Deaths')
    # plt.title(countries[i])
    # plt.xlabel('Date')
    # plt.ylabel('Cases')
    # plt.legend()
    # plt.show()

# Plot global COVID-19 trends
plt.plot(df['Date'], df['Cases'], color='yellow', label='Confirmed Cases')
plt.plot(df['Date'], df['Recovered'], color='green', label='Recovered Cases')
plt.plot(df['Date'], df['Deaths'], color='red', label='Deaths')
plt.title('COVID-19 Global Trends')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.legend()
plt.show()

# Uncomment this line if you want to print the first 100 rows of the dataframe
# print(df.head(100))

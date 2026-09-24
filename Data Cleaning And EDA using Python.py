import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Practice\Power Trading Analysis\IEX_final.csv")


df.head()

df.shape

df.columns

df.info()

## Null value check
df.isnull().sum()

## Duplicate Row check
df.duplicated().sum()

df = df.drop_duplicates()

df.columns

# Datatypes
df.dtypes

## Date formatting

print(df['Date'].head(10))
print(df['Date'].tail(20))


df['Date'] = pd.to_datetime(
    df['Date'],
    format='%d-%m-%Y',
    errors='coerce'
)

print(df['Date'].isnull().sum())


## Filling missing values in numeric columns with median
numeric_columns = df.select_dtypes(include=np.number).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())


## Filling missing values in Text columns with median

text_columns = df.select_dtypes(include='object').columns

for col in text_columns:
    df[col] = df[col].fillna(df[col].mode()[0])



df.describe()

## Check Outliers
import matplotlib.pyplot as plt

plt.figure(figsize = (15, 6))
df.boxplot()
plt.xticks(rotation = 90)
plt.show()



###### EDA(Exploratory Data Analysis) ###########

## Creating Year, Month, Day Columns

df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day


df[['Date','year','month','day']].head()


df.describe().T


## Correlation metrix

correlation = df.corr(numeric_only = True)
(correlation)


## Correlation Heatmap
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize = (20, 15))

sns.heatmap(correlation, cmap = 'coolwarm', annot = False)
plt.title("Correlation Matrix")
plt.show()


## Distribution of MCP
for col in df.columns:
    if "mcp" in col:
        print(col)
        

plt.figure(figsize=(8,5))

plt.hist(df["MCP (Rs/MWh) *"], bins=40)

plt.title("Distribution of MCP")
plt.xlabel("MCP")
plt.ylabel("Frequency")

plt.show()


## Monthly Average of MCP
monthly = df.groupby('month')["MCP (Rs/MWh) *"].mean()

monthly.plot(kind='bar',
             figsize=(10,5))

plt.title("Average Monthly MCP")

plt.show()



### FEATURE ENGINEERING FOR WEATHER COLUMNS

# Average Temperature
temp_cols = [col for col in df.columns if 'temperature' in col]
df['avg_temperature'] = df[temp_cols].mean(axis=1)

# Average Relative Humidity
humidity_cols = [col for col in df.columns if 'relative_humidity' in col]
df['avg_humidity'] = df[humidity_cols].mean(axis=1)

# Average Wind Speed
wind_cols = [col for col in df.columns if 'wind_speed' in col]
df['avg_wind_speed'] = df[wind_cols].mean(axis=1)

# Average Cloud Cover
cloud_cols = [col for col in df.columns if 'cloud_cover' in col]
df['avg_cloud_cover'] = df[cloud_cols].mean(axis=1)

# Average Solar Radiation
radiation_cols = [col for col in df.columns if 'shortwave_radiation' in col]
df['avg_radiation'] = df[radiation_cols].mean(axis=1)

print("New Features Created Successfully!")



df[['avg_temperature',
    'avg_humidity',
    'avg_wind_speed',
    'avg_cloud_cover',
    'avg_radiation']].head()


## Relationship between Temperature and MCP
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

plt.scatter(
    df['avg_temperature'],
    df['MCP (Rs/MWh) *'],
    alpha=0.3
)

plt.xlabel("Average Temperature (°C)")
plt.ylabel("MCP (Rs/MWh)")
plt.title("Average Temperature vs MCP")

plt.grid(True)

plt.show()


## Weather Correlation
weather_corr = df[
    [
        'avg_temperature',
        'avg_humidity',
        'avg_wind_speed',
        'avg_cloud_cover',
        'avg_radiation',
        'MCP (Rs/MWh) *'
    ]
]

print(weather_corr.corr())


## Time Series
daily = df.groupby('Date')['MCP (Rs/MWh) *'].mean()

plt.figure(figsize=(15,5))

daily.plot()

plt.title("Daily MCP Trend")

plt.show()


# Saved the Cleaned dataset 
df.to_csv(r"C:\Practice\Power Trading Analysis\IEX_cleaned.csv", index=False)


# Statistical Analysis 

columns = [
    'Hour',
    'Purchase Bid (MW)',
    'Sell Bid (MW)',
    'MCV (MW)',
    'Final Scheduled Volume (MW)',
    'MCP (Rs/MWh) *',
    'Mundra_temperature_2m (°C)',
    'Mundra_relative_humidity_2m (%)'
]

data = df[columns]

statistics = pd.DataFrame({
    'Mean': data.mean(),
    'Median': data.median(),
    'Mode': data.mode().iloc[0],
    'Variance': data.var(),
    'Standard Deviation': data.std(),
    'Range': data.max() - data.min(),
    'Skewness': data.skew(),
    'Kurtosis': data.kurt()
})

print(statistics)


## Histogram
for column in columns:
    plt.figure(figsize=(6,4))
    sns.histplot(data[column], bins=20)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


## Scatterplot
for i in range(len(columns)):
    for j in range(i+1, len(columns)):

        plt.figure(figsize=(8,5))

        sns.scatterplot(
            data=data,
            x=columns[i],
            y=columns[j]
        )

        plt.title(f'{columns[i]} vs {columns[j]}')

        plt.tight_layout()
        plt.show()


## Boxplot
for column in columns:
    plt.figure(figsize=(8,5))

    sns.boxplot(y=data[column])

    plt.title(f'Box Plot of {column}')
    plt.ylabel(column)

    plt.tight_layout()
    plt.show()


## Heatmap
plt.figure(figsize=(10,8))

corr = data.corr()

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()










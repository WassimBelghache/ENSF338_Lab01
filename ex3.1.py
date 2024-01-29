import json
import matplotlib.pyplot as plt

file_path = 'internetdata.json'

low_income_countries = []
high_income_countries = []

try:
    with open(file_path, 'r') as file:
        data = json.load(file)

    for d in data:
        income = d.get('incomeperperson')
        internet_rate = d.get('internetuserate')

        if income is not None and internet_rate is not None:
            if income < 10000:
                low_income_countries.append(internet_rate)
            elif income >= 10000:
                high_income_countries.append(internet_rate)

    if low_income_countries:
        plt.figure(figsize=(10,6))
        plt.hist(low_income_countries, bins=20, color='blue', alpha=0.7)
        plt.title('Internet Usage in Low-Income Countries')
        plt.xlabel('Internet Usage Rate')
        plt.ylabel('Number of Countries')
        plt.savefig('hist1.png')

    if high_income_countries:
        plt.figure(figsize=(10,6))
        plt.hist(high_income_countries, bins=20, color='green', alpha=0.7)
        plt.title('Internet Usage in High-Income Countries')
        plt.xlabel('Internet Usage Rate')
        plt.ylabel('Number of Countries')
        plt.savefig('hist2.png')

except FileNotFoundError:
    print(f'File not found: {file_path}')
except json.JSONDecodeError:
    print(f'Error deconding JSON from the file: {file_path}')
except Exception as e:
    print(f'An error occured: {e}')
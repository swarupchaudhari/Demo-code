import pandas as pd

def calculate_demographic_data(print_data=True):

    # Read the dataset
    df = pd.read_csv("adult.data.csv")

    # 1. Count people of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    men = df[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(), 1)

    # 3. Percentage of people with Bachelors degree
    bachelors = df[df['education'] == 'Bachelors']
    percentage_bachelors = round((len(bachelors) / len(df)) * 100, 1)

    # 4. Percentage of people with advanced education earning >50K
    higher_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = round(
        (higher_edu['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Percentage of people without advanced education earning >50K
    lower_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = round(
        (lower_edu['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Minimum work hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of rich people working minimum hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 8. Country with highest percentage of rich people
    rich_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_country = df['native-country'].value_counts()
    country_percentage = (rich_country / total_country) * 100

    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 9. Most common occupation for rich people in India
    india_rich = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Print results if needed
    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich percentage (min hours):", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country percentage:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
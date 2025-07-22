import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r"E:\DB_DS\DS\adult.data.csv")
    df = df.dropna()

    # How many of each race are represented in this dataset?
    race_count = df["race"].value_counts()

    # What is the average age of men?
    fltr = df.loc[df["sex"] == "Male"]
    average_age_men = round(fltr["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    fltr2 = df.loc[df["education"] == "Bachelors"]
    percentage_bachelors = round((len(fltr2) / len(df)) * 100, 1)

    # Percentage of people with advanced education that make >50K
    higher_education = df.loc[df["education"].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df.loc[~df["education"].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = higher_education[higher_education["salary"] == ">50K"]
    lower_education_rich = lower_education[lower_education["salary"] == ">50K"]

    percentage_higher_education_rich = round((len(higher_education_rich) / len(higher_education)) * 100, 1)
    percentage_lower_education_rich = round((len(lower_education_rich) / len(lower_education)) * 100, 1)

    # Minimum hours per week
    min_work_hours = df["hours-per-week"].min()

    # Rich percentage among those who work minimum hours
    min_workers = df[df["hours-per-week"] == min_work_hours]
    min_workers_rich = min_workers[min_workers["salary"] == ">50K"]
    num_min_workers = len(min_workers)
    rich_percentage = round((len(min_workers_rich) / num_min_workers) * 100, 1)

    # Country with highest percentage of rich
    rich_people = df[df["salary"] == ">50K"]
    country_rich_count = rich_people["native-country"].value_counts()
    country_total_count = df["native-country"].value_counts()
    country_rich_percentage = (country_rich_count / country_total_count) * 100
    country_rich_percentage = country_rich_percentage.dropna()

    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # Top occupation in India for rich people
    india_rich = df[(df["salary"] == ">50K") & (df["native-country"] == "India")]
    top_IN_occupation = india_rich["occupation"].mode()[0]


    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {percentage_higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {percentage_lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
    'race_count': race_count,
    'average_age_men': average_age_men,
    'percentage_bachelors': percentage_bachelors,
    'percentage_higher_education_rich': percentage_higher_education_rich,  # ✅ صح
    'percentage_lower_education_rich': percentage_lower_education_rich,    # ✅ صح
    'min_work_hours': min_work_hours,
    'rich_percentage': rich_percentage,
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
        }



# print(calculate_demographic_data())
# df = pd.read_csv(r"E:\DB_DS\DS\adult.data.csv")
# print(df.columns)
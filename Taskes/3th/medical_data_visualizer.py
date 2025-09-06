import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"E:\DB_DS\DS\Taskes\3th\medical_examination.csv"
print(f"ur file path is : \n r{file_path}")

class MedicalAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.df_melted = None

    # Read data from CSV
    def __read_data(self):
        self.df = pd.read_csv(self.file_path)
        return self.df

    # Calculate BMI and add 'overweight' column
    def __calculation(self):
        self.df["BMI"] = self.df["weight"] / (self.df["height"]/100)**2
        self.df["overweight"] = (self.df["BMI"] > 25).astype(int)
        return self.df

    # Normalize cholesterol and gluc values (1 -> 0, else -> 1)
    def __normalize_columns(self):
        self.df["cholesterol"] = self.df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
        self.df["gluc"] = self.df["gluc"].apply(lambda x: 0 if x == 1 else 1)
        return self.df

    # Clean data (valid blood pressure + remove outliers in height/weight)
    def __clean_data(self):
        self.df = self.df[
            (self.df["ap_lo"] < self.df["ap_hi"]) &
            (self.df["height"] >= self.df["height"].quantile(0.025)) &
            (self.df["height"] <= self.df["height"].quantile(0.975)) &
            (self.df["weight"] >= self.df["weight"].quantile(0.025)) &
            (self.df["weight"] <= self.df["weight"].quantile(0.975))
        ]
        return self.df

    # Reshape data for categorical plot (wide -> long)
    def __melt_data(self):
        self.df_melted = self.df.melt(
            id_vars=["cardio"], 
            value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
        )
        return self.df_melted

    # Draw categorical plot
    def __categorical_data(self):
        sns.catplot(x="variable", hue="value", kind="count", data=self.df_melted)
        plt.title('Categorical Plot')
        plt.show()

    # Draw correlation heatmap
    def __correlation_heatmap(self):
        corr = self.df.corr()
        sns.heatmap(
            corr,
            mask=np.triu(np.ones_like(corr, dtype=bool)),
            annot=True,
            fmt=".1f",
            cmap="coolwarm"
        )
        plt.title("Correlation Heatmap")
        plt.show()

    # Run all pipeline
    def display(self):
        self.__read_data()
        self.__calculation()
        self.__normalize_columns()
        self.__clean_data()
        self.__melt_data()
        self.__categorical_data()
        self.__correlation_heatmap()



# analysis = MedicalAnalysis(file_path)
# analysis.dis()

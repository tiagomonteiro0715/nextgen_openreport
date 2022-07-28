'''
Before running this script, place the .csv files in "https://github.com/tiagomonteiro0715/next-gen_openreport/blob/main/README.md" in the folder CSVFILES
'''

import pandas as pd


df_collection = {
    0: " ",
    1: " ",
    2: " "
}

path_robotics = "CSVFILES/ARK_AUTONOMOUS_TECH._&_ROBOTICS_ETF_ARKQ_HOLDINGS.csv"
path_internet = "CSVFILES/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv"
path_DNA = "CSVFILES/ARK_GENOMIC_REVOLUTION_ETF_ARKG_HOLDINGS.csv"

count = 0
def filterArkinvestCSV(path, save):

    df = pd.read_csv(path)

    df.sort_values(['market value ($)'], ascending=False)
    date = df["date"][1]

    collums_to_drop = ['fund', "ticker", "cusip", "weight (%)", "date"]
    for collum in range(len(collums_to_drop)):
        df = df.drop(collums_to_drop[collum], axis = 1)

    df = df.head(10)

    df_collection[save] = df

    print("\n\nDate of " + path + " file is " + date)

filterArkinvestCSV(path_robotics, 0)
filterArkinvestCSV(path_internet, 1)
filterArkinvestCSV(path_DNA, 2)


for i in range(3):
    print("\n\n")
    print(df_collection[i])   

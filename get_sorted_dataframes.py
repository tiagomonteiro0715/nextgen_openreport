'''
Before running this script, place the .csv files in "https://github.com/tiagomonteiro0715/next-gen_openreport/blob/main/README.md" in the folder CSVFILES
'''

import pandas as pd

arkPathsArr = ["CSVFILES/ARK/ARK_AUTONOMOUS_TECH._&_ROBOTICS_ETF_ARKQ_HOLDINGS.csv","CSVFILES/ARK/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv","CSVFILES/ARK/ARK_GENOMIC_REVOLUTION_ETF_ARKG_HOLDINGS.csv"]
#tentar com array de paths fazer função unica para recolher informações, á base de ficheiros na pasta. range(len(arkPathsArr))
df_ark_collection = {
    0: " ",
    1: " ",
    2: " ",
}

count = 0
def filterArkinvestCSV(path, countervar):
    global count
    df = pd.read_csv(path)

    df.sort_values(['market value ($)'], ascending=False)
    date = df["date"][1]

    collums_to_drop = ['fund', "ticker", "cusip", "weight (%)", "date"]
    for collum in range(len(collums_to_drop)):
        df = df.drop(collums_to_drop[collum], axis = 1)

    countervar = countervar + 1

    df_ark_collection[countervar] = df

    print(df)

    print("\nDate of " + path + " file is \n\n\n" + date)


for i in range(3):
    filterArkinvestCSV(arkPathsArr[i], count)
    print("\n\n-------------------------------------\n\n" + str(count) + "\n\n-------------------------------------\n\n")

#------------------------------------------------------------------------------------------

df_fund_collection = {
    0:" ",
    1:" ",
    2:" "
}

fundPathsArr = ["CSVFILES/FUND/ENERGY.csv","CSVFILES/FUND/HEALTH_CARE_FUND.csv","CSVFILES/FUND/TECH_FUND.csv"  ]


def filterFundinvestCSV(path):
    df = pd.read_csv(path)

    collums_to_drop = ['nok', "sector", "ownership", "id", "type", "voting"]
    for collum in range(len(collums_to_drop)):
        df = df.drop(collums_to_drop[collum], axis = 1)

    df = df.sort_values(['usd'], ascending=False)

    df = df.reset_index(drop="index")

filterFundinvestCSV(fundPathsArr[0])

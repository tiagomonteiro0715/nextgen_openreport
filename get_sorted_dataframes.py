import pandas as pd

arkPathsArr = ["CSVFILES/ARK/ARK_AUTONOMOUS_TECH._&_ROBOTICS_ETF_ARKQ_HOLDINGS.csv","CSVFILES/ARK/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv","CSVFILES/ARK/ARK_GENOMIC_REVOLUTION_ETF_ARKG_HOLDINGS.csv"]
fundPathsArr = ["CSVFILES/FUND/ENERGY.csv","CSVFILES/FUND/HEALTH_CARE_FUND.csv","CSVFILES/FUND/TECH_FUND.csv"  ]

df_ark_collection = {
    0: " ",
    1: " ",
    2: " ",
}

countFund = 0
df_fund_collection = {
    0:" ",
    1:" ",
    2:" "
}


countArk = 0
def filterArkinvestCSV(path, countervar):
    global countArk
    df = pd.read_csv(path)

    df.sort_values(['market value ($)'], ascending=False)
    date = df["date"][1]

    collums_to_drop = ['fund', "ticker", "cusip", "weight (%)", "date", "shares"]
    for collum in range(len(collums_to_drop)):
        df = df.drop(collums_to_drop[collum], axis = 1)

    countervar = countervar + 1

    df_ark_collection[countervar] = df

    df = df.rename(columns={'market value ($)':'usd'})


    print(df)

    print("\nDate of " + path + " file is \n\n\n" + date)

#------------------------------------------------------------------------------------------

def filterFundinvestCSV(path, countervar):
    df = pd.read_csv(path)

    collums_to_drop = ['nok', "sector", "ownership", "id", "type", "voting", "country"]
    for collum in range(len(collums_to_drop)):
        df = df.drop(collums_to_drop[collum], axis = 1)

    df = df.sort_values(['usd'], ascending=False)

    df = df.reset_index(drop="index")

    countervar = countervar + 1

    df_fund_collection[countervar] = df

    print(df)

for i in range(3):
    filterArkinvestCSV(arkPathsArr[i], countArk)
    filterFundinvestCSV(fundPathsArr[i], countFund)




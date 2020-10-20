import os
import shutil
import pandas as pd

def check_and_run_operation(folder_to_build, folder_to_use, start_message, operation):
    if os.path.exists(f"../Storage/{folder_to_build}"):
        print(f"{folder_to_build} exists, no need to create this folder.")
    elif os.path.exists(f"../Storage/{folder_to_use}") and not os.path.exists(f"../Storage/{folder_to_build}"):
        print()
        print(f"{start_message}")
        print()
        os.mkdir(f"../Storage/{folder_to_build}")
        count = 0
        no_of_files = len(os.listdir(f"../Storage/{folder_to_use}"))
        for file in os.listdir(f"../Storage/{folder_to_use}"):
            count += 1
            print(f"Currently in file {count} of {no_of_files}")
            operation(file, folder_to_build, folder_to_use)
    else:
        print("Please put the Storage folder at the top level of this folder.")
        exit(1)

# Extract the csvs from within folders
def extract_csvs_from_companies(file, folder_to_build, folder_to_use):
    for csv in os.listdir(f"../Storage/{folder_to_use}/{file}"):
        shutil.copyfile(f"../Storage/{folder_to_use}/{file}/{csv}", f"../Storage/{folder_to_build}/{csv}")

check_and_run_operation("Companies_csvs", "Companies", "EXTRACTING CSV FROM COMPANIES", extract_csvs_from_companies)

# Dropping rows with NaN values
def csvs_dropna(file, folder_to_build, folder_to_use):
    df = pd.read_csv(f"../Storage/{folder_to_use}/{file}", index_col=[0])
    df = df.dropna()
    df.to_csv(f"../Storage/{folder_to_build}/{file}")

check_and_run_operation("Companies_dropna", "Companies_csvs", "DROP ROWS WITH NaN VALUES IN ALL CSVS", csvs_dropna)

# Remove csvs with < 2 months of data
def remove_csvs_with_less_than_2_months_of_data(file, folder_to_build, folder_to_use):
    df = pd.read_csv(f"../Storage/{folder_to_use}/{file}", index_col=[0])
    if df.shape[0] > 60:
        print(True)
        df.to_csv(f"../Storage/{folder_to_build}/{file}")

check_and_run_operation("Companies_more_than_2_months_data", "Companies_dropna", "FILTER AND GET CSVS WITH > 2 MONTHS OF DATA", remove_csvs_with_less_than_2_months_of_data)

# Remove extra data for companies csvs that have > 2 years of data
def remove_extra_data(file, folder_to_build, folder_to_use):
    df = pd.read_csv(f"../Storage/{folder_to_use}/{file}", index_col=[0])

    if df.shape[0] > 731:
        df = df.iloc[-731:]

    df.to_csv(f"../Storage/{folder_to_build}/{file}")

check_and_run_operation("Companies_data_in_range", "Companies_more_than_2_months_data", "REMOVE EXTRA DATA FROM CSVS", remove_extra_data)

# Adding Company name and Exchange to the csvs
def add_company_name_and_exchange(file, folder_to_build, folder_to_use):
    df = pd.read_csv(f"../Storage/{folder_to_use}/{file}", index_col=[0])

    df["Company"] = file[:-7]
    df["Exchange"] = file[-7:-4]

    df.to_csv(f"../Storage/{folder_to_build}/{file}")

check_and_run_operation("Companies_with_name_and_exchange", "Companies_data_in_range", "ADDING NAME AND EXCHANGE DATA TO COMPANY CSVS", add_company_name_and_exchange)

def create_bollinger_bands(file, folder_to_build, folder_to_use):
    df = pd.read_csv(f"../Storage/{folder_to_use}/{file}", index_col=[0])

    df["SMA20"] = df["Close"].rolling(window=20, min_periods=1).mean()

    sigma = df["Close"].rolling(window=20, min_periods=1).std()
    sigma[0] = sigma[1]

    df["SMA20_Upper_std1"] = df["SMA20"] + sigma
    df["SMA20_Upper_std2"] = df["SMA20"] + (sigma * 2)
    df["SMA20_Upper_std3"] = df["SMA20"] + (sigma * 3)

    df["SMA20_Lower_std1"] = df["SMA20"] - sigma
    df["SMA20_Lower_std2"] = df["SMA20"] - (sigma * 2)
    df["SMA20_Lower_std3"] = df["SMA20"] - (sigma * 3)

    df.to_csv(f"../Storage/{folder_to_build}/{file}")

check_and_run_operation("Companies_with_bollinger_bands", "Companies_with_name_and_exchange", "ADDING BOLLINGER BANDS DATA TO ALL COMPANY CSVS", create_bollinger_bands)

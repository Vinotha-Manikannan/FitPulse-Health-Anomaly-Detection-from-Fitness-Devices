import pandas as pd


BASE_PATH = "FitPulse Health Anomaly Detection from Fitness Devices/Milestone1/data"

def preprocess_data():
    print("Starting preprocessing...")

    hr = pd.read_csv(f"{BASE_PATH}/heartrate.csv")
    steps = pd.read_csv(f"{BASE_PATH}/steps.csv")
    sleep = pd.read_csv(f"{BASE_PATH}/sleep.csv")

    hr["Time"] = pd.to_datetime(hr["Time"], utc=True)
    steps["ActivityMinute"] = pd.to_datetime(steps["ActivityMinute"], utc=True)
    sleep["SleepDay"] = pd.to_datetime(sleep["SleepDay"], utc=True)

    hr = hr.rename(columns={
        "Time": "timestamp",
        "Value": "heart_rate"
    })

    steps = steps.rename(columns={
        "ActivityMinute": "timestamp",
        "Steps": "steps"
    })

    sleep = sleep.rename(columns={
        "SleepDay": "timestamp",
        "TotalMinutesAsleep": "sleep"
    })

 
    steps["steps"] = steps["steps"].fillna(0)
    sleep["sleep"] = sleep["sleep"].fillna(0)

    hr = hr.dropna(subset=["timestamp"])

   
    hr_1min = (
        hr
        .groupby(["Id", pd.Grouper(key="timestamp", freq="1min")])["heart_rate"]
        .mean()
        .reset_index()
    )


    final_df = hr_1min.merge(
        steps[["Id", "timestamp", "steps"]],
        on=["Id", "timestamp"],
        how="left"
    )

    final_df = final_df.merge(
        sleep[["Id", "timestamp", "sleep"]],
        on=["Id", "timestamp"],
        how="left"
    )

    final_df["steps"] = final_df["steps"].fillna(0)
    final_df["sleep"] = final_df["sleep"].fillna(0)

   
    final_df = final_df.sort_values(["Id", "timestamp"])

  
    final_df.to_csv(f"{BASE_PATH}/cleaned_dataset.csv", index=False)

    print("Preprocessing completed successfully!")
    print("Cleaned dataset saved as cleaned_dataset.csv")

if __name__ == "__main__":
    preprocess_data()


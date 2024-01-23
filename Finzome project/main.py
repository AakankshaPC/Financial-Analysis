from fastapi import FastAPI, File, UploadFile, HTTPException, Form
import glob
import pandas as pd
from io import BytesIO



app = FastAPI()

def calculate_volatility(df):
    # Calculate Daily Returns
    df['Daily Returns'] = df['Close'].pct_change()

    # Calculate Daily Volatility
    daily_volatility = df['Daily Returns'].std()

    # Calculate Annualized Volatility
    annualized_volatility = daily_volatility * (252 ** 0.5)  # Assuming 252 trading days in a year

    return daily_volatility, annualized_volatility


@app.post("/compute_volatility")
async def compute_volatility(
    file: UploadFile = File(None),
    directory_path: str = Form(None)
):
    if file is None and directory_path is None:
        raise HTTPException(status_code=400, detail="Either provide a file or a directory path.")

    if file:
        # Read data from the uploaded CSV file
        content = await file.read()
        ohlc_data = pd.read_csv(BytesIO(content), parse_dates=['Date'])
    elif directory_path:
        # Read data from CSV files in the specified directory
        ohlc_data = pd.concat([pd.read_csv(f, parse_dates=['Date']) for f in glob.glob(f"{directory_path}/*.csv")])

    # Calculate volatility
    daily_volatility, annualized_volatility = calculate_volatility(ohlc_data)

    return {"daily_volatility": daily_volatility, "annualized_volatility": annualized_volatility}
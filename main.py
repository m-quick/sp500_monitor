import pandas_datareader.data as web
import pandas as pd
import seaborn as sns
import datetime
import matplotlib.pyplot as plt


def get_returns(
    from_date: datetime.date = datetime.date(2023, 1, 1),
    to_date: datetime.date = datetime.date.today(),
) -> None:
    index_price = web.DataReader(["sp500"], "fred", from_date, to_date)
    index_price = (
        index_price.reset_index()
        .dropna(subset=["sp500"])
        .rename(columns={"sp500": "closing_price"})
    )
    index_price["pct_change_total"] = (
        (index_price["closing_price"] - index_price["closing_price"].iloc[0])
        / index_price["closing_price"].iloc[0]
        * 100
    )
    index_price.to_csv("S&P500_latest.csv", index=False)
    price_chart = sns.lineplot(data=index_price, x="DATE", y="pct_change_total")
    plt.savefig("S&P500_returns.jpg")


if __name__ == "__main__":
    get_returns()

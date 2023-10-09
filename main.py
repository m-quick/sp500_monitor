import pandas_datareader.data as web
import pandas as pd
import seaborn as sns
import datetime
import matplotlib.pyplot as plt


def get_returns(
    from_date: datetime.date = datetime.date(2023, 4, 14),
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

    plt.figure(figsize=(20, 10))
    price_chart = sns.lineplot(data=index_price, x="DATE", y="pct_change_total")
    price_chart.axhline(y=0, linewidth=2, color="orange", ls=":")
    plt.xticks(rotation=45)
    price_chart.set(xlabel=" ", ylabel="Percent return")
    plt.fill_between(
        index_price["DATE"],
        index_price["pct_change_total"],
        0,
        where=(index_price["pct_change_total"] >= 0),
        interpolate=True,
        color="green",
        alpha=0.5,
    )
    plt.fill_between(
        index_price["DATE"],
        index_price["pct_change_total"],
        0,
        where=(index_price["pct_change_total"] < 0),
        interpolate=True,
        color="red",
        alpha=0.5,
    )
    plt.savefig("S&P500_returns.jpg")


if __name__ == "__main__":
    get_returns()

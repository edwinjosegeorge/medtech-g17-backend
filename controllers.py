import pickle
from datetime import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta


def forcast_drug(drug_name: str, end_date: datetime.date) -> dict:
    label_encoder = pickle.load(open("data/le.pickle.dat", 'rb'))
    code = label_encoder.transform([drug_name])

    start_date = datetime.now().date()
    delta = relativedelta(end_date, start_date)
    month_count = delta.years * 12 + delta.months

    codes: list[int] = []
    years: list[int] = []
    months: list[int] = []

    year = start_date.year
    month = start_date.month

    for _ in range(month_count):
        years.append(year)
        months.append(month)
        codes.append(code)

        month += 1
        if month == 13:
            month = 1
            year += 1

    model = pickle.load(open("data/GBRegressor.pickle.dat", 'rb'))
    ddf = pd.DataFrame({"year": years, "month": months, "drug": codes})
    values = model.predict(ddf)
    values = list(values * 1.3)  # add bias

    return {
        'name': drug_name,
        'forecast': [x + 1 for x, _ in enumerate(months)],
        'data': values,
    }

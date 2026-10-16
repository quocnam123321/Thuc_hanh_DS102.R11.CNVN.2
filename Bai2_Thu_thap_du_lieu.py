from io import StringIO
import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

headers = {
    "User-Agent": "NamNguyen-Bai2/1.0 (educational project)"
}

response = requests.get(url, headers=headers, timeout=30)
response.raise_for_status()

tables = pd.read_html(StringIO(response.text), match="Location")
data = tables[0].copy()

columns = []

for column in data.columns:
    if isinstance(column, tuple):
        column_name = " ".join(str(part) for part in column)
    else:
        column_name = str(column)

    columns.append(column_name.strip())

data.columns = columns

location_column = next(
    column for column in data.columns if column.startswith("Location")
)
population_column = next(
    column for column in data.columns if column.startswith("Population")
)

data = data[
    data[location_column].astype(str).str.strip() != "World"
].copy()

data[population_column] = (
    data[population_column]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace(r"\[.*?\]", "", regex=True)
    .str.strip()
)

data[population_column] = pd.to_numeric(
    data[population_column],
    errors="coerce"
)

data = data.dropna(subset=[population_column])
data = data.drop_duplicates(subset=[location_column])

if len(data) < 100:
    raise ValueError(f"Chỉ lấy được {len(data)} bản ghi, cần ít nhất 100.")

data.to_csv("population_data.csv", index=False, encoding="utf-8-sig")
data.to_csv(
    "population_data.tsv",
    sep="\t",
    index=False,
    encoding="utf-8-sig"
)
data.to_json(
    "population_data.json",
    orient="records",
    force_ascii=False,
    indent=2
)

largest = data.loc[data[population_column].idxmax()]
smallest = data.loc[data[population_column].idxmin()]

print("Số bản ghi:", len(data))
print("Số cột:", len(data.columns))
print("Tên các cột:", list(data.columns))
print("Dân số trung bình:", round(data[population_column].mean()))
print(
    "Dân số cao nhất:",
    largest[location_column],
    "-", int(largest[population_column])
)
print(
    "Dân số thấp nhất:",
    smallest[location_column],
    "-", int(smallest[population_column])
)

print("\nĐã lưu population_data.csv, population_data.tsv và population_data.json")
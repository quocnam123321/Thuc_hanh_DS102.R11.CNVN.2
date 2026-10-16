# Thuc_hanh_DS102.R11.CNVN.2

## Tên: Nguyễn Quốc Nam

## MSSV: 24521118

## Bài thực hành 01

## Bài 1 – Tìm điểm cực trị

Dùng NumPy và phương pháp Newton–Raphson để tìm điểm cực trị của hàm số:
\[
f(x,y)=2(x-1)^2+2(x-1)(y+2)+2(y+2)^2
\]
Kết quả: điểm cực tiểu (1, -2), giá trị hàm số 0.

## Bài 2 – Thu thập dữ liệu

Thu thập dữ liệu dân số từ Wikipedia: https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population (hoặc xem trang nguồn: [List of countries and dependencies by population](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population)). Làm sạch dữ liệu bằng pandas và lưu thành CSV, TSV, JSON.
Bộ dữ liệu cần có ít nhất 100 bản ghi. Báo cáo mô tả và thống kê được nộp riêng.

Các tệp dữ liệu đầu ra: [population_data.csv](https://github.com/quocnam123321/Thuc_hanh_DS102.R11.CNVN.2/blob/main/population_data.csv), [population_data.tsv](https://github.com/quocnam123321/Thuc_hanh_DS102.R11.CNVN.2/blob/main/population_data.tsv), [population_data.json](https://github.com/quocnam123321/Thuc_hanh_DS102.R11.CNVN.2/blob/main/population_data.json)

## Cách chạy

python -m pip install numpy requests pandas lxml openpyxl
python bai1.py
python bai2.py

import xlrd

excel_data_file = xlrd.open_workbook("./DATA.xlsx")
sheet = excel_data_file.sheet_by_index(0)

batch_Names_wanted = []
row_number = sheet.nrows


if row_number:
    for row in range(0, row_number):
        batch_Names_wanted.append(
            str(sheet.row(row)[0])
            .replace("text:", "")
            .replace("'", "")
            .replace(":", "")
            .replace(".", "")
        )
    print("Количество запрашиваемых пакетов:", len(batch_Names_wanted))
else:
    print("Excel файл с данными пустой или заполнен неверно")

print("\n".join(batch_Names_wanted))


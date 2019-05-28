import xlsxwriter
def export_to_excel(data, filename):
    """
    Exports data to excel
    :param data: Data to be exported to excel file(Should be in list, a main list containing row data in separate lists)
    :param filename: Filename for the exported data file(Without extension)
    :return: response after sending email
    """
    success = False
    try:
        workbook = xlsxwriter.Workbook(filename + '.xlsx')
        worksheet = workbook.add_worksheet()

        # # Data format.
        # expenses = (
        #     ['Reent', 1000],
        #     ['Gas', 100],
        #     ['Food', 300],
        #     ['Gym', 50],
        # )

        row = 0
        col = 0

        # Iterate over the data and write it out row by row.
        for each_row in data:
            for each_column in each_row:
                worksheet.write(row, col, each_column)
                col += 1
            col = 0
            row += 1

        workbook.close()
        success = True
        return success
    except:
        return success

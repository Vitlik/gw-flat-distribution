from openpyxl import load_workbook


def save_data(file, list_allocations, max_happiness):
    print("Starting save.")
    wb = load_workbook(file)

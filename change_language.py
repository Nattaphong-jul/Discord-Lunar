import pandas as pd
def language_change(text):
    sheet_id = "1-fohOO-giNMncCy5oLKHrfrxVY4_moaoWkvb2v9BuJQ"
    sheet_name = "Language_Change"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url)
    converted = ""
    for i in text:
        try:
            if i in df['Eng'].tolist():
                converted = converted + str(df['Thai'][df['Eng'].tolist().index(i)])
            elif i in df['Shift_Eng'].tolist():
                converted = converted + str(df['Shift_Thai'][df['Shift_Eng'].tolist().index(i)])
            elif i == " ":
                converted = converted + " "
            else:
                converted = converted + i
                
        except:
            continue
    return converted
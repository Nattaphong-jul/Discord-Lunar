import pandas as pd
def language_change(text: str):
    sheet_id = "1-fohOO-giNMncCy5oLKHrfrxVY4_moaoWkvb2v9BuJQ"
    sheet_name = "Language_Change"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url)
    converted = ""
    for i in str(text):
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

def language_change_th(text: str):
    sheet_id = "1-fohOO-giNMncCy5oLKHrfrxVY4_moaoWkvb2v9BuJQ"
    sheet_name = "Language_Change"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url)
    converted = ""
    for i in str(text):
        try:
            if i in df['Thai'].tolist():
                converted = converted + str(df['Eng'][df['Thai'].tolist().index(i)])
            elif i in df['Shift_Eng'].tolist():
                converted = converted + str(df['Shift_Eng'][df['Shift_Thai'].tolist().index(i)])
            elif i == " ":
                converted = converted + " "
            else:
                converted = converted + i
                
        except:
            continue
    return converted
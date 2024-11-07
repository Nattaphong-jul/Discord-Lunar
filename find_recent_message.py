import pandas as pd
def find_recent(server, channel):
    log = pd.read_csv('log.csv')
    last_index = len(log['Server']) - 2
    while last_index >= 0:
        if log['Server'][last_index] == server and log['Channel'][last_index] == channel:
            return log['Message'][last_index]
        last_index -= 1
    return 'หนูหาข้อความไม่เจออ่ะคะ'
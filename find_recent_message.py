import pandas as pd
def find_recent(server: str, channel: str):
    log = pd.read_csv('log.csv').astype(str)
    find = 1
    while find < log.shape[0]:
        print(-find)
        if log.iloc[-find]['Server'] == server and log.iloc[-find]['Channel'] == channel:
            return log.iloc[-find]['Message']
        find += 1

    return 'หนูหาข้อความไม่เจออ่ะคะ'

# print(find_recent('Lunaar', 'bot-test'))
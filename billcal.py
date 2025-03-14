def calculate_bill():
    import pandas as pd
    sheet_id = "1y8rZlKght5j9bNIxx9lbTGQc7CQa_YiUUIHV-CIO2nM"
    sheet_name = "Bill"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    bill = pd.read_csv(url) # Read google sheet
    # print(bill)

    member = set([name for i in bill['People Name'].to_list() for name in i.split()])
    # print(member)

    menu = bill['Menu'].to_list()
    # print(menu)

    def round_up(num: float):
        if num - int(num) > 0:
            return int(num) + 1
        return int(num)

    all_total = 0
    calculated_result = ""
    for n in member:
        result = f"**__{n}__**"
        total = 0 # reset total to be 0
        for i in range(len(menu)):
            divider = len(bill['People Name'][i].split())
            if n in bill['People Name'][i].split():
                price = round_up((bill['Price'][i] * int(bill['Amount'][i])) / divider) # If the price have decimal, price + 1

                result = f"{result}\n-# {str(bill['Menu'][i])[0:20]}: {int(price)}" # Limit the menu name to be <= 20 char
                total = total + price

        if bill['Additional'][0] != 0: # Check if any additional cost
            additional = round_up(bill['Additional'][0]/len(member))
            result = f"{result}\n-# Additional: {additional}"
            total = total + additional # Add the additional value ex.VAT to the total
        all_total = all_total + total
        result = f"{result}\n**Total**: {total}\n{"-"*20}"
        calculated_result = calculated_result + result + '\n'
    calculated_result = calculated_result + f"**Grand Total** = {all_total + bill['Additional'][0]}\n-# Any decimal amount in the bill will be rounded up"

    return calculated_result
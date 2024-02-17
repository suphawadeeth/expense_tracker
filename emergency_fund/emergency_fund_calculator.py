import pandas as pd
import datetime as dt 

def emergency_fund_calculator(name):
    df = pd.read_csv(f'{name}.csv')
    df = df[df["category"].str.contains('Savings|Investments',regex=True) == False] # drop the "Savings & Investments" if any
    df['date'] = pd.to_datetime(df['date']) #change data into the datetime type
    df['year_month'] = df['date'].dt.to_period('M').astype(str) #extract YYYY-MM 
    df = df[df['date'] < dt.date.today().strftime("%Y-%m")] #filter all data except current month
    avg_monthly = df.groupby(['year_month']).sum().mean() #calculate average amount
    
    fam_status = input("""Enter a number that describes your status: \n
    '1' single with no dependents & a stable income \n 
    '2' married & both have a stable income \n 
    '3' married with a single income/single parent\n 
    '4' irregular income/your job is seasonal \n 
    '5' someone in your home is chronically ill \n 
    '6' you or your partner is self-employed, works on commision, has a irregular income \n 
    """)
    
    if fam_status in ['1','2']:
        emerg_fund = avg_monthly*3
    else:
        emerg_fund = avg_monthly*6
    
    print("YOUR EMERGENCY FUND: ", emerg_fund)

    return emerg_fund


emergency_fund_calculator(name='test')
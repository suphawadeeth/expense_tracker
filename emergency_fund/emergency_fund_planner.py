# import libraries
import pandas as pd
import datetime as dt
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
import os

def emergency_fund_calculator():
    
    """
    This function will calculate your emergency fund based on your expenses and your situation. 
    As a result, the user will receive the amount they should have for their emergency fund.
    """
    
    name = input('Enter your name: ')
    
    df = pd.read_csv(f'{name}.csv')
    df = df[df["category"].str.contains("Savings & Investments") == False] # drop the "Savings & Investments" if any
    df['date'] = pd.to_datetime(df['date']) #change data into the datetime type
    df['year_month'] = df['date'].dt.to_period('M').astype(str) #extract YYYY-MM 
    df = df[df['date'] < dt.date.today().strftime("%Y-%m")] #filter all data except current month
    avg_monthly = df.groupby(['year_month']).sum().mean() #calculate average amount each category
    
    fam_status = input("""Enter a number that describes your status: \n
    '1' single with no dependents & a stable income \n 
    '2' married & both have a stable income \n 
    '3' married with a single income/single parent\n 
    '4' irregular income/your job is seasonal \n 
    '5' someone in your home is chronically ill \n 
    '6' you or your partner is self-employed, works on commision, has a irregular income \n 
    """)
    
    if fam_status in ['1','2']:
        em_goal = avg_monthly*3
    else:
        em_goal = avg_monthly*6
    
    print("YOUR EMERGENCY FUND GOAL: ", em_goal)

    return em_goal

def emerg_fund_status():
    em_goal = float(emergency_fund_calculator())
    base_amount = input("""
        Enter the current balance in your emergency fund account: 
        Enter '0' if the emergency fund is not set up:
        """)
    base_amount = float(base_amount)
    diff = float(em_goal-base_amount)
    if diff < 0:
        diff = -(diff)
        position = 'Exceed (+)'
        diff_color = "#fecb52"
        base_amount = em_goal
        balance = 'Fund Filled'
    else:
        position = 'Shortened (-)'
        diff_color = "#e45756"
        balance = 'Balance'
    data = [['Goal',em_goal,'set'], [f'{balance}',base_amount,'active'], [f'{position}',diff,'active']]
    df = pd.DataFrame(data, columns=['type','amount','status'])
    grouped = df[df["status"].str.contains("set")==False]

    # create subdirectory, for saving plot images
    if not os.path.exists("images"):
        os.mkdir("images")

    # create bar plot
    fig = px.bar(grouped, x="amount", y="status", color='type', orientation='h',
                 hover_data=["type"],
                 height=250, 
                 title='Emergency Fund Status',
                 labels={'amount':'Amount',
                         'status':'Status',
                         'type':''
                        },
                 color_discrete_sequence=["#00cc96", f"{diff_color}"]
                )
    fig.update_yaxes(visible=False, showticklabels=False)
    fig.add_vline(x=f"{em_goal}", line_width=3, line_dash="dash", line_color="#b68100")
    fig.write_html("images/fig1.html")
    fig.write_image("images/fig1.png")
    fig.show()
    return em_goal, base_amount

def emerg_saving_plan(diff, em_goal):
    if diff > 0:
        while True:
            n_months = input('Enter number of months you aim to hit the goal: ')
            saving_amount_per_mouth = round(em_goal/int(n_months))
            print(f"\n In the next {n_months} months, you will save '{saving_amount_per_mouth}' aside for your emergency fund each month")
            accept = input("""
            Enter '1' to ACCEPT this plan 
            Enter '2' to ADJUST the plan
            """)
            if accept == '1':
                print(f"""
                Your GOAL:
                - have '{em_goal}' in your emergency fund account

                Your PLAN:
                - save '{saving_amount_per_mouth}' every month, for the next {n_months} months
                """)
                break
            else:
                continue
        else:
            pass
def emerg_fund_planner(em_goal, base_amount):
    diff = em_goal-base_amount
    if diff > 0:
        emerg_saving_plan(diff, em_goal)
    else:
        print('Congratulations! You have successfully built your emergency fund!')

def main():
    em_goal, base_amount = emerg_fund_status()
    emerg_fund_planner(em_goal, base_amount)
main()
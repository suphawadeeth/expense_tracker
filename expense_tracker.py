# import libraries
import pandas as pd
import plotly.express as px
import datetime as dt
import sqlalchemy as alch
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import warnings
warnings.filterwarnings('ignore')


def date_str_validate():
    """
    Validate date format from user's input
    """
    while True:
        date = input("Enter the date (YYYY-MM-DD) or 'today': ")
        if date == 'today':
            date = dt.date.today()
            break
        try: 
            date = dt.date.fromisoformat(date)
            break
        except:
            print("Incorrect data format, should be YYYY-MM-DD")
            continue
    return date

def cumulative_expenses():

    """
    THIS FUNCTION ASK USER FOR DATE, DESCRIPTION ON WHAT THEY'VE SPENT, AND AMOUNT OF EXPENSE.
    EACH ITEM WILL BE SORTED INTO CATEGORY AND STORED IN A DATAFRAME.
    """
    
    try:
        name = input("Your name: ")
        df = pd.read_csv(f"{name}.csv")  
    except:
        df = pd.DataFrame(columns=['date', 'description', 'category', 'amount'])
    
    recent_data = pd.DataFrame(columns=['date','description','category','amount'])
    
    while True:
        date = date_str_validate()

        desc = input("What have you spent on? ")
        if desc in ['cloth', 'watch', 'shoes', 'shirt', 'pants','skirt', 'dress', 'hat']:
            cat = 'Shopping'
        elif desc in ['lidl', 'kaufland', 'food', 'veggies', 'meat', 'eggs', 'milk', 'aldi', 'edeka', 'rewe', 'penny', 'netto']:
            cat = 'Food & Grocery'
        elif desc in ['meals', 'meal', 'drink','coffee','bakery', 'cake']:
            cat = 'Bar & Restaurants'
        elif desc in ['bus', 'flight','train','taxi']:
            cat = 'Transport & Car'
        elif desc in ['rent', 'apartment']:
            cat = 'Rent'
        elif desc in ['stock','fund','bond','investment','invest','Scalable Capital','Trade Republic','scalable','trade republic']:
            cat = 'Investments'
        elif desc in ['emergency fund','saving']:
            cat = 'Savings'
        elif desc in ['withdraw', 'cash']:
            cat = 'Cash'
        elif desc in ['ATM']:
            cat = 'ATM'
        elif desc in ['accommodation','room','hostel','hotel', 'airbnb']:
            cat = 'Travel'
        elif desc in ['internet']:
            cat = 'Household & Utilities'
        elif desc in ['rossmann', 'dm', 'mueller']:
            cat = 'Healthcare & Drug' 
        elif desc in ['book', 'journal', 'notebook', 'study', 'course','seminar','coaching']:
            cat = 'Personal Development' 
        elif desc in ['donation']:
            cat = 'Giving'       
        else:
            cat = 'Other'
            
        amount = float(input("How much did you spend? "))
        data = [[date, desc, cat, amount]]
        new_df = pd.DataFrame(data, columns=['date','description','category','amount'])
        recent_data = pd.concat([recent_data, new_df], ignore_index=True)
        df = df.append(new_df, ignore_index = True)
        done = input('Type "done" when finish or "else" to add more items >> ')   
        if done == 'done':
            break   
        else:
            continue
            
    df.to_csv(f"{name}.csv", index=False)
    
    print("LASTEST FIVE EXPENSES: \n",df.tail(5),"\nGood day! "+name+"\nNEWLY ADDED ITEM(S): \n",recent_data)

    return df, recent_data, name

def analyze_expense(df):
    
    """
    THIS FUNCTION TAKE DATAFRAME AND SUMMARIZE THE CUSTUMER'S EXPENSES MONTHLY/YEARLY
    """
    
    df['date'] = pd.to_datetime(df['date']) #change data into the datetime type
    df['year_month'] = df['date'].dt.to_period('M').astype(str) #extract YYYY-MM 
    df['year'] = df['date'].dt.strftime('%Y') #extract year
    grouped_m = round(df.groupby(['category']).mean(),2).sort_values('amount',ascending=False) #calculate monthly average amount each category
    grouped_y_sum = round(df.groupby(['year','category']).sum(),2).sort_values(['year','amount'],ascending=True).reset_index()
    cat_names = grouped_m.reset_index() #after calculate, we'll list the category names ranked by the amount of expenses
    cat_names = cat_names['category'].values.tolist() #get the category names
    
    # create 'images' directoy, for saving images from plotting
    if not os.path.exists("images"):
        os.mkdir("images")

    # monthly expenses
    fig = px.pie(grouped_m, values='amount', 
                 names = cat_names, color=cat_names,
                 title="Average Monthly Expenses")
    fig.show()
    fig.write_html("images/fig1.html")
    
    # total expenses (so far)
    fig = px.bar(df, x='year_month', y='amount', color='category',
                 labels={'amount':'Total Amount',
                        'year_month':'Date'},
                 title='Montly Total Expenses',)
    fig.show()
    fig.write_html("images/fig2.html")
    
    # yearly expenses
    fig = px.bar(grouped_y_sum, x='year', y='amount', color='category',
                labels={'amount':'Amount', 'year':'Year'},
                title="Yearly Total Expenses by Category")
    fig.show()
    fig.write_html("images/fig3.html")

#### Write data on SQL server
# set up environment
load_dotenv()
user, sql_password = os.getenv('user'), os.getenv('sql_password')
db_name = 'budget'
connection_data = f"mysql+pymysql://{user}:{sql_password}@localhost/{db_name}"
engine = alch.create_engine(connection_data)
cur = engine.connect()

def write_to_sql(df, name, recent_data=None):
    
    """
    USER'S EXPENSES DATA WILL BE STORED IN A SQL DATABASE UNDER USER'S NAME
    """
        
    # create a table in the database if not exists
    cur.execute(text(
    f"""
    CREATE TABLE IF NOT EXISTS {name} (
    id INTEGER PRIMARY KEY,
    date DATE,
    description TEXT,
    category TEXT,
    amount FLOAT);
    """))
    
    # write data to SQL database
    try:
        new_df.to_sql(f'{name}', con=engine, if_exists='append', chunksize=2000, index=False)
    except:
        df.to_sql(f'{name}', con=engine, if_exists='replace', chunksize=2000, index=False)


def main():
    action = input("""
    Enter '1' to ADD expense \n
    Enter '2' to VIEW your expenses:
    
    """)
    if action == '1':
        df, recent_data, name = cumulative_expenses()
        write_to_sql(df, name, recent_data)
        analyze_expense(df)
    else:
        try:
            name = input("Your name: ")
            df = pd.read_csv(f'{name}.csv')
        except:
            df = pd.DataFrame(columns=['date','description','category','amount'])
        analyze_expense(df)

main()
# Expense Tracker
Expense Tracker is a simple Python program designed to empower users to meticulously record every dollar spent on their expenses.

## Why?
The underlying motivation behind developing Expense Tracker is the recognition that effective money management is integral to financial well-being. Often, the primary reason people face financial challenges is due to a lack of proper money management.

Highlighting the importance of financial planning, keeping track of your expenses stems from the fact that budgeting is one of the top 5 habits seen in millionaires.

### The Path to Wealth
Planning your budget serves as a crucial step on the path to wealth. Before amassing a fortune, it is essential to have a clear understanding of your current financial standing.

## Features
Expense Tracker functions by consistently recording your expenses over time and providing insightful analyses of your spending patterns. By summarizing your expenses on a monthly and yearly basis, this program aims to assist you in:

- **Understanding Your Spending Habits**: Gain insights into your financial behavior.
- **Identifying Expense Categories**: Clearly visualize where your money is being allocated.
- **Raising Awareness**: Foster an awareness of your spending habits, serving as the first step towards making informed adjustments.

## How It Works
1. **Input Your Expenses**: Log every expenditure, providing details such as date, description, category, and amount.
2. **Monthly and Yearly Summaries**: Obtain comprehensive breakdowns of your spending at regular intervals.
3. **Visual Analytics**: Utilize graphical representations to better understand your financial trends.

## Example Snapshot

Here's a glimpse of what using Expense Tracker looks like:

![Expense Tracker Analytics](https://github.com/suphawadeeth/expense_tracker/blob/master/monthly_exp_pie.png)
*Caption: Visual analytics and breakdown of your expenses*

### Monthly Chart
![Monthly Chart](https://github.com/suphawadeeth/expense_tracker/blob/master/monthly_exp_bar.png)
*Caption: Analyze your monthly spending patterns with a bar chart.*

### Yearly Chart
![Yearly Chart](https://github.com/suphawadeeth/expense_tracker/blob/master/yearly_tot_exp_bar.png)
*Caption: Gain insights into your yearly expenses through a bar chart.*

This example snapshot illustrates the user interface and some of the features you can expect when using the Expense Tracker. Feel free to explore the app and track your expenses with ease!

## Future Plans

The next step in this project is to develop a Budget Planning App, which will not only track expenses but also help users plan their budgets effectively. The Budget Planning App will include features such as:

- Income tracking
- Expense categorization
- Budget goal setting
- Real-time tracking against budget goals
- Insights and suggestions for better financial planning

Stay tuned for more updates and enhancements to help you take control of your finances!

## How to Use

To get started, you can use the example spending record file 'myexpenses.csv' provided in this repository. Simply input 'myexpenses' when prompted for 'Your name:'.

The program allows users to start from zero records, and it will record expenses under their specified name. Since this is designed as a personal expense tracker, it saves data as a CSV file locally on your machine.

**Usage Steps:**
1. Clone or download this repository to your local machine.
2. Run the Expense Tracker program.
3. Input your name when prompted for 'Your name:' to start recording your spending and follow the steps.
   - Alternatively, input 'myexpenses' when prompted for 'Your name:' to use the example spending record to see how this works.
4. Explore the features of the program, analyze your spending habits, and gain insights into your expenses.


## Future Development

The current version of the Expense Tracker is designed for personal use, saving data as a CSV file locally. The next steps in development include connecting to an SQL database for more complex and long-term data storage. Please note that this feature is currently undergoing development and is not yet complete.

Feel free to experiment with the example record and provide feedback or contribute to the ongoing development.

**Update History:**
**2024/02/15:**
- Implemented a connection to the SQL database (completed).
- Developed the Emergency Fund Calculator as part of this project; it is now completed and ready for use.

**2024/02/17:**
- Introduced the Emergency Fund Planner (completed).
   - This feature provides users with an overview of their fund status, as illustrated in the examples below:

      - **Case 1: Successful Emergency Fund Build**
      ```markdown
      ![Status Bar|Case 1](https://github.com/suphawadeeth/expense_tracker/blob/master/yearly_tot_exp_bar.png)
      *Caption: The user has successfully built the emergency fund (labeled as exceed +), surpassing the set goal. The dashed line indicates the emergency fund goal, calculated based on their expenses.*
      ```

      - **Case 2: Emergency Fund Status Below Goal**
      ```markdown
      ![Status Bar|Case 2](https://github.com/suphawadeeth/expense_tracker/blob/master/yearly_tot_exp_bar.png)
      *Caption: The user's emergency fund balance is below the goal (dashed line). The plot displays the current balance and the shortened amount needed to reach the goal (labeled as shortened -). This visualization helps users plan to achieve their financial objectives.*
      ```

Next steps:
- design a budget app that allow user to plan their budget every month


## Let's Connect and Collaborate!

I am open to suggestions, collaborations, and discussions with fellow developers, data analysts, data scientists, and anyone passionate about data. Let's connect and help each other grow! Feel free to reach out through the following channels:

- **LinkedIn**: [Connect on LinkedIn](https://www.linkedin.com/in/bunthot/)
- **Email**: Drop me a message at bunthot.su(at)proton.me

Whether you have feedback, ideas, or just want to chat about data-related topics, I look forward to hearing from you. Let's build and learn together!

Cheers!
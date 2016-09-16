# FinanceWebApp
This is the web-version of the C# Finance Application I was in the process of creating.
Currently the application is connected to a postgreSQL database hosted by Heroku.

You can find the web application at:
	https://financewebapp.herokuapp.com
with sample login credentials:
username: admin
password: admin
* Web app may not be up-to-date

Features:
- Based on the user who is logged in, there is a custom Watchlist that displays the companies that the user
is following and the ask and bid prices with a 15 minute delay. The information is pulled from Yahoo Finance.

Reminders for myself:
- Make sure to have virtual environment turned on by running this command:
      source venv/bin/activate
- Make sure to set APP_SETTINGS and DATABASE_URL local environment variable when starting up terminal each time by running these commands:
      export APP_SETTINGS="config.DevelopmentConfig"
      export DATABASE_URL="postgresql://localhost/financewebapp_dev"
- To run the app locally, use this command:
      python manage.py runserver
- psql database name is financewebapp_dev. Use \c to connect and \d to view
- Add comments!!!

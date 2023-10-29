import smtplib
import datetime as dt

my_email = "adhrinclips4@gmail.com"
password = "fzfluixxechixsfx"

# A list of who you want to send the email to
to_emails = ["dipesh.ifpatel@gmail.com", "nirupa.d.patel@gmail.com", "bunciedp@gmail.com", "dhruvdp.2004@gmail.com"]

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = days_of_week[day_of_week]
print(day)



subject = f"Happy {day}!"
message = f"Hope you have a great day! \n\n test"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_emails,
        msg=f"Subject: {subject}\n\n Dear Fam, \n\n {message}")
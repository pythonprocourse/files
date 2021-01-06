Title: Automated Emails
Description: An app that reads user names, email addresses, and interests from an Excel file and sends an email to each user
with news feeds about the user's interest every morning.
Objects: ExcelFile:
            filepath
            get_data()
         Email:
             sender
             receiver
             subject
             body
             send()
         NewsFeed:
            data
            get()

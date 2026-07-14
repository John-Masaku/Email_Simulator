# 📧 Python Email System

A simple object-oriented email simulation built in Python.

## Features

- Create users
- Send emails
- Receive emails
- Read emails
- Delete emails
- Email timestamps
- Read/Unread status
- Inbox management

## Project Structure

```
email_system.py
```

## Classes

### Email

Represents an email message.

Attributes

- sender
- receiver
- subject
- body
- timestamp
- read

### User

Represents a system user.

Methods

- send_email()
- check_inbox()
- read_email()
- delete_email()

### Inbox

Stores and manages received emails.

Methods

- receive_email()
- list_emails()
- read_email()
- delete_email()

## Example Output

```
Email sent from Tory to Ramy!

Email sent from Ramy to Tory!

Ramy's Inbox:

Your Emails:
1. [Unread] From: Tory | Subject: Hello | Time: 2026-07-14 10:30

--- Email ---
From: Tory
To: Ramy
Subject: Hello
Received: 2026-07-14 10:30
Body: Hi Ramy, just saying hello!
------------

Email deleted.

Ramy's Inbox:
Your inbox is empty.
```

## Concepts Used

- Classes
- Objects
- Methods
- Composition
- Encapsulation
- Lists
- String formatting
- datetime module

import datetime
#Core Email and User classes for the Email Simulator application.
class Email:
    # Creates a new email with sender, receiver, subject and body.
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    # Marks the email as read.
    def mark_as_read(self):
        self.read = True

    # Displays the full email details.
    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    # Returns a short summary used when listing emails.
    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
    
# Inbox Management

# Stores and manages emails received by a user.
class Inbox:
    # Creates an empty inbox.
    def __init__(self):
        self.emails = []

    # Adds a received email to the inbox.
    def receive_email(self, email):
        self.emails.append(email)

    # Displays all emails in the inbox.
    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return

        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    # Opens and displays a selected email.
    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return

        actual_index = index - 1

        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        self.emails[actual_index].display_full_email()

    # Deletes an email from the inbox.
    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return

        actual_index = index - 1

        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        del self.emails[actual_index]
        print('Email deleted.\n')

        
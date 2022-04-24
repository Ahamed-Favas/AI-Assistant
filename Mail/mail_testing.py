import imaplib
import email
from cryptography.fernet import Fernet
import sys
imap_server = "imap.gmail.com"
file1 = open(r'username.txt', 'r')
file2 = open(r'password.txt', 'r')
content_list1 = file1.readlines()
content_list2 = file2.readlines()

username = content_list1[0]
password = content_list2[0]

print("Username", username)
print("Password", password)
password = bytes(password, encoding='utf-8')
print(password)
key = Fernet.generate_key()


# password = bytes(password, encoding='utf-8')
r = Fernet(key)
# token = r.encrypt(password)
# print(token)
test1=r.decrypt(password)
print(test1)
mail  = imaplib.IMAP4_SSL('imap.gmail.com')
(retcode, capabilities) = mail.login(username,test1.decode('utf-8'))
mail.list()
mail.select('inbox')

n=0
(retcode, messages) = mail.search(None, '(UNSEEN)')
if retcode == 'OK':

    for num in messages[0].split() :
        print('Processing ')
        n=n+1
        typ, data = mail.fetch(num,'(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                original = email.message_from_bytes(data[0][1])

                print (original['From'])
                print (original['Subject'])
                typ, data = mail.store(num,'+FLAGS','\\Seen')

print(n)
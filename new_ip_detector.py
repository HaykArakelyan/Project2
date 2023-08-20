import os
import subprocess
import smtplib
from email.mime.text import MIMEText

def get_new_ips(existing_ips):
        res = subprocess.run('grep "Failed" /var/log/auth.log | awk \'{print $(NF-3)}\' | sort | uniq', shell=True, capture_output=True, text=True)
        current_ips = set(res.stdout.strip().splitlines())

        new_ips = current_ips - existing_ips

        return new_ips


def send_email(new_ips):
    email = 'hayk.arakelyan.cloud@gmail.com'
    password = 'utdnrceffqvuydll'

    msg = MIMEText('New IP detected:\n\n ' + '\n'.join(new_ips))
    msg['Subject'] = 'New IP Detected!!!'
    msg['From'] = email
    msg['To'] = email


    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, msg.as_string())
        print('Email send!!!')
    except Exception as e:
        print('Failed to send and Email ', e)


existing_ips = set()

if os.path.exists('existing_ips.txt'):
    with open('existing_ips.txt', 'r') as existing_ips_file:
        existing_ips = set(existing_ips_file.read().splitlines())


new_ips = get_new_ips(existing_ips)

if new_ips:
    print('There are NEW IP addresses: ', new_ips)
    send_email(new_ips)
    with open('existing_ips.txt', 'w') as new_ips_file:
        new_ips_file.write('\n'.join(existing_ips.union(new_ips)))
else:
    print("There are NO new IP addresses!")

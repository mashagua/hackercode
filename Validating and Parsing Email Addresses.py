import email.utils
import re
x= [input() for i in range(int(input()))]
for i in range(len(x)):
    email_valid=email.utils.parseaddr(x[i])
    if isinstance(email_valid,tuple):
        if re.match('[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$',email_valid[1]):
            print(email.utils.formataddr(email_valid))

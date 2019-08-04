#THIS is test
with open("hello1.py") as fh:
    count = 0
    text = fh.read()
    for character in text:
        if character.isupper():
            count += 1
print(count)

print(7/2)
print(7//2)

abc = 1,000,000
#a b c = 1000 2000 3000
a,b,c = 1000, 2000, 3000
a_b_c = 1,000,000

class XError(Exception): pass

try:
    if '1' != 1:
        raise XError("someError")
    else:
        print("someError has not occured")
except XError:
    print("someError has occured")

import numpy as np
arr = np.array([1, 3, 2, 4, 5])
arr1 = arr.argsort()
print(arr1[-3:][::-1])

from django.http import HttpResponse
import datetime

def Current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html> % now"
    return HttpResponse(html)

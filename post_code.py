import re
zip_code = "1234567"
pattern = r'^/d{7}$'
if re.match(pattern, zip_code):
    print("OK")
else:
    print("NG")

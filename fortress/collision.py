import requests

pdf1 = requests.get("http://localhost:8888/1-pdf.320")
pdf2 = requests.get("http://localhost:8888/2-pdf.320")

params = {'user' : pdf1.content, 'pass' : pdf2.content}

r = requests.get("http://temple.fortress:7331/t3mple_0f_y0ur_51n5.php/", params=params)
print(r.text)

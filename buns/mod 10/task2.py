import re
import requests

def getting_list_of_subheadings(link):
    content=requests.get(link).text
    sample=re.compile(r"<h3.*?>(.*?)<\/h3>")
    subheadings=sample.findall(content)
    return subheadings

list_of_subheadings = getting_list_of_subheadings("http://www.columbia.edu/~fdc/sample.html")
print(list_of_subheadings)
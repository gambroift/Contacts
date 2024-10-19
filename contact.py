import pandas as pd
from bs4 import BeautifulSoup


# Open the HTML file
with open("contacts.html", "r", encoding="utf-8") as file:
    # Read the file's content
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "lxml")  # or "html.parser"

# Now you can access and manipulate the content
#print(soup.prettify())

entries = soup.find_all("div", class_="entry clearfix")
phone_number=[]
label=[]
first_name=[]
last_name=[]
for entry in entries:
    # Extract the contact's initials, name, and details
    
    full_name = entry.find("div", class_="name bold").text.strip()
    phone = entry.find("div", class_="details_entry details").text.strip()
    phone_number.append(int(phone.replace(" ", "")[-10:])) # Remove empty spaces and save only 10 digit of phone number (my case)
    label.append("cell phone")
    name_parts = full_name.split(" ", 1)  # Split by the first space
    first_name.append(name_parts[0])
    last_name.append(name_parts[1] if len(name_parts) > 1 else "") # Nothing if there is no surname

    
    
df = pd.read_csv('empty.csv')
df['First Name'] = first_name
df['Last Name'] = last_name
df['Phone 1 - Label'] = label
df['Phone 1 - Value'] = phone_number

df.to_csv("contacts.csv", index=False)

print("DataFrame saved to 'contacts.csv'")


logo = """

            ,.,   '          ,·'´¨;.  '                                   ,.,   '               ,. –  - .,  °              , ·. ,.-·~·.,   ‘               ,.         ,·´'; '  
          ;´   '· .,         ;   ';:\           .·´¨';\                 ;´   '· .,             ';_,.., _     '`. '         /  ·'´,.-·-.,   `,'‚          ;'´*´ ,'\       ,'  ';'\° 
        .´  .-,    ';\      ;     ';:'\      .'´     ;:'\              .´  .-,    ';\            \:::::::::::';   ,'\       /  .'´\:::::::'\   '\ °        ;    ';::\      ;  ;::'\ 
       /   /:\:';   ;:'\'    ;   ,  '·:;  .·´,.´';  ,'::;'             /   /:\:';   ;:'\'           '\_;::;:,·´  .·´::\‘  ,·'  ,'::::\:;:-·-:';  ';\‚       ;      '\;'      ;  ;:::; 
     ,'  ,'::::'\';  ;::';   ;   ;'`.    ¨,.·´::;'  ;:::;            ,'  ,'::::'\';  ;::';               , '´ .·´:::::;'   ;.   ';:::;´       ,'  ,':'\‚     ,'  ,'`\   \      ;  ;:::; 
 ,.-·'  '·~^*'´¨,  ';::;   ;  ';::; \*´\:::::;  ,':::;‘        ,.-·'  '·~^*'´¨,  ';::;             .´  .'::::::;·´'     ';   ;::;       ,'´ .'´\::';‚    ;  ;::;'\  '\    ;  ;:::;  
 ':,  ,·:²*´¨¯'`;  ;::';  ';  ,'::;   \::\;:·';  ;:::; '        ':,  ,·:²*´¨¯'`;  ;::';         .·´ ,·´:::::;·´         ';   ':;:   ,.·´,.·´::::\;'°   ;  ;:::;  '\  '\ ,'  ;:::;'  
 ,'  / \::::::::';  ;::';  ;  ';::;     '*´  ;',·':::;‘          ,'  / \::::::::';  ;::';      ,·´  .´;::–·~^*'´';\‚      \·,   `*´,.·'´::::::;·´     ,' ,'::;'     '\   ¨ ,'\::;'   
,' ,'::::\·²*'´¨¯':,'\:;   \´¨\::;          \¨\::::;          ,' ,'::::\·²*'´¨¯':,'\:;       '.,_ ,. -·~:*'´¨¯:\:\ °    \\:¯::\:::::::;:·´        ;.'\::;        \`*´\::\; °  
\`¨\:::/          \::\'    '\::\;            \:\;·'           \`¨\:::/          \::\'        \:::::::::::::::::::\;       `\:::::\;::·'´  °         \:::\'          '\:::\:' '    
 '\::\;'            '\;'  '    '´¨               ¨'              '\::\;'            '\;'  '       \:;_;::-·~^*'´¨¯'             ¯                      \:'             `*´'‚      
   `¨'                                                          `¨'                                                           ‘                                                


"""
print(logo)

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Function to extract the price from the product page
def get_amazon_price(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the price element - this might need to be adjusted based on the actual HTML structure
    price_element = soup.find(id='priceblock_ourprice') or soup.find(id='priceblock_dealprice')
    if price_element:
        price = price_element.get_text()
        return float(price.replace('$', '').replace(',', '').strip())
    return None


# Function to send an email notification
def send_email(to_email, from_email, from_password, subject, body):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.send_message(msg)
    server.quit()


# Amazon product URL
url = 'https://www.amazon.com/dp/YOUR_PRODUCT_ID'
# Headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Email settings
to_email = 'mkamilleo2004@gmail.com'
from_email = 'mkamilleo2004@gmail.com'
from_password = 'xyz'
subject = 'Amazon Price Drop Alert!'

# Price threshold
price_threshold = 300.0  # Adjust to your desired price

# Check the price
current_price = get_amazon_price(url, headers)
if current_price and current_price < price_threshold:
    body = f'The price for the product has dropped to ${current_price}. Check it out at {url}'
    send_email(to_email, from_email, from_password, subject, body)
    print("Email sent!")
else:
    print("No price drop detected or could not fetch the price.")

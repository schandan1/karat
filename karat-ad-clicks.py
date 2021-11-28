completed_purchase_user_ids = ["3123122444","234111110", "8321125440", "99911063"]

ad_clicks = [
#"IP_Address,Time,Ad_Text",
"122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
"96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
"122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
"82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
"92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
"122.121.0.155,2017-01-01 03:18:55,Buy wool coats for your pets",
"92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

all_user_ips = [
#"User_ID,IP_Address",
"2339985511,122.121.0.155",
"234111110,122.121.0.1",
"3123122444,92.130.6.145",
"39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
"8321125440,82.1.106.8",
"99911063,92.130.6.144"
]

"""
Expected output:
1 of 2 2017 Pet Mittens
0 of 1 The Best Hollywood Coats
3 of 4 Buy wool coats for your pets
"""
from collections import defaultdict

def find_clicks():
    user_to_ip = defaultdict(str)
    for user_ip in all_user_ips:
        user, ip = user_ip.split(",")
        user_to_ip[user] = ip

    purchased_ips = []
    for user in completed_purchase_user_ids:
        purchased_ips.append(user_to_ip[user])

    ad_clicked = defaultdict(int)
    ad_purchased = defaultdict(int)

    for ad_click in ad_clicks:
        ip, date, ad = ad_click.split(",")
        ad_clicked[ad] += 1
        if ip in purchased_ips:
            ad_purchased[ad] += 1

    for k,v in ad_clicked.items():
        print(f"{ad_purchased[k]} of {v}  {k}")

find_clicks()


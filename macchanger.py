import subprocess #Subprocess Linux komutlarını kullanma
try:
    print("""
#---------------------------------------------------------------------#
#    _     _____   _  _____   ____ ___ ____ _     _____               #
#   / \   |__  /  / \|_   _| |  _ \_ _/ ___| |   | ____|              #
#  / _ \    / /  / _ \ | |   | | | | | |   | |   |  _|                #
# / ___ \  / /_ / ___ \| |   | |_| | | |___| |___| |___               #
#/_/   \_\/____/_/   \_\_|   |____/___\____|_____|_____|              #
#                                                                     #
# __  __    _    ____    ____ _   _    _    _   _  ____ _____ ____    #
#|  \/  |  / \  / ___|  / ___| | | |  / \  | \ | |/ ___| ____|  _ \   #
#| |\/| | / _ \| |     | |   | |_| | / _ \ |  \| | |  _|  _| | |_) |  #
#| |  | |/ ___ \ |___  | |___|  _  |/ ___ \| |\  | |_| | |___|  _ <   #
#|_|  |_/_/   \_\____|  \____|_| |_/_/   \_\_| \_|\____|_____|_| \_\  #
#---------------------------------------------------------------------#
                   @azatdicle Bu bir denemedir
""")
    print("Orginal ip:1 / Fake ip:2")
    a=int(input("Secenek:"))
    if a==1:
       subprocess.call(['ifconfig','eth0','down'])
       subprocess.call(['ifconfig','eth0','hw','ether','00:20:7d:de:45:c8'])
       subprocess.call(['ifconfig','eth0','up'])
       subprocess.call(['ifconfig'])
    elif a==2:
       subprocess.call(['ifconfig','eth0','down'])
       subprocess.call(['ifconfig','eth0','hw','ether','88:30:40:50:70'])
       subprocess.call(['ifconfig','eth0','up'])
       subprocess.call(['ifconfig'])
    else:
       print("Hatalı İslem")
except: #Hatayı yazdır
    print("Harf değil sayı Giriniz")

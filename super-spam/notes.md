# Super-Spam

## Initial info

General Uvilix:

Good Morning! Our intel tells us that he has returned. Super-spam, the evil alien villain from the planet Alpha Solaris IV from the outer reaches of the Andromeda Galaxy. He is a most wanted notorious cosmos hacker who has made it his lifetime mission to attack every Linux server possible on his journey to a Linux-free galaxy. As an avid Windows proponent, Super-spam has now arrived on Earth and has managed to hack into OUR Linux machine in pursuit of his ultimate goal. We must regain control of our server before it's too late! Find a way to hack back in to discover his next evil plan for total Windows domination! Beware, super-spam's evil powers are to confuse and deter his victims.

## Recon

### Nmap
```
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Home :: Super-Spam
|_http-generator: concrete5 - 8.5.2
|_http-server-header: Apache/2.4.29 (Ubuntu)
4012/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 86:60:04:c0:a5:36:46:67:f5:c7:24:0f:df:d0:03:14 (RSA)
|   256 ce:d2:f6:ab:69:7f:aa:31:f5:49:70:e5:8f:62:b0:b7 (ECDSA)
|_  256 73:a0:a1:97:c4:33:fb:f4:4a:5c:77:f6:ac:95:76:ac (ED25519)
4019/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxr-xr-x    2 ftp      ftp          4096 Feb 20  2021 IDS_logs
|_-rw-r--r--    1 ftp      ftp           526 Feb 20  2021 note.txt
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.6.66.15
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
5901/tcp open  vnc     VNC (protocol 3.8)
| vnc-info:
|   Protocol version: 3.8
|   Security types:
|     VNC Authentication (2)
|     Tight (16)
|   Tight auth subtypes:
|_    STDV VNCAUTH_ (2)
6001/tcp open  X11     (access denied)
Service Info: OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.14 seconds
```
## Findings
### FTP Server on port 4019
Contains 3 files:
- note.txt
- quicknote.txt
- SamsNetwork.cap

### File content
note.txt hints:
- Unusual activity in IDS
- Activity occurs around midnight
- New blog??? 

quicknote.txt hints:
- .cap file shows how to get in

.cap file analysis:
- File doesn't show anything useful in wireshark
- Running `aircrack-ng SamsNetwork.cap -w rockyou.txt`
    - Key found: sandiago
### Exploits
Initial foothold:
- Step 1: 
From the `.cap` file we can extract the password sandiago which is then used on the user `Donald_Dump`.

- Step 2:
Concrete5 is vulnerable to RCE after `php` file types have been allowed.
A php revshell can then be uploaded.
[POC](https://hackerone.com/reports/768322)

- Step 3:
from `/home/lucy_loser/.MessagesBackupToGalactic` we find a bunch of `xor-ed` images. `$$L3qwert30kcool` stands out from `d.png`. After a while I find that it's the ssh password for `donalddump`.

- Step 4:
After logging-in as donalddump via ssh.

-Step 5: We can't access /home/donalddump so we `chmod 777 /home/donalddump`.

-Step 6: We find a `passwd` file in /home/donaldump. At first I tought is was the `/etc/passwd` file but it turns out it's the passwd file to a vnc connection that leads us to a root shell

- Step 7: read /root/.nothing/r00t.txt
```

what am i?: MZWGCZ33NF2GKZKLMRRHKPJ5NBVEWNWCU5MXKVLVG4WTMTS7PU======

KRUGS4ZANFZSA3TPOQQG65TFOIQSAWLPOUQG2YLZEBUGC5TFEBZWC5TFMQQHS33VOIQGEZLMN53GKZBAOBWGC3TFOQQHI2DJOMQHI2LNMUWCASDBMNVWK4RNNVQW4LBAMJ2XIICJEB3WS3DMEBRGKIDCMFRWWIDXNF2GQIDBEBRGSZ3HMVZCYIDNN5ZGKIDEMFZXIYLSMRWHSIDQNRQW4IDUN4QGOZLUEBZGSZBAN5TCA5DIMF2CA2LOMZSXE2LPOIQG64DFOJQXI2LOM4QHG6LTORSW2LBAJRUW45LYFYQA====
```
Base32 encoded

- Step 8: profit

### Users
- adam
- super-spam
- Adam_Admin
- Donald_Dump
- Benjamin_Blogger

### Credz
- Donald_Dump : sandiago
- donalddump (ssh) : $$L3qwert30kcool
## Questions
```
What CMS and version is being used? (format: wordpress x.x.x)
```
> concrete5 8.5.2
```
What is the user flag?
```
> flag{-eteKc=skineogyls45«ey?t+du8}
```
What type of encryption did super-spam use to send his encrypted messages?
```
> xor
```
What key information was embedded in one of super-spam's encrypted messages?
```
> \$\$L3qwert30kcool
```
What is the root flag?
```
> flag{iteeKdbu==hjK6§YuUu7-6N_} 

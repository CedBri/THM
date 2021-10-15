```PORT      STATE SERVICE     VERSION
22/tcp    open  ssh         (protocol 2.0)
| fingerprint-strings:
|   NULL:
|_    SSH-2.0-OpenSSH_8.2p1 THM{946219583339}
| ssh-hostkey:
|   3072 da:5f:69:e2:11:1f:7c:66:80:89:61:54:e8:7b:16:f3 (RSA)
|   256 3f:8c:09:46:ab:1c:df:d7:35:83:cf:6d:6e:17:7e:1c (ECDSA)
|_  256 ed:a9:3a:aa:4c:6b:16:e6:0d:43:75:46:fb:33:b2:29 (ED25519)
80/tcp    open  http        lighttpd
|_http-server-header: lighttpd THM{web_server_25352}
|_http-title: Hello, world!
139/tcp   open  netbios-ssn Samba smbd 4.6.2
445/tcp   open  netbios-ssn Samba smbd 4.6.2
8080/tcp  open  http        Node.js (Express middleware)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
10021/tcp open  ftp         vsftpd 3.0.3
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port22-TCP:V=7.92%I=7%D=10/15%Time=61698CC5%P=x86_64-pc-linux-gnu%r(NUL
SF:L,29,"SSH-2\.0-OpenSSH_8\.2p1\x20THM{946219583339}\r\n");
Service Info: OS: Unix

Host script results:
|_clock-skew: 2s
|_nbstat: NetBIOS name: NETSEC-CHALLENG, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-time:
|   date: 2021-10-15T14:14:38
|_  start_date: N/A
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled but not required
```
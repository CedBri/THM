Creation date: <%+ tp.file.creation_date("YYYY-MM-DD HH:mm") %>
Last modification: <%+ tp.file.last_modified_date("YYYY-MM-DD HH:mm") %>

# Lockdown
---
```bash
export IP="10.10.144.77"
```

## Initial info
---
Deploy the machine attached to this task and find the flags.

Banner © pngtree.com.

### DNS 
---
```
contacttracer.thm
```
## Recon
---

### Nmap
---
```PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 27:1d:c5:8a:0b:bc:02:c0:f0:f1:f5:5a:d1:ff:a4:63 (RSA)
|   256 ce:f7:60:29:52:4f:65:b1:20:02:0a:2d:07:40:fd:bf (ECDSA)
|_  256 a5:b5:5a:40:13:b0:0f:b6:5a:5f:21:60:71:6f:45:2e (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
| http-cookie-flags:
|   /:
|     PHPSESSID:
|_      httponly flag not set
|_http-title: Coronavirus Contact Tracer
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
### Feroxbuster
---

## Findings
---
**contacttracer.thm**

We can bypass the admin login with `admin' OR 1=1 -- -`. At this point we can guess the website is SQLi vulnerable.

## Exploits
---
### Initial foothold
We can SQLi the `eid` parameter from `?page=reports&eid=&...`. We can also upload a php revshell by using the admin image field. By using the SQLi we can find the path of our revshell and trigger it using the link provided in the SQLi dump.

### SSH to cyrus
We just copy our id_rsa.pub to `authorized_keys` to get ssh access instead of a shitty unstable revshell :)

### Privesc
We don't quite get privesc, but we can read `root.txt` by creating a clamav rule in `/var/lib/clamav` .

We can create the following rule to scan `/root/root.txt` and the copy it's content to `/home/cyrus/quarantine/root.txt`.

```yara
rule root{
	strings:
		$s = "thm" nocase
	condition:
		$s
}
```

## Credz
---
From `/var/www/html/classes/DBConnection.php` we get the credz to the mysql DB, then with those credz we get the admin hash `3eba6f73c19818c36ba8fea761a3ce6d` which cracks to `sweetpandemonium`. This password is reused for user `cyrus`
### Potential users
`cyrus`
`maxine`
`root`

### User/pass
`cyrus:sweetpandemonium`
## Questions
> What is the user flag?

THM{w4c1F5AuUNhHCJRtiGtRqZyp0QJDIbWS}

> What is the root flag?

THM{IQ23Em4VGX91cvxsIzatpUvrW9GZZJxm}

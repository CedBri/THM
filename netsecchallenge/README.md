# Net Sec Challenge

Practice the skills you have learned in the Network Security module.

## Task 1  Introduction
For this task all the questions about the ports are answered using the [[nmap]] results.

> What is the highest port number being open less than 10,000?

8080

> There is an open port outside the common 1000 ports; it is above 10,000. What is it?

10021

> How many TCP ports are open?

6

> What is the flag hidden in the HTTP server header?

Running `curl http://$IP` we get `Server: lighttpd THM{web_server_25352}`

> What is the flag hidden in the SSH server header?

We can get the flag by reading the [[nmap]] output. THM{946219583339}

> We have an FTP server listening on a nonstandard port. What is the version of the FTP server?

vsftpd 3.0.3

> We learned two usernames using social engineering: `eddie` and `quinn`. What is the flag hidden in one of these two account files and accessible via FTP?

By running `hydra -L userlist.txt -P rockyou.txt ftp://$IP:10021` we can quickly see that eddie's password is `jordan` and that quinn's password is `andrea`.

Then if we login as Quinn, we get `ftp_flag.txt` which contains THM{321452667098}

> Browsing to `http://10.10.146.143:8080` displays a small challenge that will give you a flag once you solve it. What is the flag?

By running `nmap -f -sN $IP` we get the flag THM{f7443f99}
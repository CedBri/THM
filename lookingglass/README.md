# Looking Glass
Creation date: <%+ tp.file.creation_date("YYYY-MM-DD HH:mm") %>

`IP=10.10.167.93`

## Initial info
---
Climb through the Looking Glass and capture the flags.


## Recon
---
### Nmap:
[[nmap]]
## Findings
---
We have ports from 9000 to 13991 that are open.
When we connection via ssh to one of the ports, we get a "higher" or "lower" response. To connect we use `ssh -o "StricHostKeyChecking=no" $IP -p $PORT`. By bruteforcing manually we find that port 12505 is the port giving us the next clue.

When connecting to it we get 
```
You've found the real service.
Solve the challenge to get access to the box
Jabberwocky
'Mdes mgplmmz, cvs alv lsmtsn aowil
Fqs ncix hrd rxtbmi bp bwl arul;
Elw bpmtc pgzt alv uvvordcet,
Egf bwl qffl vaewz ovxztiql.

'Fvphve ewl Jbfugzlvgb, ff woy!
Ioe kepu bwhx sbai, tst jlbal vppa grmjl!
Bplhrf xag Rjinlu imro, pud tlnp
Bwl jintmofh Iaohxtachxta!'

Oi tzdr hjw oqzehp jpvvd tc oaoh:
Eqvv amdx ale xpuxpqx hwt oi jhbkhe--
Hv rfwmgl wl fp moi Tfbaun xkgm,
Puh jmvsd lloimi bp bwvyxaa.

Eno pz io yyhqho xyhbkhe wl sushf,
Bwl Nruiirhdjk, xmmj mnlw fy mpaxt,
Jani pjqumpzgn xhcdbgi xag bjskvr dsoo,
Pud cykdttk ej ba gaxt!

Vnf, xpq! Wcl, xnh! Hrd ewyovka cvs alihbkh
Ewl vpvict qseux dine huidoxt-achgb!
Al peqi pt eitf, ick azmo mtd wlae
Lx ymca krebqpsxug cevm.

'Ick lrla xhzj zlbmg vpt Qesulvwzrr?
Cpqx vw bf eifz, qy mthmjwa dwn!
V jitinofh kaz! Gtntdvl! Ttspaj!'
Wl ciskvttk me apw jzn.

'Awbw utqasmx, tuh tst zljxaa bdcij
Wph gjgl aoh zkuqsi zg ale hpie;
Bpe oqbzc nxyi tst iosszqdtz,
Eew ale xdte semja dbxxkhfe.
Jdbr tivtmi pw sxderpIoeKeudmgdstd

```
It's a vigenere cipher which decodes to this [[solved poem]].

We then enter the secret and get : `jabberwock:SettleLightlyWaitedCurious
`
## Exploits
---
After logging in as jabberwock using linpeas we can find that `@reboot tweedledum bash /home/jabberwock/twasBrillig.sh` get run on every reboot as tweedledum. We can modify `twasBrillig.sh` to spawn a revshell and then reboot the box.

After catching the revshell and loging in as tweedledum, we can read the file `humptydumpty.txt` which is just an hex encoded file that decodes as as a bunch of giberish that ends with `the password is zyxwvutsrqponmlk`

We can then `su - humptydumpty` using that password. After enumerating some stuff I found we can can `Alice`'s id_rsa'.

After loging in as **Alice** and enumerating again with linpeas I didn't get much. After reading /etc/sudoers.d we finally see a path to root.

`sudo -h ssalg-gnikool /bin/bash` and **BOOM** root!


## Creds
---
jabberwock:KnocksBushesCrumpledExperiment

### Potential users
---

### User/Pass
---

## Questions
---

> Get the user flag.

> Get the root flag.
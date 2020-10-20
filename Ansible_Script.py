R1:
config t
hostname R1
int fa0/0
no shutdown
ip add 192.168.122.82 255.255.255.0

R2:
config t
hostname R2
int fa0/0
no shutdown
ip add 192.168.122.83 255.255.255.0

R3:
config t
hostname R3
int fa0/0
no shutdown
ip add 192.168.122.84 255.255.255.0

SW1:
config t
hostname SW1
int g0/0
no shutdown
no sw
ip add 192.168.122.91 255.255.255.0


SW2:
config t
hostname SW2
int g0/0
no shutdown
no sw
ip add 192.168.122.92 255.255.255.0

Network (Ansible):

nano ansible.cfg

[defaults]
inventory = ./myhosts
host_key_checking = false
timeout = 15
deprecation-warning=false
==============================================
nano myhosts
[routers]
R1
R2
R3
[switches]
SW1
SW2
===================================================
nano /etc/hosts
192.168.122.82  R1
192.168.122.83  R2
192.168.122.84  R3
192.168.122.91  SW1
192.168.122.92  SW2

cat /etc/hosts
cat ansible.cfg
cat myhosts
ansible --lists-hosts all
ansible --lists-hosts routers
ansible --lists-hosts switches
=========================================================
username hafiz password mattian
username hafiz priv 15
line vty 0 4
transport input all
login local
exit
ip domain-name hafizmatti2001.com
cry key gen rsa
1024

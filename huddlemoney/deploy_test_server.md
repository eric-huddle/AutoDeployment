# Deploy test environment user guide
This guide is used to deploy test environment automatically with vagrant and ansible in Mac OS.

## Install prerequisites

#### VirtualBox
Version: latest 
[Installation guide](https://www.virtualbox.org/wiki/Downloads)
Download *VirtualBox* installer and follow prompts to install.



#### Ansible
Version: v2.3.1.0

[Installation guide](http://docs.ansible.com/ansible/intro_installation.html)

```sh
$ brew install ansible
```

#### Vagrant
Version: v1.9.5
[Installation guide](https://www.vagrantup.com/docs/installation/)

Download the appropriate [installer](https://www.vagrantup.com/downloads.html) or [package](https://www.vagrantup.com/downloads.html) for your platform and follow the prompts.


## Setup test environment
Once you have installed the prerequisites softwares, you are ready to setup the test environment.

#### 1. Make a folder as your test environment home folder.
For example,
```sh
$ mkdir ~/huddlemoney-test1
```

#### 2. Add a template virtual box to your machine.

The template virtual boxes are those that have pre-installed some softwares like postgresql, node and so on.
The description of these boxes are:
Box Name | OS | PostgreSql | Node | Nodejs | NPM | UWSGI | Nginx |
---------|----|------------|------|--------|-----|-------|-------|
abigdream/huddlemoney-test0 | Ubuntu 16.04 Xenial | 9.5 |
abigdream/huddlemoney-test1| Ubuntu 16.04 Xenial | 9.5 | 6.11.0 | 4.2.6 | 3.10.10| 2.0.15 | 1.10.0|

**Run vagrant command to add virtual box into your machine. **
For example,
```sh
$ cd ~/huddlemoney-test1
$ vagrant box add abigdream/huddlemoney-test1
```
**Check your virtual box.**
```sh
$ vagrant box list
Apples-MacBook:testenv ericwang$ vagrant box list
abigdream/huddlemoney-test1 (virtualbox, 0.0.2)
```

#### 3. Initial and setup your virtual machine.
**Change into your test environment home folder and initial your virtual machine.**
For example,
```sh
$ cd ~/huddlemoney-test1
$ vagrant init abigdream/huddlemoney-test1
```

**Change the Virtual Box configuration.**
Run VirtualBox Manager
select [VM name]
Settings
'System' tab > Motherboard > Boor Order > [ ] Floppy (uncheck)
'Audiot' tab > [ ] Enable Audio (uncheck)
'Ports' tab > [ ] Enable Serial Port (uncheck)
OK


**Copy our code into your test environment home folder.**
```sh
$ cp huddlemoney/ ~/huddlemoney-test1/
```

**Replace the vagrantfile with our prepared vagrantfile.**
```sh
$ cp huddlemoney/roles/test-deploy-env/files/Vagrantfile  ~/huddlemoney-test1/
```

**Start up the virtual machine.**
```sh
$ vagrant up
```

#### 4. Config the connection between your virtual machine and ansible.
**Login to the virtual machind.**
```sh
$ cd ~/huddlemoney-test1/
$ vagrant ssh
```

 **Get the IP address of the virtual machine.**
```sh
$ (Virtual Machine) ifconfig
enp0s3    Link encap:Ethernet  HWaddr 02:e7:04:e9:f2:54  
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::e7:4ff:fee9:f254/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2489 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1447 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:211790 (211.7 KB)  TX bytes:161604 (161.6 KB)

enp0s8    Link encap:Ethernet  HWaddr 08:00:27:58:3c:c3  
          inet addr:172.28.128.15  Bcast:172.28.128.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fe58:3cc3/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:105 errors:0 dropped:0 overruns:0 frame:0
          TX packets:48 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:18716 (18.7 KB)  TX bytes:8574 (8.5 KB)
```
In the example above, the IP address of the virtual machine is `172.28.128.15`.

**Put the vitual machine's IP address into the Ansible inventory file.**
For example,
```sh
$ vi huddlemoney/test_servers
[test_servers]
172.28.128.15

[ansible_server]
localhost
```

**Put the IP address and domain name into the hosts file of your host machine.**
For example,
```sh
$ sudo vi /etc/hosts

172.28.128.15    test.huddle.com.au
172.28.128.15    api.test.huddle.com.au
172.28.128.15    admin.test.huddle.com.au   

```
Add the domain name above into the /etc/hosts file of your host machine. Replace the IP address with your own virtual box machine.



**Put the public key of your user into the virtual machine. The user in the virtual machine is "vagrant".**
For example,
```sh
$ pbcopy < ~/.ssh/id_rsa.pub
$ cd ~/huddlemoney-test1/
$ vagrant ssh
```
```sh
$(Virtual Machine) vi ~/.ssh/authorized_keys
```
Then, copy the public key into the ~/.ssh/authorized_keys

#### 5. Edit ansible config file.
**Define Git repo, branch and vagrant home folder**
Edit huddlemoney/group_vars/test_servers.yml
```
---
# config git repo
git_repo: git@github.com:eric-huddle/huddlemoney.git

# config git repo branch to checkout
git_repo_branch: release

# config vagrant home directory
vagrant_home_dir: /Users/ericwang/vagrant/testdeploy

# define test username (Do not modify it)
test_user: vagrant
test_user_home: /home/vagrant

# config the code destination folder
git_code_dest: "{{test_user_home}}/{{git_repo_branch}}"

# config test database
test_db_name: huddlemoneytestdb
test_db_user: huddlemoney-test-db-user
test_db_passwd: huddle123

```
`git_repo`: This is the url of your git repo. It is better to be a SSH url.
`git_repo_branch`: You can define the branch you want to check our here. 
`vagrant_home_dir`: You can define your vagrant home folder here. It is better to be a absolute path.


#### 6. Config SSH forward agent on your host machine.
Edit ~/.ssh/config in your host machine, and add configuration below into the config file.
```
host your.domain.com
    ForwardAgent yes
```
You need replace your.domain.com with either the domain or the IP address of your Vagrant virtual machine.
Once you’ve done that, just run `ssh-add` to ensure you ensure your identities are added to the SSH agent.


#### 7. Run ansible playbook to deploy test environment.
For example,
```sh
$ cd ~/huddlemoney-test1/huddlemoney
$ ansible-playbook -i test_servers deploy_test_server.yml
```


**Important, due to the fact that the huddlemoney system enabled the CORS(Cross-Origin resource sharing), if you want to access the website like http://172.28.128.15:3000 to do test, you will need to install a CORS plugin in your browser. When you want to do test, enable the plugin; when you've finished test job, disable the plugin. Or you will have some porblems when access other websites.**






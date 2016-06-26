# App Store Accounts

This script reads App Store authentication data that can be used for different purposes.

## Installation
For this to work you need a jailbroken iOS device.

* install openssh and wget from Cydia
* ssh into your device 

**default ssh password is 'alpine'. I strongly recommend you to change the dafault password.**
* install python and pip by invoking:
```
wget http://yangapp.googlecode.com/svn/debs/python_2.7.6-3_iphoneos-arm.deb && \
dpkg -i python_2.7.6-3_iphoneos-arm.deb && \
rm python_2.7.6-3_iphoneos-arm.deb && \
easy_install pip
```

* install requirements by invoking:

` pip install -r requirements.txt`

# App Store Accounts

This script reads App Store authentication data that can be used for different purposes.

Example:
```
AccountServiceTypes: 0
AccountPaidPurchasesPasswordSetting: 2
AccountSocialEnabled: False
AccountFreeDownloadsPasswordSetting: 3
AccountIsNewCustomer: False
AccountURLBagType: production
FirstName: John
LastName: Doe
DownloaderID: 0
AccountStoreFront: 143444,29 ab:9JWkzWf1
PurchaserID: 12176452568
AccountAvailableServiceTypes: 0
AccountSource: device
DidFallbackToPassword: False
AccountKind: 0
FamilyID: 0
AppleID: john.doe@gmail.com
CreditDisplayString: 
DSPersonID: 1122334455667
```


## Installation
For this to work you need a jailbroken iOS device.

* install `openssh` and `wget` from Cydia
* ssh into your device 

  **default ssh password is 'alpine'. I strongly recommend you to change the default password.**
* install python and pip by invoking:
```
  wget http://yangapp.googlecode.com/svn/debs/python_2.7.6-3_iphoneos-arm.deb && \
  dpkg -i python_2.7.6-3_iphoneos-arm.deb && \
  rm python_2.7.6-3_iphoneos-arm.deb && \
  easy_install pip
```

* install requirements by invoking:

  `pip install -r requirements.txt`

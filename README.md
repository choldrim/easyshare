#easyshare
easyshare is a share file tool for nautilus and command-line, it can sharing file easily with qrcode.

##Require
* qrcode
* bottle
* pyqt5
* python3-pil
* python-nautilus

```shell
# install qrcode, other packages was written as depends on deb pkg
sudo apt-get install python3-pip
sudo pip3 install qrcode
```

##Installation
```shell
git clone *this-project.git*
cd easyshare
dpkg-deb -b deb easyshare_1.0.deb
# install the deb package
sudo dpkg -i easyshare_1.0.deb
# if you get something wrong with dependence
# run this cmd to fix it:
# sudo apt-get install -f
```

## Or you can install manually
```shell
# install *the Require pkgs mentioned above*
# and then, run:
# sudo make install
```

##usage
### 1.nautilus
restart your nautilus if your nautilus is running
```shell
# command line way
nautilus -q ; nautilus .
```
a. choose the file you want to share
b. right-click -> easyshare


### 2.command-line
```shell
# just run easyshare + your-file directly
# eg:
easyshare your-sharing-file
```

DIY 
===

Do it Yourself (DIY) your own kivy app!

.. note::
	This guide was developed on OSX 10.9.5, python 2.7, kivy 1.8.1  

	1. brew install dpkg
	
	2. vi .bash_profile and comment this line

	#export ARCHFLAGS = "-arch x86"

1. create your app - main.py

2. save your dir in your home

```	/Users/usuario/dir
```
3. init buildozer

```	dir usuario$ buildozer init
```
4. modified the buildozer spec file

```	dir usuario$ vi buildozer.spec
```
5. create a virtualenv in your dir

```	dir usuario$ virtualenv venv --distribute
```
6. activate virtualenv

```	dir usuario$ source /venv/bin/activate
```
.. note::
	to deactivate :
	dir usuario$ deactivate

7. run buildozer - see more in : https://github.com/kivy/buildozer

```		 dir usuario$ buildozer android release
```

Signed and Zipalign
-------------------
More infos to create a signature and to zip in : https://github.com/kivy/kivy/wiki/Creating-a-Release-APK

1. change the dir

```	 dir usuario$ cd ~
```
2. Obtain a keystore 

```
	keytool -genkey -v -keystore ./keystores/<my-new-key>.keystore -alias <my-alias> -keyalg RSA -keysize 2048 -validity 10000
```
3. then signed as follows 

```
	jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ./keystores/<my-new-key>.keystore ./<my-project>/bin/<MyProject>-<version>-release-unsigned.apk <my-alias>
```
4. zip the apk already signed

```
	.buildozer/android/platform/android-sdk-21/build-tools/21.1.1/zipalign -v 4 ./<my-project>/bin/<MyProject>-<version>-release-unsigned.apk ./<my-project>/bin/<MyProject>.apk
```
.. warning:
	The zipalign script may not be in tools, but you can also find it in build-tools.

adb logcat and installation on android
--------------------------------------
1. change to dir

```	cd /Users/usuario/.buildozer/android/platform/android-sdk-21/platform-tools
```

2. install device

``` 	platform-tools usuario$ ./adb start-serve 
```

``` 	platform-tools usuario$ ./adb devices
```

3. adb install the apk on android for test

```	platform-tools usuario$ ./adb install /Users/usuario/dir/bin/<app-name>.apk
```
4. see error log

```	platform-tools usuario$ ./adb logcat
```

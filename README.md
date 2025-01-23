# adbs

---

`adbs` is a zsh plugin that provides a command `adb` for multi-device management.

# Install

clone `adbs` to your zsh plugin directory.

```
git clone https://github.com/LiushuiXiaoxia/adbs.git ~/.oh-my-zsh/custom/plugins/adbs
```

Then load as a plugin in your `.zshrc`

```
plugins+=(adbs)
```


# Usages

For example, if you want to install an app on all your devices:

```shell
# adb install
adb install -r -t app/build/outputs/apk/debug/app-debug.apk
adb: more than one device/emulator

# for adbs install
adbs install -r -t app/build/outputs/apk/debug/app-debug.apk
Executing on device: 10.23.255.111:30476, cmd: adb -s 10.23.255.111:30476 install -r -t app/build/outputs/apk/debug/app-debug.apk
Output from 10.23.255.111:30476:
Performing Streamed Install
Success

Executing on device: 10.23.255.111:37024, cmd: adb -s 10.23.255.111:37024 install -r -t app/build/outputs/apk/debug/app-debug.apk
Output from 10.23.255.111:37024:
Performing Streamed Install
Success


# adb uninstall
adb uninstall com.example.ks_demo
adb: more than one device/emulator

# for adbs uninstall
adbs uninstall com.example.ks_demo
Executing on device: 10.23.255.111:30476, cmd: adb -s 10.23.255.111:30476 uninstall com.example.ks_demo
Output from 10.23.255.111:30476:
Success

Executing on device: 10.23.255.111:37024, cmd: adb -s 10.23.255.111:37024 uninstall com.example.ks_demo
Output from 10.23.255.111:37024:
Success
```
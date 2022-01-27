#!/usr/bin/python

import os, time

for iter in xrange(5):

    adb_reboot = os.popen("sudo adb reboot")
    print(adb_reboot)
    print('[INFO] Starting Server...')
    time.sleep(15)

    adb_wait = os.popen("sudo adb wait-for-device")
    print(adb_wait)
    time.sleep(15)
    print('[INFO] Server Started! Lets Play Clash of Clans.')

    adb_device = os.popen("sudo adb devices -l")
    print(adb_device)

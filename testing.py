# import psutil
# def secs2hours(secs):
#     mm, ss = divmod(secs, 60)
#     hh, mm = divmod(mm, 60)
#     return "%d:%02d:%02d" % (hh, mm, ss)
# battery = psutil.sensors_battery()
# print("Time remaining", secs2hours(battery.secsleft))
# from ctypes import cast, POINTER
# import wmi
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# print(round(volume.GetMasterVolumeLevelScalar()*100))
# print(wmi.WMI(namespace='wmi').WmiMonitorBrightness()[0].CurrentBrightness)
# def secs2hours(secs):
#     mm, ss = divmod(secs, 60)
#     hh, mm = divmod(mm, 60)
#     # return "%d:%02d:%02d" % (hh, mm, ss)
#     return "%0dhours and %02d minutes" % (hh, mm)

# print(secs2hours(6000))
from main import initialisation
initialisation()
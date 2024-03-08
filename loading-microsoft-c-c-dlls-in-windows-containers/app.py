import ctypes

mydll = ctypes.CDLL('./lib/MyDLL.dll')

mydll.hello_world()

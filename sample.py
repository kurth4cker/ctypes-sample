import ctypes

libdouble = ctypes.cdll.LoadLibrary("libdouble.so")
print(libdouble.doubly(2))

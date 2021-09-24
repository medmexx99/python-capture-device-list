from distutils.core import setup, Extension

module_device = Extension('device',
                        sources = ['device.cpp'], 
                        # library_dirs=['C:\\Program Files\Microsoft SDKs\Windows\v6.1\Lib']
                        #library_dirs=[r'D:\\Windows Kits\10\\Lib\\10.0.19041.0\\um\\x64']
                      )

setup (name = 'WindowsDevices',
        version = '1.0',
        description = 'Get device list with DirectShow',
        ext_modules = [module_device])

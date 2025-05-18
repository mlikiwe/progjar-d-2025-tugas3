import os
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        os.chdir('files/')

    def list(self,params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK',data=filelist)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def get(self,params=[]):
        try:
            filename = params[0]
            if (filename == ''):
                return None
            fp = open(f"{filename}",'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK',data_namafile=filename,data_file=isifile)
        except Exception as e:
            return dict(status='ERROR',data=str(e))
        
    def upload(self, params=[]):
        try:
            filename = params[0]
            filedata_b64 = params[1]
            if filename == '' or filedata_b64 == '':
                return dict(status='ERROR', data='Filename or file data is empty')
            missing_padding = len(filedata_b64) % 4
            if missing_padding != 0:
                filedata_b64 += '=' * (4 - missing_padding)
            filedata = base64.b64decode(filedata_b64)
            with open(filename, 'wb') as f:
                f.write(filedata)
            return dict(status='OK', data_namafile=filename)
        except Exception as e:
            return dict(status='ERROR', data=str(e))
        
    def delete(self, params=[]):
        try:
            filename = params[0]
            if filename == '':
                return dict(status='ERROR', data='Filename is empty')
            if os.path.exists(filename):
                os.remove(filename)
                return dict(status='OK', data=f'File {filename} deleted successfully')
            else:
                return dict(status='ERROR', data=f'File {filename} not found')
        except Exception as e:
            return dict(status='ERROR', data=str(e))



if __name__=='__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))
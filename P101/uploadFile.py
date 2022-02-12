import dropbox

class TransferData(object):
     def __init__(self, accessToken):
        self.accessToken=accessToken
    
    def uploadFile(root, dirs, files, file_from, file_to, local_path, dropbox):
       for root, dirs, files in os.walk(file_from)
       relative_path= os.path.relpath(local_path, file_from)
       dropbox_path= os.path.join(file_to, relative_path)
       with open(local_path, 'rb') af f:
           dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    accessToken=accessToken
    transferdata1= Transferdata(accessToken)
    file_from=input("Enter the file to be transfered: ")
    file_to=input("Enter the destination of the path in dropbox: ")
    transferdata1.uploadFile(file_from, file_to)


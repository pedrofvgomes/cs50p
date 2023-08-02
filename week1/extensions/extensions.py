s = input('File name: ')
s = s.lower().replace(' ', '')

if s[-4:] == '.gif':
    print('image/gif')

elif s[-4:] == '.zip':
    print('application/zip')

elif s[-4:] == '.txt':
    print('text/plain')

elif s[-4:] == '.pdf':
    print('application/pdf')

elif s[-4:] == '.png':
    print('image/png')

elif s[-4:] == '.jpg':
    print('image/jpeg')

elif s[-5:] == '.jpeg':
    print('image/jpeg')

else:
    print('application/octet-stream')
''' I need to get the suffix of the file name to determine file_type I then need
to match the suffix with a media_type ex. image/jpeg case insensitive with the
following types:
.gif .jpg .jpeg .png .pdf .txt .zip
use catch _ for catch-all application/octet-stream'''


def main():


    # ask user for name of file
    file_name = input('Whats the name of your file? ')

    case_insensitive = file_name.lower().strip()


    #define file types using find type will be >=0

    gif = case_insensitive.lower().strip().find('.gif')
    jpg = case_insensitive.lower().strip().find('.jpg')
    jpeg = case_insensitive.lower().strip().find('.jpeg')
    png = case_insensitive.lower().strip().find('.png')
    pdf = case_insensitive.lower().strip().find('.pdf')
    txt = case_insensitive.lower().strip().find('.txt')
    zip =case_insensitive.lower().strip().find('.zip')






    if gif >= 0:
        print('image/gif')
    elif jpg  >=0 or jpeg >=0:
        print('image/jpeg')
    elif png >= 0:
        print('image/png')
    elif pdf >= 0:
        print('application/pdf')
    elif txt >= 0:
        print('text/plain')
    elif zip >= 0:
        print('application/zip')
    else:
        print('application/octet-stream')







main()
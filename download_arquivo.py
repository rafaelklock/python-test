"""

This program downloads files from the Internet.
Esse programa faz download de arquivos da Internet.

Rafael Klock - kklockk@gmail.com

"""

# coding: utf-8
import io  # need this lib to write in disc
import sys  # need this lib to pass the parameters
import urllib.request as request

BUFF_SIZE = 1024


def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Download {}".format((((time * BUFF_SIZE)/length)*100)))


def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Download {bytes}'.format(bytes=total_downloaded))


def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("saida.zip", mode="w")

    content_length = response.getheader('Content_length')
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)
    
    response.close()
    out_file.close()
    print("Finished")


if __name__ == "__main__":
    main()

from pytube import YouTube

def select_resolution():
    resolutions = ['highest', '1080p', '720p', '480p', '360p', '240p', '144p']
    res = input(
"""Select resolution from:
(0): Highest
(1): 1080p
(2): 720p
(3): 480p
(4): 360p
(5): 240p
(6): 144p
Your Selection: """
    )
    return resolutions[int(res)]

def main():

    print('Youtube Downloader Script\nCreated by: Ebrahim Maher\n');
    url = input('Enter Video Url: ')
    video = YouTube(url)
    print(video.title)

    all_streams = video.streams.filter(file_extension='mp4', progressive=True)

    download_stream = None

    while not download_stream:
        resolution = select_resolution()
        if resolution == 'highest':
            download_stream = all_streams.get_highest_resolution()
        else:
            download_stream = all_streams.get_by_resolution(resolution)
            if not download_stream:
                print("\n" + "Quality you entered is not found: " + resolution + "\n")

    # Got Stream, Download it ...
    path = input('Enter Path of directory (./videos): ')
    if (not path):
        path = './videos'

    print('Downloading video to ' + path + '...')
    download_stream.download(path)
    print('Downloaded Successfully!!')

main()
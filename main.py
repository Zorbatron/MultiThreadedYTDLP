import multiprocessing as mp
import yt_dlp
import os
from platform import system as ostype

def download_video(link, args):
    with yt_dlp.YoutubeDL(args) as ydl:
        ydl.download(link)

def main():
    try:
        if ostype() == 'Windows':
            os.system("build.bat")
            os.remove("build.sh")
        else:
            os.system("./build.sh")
            os.remove("build.bat")
    except FileNotFoundError:
        pass
    url = input("Input playlist URL\n")
    cont = True
    while cont:
        try:
            workerAmount = int(input("Input amount of videos to download in parallel\n"))

            ytdl = yt_dlp.YoutubeDL( {'extract_flat': True, 'quiet': True} )
            data = ytdl.extract_info(url, download=False)

            processes = []

            pool = mp.Pool(workerAmount)
            for block in data['entries']:
                r = pool.apply_async(download_video, args=[block['url'], {
                    #options go here
                    'outtmpl': './DownloadedVideos/%(title)s.%(ext)s'
                }])
                processes.append(r)
        except ValueError:
            continue
        else:
            cont = False
    for r in processes:
        r.wait()

    pool.close()
    pool.join()

    print("Done!")

if __name__ == '__main__':
    main()
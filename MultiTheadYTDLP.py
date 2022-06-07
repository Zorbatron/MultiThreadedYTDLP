import multiprocessing as mp
from yt_dlp import YoutubeDL

def download_video(link, args):
    with YoutubeDL(args) as ydl:
        ydl.download(link)

if __name__ == '__main__':
    url = input("Input playlist URL\n")
    workerAmount = int(input("Input amount of videos to download in parrallel\n"))

    ytdl = YoutubeDL( {'extract_flat': True, 'quiet': True} )
    data = ytdl.extract_info(url, download=False)

    processes = []

    pool = mp.Pool(workerAmount)
    for block in data['entries']:
        r = pool.apply_async(download_video, args=[block['url'], {
            #options go here
            'outtmpl': './DownloadedVideos/%(title)s.%(ext)s'
        }])
        processes.append(r)
    
    for r in processes:
        r.wait()

    pool.close()
    pool.join()

    print("Done!")
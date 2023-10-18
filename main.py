import multiprocessing as mp
import yt_dlp

def download_video(link, args):
    with yt_dlp.YoutubeDL(args) as ydl:
        ydl.download(link)

def main():
    url = input("Input playlist URL\n")
    workerAmount = int(input("Input amount of videos to download in parallel\n"))

    ytdl = yt_dlp.YoutubeDL( {'extract_flat': True, 'quiet': True} )
    data = ytdl.extract_info(url, download=False)

    processes = []

    pool = mp.Pool(workerAmount)
    for block in data['entries']:
        r = pool.apply_async(download_video, args=[block['url'], {
            #options go here
            'outtmpl': f'./DownloadedVideos/{data["title"]}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio'
        }])
        processes.append(r)

    for r in processes:
        r.wait()

    pool.close()
    pool.join()

    print("Done!")

if __name__ == '__main__':
    main()

# -------------------------- # 
#         VERSÃO  1.5        #
# -------------------------- # 
# By Dreaper - @juliofmendes



import youtube_dl
import os

# Obtém o caminho absoluto do diretório atual
path = os.path.abspath(os.path.dirname(__file__))

# Adiciona a pasta "Legendas" ao caminho
legendas_path = os.path.join(path, "Legendas")

def download_subtitle(video_url):
    ydl_opts = {
        'writesubtitles': 'best',
        'subtitlesformat': 'vtt',
        'allsubtitles': False,
        'subtitleslangs': ['pt', 'en'],
        'ignoreerrors': True,
        'nocheckcertificate': True,
        'skip_download': True,
        'outtmpl': os.path.join(legendas_path, f"%(title)s.[%(id)s].%(ext)s"),
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        playlist = ydl.extract_info(video_url, download=False)
        playlist_title = playlist.get('title', '')
        playlist_entries = playlist.get('entries', [])

        if not playlist_title or not playlist_entries:
            print("Não foi possível obter informações sobre a playlist")
            return

        for entry in playlist_entries:
            video_title = entry.get('title', '')
            video_id = entry.get('id', '')

            if not video_title or not video_id:
                continue

            subtitle_file = "{video_title}.vtt"
            ydl_opts['outtmpl'] = subtitle_file

            if not os.path.exists(legendas_path):
                os.makedirs(legendas_path)
                print(f"\n[AVISO]Diretório de legendas:\n {legendas_path}\n")

            ydl.download([video_url])
            print(f"Legenda baixada para o vídeo '{video_title}' como '{subtitle_file}'")

#video_url = input("Insira a URL da playlist: ")
video_url = "https://www.youtube.com/watch?v=3tmd-ClpJxA&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo"
download_subtitle(video_url)


# -------------------------- # 
#         F     I     M      #
# -------------------------- # 
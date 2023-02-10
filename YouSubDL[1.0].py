# -------------------------- # 
#         VERSÃO  1.0        #
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
        'subtitlesformat': 'srt',
        'outtmpl': os.path.join(legendas_path, f"%(id)s.%(ext)s"),
        'allsubtitles': False,
        'subtitleslangs': 'pt',
        'ignoreerrors': True,
        'nocheckcertificate': True,
        'skip_download': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        video_title = video_info.get('title', '')
        video_id = video_info.get('id', '')

        if not video_title or not video_id:
            print("Não foi possível obter informações sobre o vídeo")
            return

        if not os.path.exists(legendas_path):
            os.makedirs(legendas_path)
            print(f"\n[AVISO]Diretório de legendas:\n {legendas_path}\n")


        subtitle_file = "{video_title}.srt"
        ydl_opts['outtmpl'] = subtitle_file
        ydl.download([video_url])
        print(f"Legenda baixada para o vídeo '{video_title}' como '{subtitle_file}'")



video_url = input("Insira a URL do vídeo: ")
#video_url = "https://www.youtube.com/watch?v=Vnc0TX6Vias"
download_subtitle(video_url)


# -------------------------- # 
#         F     I     M      #
# -------------------------- # 
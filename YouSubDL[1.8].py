# -------------------------- # 
#         VERSÃO  1.8        #
# -------------------------- # 
# By Dreaper - @juliofmendes



import youtube_dl
import os

# Define o caminho para a pasta de legendas
path = os.path.abspath(os.path.dirname(__file__))
legendas_path = os.path.join(path, "Legendas")

# Variáveis para o nome da pasta da playlist e do ID da playlist
sub_path = "Hipopotomonstrosesquipedaliofobia"
playlist_id = "Hipopotomonstrosesquipedaliofobia"

# Cria o caminho para a pasta principal da playlist
main_path = os.path.join(legendas_path, sub_path)
playlist_path = os.path.join(main_path, playlist_id)

# Função para verificar se o link informado é de uma playlist ou de um vídeo
def verificar_link(link_url):
    # Verifica se a pasta de legendas existe
    if not os.path.exists(legendas_path):
        # Se não existir, cria a pasta
        os.makedirs(legendas_path)
        print(f"\n[AVISO] Diretório de legendas: {legendas_path}\n")

    # Variáveis globais para o nome da pasta da playlist e do ID da playlist
    global sub_path
    global playlist_id

    # Opções para o youtube_dl
    ydl_opts = {
        'ignoreerrors': True,
        'nocheckcertificate': True,
        'skip_download': True,
    }

    # Usa o youtube_dl para extrair informações do link
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(link_url, download=False)
        playlist_id = video_info.get('id', '')   

        # Verifica se o link é de uma playlist
        if 'entries' in video_info:
            print("\n\nSalvando legendas da PLAYLIST\n\n")
            # Se sim, define o nome da pasta como "Playlist"
            sub_path = "Playlist"
            main_path = os.path.join(legendas_path, sub_path)
            if not os.path.exists(main_path):
                os.makedirs(main_path)

            # Cria o caminho para a pasta da playlist
            playlist_path = os.path.join(main_path, playlist_id)
            if not os.path.exists(playlist_path):
                os.makedirs(playlist_path)
            return

        # Se não for uma playlist, define o nome da pasta como "[Videos]"
        else:
            print("\n\nSalvando legenda do VIDEO\n\n")
            sub_path = "[Videos]"
            main_path = os.path.join(legendas_path, sub_path)
            if not os.path.exists(main_path):
                os.makedirs(main_path)
            return
#        COLOCAR UM IF ERRO


#Define uma função chamada "download_subtitle", que recebe um link URL como entrada e baixa legenda do YouTube.
def download_subtitle(link_url):
    verificar_link(link_url)
    main_path = os.path.join(legendas_path, sub_path)
    main_path = os.path.join(main_path, playlist_id)

    ydl_opts = {
        # Especifica que as legendas devem ser baixadas com a melhor qualidade disponível.
        'writesubtitles': 'best',
        # Especifica que o formato de legendas deve ser VTT.
        'subtitlesformat': 'vtt',
        # Especifica que todas as legendas disponíveis não devem ser baixadas.
        'allsubtitles': False,
        # Especifica que as legendas em português e inglês devem ser baixadas.
        'subtitleslangs': ['pt', 'en'],
        # Ignora erros durante o download de legendas.
        'ignoreerrors': True,
        # Desabilita a verificação de certificado SSL.
        'nocheckcertificate': True,
        # Especifica que o vídeo não deve ser baixado, apenas as legendas.
        'skip_download': True,
        # Define o nome do arquivo de legendas como "título do vídeo. [id do vídeo].vtt".
        'outtmpl': os.path.join(main_path, f"%(title)s.[%(id)s].%(ext)s"),
    }
     
    # Cria uma instância de YoutubeDL com as opções especificadas.
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        # Se o caminho da pasta de legendas é "[Videos]", baixa apenas as legendas do vídeo.
        if (sub_path == "[Videos]"):
            ydl.download([link_url])

        # Se o caminho da pasta de legendas é "Playlist", baixa as legendas de todos os vídeos da playlist.
        elif(sub_path == "Playlist"):
            playlist = ydl.extract_info(link_url, download=False)
            playlist_entries = playlist.get('entries', [])   
            
            for entry in playlist_entries:
                video_title = entry.get('title', '')
                video_id = entry.get('id', '')
                if not video_title or not video_id:
                    continue
                ydl.download([entry['webpage_url']])

#        COLOCAR UM IF ERRO
        

print("\n" * os.get_terminal_size().lines) #limpar linha        
link_url = input("Insira a URL do Youtube: ")
#link_url = "https://youtube.com/playlist?list=PL4puqDxkuXpP1P52x5AuSztDQWBDsi6-B"
#link_url = "https://www.youtube.com/watch?v=Vnc0TX6Vias"
download_subtitle(link_url)



# -------------------------- # 
#         F     I     M      #
# -------------------------- # 
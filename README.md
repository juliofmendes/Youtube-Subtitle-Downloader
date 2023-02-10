# Youtube_Subtitle_Downloader

Python program to download subtitles (in Portuguese and English) from YouTube videos or playlists.
The Youtube_Subtitle_Downloader first checks if the provided URL corresponds to a playlist or an individual video. Then, it creates directories to store the downloaded subtitles and finally, it starts the download process. The downloaded subtitles are saved inside the "Subtitles" folder, in the folder created with the link ID and the name of the video or playlist, the link ID, language and extension (by default ".vtt").
  
<details>
<summary>Português</summary>
Programa em python que permite baixar legendas (em português e inglês) de vídeos ou playlists do YouTube.
O Youtube_Subtitle_Downloader primeiro verifica se a URL fornecida corresponde a uma playlist ou a um vídeo individual. Em seguida, ele cria diretórios para armazenar as legendas baixadas e, finalmente, inicia o download das legendas. As legendas baixadas são salvas dentro da pasta "Legendas", na pasta criada com o ID do link e com o nome do vídeo ou da playlist, o ID do link, a lingua e a extensão (por padrão ".vtt").
</details>

#### Screenshots
<img src="https://github.com/juliofmendes/Autocheck-M3U-List/blob/main/Screenshot_03.png?raw=true" width="30%" height="30%">     <img src="https://github.com/juliofmendes/Autocheck-M3U-List/blob/main/Screenshot_01.png?raw=true" width="30%" height="30%">     <img src="https://github.com/juliofmendes/Autocheck-M3U-List/blob/main/Screenshot_02.png?raw=true" width="30%" height="30%">




## How to use


### Download the code:
`git clone git@github.com:juliofmendes/Youtube_Subtitle_Downloader.git`


### Install the "youtube_dl" library
o run this code, you need to have the "youtube_dl" library installed and have write permission in the system directory where the code will be executed. Additionally, you need an internet connection for the code to download the YouTube subtitles. 
To install the "youtube_dl" library, you can use the following command: 
`pip install youtube-dl`


### How to use

1. Copie uma ou mais listas M3U (`.m3u`) para a pasta `Listas_Novas`;
2. Execute o comando `python Autocheck_m3u.py` no terminal;
3. Siga as orientações do programa.




## Features

- Automatic folder creation [`Legendas`,`[Videos]`,`Playlist`] if they do not already exist.
- Supports two languages, `Portuguese` and `English`, for saving subtitles.
- The program checks whether the link is from a playlist or an individual video and downloads the subtitles accordingly.
- Subtitle naming format: `Title.[Id].Language`. For example: `Video Title.[video id].pt.vtt`.
- Automatic selection of URL between playlist and video for download.
- Intelligent saving of subtitles based on their type and ID.




## ToDo
* [ ] 




## Changelog

#### V1.8 - Tratamento na captura do nome sem virgula. Correção do erro.
  <details>
  <summary>Versões Antigas</summary>

V2.7 - melhorada a captura para as tags na m3u e salvamento, agora sem erro. Resolvido o problema de salvamento dos arquivos offline na lista. Retirado a repetição do ultimo item.

V1.0 - Básico e inicial.  
</details>

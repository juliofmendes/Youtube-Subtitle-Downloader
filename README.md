# Youtube_Subtitle_Downloader

Python program to download subtitles (in Portuguese and English) from YouTube videos or playlists.
The Youtube_Subtitle_Downloader first checks if the provided URL corresponds to a playlist or an individual video. Then, it creates directories to store the downloaded subtitles and finally, it starts the download process. The downloaded subtitles are saved inside the "Subtitles" folder, in the folder created with the link ID and the name of the video or playlist, the link ID, language and extension (by default ".vtt").
  
<details>
<summary>Português</summary>
Programa em python que permite baixar legendas (em português e inglês) de vídeos ou playlists do YouTube.
O Youtube_Subtitle_Downloader primeiro verifica se a URL fornecida corresponde a uma playlist ou a um vídeo individual. Em seguida, ele cria diretórios para armazenar as legendas baixadas e, finalmente, inicia o download das legendas. As legendas baixadas são salvas dentro da pasta "Legendas", na pasta criada com o ID do link e com o nome do vídeo ou da playlist, o ID do link, a lingua e a extensão (por padrão ".vtt").
</details>

#### Screenshots
<img src="https://github.com/juliofmendes/Youtube-Subtitle-Downloader/blob/main/Screenshot_01.png?raw=true" width="30%" height="30%">     <img src="https://github.com/juliofmendes/Youtube-Subtitle-Downloader/blob/main/Screenshot_02.png?raw=true" width="30%" height="30%">




## How to use


### Download the code:
`git clone git@github.com:juliofmendes/Youtube_Subtitle_Downloader.git`


### Install the "youtube_dl" library
to run this code, you need to have the "youtube_dl" library installed and have write permission in the system directory where the code will be executed. Additionally, you need an internet connection for the code to download the YouTube subtitles. 
To install the "youtube_dl" library, you can use the following command: 
`pip install youtube-dl`


### How to use

1. Execute no terminal: `python3 .../Youtube_Subtitle_Downloader/YouSubDL[1.8].py`
2. Cole ou digite o `link` do Video ou Playlist
3. Verifique as legendas na pasta `Legendas`




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

##### V1.8 - Implemented automatic creation for `Legendas`,`[Videos]`,`Playlist` if they do not exist. Added smart saving for the [Videos] and Playlist folders, creating an internal folder with the link ID. Restructured the code to work with two functions, `verificar_link(link_url)` e `download_subtitle(link_url)`.

  <details>
  <summary>Previous Versions</summary>

V1.7 - Implemented automatic selection between the playlist video link and simple videos for download. Subtitles are now saved in the playlist folder.

V1.5 - Structured the function for reading YouTube lists. Changed the SRT extension to `VTT`. Adjustment in the naming of saving `title.[id].ext.vtt`.

V1.3 - Added the function of creating the `Legendas` folder, saving the subtitle inside the folder. Restricted the download of automatically generated subtitles. Added the possibility of the `EN` language in addition to PT-BR. Implemented the subtitle naming format `nome[id].ling.srt`.

V1.0 - Basic and initial. Saves the `PT-BR` subtitle of the video in the file folder.
</details>

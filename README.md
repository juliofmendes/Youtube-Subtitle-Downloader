# Youtube_Subtitle_Downloader

Python program to download subtitles (in Portuguese and English) from YouTube videos or playlists.
The Youtube_Subtitle_Downloader first checks if the provided URL corresponds to a playlist or an individual video. Then, it creates directories to store the downloaded subtitles and finally, it starts the download process. The downloaded subtitles are saved inside the "Subtitles" folder, in the folder created with the link ID and the name of the video or playlist, the link ID, language and extension (by default ".vtt").

Programa em python que permite baixar legendas (em português e inglês) de vídeos ou playlists do YouTube.
O Youtube_Subtitle_Downloader primeiro verifica se a URL fornecida corresponde a uma playlist ou a um vídeo individual. Em seguida, ele cria diretórios para armazenar as legendas baixadas e, finalmente, inicia o download das legendas. As legendas baixadas são salvas dentro da pasta "Legendas", na pasta criada com o ID do link e com o nome do vídeo ou da playlist, o ID do link, a lingua e a extensão (por padrão ".vtt").





This code is checking if the links in an M3U file are online or offline. The M3U file is read and parsed to extract the link, name, tvg-id, tvg-logo, and group-title. Then, the script checks the status code of the response from the server and prints the result.

It then filters the list of files to only include files with the '.m3u' file extension and prompts the user to select which file they want to check. Once the file is selected, it opens the file and parses the links, if online the link is added to an online_list. If offline it is added to an offline_list.

Overall, this script can be useful for checking the availability of links in an M3U file, which can be useful for IPTV streaming, for example.
  
  <details>
  <summary>Português</summary>
Este script verifica a disponibilidade de links em um arquivo M3U enviando uma solicitação HEAD para cada link usando a função requests.head(). Um arquivo M3U é um arquivo de texto simples que contém uma lista de URLs, geralmente usado para streaming IPTV.

O script começa definindo uma função chamada check_online() que recebe um arquivo M3U como argumento. Ele então inicializa duas listas, online_list e offline_list, e uma variável de contagem count.

Ele abre o arquivo M3U passado como argumento e lê suas linhas. Ele então itera através de cada linha do arquivo. Se a linha começa com "#EXTINF", ele usa expressões regulares para extrair o nome, tvg-id, tvg-logo e group-title da linha. Se a linha começa com "http", é considerada um link e o script envia uma solicitação HEAD para o link usando a função `requests.head()
</details>

#### Screenshots
<img src="https://github.com/juliofmendes/Autocheck-M3U-List/blob/main/Screenshot_03.png?raw=true" width="30%" height="30%">     <img src="https://github.com/juliofmendes/Autocheck-M3U-List/blob/main/Screenshot_01.png?raw=true" width="30%" height="30%">     <img src="https://github.com/juliofmendes/Autocheck-M3U-List/blob/main/Screenshot_02.png?raw=true" width="30%" height="30%">


## How to use

###Download the code:
`git clone git@github.com:juliofmendes/Youtube_Subtitle_Downloader.git`



### How to use

1. Copie uma ou mais listas M3U (`.m3u`) para a pasta `Listas_Novas`;
2. Execute o comando `python Autocheck_m3u.py` no terminal;
3. Siga as orientações do programa.


To run this code, you need to have the "youtube_dl" library installed and have write permission in the system directory where the code will be executed. Additionally, you need an internet connection for the code to download the YouTube subtitles. To install the "youtube_dl" library, you can use the following command:

pip install youtube-dl
Note that you need to have the "pip" package manager installed on your system.




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

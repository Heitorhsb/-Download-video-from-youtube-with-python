from pytube import YouTube
print("Olá, esse codigo serve para fazer o download de videos no youtube")
link = input("coloque o link do video do YouTube aqui!")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()

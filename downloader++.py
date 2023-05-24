from download import download
import asyncio
import pytube
import os

print("Welcome to downloader++")
print("""\

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMx.      .xMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMx.      .xMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMx.      .xMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMx.      .xMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMx.      .xMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMx.      .xMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMx.      .xMMMMMMMMMMMMMMM
MMMMMMMMMKdllll,        ,lllldKMMMMMMMMM
MMMMMMMMMO'                  'OMMMMMMMMM
MMMMMMMMMMKl.              .lKMMMMMMMMMM
MMMMMMMMMMMW0:.          .:0WMMMMMMMMMMM
MMMMMMMMMMMMMNk,        ,kNMMMMMMMMMMMMM
MMMMMMNMMMMMMMMXd.    .dXMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWKo::oKWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWWMMMMMWMMMMMMMMMMMMMMMm
""")
def main():
 choice = input("1: Normal Download \n2: Youtube (broken) \n3: Info \n4: Exit \n")
 if choice == "1":
  mainload()
 if choice == "2":
   print("NOTICE: PyTube doesn't work right now.")
   yt_kaputt = input("Press Enter to continue or press A to go back to menu. ")
   if yt_kaputt == "a":
     main()
   youtube()
 if choice == "3":
  info()
 if choice == "4":
  exit()
def mainload():
  url_name = ""
  while url_name == "":
   url_name = input("What are you trying to download (enter URL): ")
  file_name = ""
  while file_name == "":
    file_name = input("What's the file name: ")
  print("Now the file will begin download")
  async def program():
    download(url_name, file_name, progressbar=False)
  asyncio.run(program())
  print("Your download is finished!")
  choice = input("Do you wanna download anything else? (y/n)")
  if choice == "y":
    mainload()
  choice2 = input("Do you want to go back to the main menu? (y/n): ")
  if choice2 == "y":
    main()
def youtube():
  yt_url = ""
  while yt_url == "":
   yt_url = input("What is the YouTube URL: ")
  async def yt_dl():
   pytube.YouTube(yt_url).streams.get_highest_resolution().download()
  asyncio.run(yt_dl())
  yt_choice = input("Do you want to download another video? (y/n): ")
  if yt_choice == "y":
    youtube()
  yt_choice2 = input("Do you want to go back to the main menu? (y/n): ")
  if yt_choice2 == "y":
    main()
def info():
 print(os.uname())
 info_choice = ""
 while info_choice == "":
   info_choice = input("Press any button to go back to main menu. \n")
 main()


main()

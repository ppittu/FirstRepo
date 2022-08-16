import instaloader


def InstaDp():
    bot = instaloader.Instaloader()
    username = input("Enter instagram username: ")
    bot.download_profile(username, profile_pic_only=True)


InstaDp()

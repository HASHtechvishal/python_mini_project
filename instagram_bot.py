from instabot import Bot
bot=Bot()
bot.login(username="pythoncodeline",password="124421=vishal")
#bot.follow('cars') #its working
#bot.upload_photo("/Users/apple/Desktop/download.jpeg",caption="my first python image uploaded by insta bot in python")
bot.unfollow("cars")
#bot.send_message("hi its python",["vishal_arora1994"])#you can add number of persons
#followers = bot.get_user_followers("pythoncodeline")
#for follower in followers:
    #print(bot.get_user_info(follower))

#following = bot.get_user_following("pythoncodeline")
#for follower in following:
    #print(bot.get_user_info(follower))    
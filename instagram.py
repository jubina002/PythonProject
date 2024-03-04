from instabot import Bot
bot = Bot()
bot.login(username="mypythonaccount",
          password="mypythonaccount") 
bot.follow("bretty")

#To follow more person
list_of_user = ["user_id1", "user_id2", "user_id3", "...."]
bot.follow_users(list_of_user)

bot.unfollow("bretty")

unfollow_list = ["user_id1", "user_id2", "user_id3", "..."]
bot.unfollow_users(unfollow_list)

# To unfollow everyone use:
# Please use this part very carefully.
bot.unfollow_everyone()

bot.upload_photo("C:\Users\User\OneDrive\Desktop\PP\house.jpg",
                 caption="my cute home")


#send a message to multiple user
#sent as a group chat text
bot.send_message("I love python", ["jess", "bliss"])

# Send like in messages
# To send like to one or more person.
list = ["user_id1", "user_id2", "user_id3", "..."]
bot.send_like(list)

# Count number of followers
followers = bot.get_user_followers("mypythonaccount")
print("Total number of followers: ")
print(len(followers))

followers = bot.get_user_followers("mypythonaccount")
for follower in followers:
    print(bot.get_user_info(follower))

following = bot.get_user_following("mypythonaccount")
for Following in following:
    print(bot.get_user_info(Following))


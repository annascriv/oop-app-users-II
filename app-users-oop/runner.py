from User import Users

from FreeUser import FreeUser

from PremiumUser import PremiumUser

robert = PremiumUser("robert","robert@gmail.com", "robertoscriv")

anna = FreeUser("anna", "anna@gmail.com", "annalou")


robert.create_post()

anna.create_post()

print(Users.user_posts)
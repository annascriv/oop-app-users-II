from User import Users

class FreeUser(Users):

    def __init__(self,name, email, username):
        super().__init__(name, email, username)
        #self.counter = 0
        

    def create_post(self):
        
            if len(Users.user_posts)<2:
                super().create_post()

            else:
                print("Sorry, you have reached your posting limit.")
            


# anna = FreeUser("Anna", "anna@school.org","annascriv")

# anna.create_post()







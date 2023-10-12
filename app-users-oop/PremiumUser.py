from User import Users

class PremiumUser(Users):

    def __init__(self, name, email, username):
        super().__init__(name, email, username)

    
    def create_post(self):
        super().create_post()


# robert = PremiumUser("Robert", "robert@school.org", "robertscriv")


# robert.create_post()

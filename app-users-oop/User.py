class Users: 

    user_posts = []
    

    def __init__(self,name,email,username):
        self.name=name
        self.email=email
        self.username= username
        self.posts = []
        self.post_count=0 
        
       # self.User_posts = []

    @property
    def get_posts(self):

        return self.posts
    
    @classmethod
    def create_user(cls):
        name = input("Enter your name: \n")
        email = input("Enter your email: \n")
        username = input("Enter your username: \n")


        user = cls(name, email, username)
        return user
        

    def __repr__(self):
        return f"name: {self.name} | email: {self.email} | username: {self.username}"
    
    
    def create_post(self):
        self.post_count+=1
        id=self.post_count
        
        post_title = input("Enter the title of your post!\n")
        new_post = input("Enter what you would like to post!\n")
        
        self.posts.append( {'post number':id, 'title': post_title, 'content':new_post})
        Users.user_posts.append({'name': {self.name}, 'post number':id, 'title': post_title, 'content':new_post})
        
        print("Post added successfully!")
        
        return self.posts

  
    def delete_post(self):
        post_number = input("Enter the number of the post you would like to delete: ")
        print(post_number)
        # for i in range(len(self.posts)):
        #     if self.posts[i]['post number'] == post_number:
        #         self.posts.remove(self.posts[i]['post number'])

        for post in self.posts:
            print(post['post number'])
            if post['post number'] == int(post_number):
                    self.posts.pop(int(post_number)-1)
                    print("Your post has been successfully deleted.")
                    print(self.posts)
            else:
                print("please enter a valid post number.")    

            
        

user_one = Users("Anna", "anna@school.org", "annascriv")
# print(user_one.create_post())
# print(user_one.create_post())


user_two = Users("Robert", "robert@school.org", "robertscriv")

# print(Users.user_posts)

users = [user_one,user_two]

def prompt():
    
    user = users[-1]   
    
    #print(users)

    #user_id = users


    choice = input("""
----WELCOME to Anna's Posting Site!---
What would you like to do? 
1. Add a post
2. View your posts
3. Delete a post
4. Exit    
5. Create User
6. View all Users
                   """)
    match choice: 

        case '1':
            user.create_post()

            print(user.posts)
            print(Users.user_posts)
        
            
            return prompt()

        case '2':
            #for post in Users.posts.values():
                print(f"You have {user.post_count} posts.")
                print(user.posts)    
                return prompt()
        case '3':
            user.delete_post()
            
            prompt()

        case '4':
            print("Thank you, have a great day!")
            exit()

        case '5':
            user = Users.create_user()
            users.append(user)
            print(users)
            return prompt()
        case '6':
            print(users)
            return prompt()
       
prompt()
       


#user_one = Users("Anna", "anna@school.org",'annascriv')


# print(user_one)
# print(user_two)

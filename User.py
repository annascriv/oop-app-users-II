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
        

    def __str__(self):
        return f"{self.name}'s email is {self.email} and their username is {self.username}."
    
    
    def create_post(self):
        self.post_count+=1
        id=self.post_count
        post_title = input("Enter the title of your post!\n")
        new_post = input("Enter what you would like to post!\n")
        self.posts.append( {'post number':id, 'title': post_title, 'content':new_post})
        Users.user_posts.append({'name': {self.name}, 'post number':id, 'title': post_title, 'content':new_post})
        #self.User_posts({'post number':id, 'title': post_title, 'content':new_post})
        #Users.posts[Users.post_count] = new_post
        print("Post added successfully!")
        
        print(self.posts)

  
    def delete_post(self):
        post_number = input("Enter the number of the post you would like to delete: ")
        
        for i in range(len(self.posts)):
            if self.posts[i]['post number'] == post_number:
                self.posts.pop(i)

            
        print("Your post has been successfully deleted.")
        print(self.posts)

user_one = Users("Anna", "anna@school.org", "annascriv")
user_two = Users("Robert", "robert@school.org", "robertscriv")

print(Users.user_posts)

def prompt():
   
    

    choice = input("""
----WELCOME to Anna's Posting Site!---
What would you like to do? 
1. Add a post
2. View your posts
3. Delete a post
4. Exit    
                   """)
    match choice: 

        case '1':
            user_one.create_post()
            
            return prompt()

        case '2':
            #for post in Users.posts.values():
                print(f"You have {user_one.post_count} posts.")
                print(user_one.get_posts)    
                return prompt()
        case '3':
            user_one.delete_post()
            
            prompt()

        case '4':
            print("Thank you, have a great day!")
            exit()
            
prompt()


#user_one = Users("Anna", "anna@school.org",'annascriv')


# print(user_one)
# print(user_two)

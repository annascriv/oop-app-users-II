class Users: 

    posts = []
    post_count = 0

    def __init__(self,name,email,username):
        self.name=name
        self.email=email
        self.username= username
       # self.User_posts = []
        
        
        

    def __str__(self):
        return f"{self.name}'s email is {self.email} and their username is {self.username}."
    
    @classmethod
    def create_post(self):
        id=len(self.posts)+1
        Users.post_count+=1
        post_title = input("Enter the title of your post!\n")
        new_post = input("Enter what you would like to post!\n")
        self.posts.append( {'post number':id, 'title': post_title, 'content':new_post})
        #self.User_posts({'post number':id, 'title': post_title, 'content':new_post})
        #Users.posts[Users.post_count] = new_post
        print("Post added successfully!")
        
        print(Users.posts)

    @classmethod
    def delete_post(self):
        post_number = input("Enter the number of the post you would like to delete: ")
        for i in range(len(Users.posts)):
            if Users.posts[i][int(post_number)] == post_number:
                Users.posts.pop(post_number)

            
        print("Your post has been successfully deleted.")
        print(Users.posts)



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
            Users.create_post()
            
            return prompt()

        case '2':
            #for post in Users.posts.values():
                print(f"You have {Users.post_count} posts.")
                print(Users.posts)    
                return prompt()
        case '3':
            Users.delete_post()
            
            prompt()

        case '4':
            print("Thank you, have a great day!")
            exit()
            
prompt()


user_one = Users("Anna", "anna@school.org",'annascriv')


# print(user_one)
# print(user_two)

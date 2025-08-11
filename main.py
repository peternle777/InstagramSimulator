from socialnetwork import Network
from account import Account

class Instagram:
    def __init__(self, filename):
        self.network = Network('./'+filename)
        self.currentUser = None
    
    def login(self):
        while True:
            username = input('Enter username:').strip()
            if username.lower() == 'exit':
                return False
            if username in self.network.network:
                self.currentUser = self.network.network[username]
                print('Welcome @' + username)
                print()
            else:
                print('Username not found.  Try again.')
            
    def showUserMenu(self):
        while True:
            setTo = 'Public' if self.currentUser.private else 'Public'
            print('1 - View profile')
            print('2 - Search')
            print('3 - Requests')
            print('4 - Set to ' + setTo)
            print('5 - Log Out')
            choice = input('Choose an option (1,2,3,4):  ').strip()
            if choice == '1':
                self.viewProfile()
            elif choice == '2':
                self.search()
                # search = input('Search:  ')
                # if search in self.network

    
    def viewProfile(self):
         while True:
            print('@' + self.currentUser.username)
            print('Followers:  '+len(self.currentUser.followers))
            print('Following:  '+len(self.currentUser.following))
            print()
            print('1 - See Followers')
            print('2 - See Following')
            print('3 - Back')
            choice = input('Choose an option (1,2,3):  ').strip()
            if choice == 1:
                print('Followers:')
                for i in self.currentUser.followers:
                    print(i)
                
            elif choice == 2:
                print('Following:')
                for i in self.currentUser.following:
                    print(i)
            elif choice == 3:
                break
    
    def viewOtherProfile(self, account):
        print('@' + account.username)
        print('Followers:  ' + len(account.followers))
        print('Following:  ' + len(account.following))
        if account in self.currentUser.followers:
            print('1 - Unfollow')
        else:
            print('1 - Follow')
        print('2 - Remove')
        print('3 - Block')
        print('4 - Back')
        choice = input('Choose an option (1,2,3,4):  ').strip()
        if choice == 1 and account in self.currentUser.followers:
            self.currentUser.




    def search(self):

    def requests(self):

    def setTo(self):

    
    

            

from MyClients import UserIdClient
from MyClients import FriendsBirthdaysClient
from ProcessAges import print_gist


def main():
    print("Введите username:", end=" ")
    user_id = input()
    uid = UserIdClient(user_id).execute()
    print("User id: ", uid)

    friends_ages = FriendsBirthdaysClient(uid).execute()

    print_gist(friends_ages)


if __name__ == "__main__":
    main()
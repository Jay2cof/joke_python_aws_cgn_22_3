from chuck_noris_api import get_new_joke
from s3_access import upload_joke

while True:

    joke_data = get_new_joke()

    print(joke_data["joke"])
    rating = int(input("Was this joke funny? Scala 1-5\n"))

    if(rating > 3):
        print("Great I save the joke")
        upload_joke(joke_data)
    else:
        print("Oh ok. I dont save the joke")

    new_joke = input("new joke? yes \n")
    if new_joke != "yes":
        no_new_joke= input("realy no new funny joke? yes \n")
        if no_new_joke == "yes":
            break
        

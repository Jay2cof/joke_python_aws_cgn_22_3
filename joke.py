from chuck_noris_api import get_new_joke
from s3_access import upload_joke

joke_to_save = get_new_joke()
upload_joke(joke_to_save)

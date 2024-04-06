# instaloader library

import instaloader

i_id = input("Input Instagram Id :") 

insta = instaloader.Instaloader()

insta.download_profile(i_id,profile_pic_only=False)


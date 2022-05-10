from cProfile import Profile
import instaloader 


L = instaloader.Instaloader()
L.interactive_login('rakshit.dahal')

print(L.context)

safal_profile = Profile.get_posts()

import instaloader

# Create an instance of the Instaloader class
loader = instaloader.Instaloader()

with open('./urls.txt', 'r') as f:
    urls = f.readlines()

while (urls):
    url = urls.pop(0)
    try:
        pid = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(
            loader.context, url.split("/")[-2])
        loader.download_post(post, target=f'mv_{pid}')
    except:
        print("GONE", url)

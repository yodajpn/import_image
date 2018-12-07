import urllib.error
import urllib.request

def download_image(url, dst_path):
    try:
        data = urllib.request.urlopen(url).read()
        with open(dst_path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)

url = 'https://slackmojis.com/'
dst_path = 'Desktop'
# dst_dir = 'data/src'
# dst_path = os.path.join(dst_dir, os.path.basename(url))
download_image(url, dst_path)

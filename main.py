
from FacebookPostsScraper import FacebookPostsScraper as FPS
from json import dumps

def main():
    email    = 'YOUR_EMAIL'
    password = 'YOUR_PASSWORD'

    facebook = FPS(email, password, post_url_text='Daha Fazla')

    profiles = [
        'https://www.facebook.com/groups/202783390107516',
        "https://www.facebook.com/groups/1590438354504559"

    ]
    data = facebook.get_posts_from_list(profiles)
    str_data = dumps(data, indent=2, ensure_ascii=False, sort_keys=False)

    print(str_data)

    with open("posts.json", "w", encoding="utf8") as f:
        f.write(str_data)

if __name__ == '__main__':
    main()

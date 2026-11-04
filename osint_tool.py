import re
from urllib.parse import quote

def validate_email(email):
    pattern = r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def search_username(username):
    username = quote(username.strip())
    sites = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "Facebook": f"https://www.facebook.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "GitHub": f"https://github.com/{username}"
    }
    return sites

def main():
    print("ABOBBY OSINT PRO")
    print("----------------")
    print("Public information research only")

    target = input("Enter username: ").strip()

    if not target:
        print("Please enter a username.")
        return

    print("\nPublic profile links:")
    for site, link in search_username(target).items():
        print(f"{site}: {link}")

if __name__ == "__main__":
    main()

import webbrowser

# Dictionary mapping app names to URLs
social_apps = {
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "youtube": "https://www.youtube.com",
    "twitter": "https://twitter.com",
    "whatsapp": "https://web.whatsapp.com"
}

print("Select an app to open:")
for i, app in enumerate(social_apps.keys(), start=1):
    print(f"{i}. {app.capitalize()}")

choice = int(input("Enter the number of the app you want to open: "))

app_list = list(social_apps.keys())

if 1 <= choice <= len(app_list):
    selected_app = app_list[choice - 1]
    webbrowser.open(social_apps[selected_app])
    print(f"Opening {selected_app.capitalize()}...")
else:
    print("Invalid choice.")

from winotify import Notification, audio

def online_notifier(text):
    icon_path = r"D:\Pictures\Saved Pictures\gemini-svg.png"

    toast = Notification(
    app_id="Virtual Assistant",
    title="Online",
    msg=text,
    duration="long",
    icon= icon_path
    )

    toast.set_audio(audio.Default, loop=False)

    toast.add_actions(label="Click", launch="https://google.com/")
    toast.add_actions(label="Dismiss", launch="https://github.com/")

    toast.show()

if __name__ == "__main__":
    online_notifier("I am ready.")
from plyer import notification
import time  #for time delay in successive notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title=" Take Rest",
            message="Rest is vital for better mental health, increased concentration and memory, a healthier immune system, reduced stress, improved mood and even a better metabolism.",
            app_icon="",
            timeout=10)
        time.sleep(60*60)
from gtts import gTTS
import turtle
import random
import threading
from time import sleep
from playsound import playsound
from winsound import Beep

# Set up the screen
window = turtle.Screen()
window.title("Happy Anniversary!")
window.setup(width=600, height=600)
window.bgcolor("black")
window.tracer(0)

pen = turtle.Turtle(visible=False)
pen.penup()

colors = ['red', 'light green', 'yellow', 'light blue', 'pink']
circles = [turtle.Turtle(shape='circle') for _ in range(10)]
for circle in circles:
    circle.penup()
    circle.color(random.choice(colors))

occupied_positions = []
text_safe_zone = (-150, 150, -50, 50)

def is_valid_position(x, y, radius=30):
    if text_safe_zone[0] <= x <= text_safe_zone[1] and text_safe_zone[2] <= y <= text_safe_zone[3]:
        return False
    for pos in occupied_positions:
        if (x - pos[0]) ** 2 + (y - pos[1]) ** 2 < (radius * 2) ** 2:
            return False
    return True

def move_circles():
    occupied_positions.clear()
    for circle in circles:
        attempts = 0
        while attempts < 100:
            x, y = random.randint(-250, 250), random.randint(-250, 250)
            if is_valid_position(x, y):
                circle.goto(x, y)
                occupied_positions.append((x, y))
                break
            attempts += 1
    window.update()
    window.ontimer(move_circles, 1000)

def animate_text():
    for color in colors:
        pen.clear()
        pen.color(color)
        pen.goto(0, 0)
        pen.write("শুভ বার্ষিকী বাবা ও মা !!!", align='center', font=('Arial', 22, 'bold'))
        pen.penup()
        pen.goto(0, -30)
        pen.write("আপনার দিনটি সুখের হোক এই কামনা করি |", align='center', font=('Arial', 17, 'bold'))
        window.update()
        sleep(1)
    window.ontimer(animate_text, 5000)

def play_anniversary_tone():
    melody = [
        (523, 400), (587, 400), (659, 400), (523, 400), (0, 200),
        (523, 400), (587, 400), (659, 400), (698, 400), (0, 200),
        (698, 400), (659, 400), (587, 400), (523, 600),
        (0, 500), (784, 400), (659, 400), (698, 400), (659, 400), (587, 600)
    ]
    for freq, duration in melody:
        if freq > 0:
            Beep(freq, duration)
        else:
            sleep(duration / 1000)

def play_music():
    try:
        text = "শুভ বিবাহবার্ষিকী বাবা ও মা। আপনার দিনটি সুখের হোক এই কামনা করি।"
        tts = gTTS(text=text, lang='bn')
        tts.save("happy_anniversary.mp3")
        playsound("happy_anniversary.mp3")
    except Exception as e:
        print(f"Error playing audio: {e}")

    play_anniversary_tone()

if __name__ == "__main__":
    music_thread = threading.Thread(target=play_music)
    music_thread.start()  # Start music in a separate thread
    move_circles()
    animate_text()
    window.mainloop()
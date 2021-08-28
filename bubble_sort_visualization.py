from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 500
BG_COLOR = "#082032"
POST_COLOR = "#FF4C29"
NUMBER_OF_POSTS = 100


class Post:
    posts = []

    def __init__(self, index, position) -> None:
        self.index = index
        self.position = position
        self.width = WIDTH//NUMBER_OF_POSTS
        self.height = (HEIGHT//NUMBER_OF_POSTS) * (self.index+1)
        self.create()

    def create(self):
        self.p = canvas.create_rectangle(
            self.width*self.position, HEIGHT-self.height, self.width*(self.position+1), HEIGHT, fill=POST_COLOR, outline=POST_COLOR)

    def move(self, new_position):
        self.position = new_position
        canvas.delete(self.p)
        self.p = canvas.create_rectangle(
            self.width*self.position, HEIGHT-self.height, self.width*(self.position+1), HEIGHT, fill=POST_COLOR, outline=POST_COLOR)


def create_window():
    global window
    window = Tk()
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.resizable(height=False, width=False)
    window.config(bg="#b0a8b9")
    window.title("Bubble Sort Visualization")

    global canvas
    canvas = Canvas(width=WIDTH, height=HEIGHT,
                    bg=BG_COLOR, highlightthickness=0)
    canvas.pack()


def place_posts():
    sieve = [False for i in range(0, NUMBER_OF_POSTS)]
    for i in range(0, NUMBER_OF_POSTS):
        rand_pos = random.randint(0, NUMBER_OF_POSTS-1)
        while sieve[rand_pos]:
            rand_pos = random.randint(0, NUMBER_OF_POSTS-1)
        sieve[rand_pos] = True
        Post.posts.append(Post(i, rand_pos))


def sort():
    for i in range(0, NUMBER_OF_POSTS-1):
        for j in range(0, NUMBER_OF_POSTS-i-1):
            if Post.posts[j].position > Post.posts[j+1].position:
                p1 = Post.posts[j].position
                p2 = Post.posts[j+1].position
                Post.posts[j].move(p2)
                Post.posts[j+1].move(p1)
                canvas.itemconfig(
                    Post.posts[j].p, fill="white", outline="white")
                canvas.itemconfig(
                    Post.posts[j+1].p, fill="white", outline="white")
                window.update()
                time.sleep(0.01)
                canvas.itemconfig(
                    Post.posts[j].p, fill=POST_COLOR, outline=POST_COLOR)
                canvas.itemconfig(
                    Post.posts[j+1].p, fill=POST_COLOR, outline=POST_COLOR)
    for i in Post.posts:
        canvas.itemconfig(i.p, fill="white", outline="white")


def main():
    create_window()
    place_posts()
    sort()
    window.mainloop()


if __name__ == "__main__":
    main()

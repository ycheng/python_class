
import tkinter
from tkinter import Canvas, Label, Tk, StringVar, messagebox, Button, TOP

from random import choice
from collections import Counter


class Game():
  WIDTH = 300
  HEIGHT = 500

  def start(self):
    self.speed = 500

    self.root = Tk()
    self.root.title("Tetris")
    self.canvas = Canvas(
      self.root, 
      width=Game.WIDTH, 
      height=Game.HEIGHT)
    self.canvas.pack()

    # x1, y1, x2, y2
    # ref: http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/create_rectangle.html
    self.rec = self.canvas.create_rectangle(0, 0, 20, 20, fill='red')

    self.timer()
    self.root.mainloop()
    
  def timer(self):
    self.canvas.move(self.rec, 20, 20)
    self.root.after(self.speed, self.timer)

if __name__ == "__main__":
  game = Game()
  game.start()

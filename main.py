#!/usr/bin/env python

from manimlib.imports import *

class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        my_first_text=TextMobject("Writing with manim is fun")
        second_line=TextMobject("and easy to do!")
        second_line.next_to(my_first_text,DOWN)
        third_line=TextMobject("for me and you!")
        third_line.next_to(my_first_text,DOWN)

        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        second_line.shift(3*DOWN)
        self.play(ApplyMethod(my_first_text.shift,3*UP))

class PrintText1(Scene):
    def construct(self):
        txt = TexMobject("\\text dvsdrh\\quad\\ \\color{red}gaeadwa\\color{black}\\quad \\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}")

        self.play(Write(txt), run_time=5)
        self.wait()

if __name__ == '__main__':
    title = TextMobject("This is some LaTeX")
    title.add()

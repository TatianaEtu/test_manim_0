from manimlib.imports import *

class manim_examples(GraphScene):
    def construct(self):

        self.setup_axes()

        graph_1 = self.get_graph(lambda x: (1/2) * x ** 2 - 3)

        self.play(ShowCreation(graph_1))
        self.wait()


if __name__ == '__main__':
    title = TextMobject("This is some LaTeX")
    title.add()

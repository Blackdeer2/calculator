class Exporter:
    def __init__(self, figure):
        self.figure = figure

    def export_as_png(self, filename):
        self.figure.savefig(filename + ".png")

    def export_as_svg(self, filename):
        self.figure.savefig(filename + ".svg")

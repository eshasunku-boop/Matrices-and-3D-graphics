import wx
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

from models import MODEL

MODEL_NAMES = ["cube", "tetrahedron", "octahedron"]


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="3D Model Viewer", size=(900, 650))

        self.model = None
        self.base_vertices = None   # untouched copy, since MODEL.rotate() mutates in place
        self.edge_pairs = []
        self.limit = 1.0

        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.HORIZONTAL)

        # ---- plot ----
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(panel, -1, self.figure)
        main.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 5)

        # ---- controls ----
        controls = wx.BoxSizer(wx.VERTICAL)

        controls.Add(wx.StaticText(panel, label="Model"), 0, wx.ALL, 5)
        for name in MODEL_NAMES:
            btn = wx.Button(panel, label=name.capitalize())
            btn.Bind(wx.EVT_BUTTON, lambda evt, n=name: self.on_select(n))
            controls.Add(btn, 0, wx.EXPAND | wx.ALL, 3)

        controls.AddSpacer(15)
        controls.Add(wx.StaticText(panel, label="Rotation (degrees)"), 0, wx.ALL, 5)

        self.sliders = {}
        for axis in ("X", "Y", "Z"):
            controls.Add(wx.StaticText(panel, label=f"{axis} axis"), 0, wx.LEFT, 5)
            s = wx.Slider(panel, value=0, minValue=-180, maxValue=180,
                          style=wx.SL_HORIZONTAL | wx.SL_LABELS)
            s.Bind(wx.EVT_SLIDER, lambda evt: self.redraw())
            controls.Add(s, 0, wx.EXPAND | wx.ALL, 3)
            self.sliders[axis] = s

        reset = wx.Button(panel, label="Reset rotation")
        reset.Bind(wx.EVT_BUTTON, self.on_reset)
        controls.Add(reset, 0, wx.EXPAND | wx.ALL, 8)

        main.Add(controls, 0, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(main)

        self.on_select(MODEL_NAMES[0])

    def on_select(self, name):
        self.model = MODEL(name)
        self.base_vertices = self.model.vertices.astype(float).copy()
        # edges is an NxN adjacency matrix; take the upper triangle for unique (i, j) pairs
        self.edge_pairs = np.argwhere(np.triu(self.model.edges))
        # fixed axis limits so the view doesn't rescale while rotating
        self.limit = np.max(np.linalg.norm(self.base_vertices, axis=1)) * 1.2
        self.redraw()

    def on_reset(self, event):
        for s in self.sliders.values():
            s.SetValue(0)
        self.redraw()

    def redraw(self):
        if self.model is None:
            return

        # MODEL.rotate() accumulates, so restore the original vertices first
        self.model.vertices = self.base_vertices.copy()
        self.model.rotate(self.sliders["X"].GetValue(),
                          self.sliders["Y"].GetValue(),
                          self.sliders["Z"].GetValue())

        cols, projected = self.model.project2axis("z")   # flatten onto the xy plane
        pts = projected[:, cols]                          # (N, 2): x and y

        self.axes.clear()
        for i, j in self.edge_pairs:
            self.axes.plot([pts[i, 0], pts[j, 0]],
                           [pts[i, 1], pts[j, 1]], "b-")
        self.axes.plot(pts[:, 0], pts[:, 1], "ro", markersize=4)

        self.axes.set_xlim(-self.limit, self.limit)
        self.axes.set_ylim(-self.limit, self.limit)
        self.axes.set_aspect("equal")
        self.axes.set_xlabel("x")
        self.axes.set_ylabel("y")
        self.canvas.draw_idle()


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()

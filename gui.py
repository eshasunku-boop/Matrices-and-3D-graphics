import wx


class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(
            None,
            title="3D Graph",
            size=(900, 600)
        )

        panel = wx.Panel(self)

        # -------------------------
        # X AXIS
        # -------------------------

        x_label = wx.StaticText(panel, label="X")

        self.x_slider = wx.Slider(
            panel,
            value=0,
            minValue=-100,
            maxValue=100,
            style=wx.SL_HORIZONTAL
        )

        self.x_value = wx.StaticText(panel, label="0")

        # -------------------------
        # Y AXIS
        # -------------------------

        y_label = wx.StaticText(panel, label="Y")

        self.y_slider = wx.Slider(
            panel,
            value=0,
            minValue=-100,
            maxValue=100,
            style=wx.SL_HORIZONTAL
        )

        self.y_value = wx.StaticText(panel, label="0")

        # -------------------------
        # Z AXIS
        # -------------------------

        z_label = wx.StaticText(panel, label="Z")

        self.z_slider = wx.Slider(
            panel,
            value=0,
            minValue=-100,
            maxValue=100,
            style=wx.SL_HORIZONTAL
        )

        self.z_value = wx.StaticText(panel, label="0")

        # Connect sliders to functions
        self.x_slider.Bind(wx.EVT_SLIDER, self.change_x)
        self.y_slider.Bind(wx.EVT_SLIDER, self.change_y)
        self.z_slider.Bind(wx.EVT_SLIDER, self.change_z)

        # -------------------------
        # LAYOUT
        # -------------------------

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Graph area
        graph_area = wx.Panel(panel)
        graph_area.SetBackgroundColour("white")

        # Right side containing sliders
        slider_sizer = wx.BoxSizer(wx.VERTICAL)

        slider_sizer.Add(
            x_label,
            0,
            wx.TOP | wx.ALIGN_CENTER,
            20
        )

        slider_sizer.Add(
            self.x_slider,
            0,
            wx.ALL,
            10
        )

        slider_sizer.Add(
            self.x_value,
            0,
            wx.ALIGN_CENTER
        )

        slider_sizer.Add(
            y_label,
            0,
            wx.TOP | wx.ALIGN_CENTER,
            20
        )

        slider_sizer.Add(
            self.y_slider,
            0,
            wx.ALL,
            10
        )

        slider_sizer.Add(
            self.y_value,
            0,
            wx.ALIGN_CENTER
        )

        slider_sizer.Add(
            z_label,
            0,
            wx.TOP | wx.ALIGN_CENTER,
            20
        )

        slider_sizer.Add(
            self.z_slider,
            0,
            wx.ALL,
            10
        )

        slider_sizer.Add(
            self.z_value,
            0,
            wx.ALIGN_CENTER
        )

        main_sizer.Add(
            graph_area,
            1,
            wx.EXPAND | wx.ALL,
            20
        )

        main_sizer.Add(
            slider_sizer,
            0,
            wx.EXPAND | wx.TOP | wx.RIGHT,
            20
        )

        panel.SetSizer(main_sizer)

    # -------------------------
    # SLIDER FUNCTIONS
    # -------------------------

    def change_x(self, event):
        value = self.x_slider.GetValue()
        self.x_value.SetLabel(str(value))

    def change_y(self, event):
        value = self.y_slider.GetValue()
        self.y_value.SetLabel(str(value))

    def change_z(self, event):
        value = self.z_slider.GetValue()
        self.z_value.SetLabel(str(value))


app = wx.App()

frame = MyFrame()

frame.Show()

app.MainLoop()

import os
import wx

wildcard = "All file(*.*) | *.*"

class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "File and Folder")
        panel = wx.Panel(self, wx.ID_ANY)
        self.currentDirectory = os.getcwd()

        openfiledialogbutton = wx.Button(panel, label = "Show OPEN FileDialog")
        openfiledialogbutton.Bind(wx.EVT_BUTTON, self.onOpenFile)

    def onOpenFile(self, event):
        filedialog = wx.FileDialog(
            self, message = "Escoge un TXT",
            defaultDir = self.currentDirectory,
            defaultFile = "",
            wildcard = wildcard,
            style = wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        )
        if filedialog.ShowModal() == wx.ID_OK:
            paths = filedialog.GetPaths()
            print("Escogiste: ")
            for path in paths:
                print(path)
                for archivos in path:
                    print(filedialog.GetFilename())
            filedialog.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
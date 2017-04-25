#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Simple color picker demo app on wxPython.
"""

import wx
import os.path

class MainWindow(wx.Frame):
    """
        Main window of the app.
    """
    app_name = 'Демо'

    def __init__(self, window_size=(200, 100)):
        super(MainWindow, self).__init__(None, size=window_size)
        self.create_on_window_components()
        self.create_off_window_components()

    # Helper methods
    def create_on_window_components(self):
        """ Create components meant to be located in the window. """
        # window panel
        self.panel = wx.Panel(self, wx.ID_ANY)
        # add choose color button
        self.choose_color_btn = wx.Button(self.panel, label="Выбор цвета")
        # bind it to an event handler
        self.Bind(wx.EVT_BUTTON, self.on_choose_color, self.choose_color_btn)

        # put the button in a sizer and center it
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer()
        sizer.Add(self.choose_color_btn, 0, wx.CENTER)
        sizer.AddStretchSpacer()
        self.panel.SetSizer(sizer)

    def create_off_window_components(self):
        """ Create window components, such as menu and status bar. """
        self.create_menu()
        self.CreateStatusBar()
        self.set_title()

    def create_menu(self):
        """ Create menu of the app. """
        file_menu = wx.Menu()
        for menu_id, label, help_text, handler in \
            [
                    (
                        wx.ID_ABOUT,
                        '&О приложении',
                        'Информация о приложении',
                        self.on_about
                    ),
                    (
                        wx.ID_OPEN,
                        '&Палитра',
                        'Палитра',
                        self.on_open_palette
                    ),
                    (None, None, None, None),
                    (
                        wx.ID_EXIT,
                        '&Выход',
                        'Выход из приложения',
                        self.on_exit
                    )
            ]:
            if menu_id is None:
                file_menu.AppendSeparator()
            else:
                item = file_menu.Append(menu_id, label, help_text)
                self.Bind(wx.EVT_MENU, handler, item)

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, '&Файл') # Add the fileMenu to the MenuBar
        self.SetMenuBar(menu_bar)  # Add the menuBar to the Frame

    def set_title(self, title=None):
        """ Set title of the app """
        app_title = ''
        if title is not None:
            app_title = "%s - %s" % (self.app_name, title)
        else:
            app_title = self.app_name
        super(MainWindow, self).SetTitle(app_title)

    def show_color_code(self, code):
        """ Show color code in message dialog. """
        text = 'Вы выбрали цвет - %s' % ('#%02x%02x%02x' % code).upper()
        title = 'Выбранный цвет'
        dialog = wx.MessageDialog(
            self,
            text,
            title,
            wx.OK
        )
        dialog.ShowModal()
        dialog.Destroy()

    # Event handlers:
    def on_about(self, event):
        """ Open about dialog. """
        title = "Демо приложение на \"wxPython\""
        caption = 'О приложении'
        dialog = wx.MessageDialog(self, title, caption, wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def on_exit(self, event):
        """ Exit the app. """
        self.Close()  # Close the main window.

    def on_open_palette(self, event):
        """ Open palette window. """
        self.set_title('Палитра')
        self.Show()

    def on_choose_color(self, event):
        """ Handle 'choose' color button press. """
        dialog = wx.ColourDialog(self)
        # Ensure the full colour dialog is displayed,
        # not the abbreviated version.
        dialog.GetColourData().SetChooseFull(True)

        if dialog.ShowModal() == wx.ID_OK:
            color_code = dialog.GetColourData().GetColour().Get()
            self.show_color_code(color_code)

        dialog.Destroy()

if __name__ == '__main__':
    # run the app if module is called directly
    app = wx.App()
    frame = MainWindow()
    app.MainLoop()

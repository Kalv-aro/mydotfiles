from libqtile import widget
from .themes import *
from libqtile.command import lazy
from qtile_extras import widget as ewidget

widget_defaults = dict(
    font = "sans",
    fontsize = 14,
    padding_x = 8,
    background = Cbar,    
)
extension_defaults = widget_defaults.copy()

##mouse callbacks
def calendar(qtile):
    qtile.cmd_spawn('~/.config/eww/manythings/launchcal')

widgets = [

   widget.GroupBox(
             fontsize = 35,
             margin_x = 10,
             highlight_method = "block",
             background = Cgroups,
             foreground = Cbar,
             ),

   widget.Sep(
             background = Cbar,
             foreground = Cbar,
             linewidth = 100, 
             ),

   widget.TaskList(
             icon_size = 25, 
             max_title_width = 130,
             highlight_method = "block",
             border = CTask,
             foreground = Ctext,
             margin = 0,
             padding = 7, 
             ),

   widget.Sep(
             background = Cbar,
             foreground = Cbar,
             linewidth = 100, 
             ),

   widget.TextBox(
             fmt = border,
             foreground = Cwidget2,
             fontsize = 34,
             padding = 0,
             ),

   widget.MemoryGraph(

              background = Cwidget2,
              fill_color = Cwidget1,
              
              ),        


   widget.TextBox(
             fmt = border,
             foreground = Cwidget1,
             background = Cwidget2,
             fontsize = 34,
             padding = 0,
             ),

   widget.ThermalSensor(
             background = Cwidget1,
             foreground = "#000000",
  
             ),


   widget.TextBox(
             fmt = border,
             foreground = Cwidget2,
             background = Cwidget1,
             fontsize = 34,
             padding = 0,
             ),

   widget.Net(
             interface = interface,
             format = '{down} ↓↑ {up}',
             foreground = Ctext,
             background = Cwidget2,
             padding = 5,
             prefix = "M"
             ),


   widget.TextBox(
             fmt = border,
             foreground = Cwidget1,
             fontsize = 34,
             padding = 0,
             background = Cwidget2,
             ),



   widget.Clock(
             foreground = Ctext,
             background = Cwidget1,
             format = "%d/%m - %H:%M",
             mouse_callbacks = {'Button1': lazy.spawn("~/.config/eww/manythings/launchcal")},
             ),

   widget.TextBox(
             fmt = border,
             foreground = Cwidget2,
             background = Cwidget1,
             fontsize = 34,
             padding = 0,
             ),

  widget.PulseVolume(

              emoji=True,
              background=Cwidget2,
              foreground="#000000"

          ),

  ewidget.UPowerWidget(background = Cwidget2),

  widget.LaunchBar(
             foreground = Ctext,
             background = Cwidget2,
             default_icon = '~/images/power.png',
             progs = [('shutdown 0', '~/.config/eww/dashboard/launch_dashboard', 'logout from qtile')] 

             ),
]


    

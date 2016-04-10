# i3history

Implements a navigation history (think forward/backward in your browser) for
i3wm workspaces.


## Installation

Via pip:

    pip install git+git://github.com/pb-/i3history


## Running

You will probably want to put this into some startup file:

    i3history &


## Configuration

Add to your i3 config (this will bind i and o, just like the Vim jumplist):

    bindsym $mod+o nop history_backward
    bindsym $mod+i nop history_forward

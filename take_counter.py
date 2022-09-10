"""
Functions for track_counter ui

copyright: Parker J. Roberts - 2022
"""

from counter import Counter
import tkinter as tk


def counter_increm(x,label,root):
    """
    Increment counter by 01 and update label.

    Parameters
    ----------
    x : Counter object
        stores number to display
    label : TK Label object
        text to display take number
    root : TK interface object
        window for gui

    Returns
    -------
    None.

    """
    x.increm()
    msg = f'Take {x.count:02.0f}'
    update_label(msg,root)


def counter_reset(x,label,root):
    """
    Reset counter to 01 and update window.

    Parameters
    ----------
    x : Counter object
        stores number to display
    label : TK Label object
        text to display take number
    root : TK interface object
        window for gui

    Returns
    -------
    None.

    """
    x.reset()
    msg = f'Take {x.count:02.0f}'
    update_label(msg,root)


def update_label(msg,root):
    """
    Update label on window with message.

    Parameters
    ----------
    msg : string
        text to display on window
    root : TK interface object
        window for gui

    Returns
    -------
    label: Tk Label object
        text display for ui

    """
    label = tk.Label(root, text=msg, font=("Arial",50))
    label.grid(row=0, column=0, columnspan=6)
    return label    


def launch_box():
    """
    Initialize and run take counter gui

    Returns
    -------
    None.

    """
    
    # Initialize interface
    root = tk.Tk()
    root.geometry("250x150")
    root.title("Take Counter")

    # Initialize counter + display
    x = Counter()
    init_str = f'Take {x.count:02.0f}'
    label = update_label(init_str,root)

    # Add increment button
    btn_inc = tk.Button(root, text="+1",\
                        command=lambda: counter_increm(x,label,root),\
                        width=5, font=("Arial", 24))
    btn_inc.grid(row=1,column=0,columnspan=3)

    # Add reset button
    btn_rst = tk.Button(root, text="Reset",\
                        command=lambda: counter_reset(x,label,root),\
                        width=5, font=("Arial", 24))
    btn_rst.grid(row=1,column=3,columnspan=3)

    # Run box
    root.mainloop()


import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg


def make_empty_plot():
    fig = plt.figure()

    ax = fig.add_subplot()

    x = np.arange(0, 2*np.pi, 0.05*np.pi)

    plt.show(block=False)

    return fig, ax, x


def update_plot(offset, fig, ax, x):
    ax.clear()
    ax.plot(x+offset, np.sin(x+offset))
    plt.show(block=False)


def main():
    layout = [
        [sg.Slider(range=(0,100), default_value=0, resolution=1, orientation='horizontal', enable_events=True, key='-time_slider-')],
    ]

    window = sg.Window('surfing', layout, finalize=True)

    fig, ax, x = make_data_fig()
    while True:
        event, values = window.read()

        if event in (None, 'Cancel'):
            break

        elif event == '-time_slider-':
            draw_plot(values['-time_slider-'], fig, ax, x)

    window.close()


if __name__ == '__main__':
    main()
import glob
from os import path
import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from tqdm import tqdm


def make_empty_plot():
    fig = plt.figure()

    ax = fig.add_subplot(projection='3d')

    plt.show(block=False)

    return ax


def load_data(dirname):
    files = glob.glob(path.normpath(f'{dirname}/*.dat'))

    if len(files) == 0:
        print('file not found')
        return
    
    common = path.commonprefix(files)
    print(f'common filename: {common}')

    frames = [None] * len(files)
    print(f'{len(files)} frames found')

    for f in tqdm(files):
        frame_num = int(f[len(common):-4]) # -4: len('.dat'))
        frames[frame_num] = np.loadtxt(f)
    
    return frames


def make_grid(frame):
    assert frame.ndim == 2

    #### *.dat ####
    #  x →
    # y
    # ↓
    x = np.arange(frame.shape[1])
    y = np.arange(frame.shape[0])

    return np.meshgrid(x, y)


def update_plot(X, Y, Z, ax):
    ax.clear()
    ax.plot_surface(X, Y, Z)
    plt.show(block=False)


def main():
    layout = [
        [sg.Button('Data Dir')],
        [sg.Slider(range=(0,1), default_value=0, resolution=1, orientation='horizontal', enable_events=True, key='time_slider', disabled=True)],
    ]

    window = sg.Window('surfing', layout, finalize=True)

    ax = make_empty_plot()

    while True:
        event, values = window.read()

        if event in (None, 'Cancel'):
            break
        
        elif event == 'Data Dir':
            dirname = sg.popup_get_folder('Data directory')
            frames = load_data(dirname)
            X, Y = make_grid(frames[0])
            window['time_slider'].update(range=(0, len(frames)-1), disabled=False)
            update_plot(X, Y, frames[0], ax)

        elif event == 'time_slider':
            update_plot(X, Y, frames[int(values['time_slider'])], ax)

    window.close()


if __name__ == '__main__':
    main()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import argparse


def _3d_series_electrons():
    """Returns first transition period / 3d series data: curves points,
    elements symbol, Z range, principal quantum number, annotation coordinates.

    Returns
    -------
    tuple
        curves points, elements symbol, Z range (min and max), principal
        quantum number, annotation coordinates.
    """

    df = pd.read_csv("data/rich3d.csv")
    elements = ['Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn']
    Zmin = 21
    Zmax = 30
    N = 4

    electrons_sa = [['1', 21, 0.54], ['1', 22, 0.48], ['1', 23, 0.45],
                    ['1', 24, 0.40], ['1', 25, 0.35], ['1', 26, 0.32],
                    ['1', 27, 0.32], ['1', 28, 0.27], ['1', 29, 0.24],
                    ['1', 30, 0.20]]

    electrons_sb = [['1', 21, 0.63], ['1', 22, 0.58], ['1', 23, 0.52],
                    ['', 24, 0.50], ['1', 25, 0.47], ['1', 26, 0.45],
                    ['1', 27, 0.41], ['1', 28, 0.36], ['', 29, 0.35],
                    ['1', 30, 0.30]]

    electrons_da = [['1', 21, 0.80], ['2', 22, 0.68], ['3', 23, 0.58],
                    ['5', 24, 0.47], ['5', 25, 0.41], ['5', 26, 0.37],
                    ['5', 27, 0.26], ['5', 28, 0.19], ['5', 29, 0.13],
                    ['5', 30, 0.08]]

    electrons_db = [['', 21, 0.97], ['', 22, 0.85], ['', 23, 0.75],
                    ['', 24, 0.66], ['', 25, 0.59], ['1', 26, 0.53],
                    ['2', 27, 0.46], ['3', 28, 0.41], ['5', 29, 0.30],
                    ['5', 30, 0.25]]

    return (df, elements, Zmin, Zmax, N, electrons_sa, electrons_sb,
            electrons_da, electrons_db)


def _4d_series_electrons():
    """Returns second transition period / 4d series data: curves points,
    elements symbol, Z range, principal quantum number, annotation coordinates.

    Returns
    -------
    tuple
        curves points, elements symbol, Z range (min and max), principal
        quantum number, annotation coordinates.
    """

    df = pd.read_csv("data/rich4d.csv")
    elements = ['Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd']
    Zmin = 39
    Zmax = 48
    N = 5

    electrons_sa = [['1', 39, 0.55], ['1', 40, 0.49], ['1', 41, 0.46],
                    ['1', 42, 0.43], ['1', 43, 0.43], ['1', 44, 0.40],
                    ['1', 45, 0.37], ['', 46, 0.35], ['1', 47, 0.32],
                    ['1', 48, 0.30]]

    electrons_sb = [['1', 39, 0.63], ['1', 40, 0.58], ['', 41, 0.58],
                    ['', 42, 0.53], ['1', 43, 0.53], ['', 44, 0.52],
                    ['', 45, 0.47], ['', 46, 0.45], ['', 47, 0.42],
                    ['1', 48, 0.40]]

    electrons_da = [['1', 39, 0.80], ['2', 40, 0.68], ['4', 41, 0.54],
                    ['5', 42, 0.47], ['5', 43, 0.39], ['5', 44, 0.32],
                    ['5', 45, 0.25], ['5', 46, 0.18], ['5', 47, 0.10],
                    ['5', 48, 0.04]]

    electrons_db = [['', 39, 0.97], ['', 40, 0.85], ['', 41, 0.75],
                    ['', 42, 0.66], ['', 43, 0.59], ['2', 44, 0.48],
                    ['3', 45, 0.41], ['5', 46, 0.32], ['5', 47, 0.26],
                    ['5', 48, 0.18]]

    return (df, elements, Zmin, Zmax, N, electrons_sa, electrons_sb,
            electrons_da, electrons_db)


def _5d_series_electrons():
    """Returns third transition period / 5d series data: curves points,
    elements symbol, Z range, principal quantum number, annotation coordinates.

    Returns
    -------
    tuple
        curves points, elements symbol, Z range (min and max), principal
        quantum number, annotation coordinates.
    """

    df = pd.read_csv("data/rich5d.csv")
    elements = ['Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg']
    Zmin = 71
    Zmax = 80
    N = 6

    electrons_sa = [['1', 71, 0.39], ['1', 72, 0.38], ['1', 73, 0.36],
                    ['1', 74, 0.33], ['1', 75, 0.33], ['1', 76, 0.31],
                    ['1', 77, 0.30], ['1', 78, 0.27], ['1', 79, 0.24],
                    ['1', 80, 0.24]]

    electrons_sb = [['1', 71, 0.49], ['1', 72, 0.47], ['1', 73, 0.45],
                    ['1', 74, 0.42], ['1', 75, 0.44], ['1', 76, 0.40],
                    ['1', 77, 0.37], ['', 78, 0.35], ['', 79, 0.32],
                    ['1', 80, 0.32]]

    electrons_da = [['1', 71, 0.80], ['2', 72, 0.68], ['3', 73, 0.58],
                    ['4', 74, 0.47], ['5', 75, 0.39], ['5', 76, 0.36],
                    ['5', 77, 0.26], ['5', 78, 0.19], ['5', 79, 0.13],
                    ['5', 80, 0.08]]

    electrons_db = [['', 71, 0.97], ['', 72, 0.85], ['', 73, 0.75],
                    ['', 74, 0.66], ['', 75, 0.59], ['1', 76, 0.48],
                    ['2', 77, 0.41], ['4', 78, 0.34], ['5', 79, 0.28],
                    ['5', 80, 0.20]]

    return (df, elements, Zmin, Zmax, N, electrons_sa, electrons_sb,
            electrons_da, electrons_db)


def _plot_params(Zmin, Zmax):
    """Plot parameters (grid, labels, ticks).

    Parameters
    ----------
    Zmin : float
        Atomic number of the first element of the series
    Zmax : float
        Atomic number of the last element of the series

    Returns
    -------
    Matplotlib objects
        Fig and ax
    """

    fig, axarr = plt.subplots(figsize=(14, 10), nrows=1, ncols=1)
    ax = axarr

    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(1.5)

    ax.grid(b=True, axis='x', which='major', linestyle='--', linewidth=2.0)
    ax.tick_params(axis='x', labelsize=16, length=6, which='major', width=1.5)
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.set_xlabel('Atomic number', size=18)
    ax.set_ylabel('Energy', size=18)
    ax.set_xticks(np.arange(Zmin, Zmax+1, 1))
    ax.set_xlim(Zmin-0.7, Zmax + 0.3)
    ax.set_ylim(0, 1.1)

    return fig, ax


def rich_suter_plot(series, save=False):
    """Plots Rich and Suter diagrams.

    Parameters
    ----------
    series : string
        3d, 4d or 5d
    save : bool, optional
        Option to save the diagram in the current folder, by default False

    Raises
    ------
    ValueError
        If the series is not in ['3d', '4d' or '5d']
    """

    if series == '3d':
        series_data = _3d_series_electrons()
        figname = 'rich_suter_3d'
    elif series == '4d':
        series_data = _4d_series_electrons()
        figname = 'rich_suter_4d'
    elif series == '5d':
        series_data = _5d_series_electrons()
        figname = 'rich_suter_5d'
    else:
        raise ValueError('Not a valid transition metal series!')

    df, elements, Zmin, Zmax, N, electrons_sa, electrons_sb, electrons_da, electrons_db = series_data

    fig, ax = _plot_params(Zmin, Zmax)

    ax.plot(df['x'], df['Curve1'], linewidth=3.5)
    ax.plot(df['x'], df['Curve2'], linewidth=3.5)
    ax.plot(df['x'], df['Curve3'], linewidth=3.5)
    ax.plot(df['x'], df['Curve4'], linewidth=3.5)

    for Z in range(Zmin, Zmax+1):
        label = elements[Z-Zmin]
        ax.annotate(label, (Z, 1.05), va='center', ha='center',
                    fontsize=18, backgroundcolor='lightgray')

    label_colors = ['mistyrose', 'honeydew', 'papayawhip', 'lightcyan']

    curve_label = [[r'${0:0}s\alpha$'.format(N), electrons_sa[0][2]],
                   [r'${0:0}s\beta$'.format(N), electrons_sb[0][2]],
                   [r'${0:0}d\alpha$'.format(N-1), electrons_da[0][2]],
                   [r'${0:0}d\beta$'.format(N-1), electrons_db[0][2]]]

    for i in range(4):
        ax.annotate(curve_label[i][0],
                    (Zmin - 0.4, curve_label[i][1]), va='center', ha='center',
                    fontsize=16, backgroundcolor=label_colors[i])

    for i in range(10):
        ax.annotate(electrons_sa[i][0], (electrons_sa[i][1],
                                         electrons_sa[i][2]),
                    va='center', ha='center', fontsize=16,
                    backgroundcolor=label_colors[0])
        ax.annotate(electrons_sb[i][0], (electrons_sb[i][1],
                                         electrons_sb[i][2]),
                    va='center', ha='center', fontsize=16,
                    backgroundcolor=label_colors[1])
        ax.annotate(electrons_da[i][0], (electrons_da[i][1],
                                         electrons_da[i][2]),
                    va='center', ha='center', fontsize=16,
                    backgroundcolor=label_colors[2])
        ax.annotate(electrons_db[i][0], (electrons_db[i][1],
                                         electrons_db[i][2]),
                    va='center', ha='center', fontsize=16,
                    backgroundcolor=label_colors[3])

    ax.set_title(
        'Rich-Suter diagrams for isolated atoms in ground state - {} period'.format(series), size=18)

    if save:
        fig.savefig(figname, bbox_inches='tight', dpi=300)

    plt.show()


def _clielement():
    """
    CLI for rich_suter
    """

    parser = argparse.ArgumentParser(prog='Rich-Suter diagram plotter')
    parser.add_argument('series', help='Transition series: 3d, 4d or 5d')
    parser.add_argument('-s', '--save', action='store_true',
                        help='Saves figure in current folder')
    args = parser.parse_args()

    rich_suter_plot(args.series, save=args.save)


if __name__ == "__main__":
    _clielement()

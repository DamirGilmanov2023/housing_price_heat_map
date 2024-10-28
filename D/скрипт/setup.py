# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('draw_heatmap.py')]

setup(name='draw_heatmap',
      version='0.0.9',
      description='',
      executables=executables)
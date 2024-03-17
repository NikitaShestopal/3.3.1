from Loaderapparation import apparation

file_name = 'input01.txt'
figures = apparation.read_figures(file_name)
max_volume_figure = apparation.find_max_volume_figure(figures)


print(f"Figure with most volume: {type(max_volume_figure).__name__}")
print(f"Volume: {max_volume_figure.volume()}")
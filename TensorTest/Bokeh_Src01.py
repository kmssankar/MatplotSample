from bokeh.plotting import figure, output_file, show

# output to static HTML file
output_file("line.html")

p = figure(plot_width=800, plot_height=400)
p.border_fill_color = 'black'
p.background_fill_color = 'black'
p.outline_line_color = 'white'
p.grid.grid_line_color = 'white'
# add a circle renderer with a size, color, and alpha
p.line([10, 25, 33, 54, 95], [36, 47, 112, 24, 45],line_width=2, color="blue", alpha=0.5)

# show the results
show(p)
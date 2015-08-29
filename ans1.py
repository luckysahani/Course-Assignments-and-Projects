dimensions_skyline_list=[];
window_size=0;
with open('query1.txt') as f:
    temp_list = [[int(x) for x in line.split()] for line in f];
    dimensions_skyline_list = temp_list[0];
    window_size = temp_list[0][0]
print window_size,dimensions_skyline_list
set terminal png size 800,500 enhanced font "Helvetica,20"

#set terminal postscript enhanced
set output 'data_average_write_throughput_1_0.png'

set xtics font "Times-Roman, 20"
set ytics font "Times-Roman, 20"

red = "#FF0000"; green = "#00FF00"; blue = "#0000FF"; skyblue = "#87CEEB"; salmonred = "#fa8072";
set yrange [4:16]
set style data histogram
set style histogram cluster gap 1.0 errorbars
set style fill solid
set boxwidth 0.9 absolute
set xtics format ""
set grid

set key at 4.5, 15 vertical maxrows 2 font "Times-Roman, 24" title "K/N Ratio"
set ylabel "Average Write Throughput (MB/sec)" offset 2, 0
set xlabel 'Block Size' offset 2, 0

plot "data_write_throughput_1_0.dat" using 2:7:xtic(1)  title "1/1" lw 2 linecolor rgb 'grey60' fs pattern 4,\
     "data_write_throughput_1_0.dat" using 3:8:xtic(1)  title "2/3" lw 2 linecolor rgb 'grey50' fs pattern 5,\
     "data_write_throughput_1_0.dat" using 4:9:xtic(1)  title "3/5" lw 2 linecolor rgb 'grey50' fs pattern 6,\
     "data_write_throughput_1_0.dat" using 5:10:xtic(1) title "5/7" lw 2 linecolor rgb 'grey50' fs pattern 7,\
     "data_write_throughput_1_0.dat" using 6:11:xtic(1) title "7/9" lw 2 linecolor rgb 'grey50' fs pattern 9,\



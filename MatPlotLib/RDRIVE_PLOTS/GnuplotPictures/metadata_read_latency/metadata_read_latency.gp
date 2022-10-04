set terminal png size 800,500 enhanced font "Helvetica,20"

#set terminal postscript enhanced
set output 'metadata_average_read_latency_1_0.png'

set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"

red = "#FF0000"; green = "#00FF00"; blue = "#0000FF"; skyblue = "#87CEEB"; salmonred = "#fa8072";
set yrange [11:16.5]
set style data histogram
set style histogram cluster gap 1.0 errorbars
set style fill solid
set boxwidth 0.9 absolute
set xtics format ""
set grid

set key at 6.0, 16.3 vertical maxrows 1 font "Times-Roman, 24" title "Number of Servers"
set ylabel "Average Read Latency (ms)" offset 2, 0
set xlabel 'Metadata Size' offset 2, 0

plot "metadata_read_latency.dat" using 2:7:xtic(1)  title "1" lw 2 linecolor rgb 'grey60' fs pattern 4,\
     "metadata_read_latency.dat" using 3:8:xtic(1)  title "3" lw 2 linecolor rgb 'grey50' fs pattern 5,\
     "metadata_read_latency.dat" using 4:9:xtic(1)  title "5" lw 2 linecolor rgb 'grey50' fs pattern 6,\
     "metadata_read_latency.dat" using 5:10:xtic(1) title "7" lw 2 linecolor rgb 'grey50' fs pattern 7,\
     "metadata_read_latency.dat" using 6:11:xtic(1) title "9" lw 2 linecolor rgb 'grey50' fs pattern 9,\



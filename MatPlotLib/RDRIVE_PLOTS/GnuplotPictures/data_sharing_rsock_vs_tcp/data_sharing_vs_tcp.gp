set terminal png size 800,500 enhanced font "Helvetica,20"

#set terminal postscript enhanced
set output 'average_data_sharing_delay.png'

set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"

red = "#FF0000"; green = "#00FF00"; blue = "#0000FF"; skyblue = "#87CEEB"; salmonred = "#fa8072";
set yrange [0:25]
set style data histogram
set style histogram cluster gap 1.0 errorbars
set style fill solid
set boxwidth 0.9
set xtics format ""
set grid

set key at 5.0, 23.5 vertical maxrows 1 font "Times-Roman, 24"
set ylabel "Ave. Sharing Delay (Min)" offset 2, 0
set xlabel 'Prob. of Link Availability' offset 2, 0

plot "data_sharing_vs_tcp.dat" using 2:($2-$4):($2+$5):xtic(1) title "RSock" lw 2 linecolor rgb 'grey60' fs pattern 4,\
     "data_sharing_vs_tcp.dat" using 3:($3-$6):($3+$7):xtic(1) title "TCP"   lw 2 linecolor rgb 'grey50' fs pattern 5,\



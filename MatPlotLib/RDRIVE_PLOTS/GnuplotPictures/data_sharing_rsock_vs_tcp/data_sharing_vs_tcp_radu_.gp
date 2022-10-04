set terminal postscript eps color
set output 'average_data_sharing_delay.eps'

set yrange [0:25]
set style data histogram
set style histogram cluster gap 1.0 errorbars
set style fill solid
set boxwidth 0.9
set xtics format ""

set key font "Times-Roman, 24"
set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"

set key at 5.0, 23.5 vertical maxrows 1 font "Times-Roman, 24"
set ylabel "Data Sharing Delay [min]" font "Times-Roman, 26" 
set xlabel "Link Availability" font "Times-Roman, 26" 

plot "data_sharing_vs_tcp.dat" using 2:($2-$4):($2+$5):xtic(1) title "RSock" lw 2 linecolor rgb 'red' fs pattern 4,\
     "data_sharing_vs_tcp.dat" using 3:($3-$6):($3+$7):xtic(1) title "TCP"   lw 2 linecolor rgb 'blue' fs pattern 5,\



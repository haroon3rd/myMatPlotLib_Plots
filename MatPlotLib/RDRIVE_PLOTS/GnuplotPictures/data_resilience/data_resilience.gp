set terminal png size 800,500 enhanced font "Helvetica,20"

#set terminal postscript enhanced
set output 'data_resilience.png'

set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"

red = "#FF0000"; green = "#00FF00"; blue = "#0000FF"; skyblue = "#87CEEB"; salmonred = "#fa8072";
set yrange [0:115]
set style data histogram
set style histogram gap 1.0 errorbars
set style fill solid
set boxwidth 0.9
set grid

set key top left title "Code Rate" vertical maxrows 3 font "Times-Roman, 22"
#set key off
set ylabel "File Retrieval Success Rate" offset 2, 0
set xlabel 'Device Availability' offset 2, 0
set offset -0.5,-0.5,0,0

plot "data_resilience_0_2.dat" using 2:3:xtic(1) title "0.2" lw 3 linecolor rgb 'grey70' fs pattern 4,\
     "data_resilience_0_4.dat" using 2:3:xtic(1) title "0.4" lw 3 linecolor rgb 'grey70' fs pattern 5,\
     "data_resilience_0_6.dat" using 2:3:xtic(1) title "0.6" lw 3 linecolor rgb 'grey70' fs pattern 6,\
     "data_resilience_0_8.dat" using 2:3:xtic(1) title "0.8" lw 3 linecolor rgb 'grey70' fs pattern 7,\
     "data_resilience_1_0.dat" using 2:3:xtic(1) title "1.0" lw 3 linecolor rgb 'grey70' fs pattern 9,\



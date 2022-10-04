set terminal png size 800,500 enhanced font "Helvetica,20"

#set terminal postscript enhanced
set output 'ave_n_k_10.png'

set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"

red = "#FF0000"; green = "#00FF00"; blue = "#0000FF"; skyblue = "#87CEEB"; salmonred = "#fa8072";
set yrange [5:10]
set style data histogram
set style histogram cluster gap 1.0 errorbars
set style fill solid
set boxwidth 0.9
set xtics format ""
set grid

set key at 0.8, 9.5 vertical maxrows 2 font "Times-Roman, 24"
set ylabel "N and K" offset 2, 0
set xlabel 'w_a' offset 2, 0

plot "ave_n_k_10.dat" using 2:4:xtic(1) title "N" lw 2 linecolor rgb 'grey60' fs pattern 4,\
     "ave_n_k_10.dat" using 3:5:xtic(1) title "K" lw 2 linecolor rgb 'grey50' fs pattern 5,\



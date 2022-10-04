
set terminal postscript eps color
set output 'ave_n_k_10.eps'

set style data histogram
set style histogram cluster gap 1.0 errorbars
set style fill solid
set boxwidth 0.9
set xtics format ""

set key font "Times-Roman, 24"
set key left top
set ylabel 'k, n' font "Times-Roman, 26" 
set xlabel 'w_a' font "Times-Roman,26"
set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"

set yrange [5:10.5]

plot "ave_n_k_10.dat" using 3:5:xtic(1) title 'k' lw 2 linecolor rgb 'red' fs pattern 1,\
     "ave_n_k_10.dat" using 2:4:xtic(1) title 'n' lw 2 linecolor rgb 'blue'  fs pattern 4,\



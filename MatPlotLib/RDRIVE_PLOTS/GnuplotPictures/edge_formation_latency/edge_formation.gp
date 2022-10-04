set terminal postscript eps color
set output 'edge_formation_latency.eps'

set xtics font "Times-Roman, 22" rotate by 45 right
set ytics font "Times-Roman, 22"
set ytics 10

set style data histogram 
set style histogram cluster gap 0 errorbars
set style fill solid
set boxwidth 0.9 relative
set xtics format ""

set ylabel "Edge Formation Latency [sec]" font "Times-Roman, 26"
set xlabel 'Replica Setting' font "Times-Roman, 26" offset -10, -2

plot newhistogram "", "edge_3replica.dat" using 2:3:xtic(1) t "3 Replica" lw 2 linecolor rgb 'red' fs pattern 1,\
newhistogram "", "edge_5replica.dat" using 2:3:xtic(1) t "5 Replica"  lw 2 linecolor rgb 'blue' fs pattern 2, \
newhistogram "", "edge_7replica.dat" using 2:3:xtic(1) t "7 Replica"  lw 2 linecolor rgb 'green' fs pattern 4

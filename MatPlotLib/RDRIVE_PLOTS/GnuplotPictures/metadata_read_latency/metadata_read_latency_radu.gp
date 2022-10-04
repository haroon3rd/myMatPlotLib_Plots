set terminal postscript eps color
set output 'metadata_average_read_latency_1_0.eps'

set style data histogram
set style histogram cluster gap 1.0 errorbars
set style fill solid
set boxwidth 0.9
set xtics format ""

set key font "Times-Roman, 24"
set key left top
set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"


set yrange [11:16]

set key vertical maxrows 1 font "Times-Roman, 24" title "Number of Replicas"
set ylabel 'Read Latency [msec]' font "Times-Roman, 26" 
set xlabel 'Metadata Size [KB]' font "Times-Roman,26"


plot "metadata_read_latency.dat" using 2:7:xtic(1)  title "1" lw 2 linecolor rgb 'red' fs pattern 4,\
     "metadata_read_latency.dat" using 3:8:xtic(1)  title "3" lw 2 linecolor rgb 'blue' fs pattern 5,\
     "metadata_read_latency.dat" using 4:9:xtic(1)  title "5" lw 2 linecolor rgb 'green' fs pattern 6,\
     "metadata_read_latency.dat" using 5:10:xtic(1) title "7" lw 2 linecolor rgb 'black' fs pattern 7,\
     "metadata_read_latency.dat" using 6:11:xtic(1) title "9" lw 2 linecolor rgb 'purple' fs pattern 9,\



set terminal postscript eps color
set output 'data_average_write_throughput_1_0.eps'

set yrange [4:16]
set style data histogram
set style histogram cluster gap 1.0 errorbars
set style fill solid
set boxwidth 0.9 absolute
set xtics format ""

set key font "Times-Roman, 24"
set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"

set key top left vertical maxrows 2 font "Times-Roman, 24" title "Code Rate (k/n)"
set ylabel "Write Throughput [MB/sec]"  font "Times-Roman, 26" 
set xlabel 'Block Size [KB]' font "Times-Roman,26"

plot "data_write_throughput_1_0.dat" using 2:7:xtic(1)  title "1/1" lw 2 linecolor rgb 'red' fs pattern 4,\
     "data_write_throughput_1_0.dat" using 3:8:xtic(1)  title "2/3" lw 2 linecolor rgb 'blue' fs pattern 5,\
     "data_write_throughput_1_0.dat" using 4:9:xtic(1)  title "3/5" lw 2 linecolor rgb 'green' fs pattern 6,\
     "data_write_throughput_1_0.dat" using 5:10:xtic(1) title "5/7" lw 2 linecolor rgb 'black' fs pattern 7,\
     "data_write_throughput_1_0.dat" using 6:11:xtic(1) title "7/9" lw 2 linecolor rgb 'purple' fs pattern 9 \


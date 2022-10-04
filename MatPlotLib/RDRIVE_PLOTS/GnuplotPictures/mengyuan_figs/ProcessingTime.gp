set style line 1 lt 1 lc rgb 'blue' # --- blue
#set style line 2 lt 2 lc rgb 'black'  lw 2  # --- black

set terminal postscript eps color
set grid lc '0x303030' lw 0.1
set notitle
set xrange [0:1000]
set xtics font ',30' 100
set xlabel 'Running Time (s)' font ',40' offset 0,-1

set yrange [1:1000000]
set format y "10^{%T}"
set logscale y
set ytics font ',30'
set ylabel 'AvgDelay (ms)' font ',40' offset -4,0
set key box
#set key out vert
set key font ',35' horiz right top
set output 'obs2_ProcessingTime.eps'
set size ratio 0.5
set object circle at 50,800 size 10 fc rgb "red"
set object circle at 170,46000 size 10 fc rgb "red"
set object circle at 500,800 size 10 fc rgb "red"
set object circle at 600,36000 size 10 fc rgb "red"
plot 'RandomShuffling.dat' u 1:3 w l lw 8 dt 2 lc 'red' t 'T0', \
     'RandomShuffling.dat' u 7:9 w l lw 8 dt "." lc 'blue' t 'T1',\
     'RandomShuffling.dat' u 10:12 w l lw 8 lc '0x006400' t 'T2',\
     'RandomShuffling.dat' u 4:6 w l lw 8 dt 3 lc 'black' t 'T3', 
     
unset key
unset output

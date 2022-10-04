set terminal png size 800,500 enhanced font "Helvetica,20"

#set terminal postscript enhanced
set output 'dir_serv_res.png'

set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"

red = "#FF0000"; green = "#00FF00"; blue = "#0000FF"; skyblue = "#87CEEB"; salmonred = "#fa8072";
set yrange [0:70]
set style data histogram
set style histogram cluster gap 1.0 errorbars
set style fill solid
set boxwidth 0.9
set xtics format ""
set grid


#set key at 0.7, 27.5 vertical maxrows 2 font "Times-Roman, 24"
set key off
set ylabel "Edge Formation Delay (sec)" offset 2, 0
set xlabel 'Replica' offset 2, 0


plot "dir_serv_res.dat" using 2:7:12:xtic(1)  lw 2 linecolor rgb 'grey60' fs pattern 4,\
     "dir_serv_res.dat" using 3:8:13:xtic(1)  lw 2 linecolor rgb 'grey50' fs pattern 5,\
     "dir_serv_res.dat" using 4:9:14:xtic(1)  lw 2 linecolor rgb 'grey50' fs pattern 6,\
     "dir_serv_res.dat" using 5:10:15:xtic(1)  lw 2 linecolor rgb 'grey50' fs pattern 7,\
     "dir_serv_res.dat" using 6:11:16:xtic(1)  lw 2 linecolor rgb 'grey50' fs pattern 9,\

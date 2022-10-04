
# Scale font and line width (dpi) by changing the size! It will always display stretched.
set terminal postscript
set output 'w-a_vs_fstr.eps'
set term post landscape
set grid
#set format y "%.2t"



# Key means label...
set xlabel 'w_a' font "Times-Roman,26"
set ylabel "F^'" font "Times-Roman, 26" 
set key left top 
set key font "Times-Roman, 24"
set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"
plot "wa_vs_fstr.txt" using 1:2 title 'Network Size: 10' with linespoint ls 4 lw 6,\
"wa_vs_fstr.txt" using 1:3 title 'Network Size: 20' with linespoints ls 2 lw 6,\
"wa_vs_fstr.txt" using 1:4 title 'Network Size: 30' with linespoints ls 3 lw 6



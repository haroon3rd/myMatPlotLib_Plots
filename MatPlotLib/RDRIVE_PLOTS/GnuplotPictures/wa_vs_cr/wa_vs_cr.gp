
# Scale font and line width (dpi) by changing the size! It will always display stretched.
set terminal postscript
set output 'w-a_vs_cr.eps'
set term post landscape
set grid
#set format y "%.2t"



# Key means label...
set xlabel 'w_a' font "Times-Roman,26"
set ylabel 'CR' font "Times-Roman, 26" 
set key right top 
set key font "Times-Roman, 24"
set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"



plot "wa_vs_cr_10.txt" title 'Network Size: 10' with yerrorlines ls 4 lw 6,\
     "wa_vs_cr_20.txt" title 'Network Size: 20' with yerrorlines ls 2 lw 6,\
     "wa_vs_cr_30.txt" title 'Network Size: 30' with yerrorlines ls 3 lw 6



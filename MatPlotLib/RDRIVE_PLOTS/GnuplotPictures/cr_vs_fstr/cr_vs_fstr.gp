
# Scale font and line width (dpi) by changing the size! It will always display stretched.
set terminal postscript
set output 'cr_vs_fstr.eps'
set term post landscape
set grid
#set format y "%.2t"


# Key means label...
set key inside bottom right
set xlabel 'Coding Rate (K/N)' font "Times-Roman,26"
set ylabel "Filesize after Erasure Coding F' (MB)" font "Times-Roman, 26"
set key right top 
set key font "Times-Roman, 24"
set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"
plot  "cr_vs_fstr.txt" using 1:2 title 'F=500MB' with line ls 1 lw 4,\



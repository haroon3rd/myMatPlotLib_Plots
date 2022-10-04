
# Scale font and line width (dpi) by changing the size! It will always display stretched.
set terminal postscript
set output 'cr_vs_cost.eps'
set term post landscape
set grid
#set format y "%.2t"


# Key means label...
set key inside bottom right
set xlabel 'Coding Rate (K/N)' font "Times-Roman,26"
set ylabel 'Cost' font "Times-Roman, 26"
set key right top 
set key font "Times-Roman, 24"
set xtics font "Times-Roman, 22"
set ytics font "Times-Roman, 22"
plot  "cr_vs_cost_1.txt" using 1:2 title 'w_a=1.0' with line ls 1 lw 5,\
      "cr_vs_cost_1.txt" using 1:3 title 'w_a=0.9' with linespoints ls 2 lw 5,\
      "cr_vs_cost_1.txt" using 1:4 title 'w_a=0.8' with linespoints ls 3 lw 5,\
      "cr_vs_cost_1.txt" using 1:5 title 'w_a=0.7' with linespoints ls 4 lw 5,\
      "cr_vs_cost_1.txt" using 1:6 title 'w_a=0.6' with linespoints ls 5 lw 5,\
      "cr_vs_cost_1.txt" using 1:7 title 'w_a=0.5' with linespoints ls 6 lw 5,\
      "cr_vs_cost_1.txt" using 1:8 title 'w_a=0.4' with linespoints ls 7 lw 5,\
      "cr_vs_cost_1.txt" using 1:9 title 'w_a=0.3' with linespoints ls 8 lw 5,\
      "cr_vs_cost_1.txt" using 1:10 title 'w_a=0.2' with linespoints ls 9 lw 5,\
      "cr_vs_cost_1.txt" using 1:11 title 'w_a=0.1' with linespoints ls 10 lw 5,\
      "cr_vs_cost_1.txt" using 1:12 title 'w_a=0.0' with linespoints ls 11 lw 5,\

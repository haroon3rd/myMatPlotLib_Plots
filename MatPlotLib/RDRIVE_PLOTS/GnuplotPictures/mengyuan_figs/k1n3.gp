set style line 1 linecolor rgb 'black'  linetype 1 linewidth 1 pointtype 1 pointsize 1.5
set style line 2 linecolor rgb 'green'  linetype 1 linewidth 1 pointtype 2 pointsize 1.5
set style line 3 linecolor rgb 'red'  linetype 3 linewidth 1 pointtype 3 pointsize 1.5
set style line 4 linecolor rgb 'blue' 	linetype 1 linewidth 1 pointtype 2 pointsize 1.5
set style line 5 linecolor rgb 'purple' linetype 1 linewidth 1 pointtype 5 pointsize 1.5
set style line 6 linecolor rgb 'orange' linetype 1 linewidth 1 pointtype 6 pointsize 1.5


set terminal postscript eps color

set xrange [0:1]
set xtics font ',35'
set xlabel 'Device Availability' font ',35' offset 0,-1.5

set yrange [0:1]
set ytics font ',35'
set ylabel 'System Availability' font ',35' offset -5,0

set key samplen 4 font ',35' right bottom

set lmargin at screen 0.15
set rmargin at screen 0.95
set tmargin at screen 0.15
set bmargin at screen 0.95
show margin

set output 'k1n3.eps'
set size ratio 1

f1(x) = 3*x-3*x**2+x**3
f2(x) = 1-(1-x)**5*(1+5*x)
f3(x) = x

plot f1(x) w l ls 3 lw 5 t 'k=1,n=3',\
	 f2(x) w l ls 4 dt 3 lw 5 t 'k=2,n=6',\
	 f3(x) w l ls 1 t 'base'

unset key
unset output

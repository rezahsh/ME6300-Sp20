set ylabel "axial velocity U (m/s)"
set xlabel "y (mm)"

plot '../postProcessing/singleGraph1/2000/line_U.xy' u 1:2 w linesp t "sss"
#replot 'postProcessing/sets/7.5/line_inlet_U_UMean.xy' u 1:4 w linesp

BEGIN {FS=","}
NR>1  {s+= $27}
NR<=15 { print $27 }
END {print s}

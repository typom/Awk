BEGIN {FS=","}
NR>1  {s+= $27}
END {print s}

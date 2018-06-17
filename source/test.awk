BEGIN {FS="," }
NR>1 && $19=="CUL" {print $0}

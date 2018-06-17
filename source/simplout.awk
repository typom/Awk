BEGIN {FS=",";FPAT = "([^,]+)|(\"[^\"]+\")"}
NR>1 && $16=="GAAP" {amount[$42 "-" $2 FS $5 FS $7 FS $12 FS $19 FS $29 FS $38]+=$27}
END {for (i in amount) print(i FS amount[i]) }

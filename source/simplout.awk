BEGIN {FS=",";FPAT = "[^,]*|\"[^\"]*\""}
NR==1 {print $42 " - " $2 FS $5 FS $7 FS $12 FS $28 FS $19 FS $35 FS $38 FS $39 FS $27}
NR>1 && $16=="GAAP" {amount[$42 " - " $2 FS $5 FS $7 FS $12 FS $28 FS $19 FS $35 FS $38 FS $39]+=$27}
END {for (i in amount) print(i FS amount[i]) }

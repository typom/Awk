BEGIN {
FS="," ;
FPAT = "([^,]+)|(\"[^\"]+\")"}
NR>1 && $16=="GAAP" {accounts[$19]=$21 FS $20 }
END {for (account in accounts) print(account FS accounts[account]) }

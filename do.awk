BEGIN {
    SUM = 0
    IFS=" "
}{
    SUM += $2
}
END {
    print SUM
}
cmd="sort -m -k1,1 -k2,2n"
for input in test1.gz test2.gz; do
    cmd="$cmd <(gunzip -c '$input')"
done
eval "$cmd" | gzip -c > test.gz

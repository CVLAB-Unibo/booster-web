for setup in balanced unbalanced
do
    for split in test
    do
        for occ in all noocc
        do
            for res in full quarter half
            do
                for cls in c0 c1 c2 c3 all
                do
                    echo "{% include tables/"$setup"_"$split"_"$occ"_"$res"_"$cls".html %}"
                    cp template.html "../"$setup"_"$split"_"$occ"_"$res"_"$cls".html"
                done
            done
        done
    done
done
import os

template = open("../template.html").readlines()
template = "".join(template)

for setup in ["balanced", "unbalanced"]:
    for split in ["test"]:
        for occ in ["all", "noocc"]:
            for res in ["full", "quarter"]:
                for c in ["c0", "c1", "c2", "c3", "all"]:
                    table = setup + "_" +split + "_" + occ + "_" + res + "_" + c
                    with open("../" + table + ".html", "w") as fout:
                        fout.write(
                            template.replace("id=\"id\"", "id=\"" + table + "\"")
                            )
                        
                        


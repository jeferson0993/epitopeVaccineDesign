def join_epitopes(epitopes, linker):
    return linker.join(epitopes)

def build_vaccine(adjuvant, ctl, htl, bcl,
                  ctl_linker, htl_linker, bcl_linker,
                  block_linker):

    ctl_block = join_epitopes(ctl, ctl_linker)
    htl_block = join_epitopes(htl, htl_linker)
    bcl_block = join_epitopes(bcl, bcl_linker)

    construct = (
        adjuvant +
        block_linker +
        ctl_block +
        htl_linker +
        htl_block +
        bcl_linker +
        bcl_block
    )

    return construct

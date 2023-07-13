def get_header_footer(file):
    """
    get number of headerlines and footerlines
    """

    header,footer = 0,0
    f = open(file)
    try:
        lines = f.readlines()
    except:
        print('Error: cannot read lines of file. Do you have some special characters in the file? Try removing them and rerun')

    CONTINUE_H,CONTINUE_F = True,True
    j = 0
    while CONTINUE_H or CONTINUE_F:
        line_h = lines[j]
        line_f = lines[-1-j]
        tmp_h = line_h.split()
        tmp_f = line_f.split()
        try:
            for i in range(len(tmp_h)):
                1/float(tmp_h[i]) # divide to ensure non-zero values
            CONTINUE_H = False
        except:
            header+=1
        try:
            for i in range(len(tmp_f)):
                1/float(tmp_f[i]) # divie to ensure non-zero values
            CONTINUE_F = False
        except:
            footer+=1
        j+=1

    return header,footer

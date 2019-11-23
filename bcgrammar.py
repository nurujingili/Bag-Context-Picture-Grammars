from numpy import inf
contolv=[1,1,0]
control_bag=[["S",("S","S","S","S1"),(1,1,0),(8,8,inf),(2,2,1)],
             ["S1",("S2","S2","S2","S2"),(0,0,1),(inf,inf,inf),(0,0,-1)],
             ["S2",("Clb","Crb","Clt","Crt"), (0,4,0), (inf,inf,inf), (0,0,0)],
           ["S",("Clb","Crb","Clt","Crt"), (0,8,0), (inf,inf,inf), (-1,0,0)],
           ["Clb",("w","b","b","b"),(-inf,-inf,-inf), (inf,inf,inf),(0,0,0)],
           ["Crb",("b","w","b","b"),(-inf,-inf,-inf), (inf,inf,inf),(0,0,0)],
           ["Clt",("b","b","w","b"),(-inf,-inf,-inf), (inf,inf,inf),(0,0,0)],
           ["Crt",("b","b","b","w"),(-inf,-inf,-inf), (inf,inf,inf),(0,0,0)]]
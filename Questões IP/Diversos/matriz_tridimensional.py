# 1 dimensao[] Uma Chave 
# 2 dimensoes [[]] Duas Chaves
# 3 dimensoes [[[]]] Tres Chaves

#Quando for dar print([#linha][#coluna][#profundidade])

mat =   [   
            [ #linha 0                  (Esse traco e todo dedicado para linhas)
                [ #coluna 0 da linha 0  (Esse traco e todo dedicado para colunas)
                    1,#profundidade o 
                    2 #profundidade 1
                ],
             
                [ #coluna 1 da linha 0
                    3,#profundidade 0
                    4 #profundidade 1
                ]
            ],
             
            [ #linha 1
                [#coluna 0 da linha 1
                    5,#profundidade 0
                    6 #profundidade 1
                ],
            
                [#coluna 1 da linha 1
                    7,#profundidade 0
                    8 #profundidade 1
                ]
            ]
        ]

print(mat[0][0][1])
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    return tbl0.shape[0]

def pregunta_02():
    return tbl0.shape[1]


def pregunta_03():
    tablaModificada = tbl0.groupby('_c1')['_c1'].count().head()
    return tablaModificada

def pregunta_04():
    return tbl0.groupby('_c1')['_c2'].mean()


def pregunta_05():
    return tbl0.groupby('_c1')['_c2'].max()


def pregunta_06():
    conteo = sorted(tbl1['_c4'].unique())
    conteo = [x.upper() for x in conteo]
    
    return conteo


def pregunta_07():
    return tbl0.groupby('_c1')['_c2'].sum()

def pregunta_08():
    tabla = tbl0.copy()
    tabla['suma'] = tabla['_c0'] + tabla['_c2']
    return tabla


def pregunta_09():
    tabla = tbl0.copy()
    tabla['year'] = tabla['_c3'].map(lambda x: x.split('-')[0])
    return tabla

def pregunta_10():
    tabla = {'_c2': []}

    tabla1 = tbl0[tbl0['_c1'] == 'A']
    listaA = [str(x) for x in sorted(list(tabla1['_c2']))]
    listaA = ":".join(listaA)
    tabla['_c2'].append(listaA)
    
    tabla1 = tbl0[tbl0['_c1'] == 'B']
    listaA = [str(x) for x in sorted(list(tabla1['_c2']))]
    listaA = ":".join(listaA)
    tabla['_c2'].append(listaA)
    
    tabla1 = tbl0[tbl0['_c1'] == 'C']
    listaA = [str(x) for x in sorted(list(tabla1['_c2']))]
    listaA = ":".join(listaA)
    tabla['_c2'].append(listaA)
    
    tabla1 = tbl0[tbl0['_c1'] == 'D']
    listaA = [str(x) for x in sorted(list(tabla1['_c2']))]
    listaA = ":".join(listaA)
    tabla['_c2'].append(listaA)
    
    tabla1 = tbl0[tbl0['_c1'] == 'E']
    listaA = [str(x) for x in sorted(list(tabla1['_c2']))]
    listaA = ":".join(listaA)
    tabla['_c2'].append(listaA)
    tabla = pd.DataFrame(tabla, index=pd.Series(["A", "B", "C", "D", "E"], name="_c1"))
    return tabla

print(pregunta_10())
def pregunta_11():
    tabla = {'_c0': sorted(tbl1['_c0'].unique()),'_c4': []}
    
    for i in range(40):
        tabla1 = tbl1[tbl1['_c0'] == i]
        listaA = sorted(list(tabla1['_c4']))
        listaA = ",".join(listaA)
        tabla['_c4'].append(listaA)
    
    tabla = pd.DataFrame(tabla)
    return tabla


def pregunta_12():
    tabla = {'_c0': [x for x in range(40)], '_c5': []}
    
    for i in range(40):
        tabla1 = tbl2[tbl2['_c0'] == i]
        lista1 = [str(x) for x in list(tabla1['_c5b'])]
        lista2 = list(tabla1['_c5a'])
        lista3 = []
        for j in range(len(lista1)): lista3.append(lista2[j] + ':' + lista1[j])
        listaA = ",".join(sorted(lista3))
        tabla['_c5'].append(listaA)
    
    tabla = pd.DataFrame(tabla)
    return tabla


def pregunta_13():
    tabla = pd.merge(tbl0, tbl2, on = '_c0')
    tabla2 = tabla.groupby('_c1')['_c5b'].sum()
    return tabla2
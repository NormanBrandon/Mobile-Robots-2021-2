import os

branches = ['bautista_lopez',
            'alvarado_ramos',
            'alvarez_perez',
            'carranza_castillo',
            'guzman_santiago',
            'mendoza_suarez',
            'orozco_garcia',
            'colohua_carvajal',
            'guzman_martinez',
            'monterrubio_lopez',
            'alvarado_esquivel',
            'castillo_sanchez',
            'corona_molina',
            'espinobarros_peralta',
            'lopez_gonzalez',
            'pastor_olivera',
            'rojas_mosqueda',
            'gonzalez_mendoza',
            'hernandez_luviano',
            'saldana_hernandez']

for b in branches:
    os.system('git checkout ' + b)
    os.system('git pull origin ' + b)

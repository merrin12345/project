# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)
'''Output
             Unnamed: 0   mpg  cyl   disp   hp  ...    qsec  vs  am  gear  carb
0             Mazda RX4  21.0    6  160.0  110  ...   16.46   0   1     4     4
1         Mazda RX4 Wag  21.0    6  160.0  110  ...   17.02   0   1     4     4
2            Datsun 710  22.8    4  108.0   93  ...   18.61   1   1     4     1
3        Hornet 4 Drive  21.4    6  258.0  110  ...   19.44   1   0     3     1
4     Hornet Sportabout  18.7    8  360.0  175  ...   17.02   0   0     3     2
5               Valiant  18.1    6  225.0  105  ...   20.22   1   0     3     1
6            Duster 360  14.3    8  360.0  245  ...   15.84   0   0     3     4
7             Merc 240D  24.4    4  146.7   62  ...   20.00   1   0     4     2
8              Merc 230  22.8    4  140.8   95  ...   22.90   1   0     4     2
9              Merc 280  19.2    6  167.6  123  ...   18.30   1   0     4     4
10            Merc 280C  17.8    6  167.6  123  ...   18.90   1   0     4     4
11           Merc 450SE  16.4    8  275.8  180  ...   17.40   0   0     3     3
12           Merc 450SL  17.3    8  275.8  180  ...   17.60   0   0     3     3
13          Merc 450SLC  15.2    8  275.8  180  ...   18.00   0   0     3     3
14   Cadillac Fleetwood  10.4    8  472.0  205  ...   17.98   0   0     3     4
15  Lincoln Continental  10.4    8  460.0  215  ...   17.82   0   0     3     4
16    Chrysler Imperial  14.7    8  440.0  230  ...   17.42   0   0     3     4
17             Fiat 128  32.4    4   78.7   66  ...   19.47   1   1     4     1
18          Honda Civic  30.4    4   75.7   52  ...   18.52   1   1     4     2
19       Toyota Corolla  33.9    4   71.1   65  ...   19.90   1   1     4     1
20        Toyota Corona  21.5    4  120.1   97  ...   20.01   1   0     3     1
21     Dodge Challenger  15.5    8  318.0  150  ...   16.87   0   0     3     2
22          AMC Javelin  15.2    8  304.0  150  ...   17.30   0   0     3     2
23           Camaro Z28  13.3    8  350.0  245  ...   15.41   0   0     3     4
24     Pontiac Firebird  19.2    8  400.0  175  ...   17.05   0   0     3     2
25            Fiat X1-9  27.3    4   79.0   66  ...   18.90   1   1     4     1
26        Porsche 914-2  26.0    4  120.3   91  ...   16.70   0   1     5     2
27         Lotus Europa  30.4    4   95.1  113  ...   16.90   1   1     5     2
28       Ford Pantera L  15.8    8  351.0  264  ...   14.50   0   1     5     4
29         Ferrari Dino  19.7    6  145.0  175  ...   15.50   0   1     5     6
30        Maserati Bora  15.0    8  301.0  335  ...   14.60   0   1     5     8
31           Volvo 142E  21.4    4  121.0  109  ...   18.60   1   1     4     2

[32 rows x 12 columns]'''


cars = pd.read_csv('cars.csv',index_col = 0)

print(cars)

'''Output

                      mpg  cyl   disp   hp  ...   vs  am  gear  carb
Mazda RX4            21.0    6  160.0  110  ...    0   1     4     4
Mazda RX4 Wag        21.0    6  160.0  110  ...    0   1     4     4
Datsun 710           22.8    4  108.0   93  ...    1   1     4     1
Hornet 4 Drive       21.4    6  258.0  110  ...    1   0     3     1
Hornet Sportabout    18.7    8  360.0  175  ...    0   0     3     2
Valiant              18.1    6  225.0  105  ...    1   0     3     1
Duster 360           14.3    8  360.0  245  ...    0   0     3     4
Merc 240D            24.4    4  146.7   62  ...    1   0     4     2
Merc 230             22.8    4  140.8   95  ...    1   0     4     2
Merc 280             19.2    6  167.6  123  ...    1   0     4     4
Merc 280C            17.8    6  167.6  123  ...    1   0     4     4
Merc 450SE           16.4    8  275.8  180  ...    0   0     3     3
Merc 450SL           17.3    8  275.8  180  ...    0   0     3     3
Merc 450SLC          15.2    8  275.8  180  ...    0   0     3     3
Cadillac Fleetwood   10.4    8  472.0  205  ...    0   0     3     4
Lincoln Continental  10.4    8  460.0  215  ...    0   0     3     4
Chrysler Imperial    14.7    8  440.0  230  ...    0   0     3     4
Fiat 128             32.4    4   78.7   66  ...    1   1     4     1
Honda Civic          30.4    4   75.7   52  ...    1   1     4     2
Toyota Corolla       33.9    4   71.1   65  ...    1   1     4     1
Toyota Corona        21.5    4  120.1   97  ...    1   0     3     1
Dodge Challenger     15.5    8  318.0  150  ...    0   0     3     2
AMC Javelin          15.2    8  304.0  150  ...    0   0     3     2
Camaro Z28           13.3    8  350.0  245  ...    0   0     3     4
Pontiac Firebird     19.2    8  400.0  175  ...    0   0     3     2
Fiat X1-9            27.3    4   79.0   66  ...    1   1     4     1
Porsche 914-2        26.0    4  120.3   91  ...    0   1     5     2
Lotus Europa         30.4    4   95.1  113  ...    1   1     5     2
Ford Pantera L       15.8    8  351.0  264  ...    0   1     5     4
Ferrari Dino         19.7    6  145.0  175  ...    0   1     5     6
Maserati Bora        15.0    8  301.0  335  ...    0   1     5     8
Volvo 142E           21.4    4  121.0  109  ...    1   1     4     2

[32 rows x 11 columns]

'''

# Print out mpg column as Pandas Series
print(cars['mpg'])
'''Output
Mazda RX4              21.0
Mazda RX4 Wag          21.0
Datsun 710             22.8
Hornet 4 Drive         21.4
Hornet Sportabout      18.7
Valiant                18.1
Duster 360             14.3
Merc 240D              24.4
Merc 230               22.8
Merc 280               19.2
Merc 280C              17.8
Merc 450SE             16.4
Merc 450SL             17.3
Merc 450SLC            15.2
Cadillac Fleetwood     10.4
Lincoln Continental    10.4
Chrysler Imperial      14.7
Fiat 128               32.4
Honda Civic            30.4
Toyota Corolla         33.9
Toyota Corona          21.5
Dodge Challenger       15.5
AMC Javelin            15.2
Camaro Z28             13.3
Pontiac Firebird       19.2
Fiat X1-9              27.3
Porsche 914-2          26.0
Lotus Europa           30.4
Ford Pantera L         15.8
Ferrari Dino           19.7
Maserati Bora          15.0
Volvo 142E             21.4
Name: mpg, dtype: float64
'''
# Print out mpg column as Pandas DataFrame
print(cars[['mpg']])

'''Output
                      mpg
Mazda RX4            21.0
Mazda RX4 Wag        21.0
Datsun 710           22.8
Hornet 4 Drive       21.4
Hornet Sportabout    18.7
Valiant              18.1
Duster 360           14.3
Merc 240D            24.4
Merc 230             22.8
Merc 280             19.2
Merc 280C            17.8
Merc 450SE           16.4
Merc 450SL           17.3
Merc 450SLC          15.2
Cadillac Fleetwood   10.4
Lincoln Continental  10.4
Chrysler Imperial    14.7
Fiat 128             32.4
Honda Civic          30.4
Toyota Corolla       33.9
Toyota Corona        21.5
Dodge Challenger     15.5
AMC Javelin          15.2
Camaro Z28           13.3
Pontiac Firebird     19.2
Fiat X1-9            27.3
Porsche 914-2        26.0
Lotus Europa         30.4
Ford Pantera L       15.8
Ferrari Dino         19.7
Maserati Bora        15.0
Volvo 142E           21.4
'''

# Print out DataFrame with mpg and hp columns
print(cars[['mpg', 'hp']])
'''Output
                      mpg   hp
Mazda RX4            21.0  110
Mazda RX4 Wag        21.0  110
Datsun 710           22.8   93
Hornet 4 Drive       21.4  110
Hornet Sportabout    18.7  175
Valiant              18.1  105
Duster 360           14.3  245
Merc 240D            24.4   62
Merc 230             22.8   95
Merc 280             19.2  123
Merc 280C            17.8  123
Merc 450SE           16.4  180
Merc 450SL           17.3  180
Merc 450SLC          15.2  180
Cadillac Fleetwood   10.4  205
Lincoln Continental  10.4  215
Chrysler Imperial    14.7  230
Fiat 128             32.4   66
Honda Civic          30.4   52
Toyota Corolla       33.9   65
Toyota Corona        21.5   97
Dodge Challenger     15.5  150
AMC Javelin          15.2  150
Camaro Z28           13.3  245
Pontiac Firebird     19.2  175
Fiat X1-9            27.3   66
Porsche 914-2        26.0   91
Lotus Europa         30.4  113
Ford Pantera L       15.8  264
Ferrari Dino         19.7  175
Maserati Bora        15.0  335
Volvo 142E           21.4  109
'''




# Print out observation for Japan
print(cars.iloc[2])
'''Output
mpg      22.80
cyl       4.00
disp    108.00
hp       93.00
drat      3.85
wt        2.32
qsec     18.61
vs        1.00
am        1.00
gear      4.00
carb      1.00
Name: Datsun 710, dtype: float64
'''
# Print out observations for Australia and Egypt
print(cars.loc[['Duster 360', 'Valiant']])
'''Output
             mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb
Duster 360  14.3    8  360.0  245  3.21  3.57  15.84   0   0     3     4
Valiant     18.1    6  225.0  105  2.76  3.46  20.22   1   0     3     1
'''
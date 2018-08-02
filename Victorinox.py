#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import sys,os
from knifeUI import Application_ui
if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    from tkinter.filedialog import askopenfilename
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    from tkinter.filedialog import askopenfilename
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()
 
# built-in WL table
WL_list = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12, 13], [14, 15], [16, 17], [18, 19], [20, 21], [22, 23], [24, 25], [26, 27], [28, 29], [30, 31], [32, 33], [34, 35], [36, 61, 60], [37, 64, 63], [38, 67, 66], [39, 70, 69], [40, 73, 72], [41, 76, 75], [42, 79, 78], [43, 82, 81], [44, 85, 84], [45, 88, 87], [46, 91, 90], [47, 94, 93], [48, 97, 96], [49, 100, 99], [50, 103, 102], [51, 106, 105], [52, 109, 108], [53, 112, 111], [54, 115, 114], [55, 118, 117], [56, 121, 120], [57, 124, 123], [58, 127, 126], [59, 130, 129], [62, 133, 132], [65, 136, 135], \
[68, 139, 138], [71, 142, 141], [74, 145, 144], [77, 148, 147], [80, 151, 150], [83, 154, 153], [86, 157, 156], [89, 160, 159], [92, 163, 162], [95, 166, 165], [98, 169, 168], [101, 172, 171], [104, 175, 174], [107, 178, 177], [110, 181, 180], [113, 184, 183], [116, 187, 186], [119, 190, 189], [122, 193, 192], [125, 196, 195], [128, 199, 198], [131, 202, 201], [134, 205, 204], [137, 208, 207], [140, 211, 210], [143, 214, 213], [146, 217, 216], [149, 220, 219], [152, 223, 222], [155, 226, 225], [158, 229, 228], [161, 232, 231], [164, 235, 234], [167, 238, 237], [170, 241, 240], [173, 244, 243], [176, 247, 246], [179, 250, 249], [182, 253, 252], [185, 256, 255], [188, 259, 258], [191, 262, 261], [194, 265, 264], [197, 268, 267], [200, 271, 270], [203, 274, 273], [206, 277, 276], [209, 280, 279], [212, 283, 282], [215, 286, 285], \
[218, 289, 288], [221, 292, 291], [224, 295, 294], [227, 298, 297], [230, 301, 300], [233, 304, 303], [236, 307, 306], [239, 310, 309], [242, 313, 312], [245, 316, 315], [248, 319, 318], [251, 322, 321], [254, 325, 324], [257, 328, 327], [260, 331, 330], [263, 334, 333], [266, 337, 336], [269, 340, 339], [272, 343, 342], [275, 346, 345], [278, 349, 348], [281, 352, 351], [284, 355, 354], [287, 358, 357], [290, 361, 360], [293, 364, 363], [296, 367, 366], [299, 370, 369], [302, 373, 372], [305, 376, 375], [308, 379, 378], [311, 382, 381], [314, 385, 384], [317, 388, 387], [320, 391, 390], [323, 394, 393], [326, 397, 396], [329, 400, 399], [332, 403, 402], [335, 406, 405], [338, 409, 408], [341, 412, 411], [344, 415, 414], [347, 418, 417], [350, 421, 420], [353, 424, 423], [356, 427, 426], [359, 430, 429], [362, 433, 432], [365, 436, 435], \
[368, 439, 438], [371, 442, 441], [374, 445, 444], [377, 448, 447], [380, 451, 450], [383, 454, 453], [386, 457, 456], [389, 460, 459], [392, 463, 462], [395, 466, 465], [398, 469, 468], [401, 472, 471], [404, 475, 474], [407, 478, 477], [410, 481, 480], [413, 484, 483], [416, 487, 486], [419, 490, 489], [422, 493, 492], [425, 496, 495], [428, 499, 498], [431, 502, 501], [434, 505, 504], [437, 508, 507], [440, 511, 510], [443, 514, 513], [446, 517, 516], [449, 520, 519], [452, 523, 522], [455, 526, 525], [458, 529, 528], [461, 532, 531], [464, 535, 534], [467, 538, 537], [470, 541, 540], [473, 544, 543], [476, 547, 546], [479, 550, 549], [482, 553, 552], [485, 556, 555], [488, 559, 558], [491, 562, 561], [494, 565, 564], [497, 568, 567], [500, 571, 570], [503, 574, 573], [506, 577, 576], [509, 580, 579], [512, 583, 582], [515, 586, 585], \
[518, 589, 588], [521, 592, 591], [524, 595, 594], [527, 598, 597], [530, 601, 600], [533, 604, 603], [536, 607, 606], [539, 610, 609], [542, 613, 612], [545, 616, 615], [548, 619, 618], [551, 622, 621], [554, 625, 624], [557, 628, 627], [560, 631, 630], [563, 634, 633], [566, 637, 636], [569, 640, 639], [572, 643, 642], [575, 646, 645], [578, 649, 648], [581, 652, 651], [584, 655, 654], [587, 658, 657], [590, 661, 660], [593, 664, 663], [596, 667, 666], [599, 670, 669], [602, 673, 672], [605, 676, 675], [608, 679, 678], [611, 682, 681], [614, 685, 684], [617, 688, 687], [620, 691, 690], [623, 694, 693], [626, 697, 696], [629, 700, 699], [632, 703, 702], [635, 706, 705], [638, 709, 708], [641, 712, 711], [644, 715, 714], [647, 718, 717], [650, 721, 720], [653, 724, 723], [656, 727, 726], [659, 730, 729], [662, 733, 732], [665, 736, 735], \
[668, 739, 738], [671, 742, 741], [674, 745, 744], [677, 748, 747], [680, 751, 750], [683, 754, 753], [686, 757, 756], [689, 760, 759], [692, 763, 762], [695, 766, 765], [698, 769, 768], [701, 772, 771], [704, 775, 774], [707, 778, 777], [710, 781, 780], [713, 784, 783], [716, 787, 786], [719, 790, 789], [722, 793, 792], [725, 796, 795], [728, 799, 798], [731, 802, 801], [734, 805, 804], [737, 808, 807], [740, 811, 810], [743, 814, 813], [746, 817, 816], [749, 820, 819], [752, 823, 822], [755, 826, 825], [758, 829, 828], [761, 832, 831], [764, 835, 834], [767, 838, 837], [770, 841, 840], [773, 844, 843], [776, 847, 846], [779, 850, 849], [782, 853, 852], [785, 856, 855], [788, 859, 858], [791, 862, 861], [794, 865, 864], [797, 868, 867], [800, 871, 870], [803, 874, 873], [806, 877, 876], [809, 880, 879], [812, 883, 882], [815, 886, 885], \
[818, 889, 888], [821, 892, 891], [824, 895, 894], [827, 898, 897], [830, 901, 900], [833, 904, 903], [836, 907, 906], [839, 910, 909], [842, 913, 912], [845, 916, 915], [848, 919, 918], [851, 922, 921], [854, 925, 924], [857, 928, 927], [860, 931, 930], [863, 934, 933], [866, 937, 936], [869, 940, 939], [872, 943, 942], [875, 946, 945], [878, 949, 948], [881, 952, 951], [884, 955, 954], [887, 958, 957], [890, 961, 960], [893, 964, 963], [896, 967, 966], [899, 970, 969], [902, 973, 972], [905, 976, 975], [908, 979, 978], [911, 982, 981], [914, 985, 984], [917, 988, 987], [920, 991, 990], [923, 994, 993], [926, 997, 996], [929, 1000, 999], [932, 1003, 1002], [935, 1006, 1005], [938, 1009, 1008], [941, 1012, 1011], [944, 1015, 1014], [947, 1018, 1017], [950, 1021, 1020], [953, 1024, 1023], [956, 1027, 1026], [959, 1030, 1029], [962, 1033, 1032], [965, 1036, 1035], \
[968, 1039, 1038], [971, 1042, 1041], [974, 1045, 1044], [977, 1048, 1047], [980, 1051, 1050], [983, 1054, 1053], [986, 1057, 1056], [989, 1060, 1059], [992, 1063, 1062], [995, 1066, 1065], [998, 1069, 1068], [1001, 1072, 1071], [1004, 1075, 1074], [1007, 1078, 1077], [1010, 1081, 1080], [1013, 1084, 1083], [1016, 1087, 1086], [1019, 1090, 1089], [1022, 1093, 1092], [1025, 1096, 1095], [1028, 1099, 1098], [1031, 1102, 1101], [1034, 1105, 1104], [1037, 1108, 1107], [1040, 1111, 1110], [1043, 1114, 1113], [1046, 1117, 1116], [1049, 1120, 1119], [1052, 1123, 1122], [1055, 1126, 1125], [1058, 1129, 1128], [1061, 1132, 1131], [1064, 1135, 1134], [1067, 1138, 1137], [1070, 1141, 1140], [1073, 1144, 1143], [1076, 1147, 1146], [1079, 1150, 1149], [1082, 1153, 1152], [1085, 1156, 1155], [1088, 1159, 1158], [1091, 1162, 1161], [1094, 1165, 1164], [1097, 1168, 1167], [1100, 1171, 1170], [1103, 1174, 1173], [1106, 1177, 1176], [1109, 1180, 1179], [1112, 1183, 1182], [1115, 1186, 1185], \
[1118, 1189, 1188], [1121, 1192, 1191], [1124, 1195, 1194], [1127, 1198, 1197], [1130, 1201, 1200], [1133, 1204, 1203], [1136, 1207, 1206], [1139, 1210, 1209], [1142, 1213, 1212], [1145, 1216, 1215], [1148, 1219, 1218], [1151, 1222, 1221], [1154, 1225, 1224], [1157, 1228, 1227], [1160, 1231, 1230], [1163, 1234, 1233], [1166, 1237, 1236], [1169, 1240, 1239], [1172, 1243, 1242], [1175, 1246, 1245], [1178, 1249, 1248], [1181, 1252, 1251], [1184, 1255, 1254], [1187, 1258, 1257], [1190, 1261, 1260], [1193, 1264, 1263], [1196, 1267, 1266], [1199, 1270, 1269], [1202, 1273, 1272], [1205, 1276, 1275], [1208, 1279, 1278], [1211, 1282, 1281], [1214, 1285, 1284], [1217, 1288, 1287], [1220, 1291, 1290], [1223, 1294, 1293], [1226, 1297, 1296], [1229, 1300, 1299], [1232, 1303, 1302], [1235, 1306, 1305], [1238, 1309, 1308], [1241, 1312, 1311], [1244, 1315, 1314], [1247, 1318, 1317], [1250, 1321, 1320], [1253, 1324, 1323], [1256, 1327, 1326], [1259, 1330, 1329], [1262, 1333, 1332], [1265, 1336, 1335], \
[1268, 1339, 1338], [1271, 1342, 1341], [1274, 1345, 1344], [1277, 1348, 1347], [1280, 1351, 1350], [1283, 1354, 1353], [1286, 1357, 1356], [1289, 1360, 1359], [1292, 1363, 1362], [1295, 1366, 1365], [1298, 1369, 1368], [1301, 1372, 1371], [1304, 1375, 1374], [1307, 1378, 1377], [1310, 1381, 1380], [1313, 1384, 1383], [1316, 1387, 1386], [1319, 1390, 1389], [1322, 1393, 1392], [1325, 1396, 1395], [1328, 1399, 1398], [1331, 1402, 1401], [1334, 1405, 1404], [1337, 1408, 1407], [1340, 1411, 1410], [1343, 1414, 1413], [1346, 1417, 1416], [1349, 1420, 1419], [1352, 1423, 1422], [1355, 1426, 1425], [1358, 1429, 1428], [1361, 1432, 1431], [1364, 1435, 1434], [1367, 1438, 1437], [1370, 1441, 1440], [1373, 1444, 1443], [1376, 1447, 1446], [1379, 1450, 1449], [1382, 1453, 1452], [1385, 1456, 1455], [1388, 1459, 1458], [1391, 1462, 1461], [1394, 1465, 1464], [1397, 1468, 1467], [1400, 1471, 1470], [1403, 1474, 1473], [1406, 1477, 1476], [1409, 1480, 1479], [1412, 1483, 1482], [1415, 1486, 1485], \
[1418, 1489, 1488], [1421, 1492, 1491], [1424, 1495, 1494], [1427, 1498, 1497], [1430, 1501, 1500], [1433, 1504, 1503], [1436, 1507, 1506], [1439, 1510, 1509], [1442, 1513, 1512], [1445, 1516, 1515], [1448, 1519, 1518], [1451, 1522, 1521], [1454, 1525, 1524], [1457, 1528, 1527], [1460, 1531, 1530], [1463, 1534, 1533], [1466, 1537, 1536], [1469, 1540, 1539], [1472, 1543, 1542], [1475, 1546, 1545], [1478, 1549, 1548], [1481, 1552, 1551], [1484, 1555, 1554], [1487, 1558, 1557], [1490, 1561, 1560], [1493, 1564, 1563], [1496, 1567, 1566], [1499, 1570, 1569], [1502, 1573, 1572], [1505, 1576, 1575], [1508, 1579, 1578], [1511, 1582, 1581], [1514, 1585, 1584], [1517, 1588, 1587], [1520, 1591, 1590], [1523, 1594, 1593], [1526, 1597, 1596], [1529, 1600, 1599], [1532, 1603, 1602], [1535, 1606, 1605], [1538, 1609, 1608], [1541, 1612, 1611], [1544, 1615, 1614], [1547, 1618, 1617], [1550, 1621, 1620], [1553, 1624, 1623], [1556, 1627, 1626], [1559, 1630, 1629], [1562, 1633, 1632], [1565, 1636, 1635], \
[1568, 1639, 1638], [1571, 1642, 1641], [1574, 1645, 1644], [1577, 1648, 1647], [1580, 1651, 1650], [1583, 1654, 1653], [1586, 1657, 1656], [1589, 1660, 1659], [1592, 1663, 1662], [1595, 1666, 1665], [1598, 1669, 1668], [1601, 1672, 1671], [1604, 1675, 1674], [1607, 1678, 1677], [1610, 1681, 1680], [1613, 1684, 1683], [1616, 1687, 1686], [1619, 1690, 1689], [1622, 1693, 1692], [1625, 1696, 1695], [1628, 1699, 1698], [1631, 1702, 1701], [1634, 1705, 1704], [1637, 1708, 1707], [1640, 1711, 1710], [1643, 1714, 1713], [1646, 1717, 1716], [1649, 1720, 1719], [1652, 1723, 1722], [1655, 1726, 1725], [1658, 1729, 1728], [1661, 1732, 1731], [1664, 1735, 1734], [1667, 1738, 1737], [1670, 1741, 1740], [1673, 1744, 1743], [1676, 1747, 1746], [1679, 1750, 1749], [1682, 1753, 1752], [1685, 1756, 1755], [1688, 1759, 1758], [1691, 1762, 1761], [1694, 1765, 1764], [1697, 1768, 1767], [1700, 1771, 1770], [1703, 1774, 1773], [1706, 1777, 1776], [1709, 1780, 1779], [1712, 1783, 1782], [1715, 1786, 1785], \
[1718, 1789, 1788], [1721, 1792, 1791], [1724, 1795, 1794], [1727, 1798, 1797], [1730, 1801, 1800], [1733, 1804, 1803], [1736, 1807, 1806], [1739, 1810, 1809], [1742, 1813, 1812], [1745, 1816, 1815], [1748, 1819, 1818], [1751, 1822, 1821], [1754, 1825, 1824], [1757, 1828, 1827], [1760, 1831, 1830], [1763, 1834, 1833], [1766, 1837, 1836], [1769, 1840, 1839], [1772, 1843, 1842], [1775, 1846, 1845], [1778, 1849, 1848], [1781, 1852, 1851], [1784, 1855, 1854], [1787, 1858, 1857], [1790, 1861, 1860], [1793, 1864, 1863], [1796, 1867, 1866], [1799, 1870, 1869], [1802, 1873, 1872], [1805, 1876, 1875], [1808, 1879, 1878], [1811, 1882, 1881], [1814, 1885, 1884], [1817, 1888, 1887], [1820, 1891, 1890], [1823, 1894, 1893], [1826, 1897, 1896], [1829, 1900, 1899], [1832, 1903, 1902], [1835, 1906, 1905], [1838, 1909, 1908], [1841, 1912, 1911], [1844, 1915, 1914], [1847, 1918, 1917], [1850, 1921, 1920], [1853, 1924, 1923], [1856, 1927, 1926], [1859, 1930, 1929], [1862, 1933, 1932], [1865, 1936, 1935], \
[1868, 1939, 1938], [1871, 1942, 1941], [1874, 1945, 1944], [1877, 1948, 1947], [1880, 1951, 1950], [1883, 1954, 1953], [1886, 1957, 1956], [1889, 1960, 1959], [1892, 1963, 1962], [1895, 1966, 1965], [1898, 1969, 1968], [1901, 1972, 1971], [1904, 1975, 1974], [1907, 1978, 1977], [1910, 1981, 1980], [1913, 1984, 1983], [1916, 1987, 1986], [1919, 1990, 1989], [1922, 1993, 1992], [1925, 1996, 1995], [1928, 1999, 1998], [1931, 2002, 2001], [1934, 2005, 2004], [1937, 2008, 2007], [1940, 2011, 2010], [1943, 2014, 2013], [1946, 2017, 2016], [1949, 2020, 2019], [1952, 2023, 2022], [1955, 2026, 2025], [1958, 2029, 2028], [1961, 2032, 2031], [1964, 2035, 2034], [1967, 2038, 2037], [1970, 2041, 2040], [1973, 2044, 2043], [1976, 2047, 2046], [1979, 2050, 2049], [1982, 2053, 2052], [1985, 2056, 2055], [1988, 2059, 2058], [1991, 2062, 2061], [1994, 2065, 2064], [1997, 2068, 2067], [2000, 2071, 2070], [2003, 2074, 2073], [2006, 2077, 2076], [2009, 2080, 2079], [2012, 2083, 2082], [2015, 2086, 2085], \
[2018, 2089, 2088], [2021, 2092, 2091], [2024, 2095, 2094], [2027, 2098, 2097], [2030, 2101, 2100], [2033, 2104, 2103], [2036, 2107, 2106], [2039, 2110, 2109], [2042, 2113, 2112], [2045, 2116, 2115], [2048, 2119, 2118], [2051, 2122, 2121], [2054, 2125, 2124], [2057, 2128, 2127], [2060, 2131, 2130], [2063, 2134, 2133], [2066, 2137, 2136], [2069, 2140, 2139], [2072, 2143, 2142], [2075, 2146, 2145], [2078, 2149, 2148], [2081, 2152, 2151], [2084, 2155, 2154], [2087, 2158, 2157], [2090, 2161, 2160], [2093, 2164, 2163], [2096, 2167, 2166], [2099, 2170, 2169], [2102, 2173, 2172], [2105, 2176, 2175], [2108, 2179, 2178], [2111, 2182, 2181], [2114, 2185, 2184], [2117, 2188, 2187], [2120, 2191, 2190], [2123, 2194, 2193], [2126, 2197, 2196], [2129, 2200, 2199], [2132, 2203, 2202], [2135, 2206, 2205], [2138, 2209, 2208], [2141, 2212, 2211], [2144, 2215, 2214], [2147, 2218, 2217], [2150, 2221, 2220], [2153, 2225, 2224], [2156, 2229, 2228], [2159, 2233, 2232], [2162, 2237, 2236], [2165, 2241, 2240], \
[2168, 2245, 2244], [2171, 2249, 2248], [2174, 2253, 2252], [2177, 2257, 2256], [2180, 2261, 2260], [2183, 2265, 2264], [2186, 2269, 2268], [2189, 2271, 2270], [2192, 2273, 2272], [2195, 2275, 2274], [2198, 2277, 2276], [2201, 2279, 2278], [2204, 2281, 2280], [2207, 2283, 2282], [2210, 2285, 2284], [2213, 2287, 2286], [2216, 2289, 2288], [2219, 2291, 2290], [2222, 2223], [2226, 2227], [2230, 2231], [2234, 2235], [2238, 2239], [2242, 2243], [2246, 2247], [2250, 2251], [2254, 2255], [2258, 2259], [2262, 2263], [2266, 2267], [2292], [2293], [2294], [2295], [2296], [2297], [2298], [2299], [2300], [2301], [2302], [2303]]
#print "wl num:",len(WL_list)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

        # hex to decimal transform info
        self.varTextH2D = StringVar()
        self.varTextH2D.set("0x0 = 0")
        self.TabStrip1__Tab1Lbl['textvariable'] = self.varTextH2D

        self.Tab1varPage = StringVar()
        self.Tab1varPage.set("page")
        self.TabStrip1__Tab1PageNum['textvariable'] = self.Tab1varPage
        self.TabStrip1__Tab1PageNum.bind("<Return>",self.Page2WL)

        self.TabStrip1__Tab1WL_Button['command'] = self.Page2WL
        self.TabStrip1__Tab1Page_Button['command'] = self.WL2Page

        self.Tab1varWL = StringVar()
        self.Tab1varWL.set("WL")
        self.TabStrip1__Tab1WLNum['textvariable'] = self.Tab1varWL
        self.TabStrip1__Tab1WLNum.bind("<Return>",self.WL2Page)
        
        # Tab2 var
        self.Tab2totalBitNum = 32
        self.Tab2num = [0] * self.Tab2totalBitNum
        for FrmCnt in range(self.Tab2totalBitNum/4):
            for i in range(4):
                self.Tab2ButtonList[4*FrmCnt + i].bind('<Button-1>', self.handlerAdaptor(self.FlipBit,4*FrmCnt + i))
        self.Tab2var16 = StringVar()
        self.Tab2e['textvariable'] = self.Tab2var16
        self.Tab2var16.set("0x00000000")
        self.Tab2Confirm_Button['command'] = self.hex2bin
        self.Tab2e.bind("<Return>",self.hex2bin)
        self.Tab2Clear_Button['command'] = self.clear2zero

        # Tab3 var
        self.Tab3path = StringVar()
        self.Tab3FileList = []
        self.Tab3pathEntry['textvariable'] = self.Tab3path

        self.Tab3ButtonSelect['command'] = self.selectPath
        self.Tab3ButtonConfirm['command'] = self.ConfirmFile

        self.Tab3ButtonMerge['command'] = self.MergeFile

        # Tab4 var
        self.Tab4path = StringVar()
        self.Tab4pathEntry['textvariable'] = self.Tab4path
        
        self.Tab4ButtonSelect['command'] = self.Tab4selectPath
        self.Tab4ButtonConfirm['command'] = self.Tab4ReadFile
#tab1 func
    def toDecimal(self,num_str): # if input is heximal , transform to decimal
        if not num_str:
            result = 0 
        else:
            if num_str[:2] == '0x':
                result = int(num_str,16)
            else:
                result = int(num_str)
        tmp_str = num_str + ' = ' + str(result)
        self.varTextH2D.set(tmp_str)
        return result

    def Page2WL(self,event=None): 
        page = self.toDecimal(self.Tab1varPage.get())
        result = ''
        for wl in range(len(WL_list)):
            for p in WL_list[wl]:
                if p == page:
                    result = wl
                    break
        self.Tab1varWL.set(str(result))

    def WL2Page(self,event=None):
        wl = self.toDecimal(self.Tab1varWL.get())
        result = ', '.join(map(str,WL_list[wl]))
        self.Tab1varPage.set(result)
#tab2 func
    def FlipBit(self,bit):
        self.Tab2num[bit] = self.Tab2num[bit] ^ 1
        print self.Tab2num
        self.Tab2strvarlist[bit].set(str(self.Tab2num[bit]))
        binary = "".join(map(str,self.Tab2num))
        decimal = int(binary,2)
        self.Tab2var16.set(hex(decimal))

    def handlerAdaptor(self,fun,v):
        return lambda event, fun=fun, v=v: fun(v)

    def hex2bin(self,event=None):
        hexadecimal = self.Tab2var16.get()
        print hexadecimal
        decimal = int(hexadecimal,16)
        binary = bin(decimal)[2:]
        align_loc = self.Tab2totalBitNum - len(binary)
        for bit in range(self.Tab2totalBitNum):
            if bit >= align_loc:
                self.Tab2strvarlist[bit].set(binary[bit - align_loc])
                self.Tab2num[bit] = int(binary[bit - align_loc])
            else:
                self.Tab2strvarlist[bit].set('0')
                self.Tab2num[bit] = 0

    def clear2zero(self):
        self.Tab2var16.set("0x0")
        for bit in range(self.Tab2totalBitNum):
            self.Tab2strvarlist[bit].set("0")
            self.Tab2num[bit] = 0
#tab3 func
    def selectPath(self):
        path_ = askopenfilename()
        self.Tab3path.set(path_)

    def ConfirmFile(self):
        self.Tab3FileList.append(self.Tab3path.get())
        self.Tab3Text.delete(0.0,END)
        #print self.Tab3FileList
        self.Tab3Text.insert(END, "\n".join(self.Tab3FileList))

    def MergeFile(self):
        output = open(r"result.bin","wb")
        print "lalala"
        for item in self.Tab3FileList:
            for content in open(item,'rb'):
                output.write(content)
                #print "1 content"
        output.close()
        self.Tab3FileList = []
        print "done"
#tab4 func
    def Tab4selectPath(self):
        path_ = askopenfilename()
        self.Tab4path.set(path_)
        
    def Tab4ReadFile(self):
        fileName = self.Tab4path.get()
        print "Read File:" + fileName
        FileSize = os.path.getsize(fileName)
        print "file size:",FileSize
        f = open(fileName,'rb')
        output = open(fileName+'.txt','w')
        ll = [0]*32
        for j in range(FileSize/32):
            for i in range(32):
                ll[i]=str(ord(f.read(1)))
            print j,ll
            output.write(' '.join(ll)+'\n')
            #print ll[1]*256+ll[0]
        f.close()
        output.close()
 
if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
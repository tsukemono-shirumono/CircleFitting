# CircleFitting
circFitを実行すると点列から円のフィッティングをする

引数xs,ysに点列の座標をいれる

calc_errオプションは点と円との平均二乗誤差を返すかどうか.
デフォルトはTrue

返り値はcalc_err=Trueで4つ
calc_err=Falseで3つ
それぞれ円の中心座標x,y,半径,平均二乗誤差

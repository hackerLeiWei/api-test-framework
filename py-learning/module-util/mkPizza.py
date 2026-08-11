import pizza  # 导入整个模块
# from pizza import * # 导入模块下所有方法。这种方法并不推荐使用，因为可能会导致不通模块间同名函数或变量的名称覆盖
pizza.mkPizza(16, 'pepperoni')
pizza.mkPizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import mkPizza, sayPizza  # 导入单个方法

mkPizza(116, 'pepperoni')
mkPizza(122, 'mushrooms', 'green peppers', 'extra cheese')
sayPizza()

from pizza import mkPizza as MKPizza  # 导入单个方法并重命名

MKPizza(216, 'pepperoni')
MKPizza(222, 'mushrooms', 'green peppers', 'extra cheese')

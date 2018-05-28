# coding:utf-8


def f(sub_data, fa_data):
    if sub_data == fa_data:
        # 提前结束  减少计算
        return True
    elif len(sub_data) > len(fa_data) or type(sub_data) != type(fa_data):
        return False

    # 两数据必定类型相等、并且sub_data长度少于等于fa_data长度
    if isinstance(sub_data, dict):
        for k, v in sub_data.items():

            if k not in fa_data:
                return False

            fa_v = fa_data[k]

            print v, fa_v

            if v == fa_v:
                continue

            if type(v) == type(fa_v) and isinstance(v, (list, dict)):
                # if False返回False   True则下一个元素
                if not f(v, fa_v):
                    return False
            else:
                # 不相等， 又不是list、dict结构 则认为不是子集关系
                return False

    elif isinstance(sub_data, list):
        for idx, val in enumerate(sub_data):
            fa_val = fa_data[idx]

            print val, fa_val

            if val == fa_val:
                continue

            if type(val) == type(fa_val) and isinstance(val, (list, dict)):
                if not f(val, fa_val):
                    return False
            else:
                # 不相等， 又不是list、dict结构 则认为不是子集关系
                return False

    # 不是list、dict结构, 又不相等则不是子集关系
    else:
        print sub_data, fa_data
        return False

    return True
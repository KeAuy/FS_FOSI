import math
import random
import pandas as pd


def generate_parameters():
    while True:
        #!先定义约束变量
        # T = random.uniform(1.0, 2.0)  # !T>1，从而先试试 1 < T < 2
        T = 2
        xi = random.uniform(0.01, T/4)  # ! xi的范围是0<xi<eta<T,从而将xi可以先试试(0,T/4)
        # !eta的范围是0<xi<eta < T,不妨控制eta是(xi+0.01,T-0.01)
        eta = random.uniform(0.5, T-0.01)
        alpha = random.uniform(0.1, 0.9)  # !alpha是（0，1）上的
        beta = random.uniform(0.1, 0.9)  # !beta是（0，1）上的
        # !考虑到后面涉及Gamma(alpha + gamma+1),从而要控制其规模，此时alpha + gamma in (0.2,1.9)
        gamma = random.uniform(0.1, 1.0)

        if not (1 < alpha + beta < 2):   # ^如果不满足alpha和beta的约束，则重新循环
            continue

        #!再定义无限制变量
        lambda_ = random.uniform(0.1, 2.0)
        sigma = random.uniform(0.1, 1.0)
        a1 = random.uniform(0.1, 2)
        a2 = random.uniform(0.1, 2)
        b1 = random.uniform(0.1, 2)
        b2 = random.uniform(0.1, 2)
        c1 = random.uniform(0.1, 2)
        c2 = random.uniform(0.1, 2)
        d1 = random.uniform(0.1, 2)
        d2 = random.uniform(0.1, 2)

        p1 = random.uniform(0.01, 0.1)
        p2 = random.uniform(0.01, 0.1)

        #!计算中间量（1）
        G_alpha = math.gamma(alpha + 1)  # !p_11中分母的参数
        p11 = b1 + d1 + (c1 - lambda_ * d1) * T**alpha / G_alpha
        p12 = a1 - lambda_ * b1 + c1 - lambda_ * d1
        p21 = b2 + d2 + (a2 - lambda_ * b2) * xi**alpha / \
            G_alpha + (c2 - lambda_ * d2) * eta**alpha / G_alpha
        p22 = a2 - lambda_ * b2 + c2 - lambda_ * d2
        Delta = p11 * p22 - p12 * p21
        if abs(Delta) < 1e-5:  # !如果Delta非常小，就跳过当前循环迭代，重新生成一组参数。continue 语句会让程序跳过本次循环的剩余部分，立即开始下一轮循环
            continue
        A1 = T**alpha * abs(p22) / (abs(Delta) * G_alpha) + \
            abs(p21) / abs(Delta)
        A2 = T**alpha * abs(p12) / (abs(Delta) * G_alpha) + \
            abs(p11) / abs(Delta)

        #!计算中间量（2）
        G_alpha_beta = math.gamma(alpha + beta + 1)
        G_alpha_gamma = math.gamma(alpha + gamma + 1)
        G_gamma = math.gamma(gamma + 1)
        G_beta = math.gamma(beta + 1)

        varphi1 = abs(lambda_) / G_alpha
        varphi2 = abs(sigma) / G_alpha_gamma
        varphi3 = 1 / G_alpha_beta
        varphi4 = abs(sigma) / G_gamma
        varphi5 = 1 / G_beta

        vartheta11 = abs(lambda_ * d1 - c1) * varphi3 * \
            T**(alpha + beta) + abs(d1) * varphi5 * T**beta
        vartheta12 = abs(lambda_ * d1 - c1) * varphi2 * \
            T**(alpha + gamma) + abs(d1) * varphi4 * T**gamma
        vartheta21 = abs(lambda_ * b2 - a2) * varphi3 * \
            xi**(alpha + beta) + abs(b2) * varphi5 * xi**beta
        vartheta22 = abs(lambda_ * b2 - a2) * varphi2 * \
            xi**(alpha + gamma) + abs(b2) * varphi4 * xi**gamma
        vartheta31 = abs(lambda_ * d2 - c2) * varphi3 * \
            eta**(alpha + beta) + abs(d2) * varphi5 * eta**beta
        vartheta32 = abs(lambda_ * d2 - c2) * varphi2 * \
            eta**(alpha + gamma) + abs(d2) * varphi4 * eta**gamma

        Phi1 = A1 * abs(lambda_ * d1 - c1) * varphi1 * T**alpha + \
            A2 * abs(lambda_ * b2 - a2) * varphi1 * xi**alpha + \
            A2 * abs(lambda_ * d2 - c2) * varphi1 * eta**alpha
        Phi2 = A1 * vartheta11 + A2 * vartheta21 + A2 * vartheta31
        Phi3 = A1 * vartheta12 + A2 * vartheta22 + A2 * vartheta32

        #!计算目标式
        lhs = (varphi1 * T**alpha + Phi1) + (varphi3 * T**(alpha + beta) +
                                             Phi3) * p1 + (varphi2 * T**(alpha + gamma) + Phi2) * p2

        if lhs < 1:
            return {
                "xi": xi, "eta": eta, "T": T, "alpha": alpha, "beta": beta, "gamma": gamma,
                "lambda": lambda_, "sigma": sigma,
                "a1": a1, "a2": a2, "b1": b1, "b2": b2, "c1": c1, "c2": c2,
                "d1": d1, "d2": d2, "p1": p1, "p2": p2,
                "lhs": lhs, "Delta": Delta


            }


result = generate_parameters()
print("找到一组满足条件的参数：")
for k, v in result.items():  # &result.items()：这是一个字典的方法，它返回一个由字典中的键-值对组成的迭代器。每个键值对是一个元组，形式为 (key, value)
    print(f"{k} = {v:.4f}")

# 将计算结果转换为 DataFrame 格式
df = pd.DataFrame(result.items(), columns=["Parameter", "Value"])

# 四舍五入到2位小数
df["Value"] = df["Value"].round(2)

# 将结果保存到 Excel 文件
df.to_excel("Script\calculation_results_2.xlsx", index=False)

print("Results have been written to 'calculation_results.xlsx'.")

# FS_FOSI
Feasibility-Search-for-a-Fractional-Order-Stability-Inequality
   - 搜索分数阶不等式成立的可行参数
## 问题

- 一个18 维、连续、非线性、非凸的**可行性问题**。

- 寻找满足 $0<\xi<\eta<T,  T\ge1, \lambda>0,  \sigma \neq 0,$ 并且满足 $0<\alpha,\beta<1,\quad 1<\alpha+\beta<2,\quad \gamma>0,\quad p_1,p_2>0,$ 的参数，使得

$$
(\varphi_1 T^\alpha+\Phi_1)+(\varphi_2 T^{\alpha+\gamma}+\Phi_2)p_2 + (\varphi_3 T^{\alpha+\beta}+\Phi_3)p_1
<1.
$$

其中 $\varphi_i,\Phi_i,\Delta,A_i,\vartheta_{ij}$ 的定义为：

$$
p_{11}=b_1+d_1+\frac{(c_1-\lambda d_1)T^\alpha}{\Gamma(\alpha+1)},
$$

$$
p_{12}=a_1-\lambda b_1+c_1-\lambda d_1,
$$

$$
p_{21}=b_2+d_2
+\frac{(a_2-\lambda b_2)\xi^\alpha}{\Gamma(\alpha+1)}
+\frac{(c_2-\lambda d_2)\eta^\alpha}{\Gamma(\alpha+1)},
$$

$$
p_{22}=a_2-\lambda b_2+c_2-\lambda d_2,
\qquad
\Delta=p_{11}p_{22}-p_{12}p_{21}\ne 0.
$$

$$
A_1=\frac{T^\alpha|p_{22}|}{|\Delta|\,\Gamma(\alpha+1)}
+\frac{|p_{21}|}{|\Delta|},
\qquad
A_2=\frac{T^\alpha|p_{12}|}{|\Delta|\,\Gamma(\alpha+1)}
+\frac{|p_{11}|}{|\Delta|}.
$$

$$
\varphi_1=\frac{|\lambda|}{\Gamma(\alpha+1)},\qquad
\varphi_2=\frac{|\sigma|}{\Gamma(\alpha+\gamma+1)},\qquad
\varphi_3=\frac{1}{\Gamma(\alpha+\beta+1)},
$$

$$
\varphi_4=\frac{|\sigma|}{\Gamma(\gamma+1)},\qquad
\varphi_5=\frac{1}{\Gamma(\beta+1)}.
$$

$$
\vartheta_{11}=|\lambda d_1-c_1|\,\varphi_3 T^{\alpha+\beta}
+|d_1|\,\varphi_5 T^\beta,
$$

$$
\vartheta_{12}=|\lambda d_1-c_1|\,\varphi_2 T^{\alpha+\gamma}
+|d_1|\,\varphi_4 T^\gamma,
$$

$$
\vartheta_{21}=|\lambda b_2-a_2|\,\varphi_3 \xi^{\alpha+\beta}
+|b_2|\,\varphi_5 \xi^\beta,
$$

$$
\vartheta_{22}=|\lambda b_2-a_2|\,\varphi_2 \xi^{\alpha+\gamma}
+|b_2|\,\varphi_4 \xi^\gamma,
$$

$$
\vartheta_{31}=|\lambda d_2-c_2|\,\varphi_3 \eta^{\alpha+\beta}
+|d_2|\,\varphi_5 \eta^\beta,
$$

$$
\vartheta_{32}=|\lambda d_2-c_2|\,\varphi_2 \eta^{\alpha+\gamma}
+|d_2|\,\varphi_4 \eta^\gamma.
$$

$$
\Phi_1=A_1|\lambda d_1-c_1|\varphi_1 T^\alpha
+A_2|\lambda b_2-a_2|\varphi_1 \xi^\alpha
+A_2|\lambda d_2-c_2|\varphi_1 \eta^\alpha,
$$

$$
\Phi_2=A_1\vartheta_{11}+A_2\vartheta_{21}+A_2\vartheta_{31},
\qquad
\Phi_3=A_1\vartheta_{12}+A_2\vartheta_{22}+A_2\vartheta_{32}.
$$

其中， $a_1,a_2,b_1,b_2,c_1,c_2,d_1,d_2\in\mathbb{R}\backslash \{0\}$. 

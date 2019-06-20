---
layout: formula
title: "群论课程提要"
date: 2019-04-20 19:10:59 +0800
tags: [Course]
categories: [Course]
description: 群论课的碎碎念
---

<!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->

# <h00 id='0.0'>群论</h00>

### 目录

* [1.群的基本知识](#1.0)
* [2.有限群表示论基础](#2.0)
* [5.典型李群的张量表示](#5.0)

---

### <h01 id='1.0'>1.群的基本知识</h01>

[返回目录](#0.0)

#### 1.1群的定义

* 群的定义：乘法封闭、结合律、单位元、唯一逆元

* 群元素的个数称为群的阶数

* 若群元素对易：阿贝尔群（交换群）

* **重排定理**：设$$u$$为群$$G$$中的某一个固定元素，$$u\in G$$，则群$$G$$的每一个元素都可以写为$$g_i u$$（或$$ug_i$$）的形式，其中$$g_i\in G, i=1,2,\dotsb$$，而且对于两个不同的群元素$$g_i\neq g_j$$，有$$g_iu\neq g_ju$$

#### 1.2 群的一些例子

* 有限群、无限群、可数群、不可数群

* 阿贝尔群与非阿贝尔群

* 重排定理

* 乘法表：行元素左乘列元素。群的乘法表给出群结构的所有信息

* 平庸群：只含有单位元$$e$$

* $$S_n$$群：$$n$$阶置换群-换两个元素的位置

* $$C^n$$群：$$n$$阶循环群-幂次运算

* $$D_3$$群：六阶二面体群（正三角形对称群）-旋转$$df$$翻转$$abc$$

* SO(2)群：二维平面转动

#### 1.3 子群

* 子群一定包含有母群的唯一的单位元

* 群$$G$$的非空子集$$H$$是$$G$$的一个子群的充分必要条件是：对所有$$h_\alpha,h_\beta\in H$$，有$$h_\alpha h_\beta^{-1}\in H$$

* 两个子群的交集还是一个子群

* 平凡子群和固有子群

* 全体$$n$$阶非奇异实方阵在矩阵乘法下构成一个群，称为$$n$$阶实矩阵群，记为$$\mathrm{GL\left(n,{\Bbb R}\right)}$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;全体满足$$\mathrm{det}A=1$$的$$n$$阶复方阵在矩阵乘法下构成一个群，称为$$n$$阶复特殊矩阵群，记为$$\mathrm{SL}\left(n,{\Bbb C}\right)$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;全体满足$$\mathrm{det}A=1$$的$$n$$阶实方阵在矩阵乘法下构成一个群，称为$$n$$阶实特殊矩阵群，记为$$\mathrm{SL}\left(n,{\Bbb R}\right)$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;于是有

$$
\mathrm{SL}\left(n,{\Bbb R}\right)\subset\left\{
\begin{aligned}
&\mathrm{SL}\left(n,{\Bbb C}\right)\\
&\mathrm{GL}\left(n,{\Bbb R}\right)
\end{aligned}
\right\}\subset
\mathrm{GL}\left(n,{\Bbb C}\right)
$$

* $$D_3$$群有4个固有子群

#### 1.4 群的生成元

* 群可以由生成元乘出来

* 生成元所满足的定义关系决定了群的结构（乘法表），有限群可以由其生成元的集合与定义关系完全刻画

* $$D_3$$群所满足的定义关系为

$$
a^2=b^2=\left(ab\right)^3=e
$$

#### 1.5 陪集

* 左陪集、右陪集与代表元

* **陪集定理**：两个陪集只要有一个相同的元素，这两个陪集就完全相同

* **Lagrange定理**：有限群的子群的阶为该有限群的阶的因子

* 阶为素数的群都是循环群，而且它们只有平凡子群

#### 1.6 共轭元素与类

* 所有相互共轭的元素构成一个类

* $$D_3$$群有3个类；阿贝尔群的每一个元素自成一类

* **类定理**：有限群的类中的元素个数为该群阶的因子

#### 1.7 不变子群

* 不变子群：设$$H$$是$$G$$的一个子群，如果$$H$$包含元素$$h$$，而且它也包含与$$h$$属于同一类的所有元素$$uhu^{-1}$$，则称$$H$$是$$G$$的一个不变子群

* 阿贝尔群的子群都是不变子群

* 如果一个群不含不变子群，则称之为单群；如果一个群不含阿贝尔不变子群，则称之为半单群

* 设$$H$$是群$$G$$的一个不变子群，对于任意元素$$u\in G$$，但$$u\notin H$$，则当$$h$$取遍$$H$$的所有元素时，$$uhu^{-1}$$也给出$$H$$的所有元素，且仅给出一次，即$$uHu^{-1}=H$$

* 设$$H$$是群$$G$$的一个不变子群，可以构造$$H$$的所有陪集串为

$$
H, u_1H, u_2H, \dotsb, u_{j-1}H
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;（当$$u_i\in H$$时，陪集即为$$H$$本身）

* 如果把$$H$$的陪集串中的每一个陪集看作是一个新的元素，那么该陪集串在陪集乘法下也会构成一个群，称$$G$$对$$H$$的商群，记为$$G/H$$。若$$G$$和$$H$$的阶分别为$$n$$和$$m$$，那么$$G/H$$的阶为$$j=n/m$$

#### 1.8 群的同构

* 如果在两个群$$G$$和$$F$$的元素之间存在一一对应关系，且保持群的乘法关系不变，那么称两个群同构，记为$$G\cong F$$

* **Cayley**定理：任意一个$$n$$阶有限群都和置换群$$S_n$$的某一个子群同构

* 群$$G$$到自身的同构关系称为$$G$$的自同构（即可以交换几个元素的位置，而乘法表保持不变）

#### 1.9 群的同态

* 如果在两个群$$G=\left\{\dotsb,g_i\dotsb\right\}$$和$$F=\left\{\dotsb,f_i\dotsb\right\}$$的元素之间存在一个单向的多一对应关系，且保持群的乘法关系不变，即

$$
\begin{aligned}
g_i&\rightarrow f_i\\
g_j&\rightarrow f_j
\end{aligned}
\Rightarrow
g_ig_j\rightarrow f_if_j
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;那么称$$G$$同态于$$F$$，记为$$G\approx F$$（群$$G$$要比群$$F$$大，同态是单向的）

* 如果群$$G$$同态于群$$F$$，那么$$G$$中的互逆元素对应于$$F$$中的互逆元素

* 任何一个群$$G$$都有一个平庸的同态映射，即让$$G$$中的每个元素都对应于单位元$$e$$，$$G\approx e$$

* 设群$$G$$同态于群$$F$$，则$$G$$中与$$F$$的单位元对应的元素的集合称为$$G$$的同态核

* **同态核定理**：设群$$G$$同态于群$$F$$，则有

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1)$$G$$的同态核$$H$$是$$G$$的不变子群

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2)商群$$G/H$$与$$F$$同构

#### 1.10 群的直积

* 若阶为$$n$$的群$$G$$满足以下两个条件，就称$$G$$为它的两个子群$$G_1$$（阶为$$n_1$$）和$$G_2$$（阶为$$n_2$$）的直积，记为$$G=G_1\otimes G_2$$
  * $$G$$的**任意**元素$$g_{\alpha\beta}$$都可以**唯一**地表示为$$g_{\alpha\beta}=g_{1\alpha}g_{2\beta}$$，其中$$g_{1\alpha}\in G_1$$，$$g_{2\beta}\in G_2$$
  * 满足关系$$g_{1\alpha}g_{2\beta}=g_{2\beta}g_{1\alpha}$$

* 称$$G_1$$和$$G_2$$为$$G$$的直积因子，它们的阶满足$$n=n_1\times n_2$$

* $$G_1$$和$$G_2$$都是$$G$$的不变子群

* $$G$$对某一直积因子构成的商群与另一直积因子同构，即$$G/G_2\cong G_1$$和$$G/G_1\cong G_2$$

* 六阶循环群$$C^6=C^2\otimes C^3$$，$$C^2=\left\{a^3, a^6=e\right\},C^3=\left\{a^2, a^4, a^6=e\right\}$$

* 若阶为$$n$$的群$$G$$中只有**部分元素**满足以下两个条件，那么称$$G_1$$和$$G_2$$的直积在与$$G$$相同的乘法下构成一个阶为$$n_1\times n_2$$的群，称为$$G_1$$和$$G_2$$的直积群，记为$$G_1\otimes G_2$$。$$G_1\otimes G_2$$是群$$G$$的一个子群
  * 可以**唯一**地表示为$$g_{\alpha\beta}=g_{1\alpha}g_{2\beta}$$，其中$$g_{1\alpha}\in G_1$$，$$g_{2\beta}\in G_2$$
  * 满足关系$$g_{1\alpha}g_{2\beta}=g_{2\beta}g_{1\alpha}$$

* 对于一般的置换群，有$$S_n\otimes S_m\subset S_{n+m}$$

* 设群$$G_a=\left\{\dotsb,g_a,\dotsb\right\}$$是$$n_a$$阶群，群$$G_b=\left\{\dotsb,g_b,\dotsb\right\}$$是$$n_b$$阶群，如果他们满足以下两个条件，那么就可以吧$$G_a$$和$$G_b$$直积起来，为$$G\equiv G_a\otimes G_b=\left\{\dotsb,g_ag_b,\dotsb\right\}$$
  * $$G_a$$和$$G_b$$最多只有一个公共元素，即单位元
  * $$G_a$$中的每一个元素都与$$G_b$$中的每一个元素对易

[返回目录](#0.0)

---

### <h02 id='2.0'>2.有限群表示论基础</h02>

[返回目录](#0.0)

#### 2.1 群表示的基本概念

* 线性空间$$R_n$$上的一个与$$G$$同构的矩阵群$$A\left(G\right)$$是群$$G$$的一个矩阵表示（或线性表示），简称表示

* $$A\left(G\right)$$的作用空间$$R_n$$称为群$$G$$的表示空间，$$R_n$$的矢量称为荷载群$$G$$的表示的基，$$R_n$$的维数（基的分量个数）称为表示的维数

* 若抽象群$$G$$与矩阵群$$A\left(G\right)$$同构，则称$$A\left(G\right)$$是群$$G$$的一个忠实表示（即能够精确地反映群$$G$$的结构）；若抽象群$$G$$同态于矩阵群$$A\left(G\right)$$，则称$$A\left(G\right)$$是群$$G$$的一个非忠实表示（即只能够部分地反映群$$G$$的结构，或精确地反映由群$$G$$的同态核$$H$$生成的商群$$G/H$$的结构）

* 所有的表示矩阵都是方阵
* 群$$G$$的单位元$$e$$所对应的表示矩阵$$A\left(e\right)$$一定是一个单位矩阵$$I$$，其阶为表示空间的维数
* 互逆群元素对应的表示矩阵一定是互逆矩阵，其乘积为单位矩阵$$I$$

* 求群表示的方法：
  * 选定群$$G$$作用的一个表示空间$$V$$，设$$\left\{\dotsb,\varphi_i,\dotsb\right\}$$是$$V$$中的一组基
  * 把每个群元素$$G_\alpha\in G$$分别作用到基分量$$\varphi_i$$上，所得到的新基分量$$g_\alpha\varphi_i$$可以使用原基线性展开为$$g_\alpha\varphi_i=\sum_jA_{ji}\left(g_\alpha\right)\varphi_j$$，于是便得到了一种对应关系

$$
g_\alpha\leftrightarrow A\left(g_\alpha\right)=
\begin{pmatrix}
 & \vdots & \\
 \ldots & A_{ji} & \ldots\\
 & \vdots & 
\end{pmatrix}
$$

* 群的表示满足乘法关系$$A\left(g_\alpha\right)A\left(g_\beta\right)=A\left(g_\alpha g_\beta\right)$$

* 常常采用的基有**内积空间中的矢量基**（基本表示）和**函数基**

* 函数积：指一组正交归一的完备的函数集合
$$
\left\{\varphi_i\left(\vec{r}\right)|i=1,2,\dotsb,n\right\}
$$
，它们作为基张成的线性空间称为函数空间。每个基分量$$\varphi_i\left(\vec{r}\right)$$都是矢量坐标$$\varphi_i\left(\vec{r}\right)$$都是矢量坐标$$\vec{r}=\left(\dotsb,r_j,\dotsb\right)$$的标量函数，它们有相同的定义域，满足$$\int\varphi_i^*\left(\vec{r}\right)\varphi_j\left(\vec{r}\right)\mathrm{d}v=\delta_{ij}$$，且该空间中的任意波函数$$\Phi\left(\vec{r}\right)$$均可以用这个基展开为$$\Phi\left(\vec{r}\right)=\sum_ic_i\varphi_i\left(\vec{r}\right)$$

* 主动变换观点（包含一起动）与被动变换观点

* 若群的所有元素都对应于一个单位矩阵，就得到仅有一个矩阵的表示，称为恒等表示

* 对于$$D_3$$群，有$$c=bab,d=ab,f=ba$$

#### 2.2 表示的等价性

* 表示矩阵的相似矩阵同样是表示矩阵，有$$A'\left(G\right)=S^{-1}A\left(G\right)S$$，其中$$S$$为不同基之间的变换矩阵

#### 2.3 表示的可约性

#### 2.3.1 可约表示

* 在表示空间$$V$$中选择适当的积，可以使得相应的表示矩阵具有简单的块结构，其中的对角块方阵可以对应一较小的表示空间$$W\subset V$$

* 至包含一个矩阵元全为零的块矩阵为具有块结构的矩阵，如

$$
\begin{pmatrix}
A & B\\
0 & C
\end{pmatrix},
\begin{pmatrix}
A & 0\\
0 & C
\end{pmatrix}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中第二种情况称为对角块结构

* 称$$A\left(G\right)$$是群$$G$$在表示空间$$V$$上的一个可约表示，如果$$A\left(G\right)$$的某一等价表示$$A\left(G\right)=XA\left(G\right)X^{-1}$$具有三角块结构，即对任一元素$$g\in G$$，有

$$
A'\left(g\right)=
\begin{pmatrix}
C\left(g\right) & N\left(g\right)\\
0 & B\left(g\right)
\end{pmatrix}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$X$$为非奇异矩阵

* $$A'\left(g\right)$$中的两个对角块方阵$$C\left(G\right)=\left\{\dotsb,C\left(g\right),\dotsb\right\}$$和$$B\left(G\right)=\left\{\dotsb,B\left(g\right),\dotsb\right\}$$都是群$$G$$的表示。因为对任意$$g_\alpha,g_\beta\in G$$，有

$$
\begin{aligned}
A'\left(g_\alpha\right)A'\left(g_\beta\right)=&
\begin{pmatrix}
C\left(g_\alpha\right) & N\left(g_\alpha\right)\\
0 & B\left(g_\alpha\right)
\end{pmatrix}
\begin{pmatrix}
C\left(g_\beta\right) & N\left(g_\beta\right)\\
0 & B\left(g_\beta\right)
\end{pmatrix}\\
=&
\begin{pmatrix}
C\left(g_\alpha\right)C\left(g_\beta\right) & C\left(g_\alpha\right)N\left(g_\beta\right)+C\left(g_\beta\right)N\left(g_\alpha\right)\\
0 & B\left(g_\alpha\right)B\left(g_\beta\right)
\end{pmatrix}
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;而

$$
A'\left(g_\alpha\right)A'\left(g_\beta\right)=A'\left(g_\alpha g_\beta\right)=
\begin{pmatrix}
C\left(g_\alpha g_\beta\right) & N\left(g_\alpha g_\beta\right)\\
0 & B\left(g_\alpha g_\beta\right)
\end{pmatrix}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此有

$$
C\left(g_\alpha\right)C\left(g_\beta\right)=C\left(g_\alpha g_\beta\right)\\
B\left(g_\alpha\right)B\left(g_\beta\right)=B\left(g_\alpha g_\beta\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;它们各自保持了乘法关系不变

* 群的表示矩阵若能够对角块化，说明群的表示空间$$V$$中存在一个$$G$$不变的真子空间$$W$$，而$$V$$是不变子空间$$W$$与其互补子空间$$W^\bot$$的直和

* 在真子空间$$W$$中的表示运算：通过选取合适的基的顺序，使得对于任意矢量$$\vec{y}\in W$$，有

$$
\vec{y}=\sum_{i=1}^n y_i\vec{e}_i=\sum_{i=1}^m y_i\vec{e}_i+0=
\begin{pmatrix}
y_i\\
0
\end{pmatrix}
\begin{aligned}
&\left.\right\}m\\
&\left.\right\}n-m
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;而所有群元素在这一组基上的表示矩阵为

$$
A'\left(g\right)=
\begin{pmatrix}
C\left(g\right) & N\left(g\right)\\
0 & B\left(g\right)
\end{pmatrix}
\begin{aligned}
&\left.\right\}m\\
&\left.\right\}n-m
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$C\left(g\right)$$和$$B\left(g\right)$$分别为$$m$$阶和$$n-m$$阶的方阵，群元素对矢量$$\vec{y}$$的运算为

$$
A'\left(g\right)\vec{y}=
\begin{pmatrix}
C\left(g\right) & N\left(g\right)\\
0 & B\left(g\right)
\end{pmatrix}
\begin{pmatrix}
y_i\\
0
\end{pmatrix}=
\begin{pmatrix}
C\left(g\right)y_i\\
0
\end{pmatrix}\in W
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;即$$A'\left(g\right)$$不会将$$W$$中的表示变出$$W$$

* 可约表示具有三角块结构是由于选择了一组适当的基。若某个表示矩阵不具有三角块结构，不见得它不是不可约的，因为有可能可以通过交换基的次序构造成为可约的三角块矩阵

* 由于$$W$$是$$G$$的不变子空间，可以称表示$$C\left(G\right)$$为可约表示$$A'\left(G\right)$$到$$W$$上的缩小，记为
$$
C\left(G\right)=A'\left(G\right)|_W
$$
，此时$$C\left(G\right)$$在$$W$$上的变换行为等同于$$A'\left(G\right)$$在$$W$$上的变换行为，即

$$
C\left(G\right)\left(y_i\right)=A'\left(g\right)
\begin{pmatrix}
y_i\\
0
\end{pmatrix}
$$

* 由于$$W^\bot$$不是$$G$$的不变子空间，所以$$B\left(G\right)$$不是$$A'\left(G\right)$$到$$W^\bot$$上的缩小，对于$$\vec{z}\in W^\bot$$，一般有

$$
A'\left(g\right)\vec{z}=
\begin{pmatrix}
C\left(g\right) & N\left(g\right)\\
0 & B\left(g\right)
\end{pmatrix}
\begin{pmatrix}
0\\
z_j
\end{pmatrix}=
\begin{pmatrix}
N\left(g\right)z_j\\
B\left(g\right)z_j
\end{pmatrix}
\notin W^\bot
$$

* 称$$N\left(g\right)\neq 0$$的表示为不可分表示，或可约但不完全可约表示

#### 2.3.2 完全可约表示

* 称$$A\left(G\right)$$是群$$G$$的一个完全可约表示，如果$$A\left(G\right)$$的某一等价表示$$A'\left(G\right)=XA\left(G\right)X^{-1}$$具有如下对角块结构

$$
A'\left(g\right)=
\begin{pmatrix}
C\left(g\right) & 0\\
0 & B\left(g\right)
\end{pmatrix}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;完全可约表示是可约表示在$$N\left(g\right)=0$$时的特例

* 从表示空间的角度来看，完全可约表示具有对角块结构是由于其表示空间$$V$$是其两个$$G$$不变真子空间的直和，即

$$
V=W\otimes W^\bot=\{\underbrace{e_1,\dotsb,e_m}_W,\underbrace{e_{m+1},\dotsb,e_n}_{W^\bot}\}
$$

* 完全可约的表示矩阵具有对角块的结构，表示$$C\left(G\right)$$和$$B\left(G\right)$$分别是完全可约表示$$A'\left(G\right)$$到$$W$$和$$W^\bot$$上的缩小

#### 2.3.3 不可约表示

* 称$$A\left(G\right)$$是群$$G$$的一个不可约表示，如果$$A\left(G\right)$$的所有等价表示都不具有块结构。从表示空间的角度来看，不可约表示$$A\left(G\right)$$不具有块结构是由于在其表示空间$$V$$中不存在$$G$$不变真子空间。此表示空间也称为不可约空间

* 将一个表示分解为若干不可约表示的直和的过程称为表示的约化

* 表示$$A\left(G\right)$$是完全可约的意味着其表示空间至少有两个互补的不变子空间

* 任何群的一维表示都是不可约的（即用一个数去表示一个群元素）

* 完全可约表示相对于约化后的若干个不可约表示来说，没有增加实质上的新内容

* 二阶循环群$$C_2=\left\{a,a^2=e\right\}$$有两个一维表示：

$$
A^1\left(a\right)\rightarrow1,\ \ \ A^1\left(a^2\right)=A\left(e\right)\rightarrow1\\
A^2\left(a\right)\rightarrow-1,\ \ \ A^2\left(a^2\right)=A\left(e\right)\rightarrow1\\
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中第一个为恒等表示

* 将上面两个一维表示进行直和运算，可以得到$$C_2$$群的二维表示$$A\left(C_2\right)=A_1\left(C_2\right)\oplus A_2\left(C_2\right)$$，即

$$
A\left(a\right)\rightarrow
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}
,\ \ \ A\left(a^2\right)=A\left(e\right)=
\begin{pmatrix}
1 & 0\\
0 & -1
\end{pmatrix}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以看到其没有增加实质上的新内容

* 实数加法群$$\left\{k\right\}$$有无穷多个不等价不可约表示$$\mathrm{e}^{k x}$$，还有一个二维表示
$$
\begin{pmatrix}
1 & 0\\
x & 1
\end{pmatrix}
$$。

#### 2.4 表示的幺正性

* 若群$$G$$的某一表示的所有表示矩阵都是幺正的，则称该表示是幺正表示（或酉表示），即任意元素$$g\in G$$的表示矩阵$$A\left(g\right)$$满足幺正条件$$A^\dagger\left(g\right)=A^{-1}\left(g\right)=A\left(g^{-1}\right)$$。其中第二个等式利用了同态的性质。荷载幺正表示的空间是复内积空间

* 幺正表示可约的群表示完全可约，即幺正表示要么是完全可约的，要么是不可约的，不可能是不可分表示

* 有限维幺正表示可以分解为有限个不可约幺正表示的直和，即$$V=W_1\oplus W_2\oplus\dotsb\oplus W_i\equiv\sum_{i=1}^q\oplus W_i$$，其中$$G$$在每个$$W_i$$上的（缩小）表示$$A^{\left(i\right)}\left(G\right)$$都是不可约的幺正表示。如果在$$V$$中选择如下排序的基

$$
V=\{\underbrace{e_{1},\dotsb,e_{m_1}}_{W_1},\underbrace{e_{m_1+1},\dotsb,e_{m_1+m_2}}_{W_2},\dotsb,\underbrace{\dotsb,e_{n}}_{W_q}\}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;那么所有群元素的表示矩阵$$A\left(g\right)$$都具有如下的对角块结构

$$
\begin{aligned}
A\left(g\right)=&
\begin{pmatrix}
A^{\left(1\right)}\left(g\right) & & & \\
 & A^{\left(2\right)}\left(g\right) & & \\
 & & \ddots & \\
 & & & A^{\left(q\right)}\left(g\right)
\end{pmatrix}\\
=&A^{\left(1\right)}\left(g\right)\oplus A^{\left(2\right)}\left(g\right)\oplus \dotsb\oplus A^{\left(q\right)}\left(g\right)\\
\equiv&\sum_{i=1}\oplus c_iA^{\left(i\right)}\left(g\right)
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$c_i$$为求直和时$$A^{\left(i\right)}\left(g\right)$$出现的次数，将等价表示合在了一起写

* 表示$$A\left(G\right)$$和$$A^{\left(i\right)}\left(g\right)$$的维数满足关系$$n=\sum_i c_im_i$$

* 对于一个有限群，求其表示的任务可以总结为：**全部的**、**不等价的**、**不可约的**、**幺正表示**

#### 2.5 一些理论与应用

#### 2.5.1 Maschke定理

* **Maschke定理**：有限群在内积空间上的任意一个表示都等价于一个幺正表示

* 在给定的内积空间，如果选择一组正交归一积，那么幺正变换$$\hat{U}$$相应的矩阵就是幺正矩阵；如果选择一组非正交基，那么幺正变换相应的矩阵就是非幺正的

* 在有限维复内积空间中，由非幺正表示到幺正表示的变换实际上反映了从一组斜坐标基到正交基的变换

* 有限群的幺正表示可约则完全可约。有限群的幺正表示要么是不可约的，要么等价于有限个不可约表示的直和

#### 2.5.2 Schur引理

* **Schur引理I**（仅适用于复表示）：若一个矩阵$$M$$于群$$G$$的一个不可约表示$$A$$中的所有表示矩阵对易，即

$$
\left[M,A\left(g\right)\right]=0,\ \ \ g\in G
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;那么$$M$$一定是一个常数矩阵

$$
M=\lambda I=\lambda
\begin{pmatrix}
1 & & 0\\
 & \ddots & \\
0 & & 1
\end{pmatrix}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\lambda$$是一个常数

* $$\mathrm{SO}\left(2\right)=\left\{C_k\left(\theta\right)\right\}$$群的二维表示
$$
A=
\begin{pmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{pmatrix}
$$
是不可约的，因为对于矩阵
$$
M=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
$$
，求
$$
MA=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
\begin{pmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{pmatrix}
=0
$$
的结果可以得到$$a=d,b=-c$$，由于$$M$$不是常数矩阵，因此$$A$$为可约表示，而且是完全可约表示

* **Schur引理II**：设$$A$$和$$B$$是群$$G$$的两个不等价的不可约表示，它们的维数分别为$$S_A$$和$$S_B$$，若一个$$S_B\times S_A$$矩阵$$M$$满足$$MA\left(g\right)=B\left(g\right)M$$，那么一定有$$M=0$$

* 任何Abel群的所有不可约表示都是一维的

* $$\mathrm{SO}\left(2\right)$$的一系列不可约表示为$$A_m=\left\{\mathrm{e}^{im\theta}\right\},\left(m=0,\pm1,\pm2,\dotsb\right)$$

#### 2.6 群函数

* 若存在一个从群$$G=\left\{\dotsb,g_i,\dotsb\right\}$$到复数域$${\Bbb C}$$内的映射$$\varphi:g_i\rightarrow\varphi\left(g_i\right)$$，其中$$\varphi\left(g_i\right)$$是复数，称$$\varphi\left(g_i\right)$$为群$$G$$上的函数，简称群函数。其中$$g_i$$是自变量，取值范围是$$G$$中的所有群元素

* $$n$$阶有限群只有$$n$$个线性独立的群函数

* 任何群函数$$\varphi\left(g_i\right)$$都可以用$$\left\{f_1\left(g_i\right),f_2\left(g_i\right),\dotsb,f_n\left(g_i\right)\right\}$$展开为$$\varphi\left(g_i\right)=\sum_{k=1}^n\varphi_k f_k\left(g_i\right)$$，其中$$\varphi_i$$为展开系数。$$n$$个群函数集合
$$
\left\{f_k\left(g_i\right)|k=1,2,\dotsb,n\right\}
$$
作为群函数的基张成一个$$n$$为线性空间，称为群函数空间$$V_G$$

* 在线性空间$$V_G$$中可以引入内积。对于任意两个群函数$$\varphi_k,\varphi_l\in V_G$$，其内积定义为

$$
\langle\varphi_k|\varphi_l\rangle\equiv\frac{1}{n}\sum_{i=1}^n\varphi_k^*\left(g_i\right)\varphi_l\left(g_i\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在该内积下，各基是正教的，但是不是归一的

* 群函数集合
$$
\left\{\sqrt{n}f_k\left(g_i\right)|k=1,2,\dotsb,n\right\}
$$
构成了$$V_G$$中的一组正交归一基

* 设$$A\left(G\right)$$是群$$G$$的一个表示。按照群函数的定义，表示矩阵$$A\left(g_k\right)$$的矩阵元$$A_{ij}\left(g_k\right)$$是$$G$$上的函数，$$g_k$$是自变量。由于这里的群函数是由表示产生的，所以称它们为群表示函数。若表示$$A\left(G\right)$$的维数为$$S_A$$，那么该表示总共可以产生$$S_A^2$$个群表示函数$$A_{ij}\left(g_k\right)(i,j=1,2,\dotsb,S_A)$$。反过来，给定一个群元素$$g'\in G$$，$$S_A^2$$个群表示函数的值的集合$$A_{ij}\left(g'\right)$$给出$$g'$$的表示矩阵

#### 2.7 正交性定理和完备性定理

* **正交性定理**：设$$n$$阶有限群$$G=\left\{\dotsb,g_k,\dotsb\right\}$$有不等价不可约的幺正表示$$A^{\left(p\right)}\left(G\right)$$和$$A^{\left(r\right)}\left(G\right)$$，它们的维数分别为$$S_p$$和$$S_r$$，那么由$$A^{\left(p\right)}\left(G\right)$$产生的$$S_p^2$$个群表示函数$$A_{\mu',\nu'}^{\left(r\right)}\left(g_k\right)$$满足关系

$$
\langle A_{\mu,\nu}^{\left(p\right)}\left(g_k\right)|A_{\mu',\nu'}^{\left(r\right)}\left(g_k\right)\rangle\equiv\frac{1}{n}\sum_{k=1}^nA_{\mu,\nu}^{\left(p\right)*}\left(g_k\right)A_{\mu',\nu'}^{\left(r\right)}\left(g_k\right)=\frac{1}{S_p}\delta_{pr}\delta_{\mu\mu'}\delta_{\nu\nu'}
$$

* **完备性定理**：有限群$$G$$的全部不等价不可约幺正表示$$A^{\left(i\right)}(i=1,2,\dotsb,q)$$产生的群表示函数集合
$$
\left\{A_{\mu,\nu}^{\left(i\right)}\left(g_k\right)|i=1,2,\dotsb,q;u,v=1,2,\dotsb,S_i\right\}
$$
构成了群表示函数空间上的一个完备集，任何群函数$$\psi\left(g_k\right)$$可以展开为$$\left\{A_{\mu,\nu}^{\left(i\right)}\left(g_k\right)\right\}$$的线性组合，即$$\psi\left(g_k\right)=\sum_{i\mu\nu}C_{\mu\nu}^{\left(i\right)}A_{\mu,\nu}^{\left(i\right)}\left(g_k\right)$$，其中$$C_{\mu\nu}^{\left(i\right)}$$为展开系数。利用正交性定理可以得到
$$
C_{\mu\nu}^{\left(i\right)}=S_p\langle A_{\mu\nu}^{\left(i\right)}|\psi\rangle
$$

* 有限群$$G$$的所有不等价不可约幺正表示$$A^{\left(i\right)}(i=1,2,\dotsb,q)$$产生的群表示函数集合

$$
\left\{\sqrt{S_i}A_{\mu\nu}^{\left(i\right)}\left(g_k\right)|i=1,2,\dotsb,q;\mu,\nu=1,2,\dotsb,S_i\right\}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;是群表示函数空间中的一组正交归一基，空间维数等于$$\sum_{i=1}^qS_i^2$$

* **Burnside 定理**：有限群的所有不等价不可约表示的维数平方和等于该群的阶，即$$S_1^2+S_2^2+\dotsb+S_q^2=n$$，其中$$S_i$$的取值为自然数，且至少有一项的取值为1，因为每个群都有一个一维恒等表示

#### 2.8 特征标理论

* **特征标的定义**：设$$A=\left\{A\left(g_\alpha\right)\right\}$$是群$$G=\left\{g_\alpha\right\}$$的一个表示，表示$$A$$的特征标定义为

$$
\chi^A=\left\{\dotsb,\chi^A\left(g_\alpha\right)=\sum_iA_{ii}\left(a_\alpha\right),\dotsb\right\}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\chi^A\left(g_\alpha\right)$$为表示矩阵的迹$$\mathrm{Tr}A\left(g_\alpha\right)$$，称为群元素$$g_\alpha$$的特征标

* 特征标$$\chi^A\left(g_\alpha\right)$$是一个群函数（从群到数的映射）

* 对群的某一表示来说，其单位元的特征标就等于该表示的维数

* 等价表示的特征标相等

* 不可约幺正表示的特征标的模等于1

* **特征标的第一正交关系**：不等价的不可约幺正表示的特征标正交，因为

$$
\langle\chi^{\left(p\right)}|\chi^{\left(r\right)}\rangle=\frac{1}{n}\sum_{k=1}^n\chi^{\left(p\right)}\left(g_k\right)\chi^{\left(r\right)}\left(g_k\right)=\frac{1}{n}\sum_{i,i'}\sum_{k=1}^nA_{ii}^{\left(p\right)*}\left(g_k\right)A_{i'i'}^{\left(r\right)}\left(g_k\right)=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;即
$$
\langle\chi^{\left(p\right)}|\chi^{\left(r\right)}\rangle=\delta_{pr}
$$

* 可约表示的特征标等于它所包含的不可约表示的特征标之和

* 特征标相等的表示等价

* 两表示等价的充分必要条件是它们的特征标相等

* 可约表示的特征标的模大于1

* 同类元素的特征标相等

* 称群函数$$f\left(K_i\right)$$是类函数，如果它满足$$f\left(K_i\right)=f\left(g_i\right)$$，其中$$K_i$$是群$$G$$中包含群元素$$g_i$$的类

* 利用类函数的性质，特征标的第一正交关系还可以写为

$$
\frac{1}{n}\sum_{i=1}^qn_i\chi^{\left(p\right)*}\left(K_i\right)\chi^{\left(r\right)}\left(K_i\right)=\delta_{pr}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$q$$是$$G$$的类的个数，$$n_i$$是第$$i$$个类$$K_i$$包含的元素个数

* **特征标的第二正交关系**：

$$
\frac{n_i}{n}\sum_{p=1}^q\chi^{\left(p\right)*}\left(K_i\right)\chi^{\left(p\right)}\left(K_{i'}\right)=\delta_{ii'}
$$

* **完备性定理**：全部不等价不可约幺正表示的特征标集合$$\left\{\chi^{\left(i\right)}\left(K_j\right)\right\}$$在类函数空间上是完备的。该集合可以作为类函数空间的一组基，空间中的任意类函数$$f\left(K_j\right)$$都可以用该组基线性展开，即$$f\left(K_j\right)=\sum_iC_i\chi^{\left(i\right)}\left(K_j\right)$$

* 因为一个不可约表示给出一个类函数，所以全部不等价不可约表示的数目等于类函数的数目。而完备的类函数的数目等于类的数目，于是对于有限群，有：**不等价不可约的表示的数目等于类的数目**

* 特征标的用途：
  * 判断两个表示是否等价（相等就等价）
  * 判断一个表示是否可约（可约的特征标模大于1，不可约的特征标正交）
  * 计算某一表示中包含哪些不可约表示，以及它们出现的次数

* $$D_3$$群的各种不可约表示有：
  * 一维不可约表示$$A_1$$：$$A_1\left(e\right)=A_1\left(d\right)=A_1\left(f\right)=1$$，$$A_1\left(a\right)=A_1\left(b\right)=A_1\left(c\right)=-1$$
  * 二维表示$$\Gamma$$为：

$$
\Gamma\left(e\right)=
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix},
\Gamma\left(d\right)=
\begin{pmatrix}
-\frac{1}{2} & -\frac{\sqrt{3}}{2}\\
\frac{\sqrt{3}}{2} & -\frac{1}{2}
\end{pmatrix},
\Gamma\left(f\right)=
\begin{pmatrix}
-\frac{1}{2} & \frac{\sqrt{3}}{2}\\
-\frac{\sqrt{3}}{2} & -\frac{1}{2}
\end{pmatrix}
$$

$$
\Gamma\left(a\right)=
\begin{pmatrix}
-1 & 0\\
0 & 1
\end{pmatrix},
\Gamma\left(b\right)=
\begin{pmatrix}
\frac{1}{2} & \frac{\sqrt{3}}{2}\\
\frac{\sqrt{3}}{2} & \frac{1}{2}
\end{pmatrix},
\Gamma\left(c\right)=
\begin{pmatrix}
\frac{1}{2} & -\frac{\sqrt{3}}{2}\\
-\frac{\sqrt{3}}{2} & -\frac{1}{2}
\end{pmatrix}
$$

* $$D_3$$群的全部不等价不可约表示的矩阵元与相应的函数值为

$$
\begin{matrix}
& &e &d &f &a &b &c\\
&S &1 &1 &1 &1 &1 &1\\
&A_1 &1 &1 &1 &-1 &-1 &-1\\
&\Gamma_{11} &1 &-1/2 &-1/2 &1 &-1/2 &-1/2\\
&\Gamma_{12} &0 &\sqrt{3}/2 &-\sqrt{3}/2 &0 &\sqrt{3}/2 &-\sqrt{3}/2\\
&\Gamma_{21} &0 &-\sqrt{3}/2 &\sqrt{3}/2 &0 &\sqrt{3}/2 &-\sqrt{3}/2\\
&\Gamma_{22} &1 &-1/2 &-1/2 &-1 &1/2 &1/2
\end{matrix}
$$

* $$D_3$$群的特征标表为

$$
\begin{matrix}
  & K_1=\left\{e\right\} & K_2=\left\{d,f\right\} & K_3=\left\{a,b,c\right\}\\
\chi^S\left(K_i\right) & 1 & 1 & 1\\
\chi^{A_1}\left(K_i\right) & 1 & 1 & -1\\
\chi^{\Gamma}\left(K_i\right) & 2 & -1 & 0
\end{matrix}
$$

#### 2.9 正则表示

#### 2.10 群表示的直积

* 设$$A=\left\{A\left(g_i\right)\right\}$$和$$B=\left\{B\left(g_i\right)\right\}$$是群$$G=\left\{g_i\right\}$$的两个表示，那么它们的直积$$A\otimes B=\left\{A\left(g_i\right)\otimes B\left(g_i\right)\right\}$$也是群$$G$$的一个表示

* 两个表示的直积的特征标等于这两个表示的特征标的乘积，即$$\chi^{A\otimes B}=\chi^A\chi^B$$

* 群的两个不可约表示的直积表示一般是可约的。对于有限群来说，其两个不可约表示的直积如果可约则必然完全可约，即可以分解为该群的不可约表示的直和

* 设$$A^{\left(i\right)}$$和$$A^{\left(j\right)}$$是$$n$$阶有限群$$G$$的两个不可约表示，那么有

$$
A^{\left(i\right)}\left(g\right)\otimes A^{\left(j\right)}\left(g\right)=\sum_k\oplus a_{ijk}A^{\left(k\right)}\left(g\right),\ \ \ g\in G
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这种分解方式称为CG展开，其中$$a_{ijk}$$称为约化系数，是一个非负整数，代表$$A^{\left(k\right)}\left(g\right)$$在直积表示中出现的次数

* 利用这些不可约表示的特征标，可以确定出$$a_{ijk}$$的值，即有

$$
a_{ijk}=\langle\chi^{\left(k\right)}|\chi^{\left(i\right)\otimes\left(j\right)}\rangle=\frac{1}{n}\sum_{l=1}^n\chi^{\left(k\right)}\left(g_l\right)^*\chi^{\left(i\right)\otimes\left(j\right)}\left(g_l\right)=
\frac{1}{n}\sum_{l=1}^n\chi^{\left(k\right)}\left(g_l\right)^*\chi^{\left(i\right)}\left(g_l\right)\chi^{\left(j\right)}\left(g_l\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\chi^{\left(k\right)}$$和$$\chi^{\left(i\right)\otimes\left(j\right)}$$分别是$$A^{\left(k\right)}$$和$$A^{\left(i\right)}\otimes A^{\left(j\right)}$$的特征标。上式也可写为

$$
a_{ijk}=\frac{1}{n}\sum_{l=1}^qn_l\chi^{\left(k\right)}\left(K_l\right)^*\chi^{\left(i\right)}\left(K_l\right)\chi^{\left(j\right)}\left(K_l\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$n_l$$是类$$K_l$$中的元素的数目

* 在表示空间中，有$$g\Phi_{i\alpha}=\left(g\psi_i\right)\left(g\varphi_\alpha\right)$$

* 荷载不可约表示$$A^{\left(k\right)}$$的基可以由$$\left\{\Phi_{i\alpha}\right\}$$的线性组合给出，即

$$
\phi_m^{\left(k\right),t}=\sum_{i\alpha}C_{m,i\alpha}^{\left(k\right),t}\Phi_{i\alpha}=\sum_{i\alpha}C_{m,i\alpha}^{\left(k\right),t}\psi_i\varphi_\alpha$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中展开系数$$C_{m,i\alpha}^{\left(k\right),t_k}$$称为群$$G$$的CG系数，$$m=1,2,\dotsb,S_k$$为基分量的标记，$$t_k$$用来区分等价的不可约表示

* $$D_3$$群的三个不可约表示$$S,A,\Gamma$$的直积表示以及约化为

$$
\begin{aligned}
&S\otimes A=A\\
&S\otimes \Gamma=\Gamma\\
&A\otimes \Gamma=\Gamma\\
&\Gamma\otimes\Gamma=S\oplus A\oplus\Gamma
\end{aligned}
$$

* 任何表示与恒等表示的直积等于该表示
* 不可约表示与一维表示的直积等于该不可约表示

* 当且仅当两个互为共轭表示的直积表示中才会出现且只出现一次恒等表示

#### 2.11 直积群的表示

* 两个群$$G_1=\left\{g_{1\alpha}\right\}$$和$$G_2=\left\{g_{2\beta}\right\}$$的直积群为$$G=G_1\otimes G_2=\left\{g_{\alpha\beta}\equiv g_{1\alpha}g_{2\beta}\right\}$$，因子群$$G_1$$和$$G_2$$都是$$G$$的不变子群

* 设$$A\left(G_1\right)=\left\{A\left(g_{1\alpha}\right)\right\}$$，$$B\left(G_2\right)=\left\{B\left(g_{2\beta}\right)\right\}$$分别是$$G_1$$和$$G_2$$的表示，那么它们的直积

$$
C\left(G\right)=A\left(G_1\right)\otimes B\left(G_2\right)=\left\{A\left(g_{1\alpha}\right)\otimes B\left(g_{2\beta}\right)\right\}=\left\{C\left(g_{\alpha\beta}\right)\right\}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;是直积群$$G=G_1\otimes G_2$$的表示（满足保乘关系）

* 直积群的特征标等于其因子群的特征标的乘积，即有

$$
\chi^{A\otimes B}\left(G\right)=\chi^A\left(G_1\right)\chi^B\left(G_2\right)
$$

* 如果直积群中的因子群的表示都是不可约的，那么该直积群的表示也是不可约的。如果其中一个因子群的表示是可约的，那么该直积群的表示就是可约的
* 直积群的类的个数等于其因子群的类的个数之积，所以它的不可约表示的个数等于其因子群的不可约表示的个数之积
* 直积群的不可约表示完全由其直积因子群的不可约表示决定

* 直积群的任意不可约表示都可以由它的两个因子群的不可约表示的直积构成
* 直积群的任意表示都可以约化称为一些不可约表示的直和，其中每个表示都是两个因子群的不可约表示的直积

#### 2.12  Dirac群和Clifford代数

* 在相对论量子力学中，4个Dirac矩阵$$\gamma_\mu$$满足关系$$\gamma_\mu\gamma_\nu+\gamma_nu\gamma_\mu=2\delta_{\mu\nu}$$，其中$$\gamma_\mu$$是由2阶单位阵和Pauli矩阵构成的4阶矩阵

* 定义乘法之后，可以由$$\gamma_\mu$$生成32个独立的群元素

$$
\left\{\pm1,\pm\gamma_\mu,\pm\gamma_\mu\gamma_\nu\left(\mu<\nu\right),\pm\gamma_\mu\gamma_5,\pm\gamma_5\right\}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\gamma_5=\gamma_1\gamma_2\gamma_3\gamma_4$$，有$$\gamma_5^2=1$$

* 即会构成一个32阶的群，称之为Dirac群$$G_D$$，群元素分为17个类（1+1+4+6+4+1）

* 设$$\gamma_\mu$$矩阵的阶为$$S>1$$，则利用迹的循环性，可以得到$$\gamma_i\left(i=1,2,\dotsb,32\right)$$的特征标满足

$$
\chi\left(\gamma_i\right)=\left\{
\begin{aligned}
&0 &\gamma_i\neq\pm1\\
&S &\gamma_i=1\\
&-S &\gamma_i=-1
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若对$$\gamma_\mu$$所取的矩阵实现使得$$G_D$$的资深表示是不可约的，那么有

$$
1=\langle\chi|\chi\rangle=\frac{1}{32}\sum_{i=1}^32\chi^*\left(\gamma_i\right)\chi\left(\gamma_i\right)=\frac{1}{32}\left[S^2+\left(-S\right)^2\right]=\frac{1}{16}S^2
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;得到$$S=4$$，即$$\gamma_\mu$$的不可约表示矩阵的阶为4，$$G_D$$有16个1维不可约表示和1个4维不可约表示

* 假设$$\gamma_4$$是对角阵，考虑到$$\gamma_4^2=1$$，$$\mathrm{Tr}\gamma_4=0$$，设
$$
\gamma_4=
\begin{pmatrix}
I & 0\\
0 & -I
\end{pmatrix}$$，而$$\gamma_1$$、$$\gamma_2$$、$$\gamma_3$$应当满足
$$
\gamma_i=
\begin{pmatrix}
0 & N_i\\
N_i^\dagger & 0
\end{pmatrix}
$$，其中$$N_i^\dagger N_j+N_j^\dagger N_i=2\delta_{ij}I$$。因此可以取Pauli矩阵$$N_i=\sigma_i,\left(i=1,2,3\right)$$作为一组特解，求出$$\gamma_1$$、$$\gamma_2$$、$$\gamma_3$$的矩阵形式为
$$
\gamma_i=
\begin{pmatrix}
0 & \sigma_i\\
\sigma_i & 0
\end{pmatrix}
$$

* Clifford代数：满足结构$$\gamma_\mu\gamma_\nu+\gamma_\nu\gamma_\mu=2\eta_{\mu\nu}$$的结构的代数，其中$$\mu,\nu=1,2,\dotsb$$，$$p+q\equiv N$$，且

$$
\eta_{\mu\nu}=\left\{
\begin{aligned}
&0 &\mu\neq\nu\\
&1 &\mu=\nu=1,2,\dotsb,p\\
&-1 &\mu=\nu=p+1,p+2,\dotsb,p+q
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;记此代数为$$C\left(p,q\right)$$，显然$$C\left(4,0\right)$$就是Dirac代数

#### 2.13 广义投影算符

* 一个$$S_p$$维的不可约表示可以构造出$$S_p^2$$个广义投影算符，所以$$n$$阶有限群$$G$$一共有$$n$$个广义投影算符
$$
\left\{P_{mn}^{\left(i\right)}|i=1,2,\dotsb,q;m,n=1,2,\dotsb,S_i\right\}
$$，其中$$q$$为类的个数

* 两个广义投影算符$$P_{kl}^{\left(p\right)}$$和$$P_{st}^{\left(r\right)}$$满足乘法规则$$P_{kl}^{\left(p\right)}P_{st}^{\left(r\right)}=\delta_{pr}\delta_{ls}P_{kt}^{\left(p\right)}$$

* 如果已经知道荷载$$S_p$$维不可约表示$$A^{\left(p\right)}$$的某一个基分量，那么可以利用$$P_{kl}^{\left(p\right)}$$将其与$$S_p-1$$个基分量找出来

[返回目录](#0.0)

---

### <h05 id='5.0'>5.典型李群的张量表示</h05>

[返回目录](#0.0)

#### 5.1 李群的例子

* 阶数：李群的独立实参数的个数

* 复一般线性群$${\rm GL}(n,{\Bbb C})$$的阶数为$$2n^2$$

* 实一般线性群$${\rm GL}(n,{\Bbb R})$$的阶数为$$n^2$$

* 复特殊线性群（幺模，行列式为1）$${\rm SL}(n,{\Bbb C})$$的阶数为$$2n^2-2$$

* 实特殊线性群（幺模，行列式为1）$${\rm SL}(n,{\Bbb R})$$的阶数为$$n^2-1$$

* 酉群
$$\{u|u\in {\rm GL}(n,{\Bbb C}),u^\dagger u=uu^\dagger=I_n\}$$
的阶数为$$2n^2-\frac{1}{2}n(n-1)\times2-n=n^2$$。其中$$n$$没有乘二是因为幺正本身已经保证了对角元为实数

* 在酉群$${\rm U}(n)$$的作用下矢量空间中内积保持不变，即有

$$
\sum_{i=1}^n|x_i|^2=\sum_{i=1}^n|x'_i|^2
$$

* 引入$${\rm U}(n,m)$$群的概念，定义为保持

$$
\sum_{i=1}^n|x_i|^2-\sum_{i=n+1}^m|x_i|^2=\sum_{i=1}^n|x'_i|^2-\sum_{i=n+1}^m|x'_i|^2
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;不变的线性变换

* 满足幺模条件的$${\rm U}(n)$$群为$${\rm SU}(n)$$群。由于幺正条件已经保证了行列式的模方为1，因此其阶数为$$n^2-1$$

* 类似的可以定义出$${\rm SU}(n,m)$$群

* 复正交群$${\rm O}(n,\Bbb C)=\{R\in{\rm GL}(n,\Bbb C),R^TR=RR^T=I_n\}$$的阶数为$$2n^2-\frac{1}{2}n(n-1)\times2-2n=n(n-1)$$

* 实数域上的实正交群$${\rm O}(n,\Bbb R)=\{R\in{\rm GL}(n,\Bbb R),R^TR=RR^T=I_n\}$$的阶数为$$n^2-\frac{1}{2}n(n-1)-n=\frac{1}{2}n(n-1)$$

* $$\rm O$$群保持长度不变，$$\rm U$$群保持内积不变

* 同样可以引入$${\rm O}(n,m)$$群

* 满足幺模条件的复正交群为复特殊正交群
$${\rm SO}(n,{\Bbb C})=\{R|R\in{\rm O}(n,{\Bbb C}),{\rm det}R=1\}$$，其阶数为$$n(n-1)$$，因为幺模条件没有增加任何实质上的限制

* 实数域上的实特殊正交阵$${\rm SO}(n)$$群的阶数为$$\frac{1}{2}n(n-1)$$，它与$$n$$维实线性矢量空间中的纯转动群同构

* $${\rm SO}(3,1)$$群为Lorentz群，它保持Minkowski空间中的四维矢量$$(x,y,z,ict)$$的长度$$x^2+y^2+z^2-c^2t^2$$不变

* 保持$$2n$$维复线性矢量空间$$V_n$$中的两个矢量$$(x_1,\dotsb,x_n;x'_1,\dotsb,x'_n)$$和$$(y_1,\dotsb,y_n;y'_1,\dotsb,y'_n)$$的反对称双线性形式$$\sum_{i=1}^n(x_iy'_i-x'_iy_i)$$不变的所有复线性变换构成$$2n$$维复辛群，记为$${\rm Sp}(2n,{\Bbb C})$$。其定义为

$$
{\rm Sp}(2n,{\Bbb C})=\{g|g\in{\rm SL}(2n,{\Bbb C}),g^TJg=J\}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中
$$
J=
\begin{pmatrix}
0 & I_n\\
I_n & 0
\end{pmatrix}
$$

* 仅当矢量空间的维数是偶数时，才能定义辛群

* 可以类似地定义出$$2n$$维酉辛群

* 辛群$${\rm Sp}(2n,{\Bbb C})$$的阶为
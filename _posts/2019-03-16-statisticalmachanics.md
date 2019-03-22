---
layout: formula
title:  "统计力学公式"
date:   2019-03-16 09:00:00 +0800
tags: [Qualifying Exam, Physics]
categories: [Qualifying Exam]
description: 博资考中可能用到的统计力学原理与公式
---

<!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->

# <h00 id='0.0'>统计力学公式</h00>

### 目录

* [1.玻尔兹曼统计与配分函数](#1.0)
* [2.玻色-爱因斯坦统计](#2.0)
* [3.费米-狄拉克统计](#3.0)
* [4.巨配分函数与各力学量](#4.0)
* [5.三种统计的关系](#5.0)
* [6.关于态密度与配分函数的计算](#6.0)
* [7.其它一些热力学量的关系与琐碎的项](#7.0)

---

### <h01 id='1.0'>1.玻尔兹曼统计与配分函数</h01>

[返回目录](#0.0)

* 将可分辨的全同近独立粒子组成的，且处在某一个状态上的粒子数不受限制的系统称为玻尔兹曼系统。设系统包含若干能级，第$$l$$个能级的能量为$$\varepsilon_l$$、包含$$g_l$$个量子态，且第$$l$$个能级上的粒子数为$$a_l$$，则由于每一个量子态可以容纳的粒子数不受限制，系统总的微观状态数可以表示为

$$
\omega_{M.B}=\frac{N!}{\prod\limits_l a_l!}\prod\limits_l g_l^{a_l}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据系统粒子数与总能量的限制条件，有

$$
a_l=g_l\mathrm{e}^{-\alpha-\beta\varepsilon_l}=\frac{g_l}{\mathrm{e}^{\alpha+\beta\varepsilon_l}}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中

$$
\alpha = -\frac{\mu}{k_BT},\ \ \ \beta=\frac{1}{k_BT}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;相应地可以将系统的粒子数与总内能表示为

$$
N = \sum\limits_l a_l = \sum\limits_l g_l \mathrm{e}^{-\alpha-\beta\varepsilon_l}\\
U_l = \sum\limits_l \varepsilon_l a_l = \sum\limits_l \varepsilon_l g_l \mathrm{e}^{-\alpha-\beta\varepsilon_l}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可引入配分函数

$$
Z' = \sum\limits_l g_l \mathrm{e}^{-\beta\varepsilon_l}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则有

$$
\alpha = \ln \frac{Z'}{N}\ \ \ U = -N \frac{\partial}{\partial\beta} \ln Z'\ \ \ p=\frac{N}{\beta}\frac{\partial}{\partial V}\ln Z'
$$

* 玻尔兹曼系统的熵可以表示为

$$
S=Nk_B\left(\ln Z'-\beta\frac{\partial \ln Z'}{\partial \beta}\right)=k_B\ln\omega_{max}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;自由能大小为

$$
F=U-TS=-N\frac{\partial}{\partial\beta}\ln Z'-Nk_BT\left(\ln Z'-\beta\frac{\partial \ln Z'}{\partial \beta}\right)=-\frac{N}{\beta}\ln Z'
$$

[返回目录](#0.0)

---

### <h02 id='2.0'>2.玻色-爱因斯坦统计</h02>

[返回目录](#0.0)

* 将由不可分辨全同近独立粒子组成的，且处在某一个状态上的粒子数不受限制的系统称为玻色系统。设系统包含若干能级，第$$l$$个能级的能量为$$\varepsilon_l$$、包含$$g_l$$个量子态，且第$$l$$个能级上的粒子数为$$a_l$$，则系统的总微观状态数可以表示为

$$
\omega_{B.E.}=\prod\limits_l\frac{\mathcal{A}_{g_l-1+a_l}^{g_l-1+a_l}}{\mathcal{A}_{g_l-1}^{g_l-1}\mathcal{A}_{a_l}^{a_l}}=\prod\limits_l\frac{\left(g_l+a_l-1\right)!}{a_l!\left(g_l-1\right)!}=\prod\limits_l \mathcal{C}_{g_l+a_l-1}^{a_l}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据系统粒子数与总能量的限制条件，有

$$
a_l=\frac{g_l}{\mathrm{e}^{\alpha+\beta\varepsilon_l}-1}
$$

[返回目录](#0.0)

---

### <h03 id='3.0'>3.费米-狄拉克统计</h03>

[返回目录](#0.0)

* 将由不可分辨全同近独立粒子组成的，且在某一个状态上只能同时存在一个粒子的系统称为费米系统。设系统包含若干能级，第$$l$$个能级的能量为$$\varepsilon_l$$、包含$$g_l$$个量子态，且第$$l$$个能级上的粒子数为$$a_l$$，则系统的总微观状态数可以表示为

$$
\omega_{F.D.}=\prod\limits_l\mathcal{C}_{g_l}^{a_l}=\prod\limits_l\frac{g_l!}{a_l!{\left(g_l-a_l\right)!}}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据系统粒子数与总能量的限制条件，有

$$
a_l=\frac{g_l}{\mathrm{e}^{\alpha+\beta\varepsilon_l}+1}
$$

[返回目录](#0.0)

---

### <h04 id='4.0'>4.巨配分函数与力学量</h04>

[返回目录](#0.0)

* 对于玻色系统与费米系统，可以构造巨配分函数有

$$
\mathit{\Xi}'_{B.E.}=\prod\limits_l\left(1-\mathrm{e}^{-\alpha-\beta\varepsilon_l}\right)^{-g_l},\ \ \ 
\mathit{\Xi}'_{F.D.}=\prod\limits_l\left(1+\mathrm{e}^{-\alpha-\beta\varepsilon_l}\right)^{-g_l}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;两系统的平均总粒子数、内能和压强的微观统计表达式相同，可以表示为

$$
N=-\frac{\partial}{\partial\alpha}\ln\mathit{\Xi}'\ \ \ 
U=-\frac{\partial}{\partial\beta}\mathit{\Xi}'\ \ \ 
p=\frac{1}{\beta}\frac{\partial}{\partial V}\ln\mathit{\Xi}'
$$

[返回目录](#0.0)

---

### <h05 id='5.0'>5.三种统计的关系</h05>

[返回目录](#0.0)

* 当任一能级$$\varepsilon_l$$上的粒子数均远小于该能级的量子态数，即

$$
\frac{a_l}{\omega_l}\ll1,\ l=1,2,3,\dotsb
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;时，被称为经典极限条件（或非简并性条件），此时各个统计中系统的微观状态数可以近似为

$$
\omega_{B.E.}\approx\omega_{F.D.}\approx\prod\limits_l\frac{\omega_l^{a_l}}{a_l!}=\frac{\omega}{N!}
$$

* 对于满足经典极限条件的玻色系统和费米系统，其内能与广义力的微观统计表达式与玻尔兹曼系统完全相同，但是由于其微观粒子的不可分辨性，需要将玻尔兹曼关系改写为

$$
S_{B.E.}=k\ln\frac{\omega_{B.E.}}{N!},\ \ \ S_{F.D.}=k\ln\frac{\omega_{F.D.}}{N!}
$$

* 不管对何种分布，关系$$S=k_B\ln\omega$$始终满足

* 斯特林公式：$$\ln m!\approx m\left(\ln m-1\right)$$

* 整理表格如下

|              | 麦克斯韦-玻尔兹曼系统 | 玻色-爱因斯坦系统 | 费米-狄拉克系统 |
| :----------: | :---------: | :-------: | :------: |
| 微观状态数 | $$\omega_{M.B}=\frac{N!}{\prod\limits_l a_l!}\prod\limits_l g_l^{a_l}$$ | $$\omega_{B.E.}=\prod\limits_l \mathcal{C}_{g_l+a_l-1}^{a_l}$$ | $$\omega_{F.D.}=\prod\limits_l\mathcal{C}_{g_l}^{a_l}$$ |
| 第$$l$$能级的粒子数 | $$a_l=\frac{g_l}{\mathrm{e}^{\alpha+\beta\varepsilon_l}}$$ | $$a_l=\frac{g_l}{\mathrm{e}^{\alpha+\beta\varepsilon_l}-1}$$ | $$a_l=\frac{g_l}{\mathrm{e}^{\alpha+\beta\varepsilon_l}+1}$$ |
| （巨）配分函数 | $$Z'=\sum\limits_l g_l\mathrm{e}^{-\beta\varepsilon_l}$$ | $$\mathit{\Xi}'=\prod\limits_l\left(1-\mathrm{e}^{-\alpha-\beta\varepsilon_l}\right)^{-g_l}$$ | $$\mathit{\Xi}'=\prod\limits_l\left(1+\mathrm{e}^{-\alpha-\beta\varepsilon_l}\right)^{-g_l}$$ |
| 粒子数$$N$$ | $$N=Z'\mathrm{e}^{-\alpha}$$ | $$N=-\frac{\partial}{\partial\alpha}\ln\mathit{\Xi}'$$ | $$N=-\frac{\partial}{\partial\alpha}\ln\mathit{\Xi}'$$ |
| 内能$$U$$ | $$U=-\frac{\partial}{\partial\beta}\ln Z'$$ | $$U=-\frac{\partial}{\partial\beta}\ln\mathit{\Xi}'$$ | $$U=-\frac{\partial}{\partial\beta}\ln\mathit{\Xi}'$$ |
| 压强$$p$$ | $$p=\frac{1}{\beta}\frac{\partial}{\partial V}\ln Z'$$ | $$p=\frac{1}{\beta}\frac{\partial}{\partial V}\ln\mathit{\Xi}'$$ | $$p=\frac{1}{\beta}\frac{\partial}{\partial V}\ln\mathit{\Xi}'$$ |
| 熵$$S$$ | $$S=k_B\left(\ln Z'-\beta\frac{\partial}{\partial\beta}\ln Z'\right)=k_B\ln Z'+\frac{U}{T}$$ | $$S=k_B\left(\ln\mathit{\Xi}'+\alpha N+\beta U\right)$$ | $$S=k_B\left(\ln\mathit{\Xi}'+\alpha N+\beta U\right)$$ |
{:class="table table-bordered"}
{:.table-striped}

[返回目录](#0.0)

---

### <h06 id='6.0'>6.关于态密度与配分函数的计算</h06>

[返回目录](#0.0)

#### 对于某一运动的粒子，计算其运动的配分函数的大致步骤如下：

* 首先写出其配分函数的一般表达式有

$$
Z'=\int\frac{\mathrm{d}\omega}{h^3}\mathrm{e}^{-\alpha-\beta\varepsilon}=\int\frac{1}{h^3}\mathrm{e}^{-\alpha-\beta\varepsilon}\mathrm{d}x\mathrm{d}y\mathrm{d}z\mathrm{d}p_x\mathrm{d}p_y\mathrm{d}p_z
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\mathrm{d}\omega$$是对动量空间与真实空间的积分（包含6个积分变量）

* 接下来，从$$\varepsilon$$中将空间部分与速度部分分开，空间部分与$$\mathrm{d}x$$一起积分，速度部分与$$\mathrm{d}p_x$$一起积分。真实空间的体积元化为球积分有

$$
\mathrm{d}x\mathrm{d}y\mathrm{d}z=r^2\mathrm{d}r\sin\theta\mathrm{d}\theta\mathrm{d}\varphi
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;动量空间的体积元化为求面积分有

$$
\mathrm{d}p_x\mathrm{d}p_y\mathrm{d}p_z=4\pi p^2\mathrm{d}p
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;分别积分并相乘，即可得到配分函数的表达式

* 若已知配分函数，则态密度可以表示为

$$
p=\frac{1}{Z}\int_x\int_p\frac{1}{h^3}\mathrm{e}^{-\alpha-\beta\varepsilon}\mathrm{d}x\mathrm{d}p
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\int_x$$和$$\int_p$$分别为对指定空间范围和动量范围的积分

[返回目录](#0.0)

---

### <h07 id='7.0'>7.其它一些热力学量的关系与琐碎的项</h07>

[返回目录](#0.0)

* 亥姆霍兹自由能：$$F=U-TS=-k_BT\ln Z$$
* 吉布斯函数：$$G=N\mu=-Nk_BT\alpha$$
* 巨热力势：$$\Psi=F-G=-k_BT\ln\mathit{\Xi}'$$

* 理想气体的熵

$$
S_m=C_{V,m}\ln T+R\ln V_m+S_0
$$

* 积分运算

$$
\int_0^\infty\mathrm{e}^{-x^2}x^2\mathrm{d}x=\frac{\sqrt{\pi}}{4}\\
\int_0^\infty\mathrm{e}^{-x^2}x\mathrm{d}x=\frac{1}{2}\\
\int_0^\infty\mathrm{e}^{-x^2}\mathrm{d}x=\frac{\sqrt{\pi}}{2}
$$

* 无限求和的结果

$$
\sum\limits_k^\infty\mathrm{e}^{-ak}=\frac{1}{1-\mathrm{e}^{-a}}
$$

* 全同粒子的附加项吉布斯自由能为$$k_BT\ln n!$$

* 斯特林公式：$$\ln m!\approx m\left(\ln m-1\right)$$

* 热力学变换：$$\mathrm{d}U=T\mathrm{d}S-p\mathrm{d}V$$，$$H=U+pV$$，$$F=U-TS$$，$$G=U-TS+pV$$

* 组合系统的配分函数可以表示为**独立子系统**的配分函数的乘积

* 若已知系统内能$$U$$，求解各力学量：

$$
T=\frac{\partial U}{\partial S},\ \ \ p=-\frac{\partial U}{\partial V},\ \ \ \mu=\frac{\partial U}{\partial N}
$$

* 等容摩尔热容与等压摩尔热容：

$$
C_{V,m}=\frac{N_A}{N}\frac{\partial U}{\partial T},\ \ \ C_{p,m}=\frac{N_A}{N}\frac{\partial H}{\partial T},\ \ \ \gamma=\frac{C_p}{C_V}
$$

* 当粒子数不守恒时，有$$\alpha=-\mu/k_BT=0$$

* 克劳修斯-克拉伯龙方程：

$$
\frac{\mathrm{d}p}{\mathrm{d}T}=\frac{L}{T\left(V_l-V_s\right)}
$$

* 黑体辐射在$$f\sim f+\mathrm{d}f$$频率范围内的辐射能量密度可以表示为

$$
U\left(f,T\right)\mathrm{d}f=\frac{8\pi hf^3}{c^3}\frac{1}{\mathrm{e}^{hf/k_BT}-1}\mathrm{d}f
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;相应的光子数密度可以表示为

$$
n\left(f,T\right)\mathrm{d}f=\frac{8\pi f^2}{c^3}\frac{1}{\mathrm{e}^{hf/k_BT}-1}\mathrm{d}f
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;总的光子数密度为

$$
n\left(T\right)=\int_0^\infty n\left(f,T\right)\mathrm{d}f=8\pi\left(\frac{k_BT}{cn}\right)^3\int_0^\infty\frac{x^2}{\mathrm{e}^x-1}\mathrm{d}x
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中，积分的数值结果为

$$
\int_0^\infty\frac{x^2}{\mathrm{e}^x-1}\mathrm{d}x\approx2.404
$$

* 单个气体分子转动的配分函数可以表示为

$$
z_R=\sum_J\left(2J+1\right)\mathrm{e}^{-\varepsilon_J}\ \ \ \varepsilon_J=\frac{\hbar^2}{2I}J\left(J+1\right)
$$

[返回目录](#0.0)

---

特别感谢CMQ同学的讲解和SJW同学的讨论。祝我们好运！
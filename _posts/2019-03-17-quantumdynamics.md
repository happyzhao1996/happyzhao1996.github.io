---
layout: formula
title:  "量子力学公式"
date:   2019-03-17 15:52:54 +0800
tags: [Qualifying Exam, Physics]
categories: [Qualifying Exam]
description: 博资考中可能用到的量子力学原理与公式
---

<!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->

# <h00 id='0.0'>量子力学公式</h00>

### 目录

* [1.关于粒子的散射](#1.0)
* [2.关于一维谐振子](#2.0)
* [3.一维谐振子的坐标表象](#3.0)
* [4.关于有限深方势阱](#4.0)
* [5.关于自旋](#5.0)
* [6.关于微扰](#6.0)
* [7.其它一琐碎的项](#7.0)

---

### <h01 id='1.0'>1.关于粒子的散射</h01>

[返回目录](#0.0)

* 粒子散射的能量需要在质心系中计算

* 约化质量$$\mu=\left(m_1m_2\right)/\left(m_1+m_2\right)$$

* 高能情况下应用Born近似，则散射波振幅可以表示为

$$
f\left(\theta\right)=-\frac{2\mu}{\hbar^2}\int_0^\infty\frac{\sin qr}{qr}V\left(r\right)\cdot r^2\mathrm{d}r
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$q=2k\sin\left(\theta/2\right)$$，积分可能需要用到分部积分公式

* 对于自旋为$$1/2$$的粒子，总自旋的不同取值所对应的微分散射截面分别为

$$
\sigma_s=\sigma_{S=1}=\left|f\left(\theta\right)-f\left(\pi-\theta\right)\right|^2\\
\sigma_a=\sigma_{S=0}=\left|f\left(\theta\right)+f\left(\pi-\theta\right)\right|^2
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\sigma_s$$为交换对称的自旋三态，$$\sigma_a$$为交换反对称的自旋单态

* 总的散射截面可以表示为

$$
\sigma\left(\theta\right)=\frac{3}{4}\sigma_s\left(\theta\right)+\frac{1}{4}\sigma_a\left(\theta\right)
$$

* 测得$$S=1$$和$$S=0$$的概率分别为

$$
p_1=\frac{3}{4}\frac{\sigma_s\left(\theta\right)}{\sigma\left(\theta\right)},\ \ \ p_0=\frac{1}{4}\frac{\sigma_a\left(\theta\right)}{\sigma\left(\theta\right)}
$$

* 其中$$S=1$$的情况中包含了自旋都朝上、自旋都朝下和自旋交换对称的叠加态三种状态，各自几率相等

[返回目录](#0.0)

---

### <h02 id='2.0'>2.关于一维谐振子</h02>

[返回目录](#0.0)

* 对于一维谐振子，其哈密顿量可以表示为

$$
\hat{H}=\frac{p^2}{2m}+\frac{1}{2}m\omega x^2
$$

* 若引入无量纲算符

$$
\hat{P}=\sqrt{\frac{1}{m\omega\hbar}}p,\ \ \ \hat{Q}=\sqrt{\frac{m\omega}{\hbar}}x
$$

* 则升降算符可以表示为

$$
\hat{a}^+=\frac{1}{\sqrt{2}}\left(\hat{Q}+i\hat{P}\right),\ \ \ \hat{a}=\frac{1}{\sqrt{2}}\left(\hat{Q}-i\hat{P}\right),
$$

* 升降算符的组合为粒子数算符
$$\hat{n}=\hat{a}^+\hat{a}$$
，则哈密顿量可以表示为

$$
\hat{H}=\left(\hat{n}+\frac{1}{2}\right)\hbar\omega
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面求它的本征值和本征态

* 设本征方程为
$$\hat{n}\left|n\right>=n\left|n\right>$$
由于升降算符满足
$$\left[\hat{a},\hat{a}^+\right]=\hat{a}\hat{a}^+-\hat{a}^+\hat{a}=1$$
，因此

$$
\hat{n}\hat{a}\left|n\right>=\hat{a}^+\hat{a}\hat{a}\left|n\right>=\left(\hat{a}\hat{a}^+-1\right)\hat{a}\left|n\right>\\
=\left(\hat{a}\hat{a}^+\hat{a}-\hat{a}\right)\left|n\right>=\hat{a}\left(\hat{a}^+\hat{a}-1\right)\left|n\right>\\
=\hat{a}\left(\hat{n}-1\right)\left|n\right>=\left(n-1\right)\hat{a}\left|n\right>\\
\hat{n}\hat{a}^+\left|n\right>=\hat{a}^+\hat{a}\hat{a}^+\left|n\right>=\hat{a}^+\left(\hat{a}^+\hat{a}+1\right)\left|n\right>\\
=\hat{a}^+\left(\hat{n}+1\right)\left|n\right>=\left(n+1\right)\hat{a}^+\left|n\right>
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;即
$$\hat{a}\left|n\right>$$
和
$$\hat{a}^+\left|n\right>$$
都是算符$$\hat{n}$$的本征态

* 考虑到
$$\hat{a}\left|n\right>$$
和
$$\hat{a}^+\left|n\right>$$
各自的本征值为$$n-1$$和$$n+1$$，我们将各自的作用方程写为

$$
\hat{a}\left|n\right>=a_n\left|n-1\right>\\
\hat{a}^+\left|n\right>=b_n\left|n+1\right>\\
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;共轭的方程为

$$
\left<n\right|\hat{a}^+=\left<n-1\right|a_n^*\\
\left<n\right|\hat{a}=\left<n+1\right|b_n^*\\
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;分别相乘，可以解出
$$
a_n=\sqrt{n},\ \ \ b_n=\sqrt{n+1}
$$
即有

$$
\hat{a}\left|n\right>=\sqrt{n}\left|n-1\right>\\
\hat{a}^+\left|n\right>=\sqrt{n+1}\left|n+1\right>
$$

[返回目录](#0.0) 

---

### <h03 id='3.0'>3.一维谐振子的坐标表象</h03>

[返回目录](#0.0)

* 在坐标表象下，使用公式
$$
\hat{a}\left|0\right>=0
$$
可以计算得到一维谐振子基态波函数为

$$
\Psi_0\left(x\right)=\left(\frac{m\omega}{\pi\hbar}\right)^{\frac{1}{4}}\mathrm{e}^{-\frac{m\omega}{2\hbar}x^2}
$$

[返回目录](#0.0)

---

### <h04 id='4.0'>4.关于有限深方势阱</h04>

[返回目录](#0.0)

* 设能量为$$E$$，势阱范围为$$\left[-a/2,a/2\right]$$，势阱内能势能为$$0$$，势阱外势能为$$V$$

* 在坐标表象下进行研究。写出薛定谔方程为

$$
\hat{H}\psi=E\psi
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于在坐标表象下，哈密顿量可以表示为

$$
\hat{H}=\frac{\hat{p}^2}{2m}+V\left(x\right)
$$

$$
\hat{p}=-i\hbar\frac{\partial}{\partial x}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此薛定谔方程可以表示为

$$
-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}\psi\left(x\right)+V\left(x\right)\psi\left(x\right)=E\psi\left(x\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以变形为

$$
\ddot{\psi}\left(x\right)+\frac{2m\left[E-V\left(x\right)\right]}{\hbar^2}\psi\left(x\right)=0
$$

* 当$$x\in\left[-a/2,a/2\right]$$时，有$$V\left(x\right)=0$$，即哈密顿方程变为

$$
\ddot{\psi}\left(x\right)+\frac{2mE}{\hbar^2}\psi\left(x\right)=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此时令$$k^2=2mE/\hbar^2$$，则有

$$
\ddot{\psi}\left(x\right)+k^2\psi\left(x\right)=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可解得

$$
\left\{
\begin{aligned}
\psi_1\left(x\right)&=A\cos kx\\
\psi_2\left(x\right)&=B\sin kx
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;分别对应偶宇称和奇宇称。根据积分可以确定归一化系数，得到

$$
\left\{
\begin{aligned}
\psi_1\left(x\right)&=\sqrt{\frac{2}{a}}\cos kx\\
\psi_2\left(x\right)&=\sqrt{\frac{2}{a}}\sin kx
\end{aligned}
\right.
$$

* 当$$x\notin\left[-a/2,a/2\right]$$时，有$$V\left(x\right)=V$$，即哈密顿方程变为

$$
\ddot{\psi}\left(x\right)-\frac{2m\left(V-E\right)}{\hbar^2}\psi\left(x\right)=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若$$V>E$$，则可令$$\beta^2=2m\left(V-E\right)/\hbar^2$$，则有

$$
\ddot{\psi}\left(x\right)-\beta^2\psi\left(x\right)=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可解得

$$
\left\{
\begin{aligned}
\psi_-\left(x\right)&=C\mathrm{e}^{i\beta x}\\
\psi_+\left(x\right)&=D\mathrm{e}^{-i\beta x}
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$C$$和$$D$$的值可以通过势场突变处波函数及其导数连续的条件求得

[返回目录](#0.0)

---

### <h05 id='5.0'>5.关于自旋</h05>

[返回目录](#0.0)

* 在$$S_z$$表象下，泡利矩阵可以表示为

$$
\sigma_x=
\begin{pmatrix}
0 & 1\\
1 & 0
\end{pmatrix}
,\ \ \ 
\sigma_y=
\begin{pmatrix}
0 & -i\\
i & 0
\end{pmatrix}
,\ \ \ 
\sigma_z=
\begin{pmatrix}
1 & 0\\
0 & -1
\end{pmatrix}
$$

* 自旋与泡利矩阵的关系为$$S_i=\hbar\sigma_i/2$$

* 首先写出哈密顿量和薛定谔方程，然后一般都是**在$$S_z$$表象下用矩阵进行运算**

* 考虑两个自旋的时候，使用耦合表象可能会简单一些

[返回目录](#0.0)

---

### <h06 id='6.0'>6.关于微扰</h06>

[返回目录](#0.0)

* 对于非简并态微扰，首先使用常规的流程和原始哈密顿量$$\hat{H}_0$$计算得到体系的基态能量$$E_0$$和基态波函数
$$\left|\psi\right>$$
，然后利用公式

$$
E_1=\left<\psi\right|\hat{H}'\left|\psi\right>
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;即可计算得到体系微扰的一阶能量近似

* 对于简并态微扰，可以用矩阵进行表示。设系统有$$n$$个简并的基态
$$\left|\psi_1\right>$$、
$$\left|\psi_2\right>$$、
$$\dotsb$$、
$$\left|\psi_n\right>$$，
则可以写出矩阵

$$
\begin{pmatrix}
\left<\psi_1\right|\hat{H}'\left|\psi_1\right> & \dotsb & \left<\psi_1\right|\hat{H}'\left|\psi_n\right>\\
\vdots & \ddots & \vdots\\
\left<\psi_n\right|\hat{H}'\left|\psi_1\right> & \dotsb & \left<\psi_n\right|\hat{H}'\left|\psi_1\right>
\end{pmatrix}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将该矩阵对角化（或求出其本征值），则对角元（本征值）就是考虑一阶微扰之后的能量修正项

* 

[返回目录](#0.0)

---

### <h07 id='7.0'>7.其它一些琐碎的项</h07>

[返回目录](#0.0)

* 波函数的模的平方为概率，具体计算的时候可以计算波函数与其共轭的波函数乘积并积分得到；若为矩阵表示，需要注意右矢变左矢的时候纵向矩阵要变成横向矩阵，所有的虚数部分要加负号

* 折合质量

$$
\mu=\frac{m_1m_2}{m_1+m_2}
$$

* 束缚态：在无限远处波函数为零的状态称为束缚态

*  两个自旋为$$\vec{S}$$的粒子，其能级可以表示为

$$
\vec{S}_1\cdot\vec{S}_2=\frac{1}{2}\left[\left(\vec{S}_1+\vec{S}_2\right)^2-\vec{S}_1^2-\vec{S}_2^2\right]
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$$\vec{S}_1+\vec{S}_2$$的值可以取为

$$
S_1+S_2,\ S_1+S_2-1,\ \dotsb,\ \left|S_1-S_2+1\right|,\ \left|S_1-S_2\right|
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若单个自旋的取值为$$1/2$$，则$$\vec{S}_1+\vec{S}_2$$的取值为$$1$$、$$0$$；

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若单个自旋的取值为$$1$$，则$$\vec{S}_1+\vec{S}_2$$的取值为$$2$$、$$1$$、$$0$$

* 相差一个常数的两个算符具有共同的本征态

* 积分运算

$$
\int_0^\infty\mathrm{e}^{-x^2}x^2\mathrm{d}x=\frac{\sqrt{\pi}}{4}\\
\int_0^\infty\mathrm{e}^{-x^2}x\mathrm{d}x=\frac{1}{2}\\
\int_0^\infty\mathrm{e}^{-x^2}\mathrm{d}x=\frac{\sqrt{\pi}}{2}
$$

* 在计算波函数的时候，一定要注意边界条件。常见的边界条件有：
  * 无穷远处波函数为零
  * 原点处波函数为有限值
  * 波函数在势场突变点连续，波函数的导数也连续

* 对易关系

$$
\left[\hat{x},\hat{H}\right]=\left[\hat{x},\frac{\hat{p}^2}{2m}\right]
=\left[\hat{x},\frac{\hat{p}}{2m}\right]\hat{p}
$$

* $$\delta$$函数的积分

$$
\int f\left(x\right)\delta\left(x-x_0\right)\mathrm{d}x=f\left(x_0\right)
$$

[返回目录](#0.0)

---

特别感谢CMQ同学的讲解。祝我好运！
---
layout: formula
title:  "电动力学公式"
date:   2018-10-05 21:00:00 +0800
tags: [Qualifying Exam, Physics]
categories: [Qualifying Exam]
description: 博资考中可能用到的电动力学公式
---

# 电动力学公式

### <h00 id='0.0'>目录</h00>

* [第一章 电磁现象的普遍规律](#1.0)
* [第二章 静电场](#2.0)
* [第三章 静磁场](#3.0)
* [第四章 电磁波的传播](#4.0)
* [第五章 电磁波的辐射](#5.0)
* [第六章 狭义相对论](#6.0)
* [第七章 带电粒子和电磁场的相互作用](#7.0)

---

### <h01 id='1.0'>第一章 电磁现象的普遍规律</h01>

[返回目录](#0.0)

* 库仑定律：

$$
F=\frac{QQ'}{4\pi\varepsilon_0r^2},\ \ \ \ \ \vec{F}=\frac{QQ'}{4\pi\varepsilon_0r^3}\vec{r}
$$

* 电场强度：

$$
E=\sum_i\frac{Q_i}{4\pi\varepsilon_0r^2},\ \ \ \ \ \vec{E}=\sum_i\frac{Q_i\vec{r}_i}{4\pi\varepsilon_0r^3}\\\\
\vec{E}\left(x\right)=\int_V\frac{\rho\left(\vec{x'}\right)\vec{r}}{4\pi\varepsilon_0r^3}\mathrm{d}V'
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$x'$$、$$V'$$为表示源点，$$x$$表示场点

* 静电场的散度与高斯定理：

$$
\oint_S\vec{E}\cdot\mathrm{d}\vec{S}=\frac{Q}{\varepsilon_0}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$Q$$为高斯面所包围的总电荷，写成微分形式有

$$
\nabla\cdot\vec{E}=\frac{\rho}{\varepsilon_0}
$$

* 静电场的旋度为零，即有

$$
\oint_L\cdot\mathrm{d}\vec{l}=0,\ \ \ \ \ \nabla\times\vec{E}=0
$$

* 通过任意曲面$$S$$的总电流可以表示为

$$
U=\int_S\vec{J}\cdot\mathrm{d}\vec{S}
$$

* 毕奥萨伐尔定律：

$$
\vec{B}\left(\vec{x}\right)=\frac{\mu_0}{4\pi}\int_V\frac{\vec{J}\left(x'\right)\times\vec{r}}{r^3}\mathrm{d}V'
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于细导线，有

$$
\vec{B}\left(\vec{x}\right)=\frac{\mu_0}{4\pi}\oint\frac{I\mathrm{d}\vec{l}\times\vec{r}}{r^3}
$$

* 磁场的环量和旋度：

$$
\oint_L\vec{B}\cdot\mathrm{d}\vec{l}=\mu_0I,\ \ \ \ \ \nabla\times\vec{B}=\mu_0\vec{J}
$$

* 麦克斯韦方程组：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;积分形式：

$$
\left\{
\begin{aligned}
&\oint_L\vec{E}\cdot\mathrm{d}\vec{l}=-\frac{\mathrm{d}}{\mathrm{d}t}\int_S\vec{B}\cdot\mathrm{d}\vec{S}\\\\
&\oint_L\vec{H}\cdot\mathrm{d}\vec{l}=I_f+\frac{\mathrm{d}}{\mathrm{d}t}\int_S\vec{D}\cdot\mathrm{d}\vec{S}\\\\
&\oint_S\vec{D}\cdot\mathrm{d}\vec{S}=Q_f\\\\
&\oint_S\vec{B}\cdot\mathrm{d}\vec{S}=0
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;微分形式：

$$
\left\{
\begin{aligned}
&\nabla\times\vec{E}=-\frac{\partial \vec{B}}{\partial t}\\\\
&\nabla\times\vec{H}=\vec{J}+\frac{\partial \vec{D}}{\partial t}\\\\
&\nabla\cdot\vec{D}=\rho\\\\
&\nabla\cdot\vec{B}=0
\end{aligned}
\right.
$$

* 介质的电极化：电极化强度矢量$$\vec{P}=\chi_e\varepsilon_0\vec{E}$$，电位移矢量$$\vec{D}=\varepsilon_0\vec{E}+\vec{P}=\varepsilon\vec{E}$$，其中

$$
\varepsilon=\varepsilon_r\varepsilon_0,\ \ \ \ \ \varepsilon_r=1+\chi_e
$$

* 介质的磁化：磁化强度$$\vec{M}=\chi_M\vec{H}$$，磁场强度$$\vec{H}=\vec{B}/\mu_0-\vec{M}$$即$$\vec{B}=\mu_0\left(\vec{H}+\vec{M}\right)=\mu\vec{H}$$，其中

$$
\mu=\mu_0\mu_r,\ \ \ \ \ \mu_r=1+\chi_M
$$

* 电流密度与电场强度的关系为$$\vec{J}=\sigma\vec{E}$$

* 电场强度$$\vec{E}$$的切向连续，磁感应强度$$\vec{B}$$的法向连续。其它边值关系有

$$
\left\{
\begin{aligned}
\vec{e}_n\times\left(\vec{E}_2-\vec{E}_1\right)&=0\\\\
\vec{e}_n\times\left(\vec{H}_2-\vec{H}_1\right)&=\vec{\alpha}\\\\
\vec{e}_n\cdot\left(\vec{D}_2-\vec{D}_1\right)&=\sigma\\\\
\vec{e}_n\cdot\left(\vec{B}_2-\vec{B}_1\right)&=0
\end{aligned}
\right.
$$

* 电偶极子是一对间距为$$l$$、电荷量为$$q$$的点电荷，可由$$\vec{p}=q\vec{l}$$来表示。位于$$\vec{r_0}$$处的电偶极子在$$\vec{r}$$处产生的电势为

$$
\varphi=\frac{1}{4\pi\varepsilon_0}\frac{\vec{p}\cdot\left(\vec{r}-\vec{r}_0\right)}{\left|\vec{r}-\vec{r}_0\right|^3}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;电偶极子从负电荷指向正电荷的方向为电偶极子的方向

[返回目录](#0.0)

---

### <h02 id='2.0'>第二章 静电场</h02>

[返回目录](#0.0)

* 静电场是无旋的，因此可以引入一个标势$$\varphi$$来描述静电场，有$$\vec{E}=-\nabla\varphi$$

* 对于点电荷，其空间电势为（若取无穷远处为势能零点）

$$
\varphi\left(P\right)=\sum_i\frac{Q_i}{4\pi\varepsilon_0 r}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于连续分布的带电体，其空间电势为（若取无穷远处为势能零点）

$$
\varphi\left(\vec{x}\right)=\int_V\frac{\rho\left(\vec{x}'\right)\mathrm{d}V'}{4\pi\varepsilon_0r}
$$

* 导体内部不带静电荷；导体内部电场为零；导体表面为等势面

* 在球坐标中求解关于电势$$\varphi$$的拉普拉斯方程可得到其通解为

$$
\begin{aligned}
\varphi\left(R,\theta,\phi\right)=&\sum_{n,m}\left(a_{nm}+\frac{b_{nm}}{R^{n+1}}\right)P_n^m\left(\cos\theta\right)\cos m\phi\\\\
&+\sum_{n,m}\left(c_{nm}R^n+\frac{d_{nm}}{R^{n+1}}\right)P_n^m\left(\cos\theta\right)\sin m\phi
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若体系对称，电势与方位角$$\varphi$$无关，则可将其表示为

$$
\varphi=\sum_{n=0}\left(a_nR^n+\frac{b_n}{R^{n+1}}\right)P_n\left(\cos\theta\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$P_n\left(\cos\theta\right)$$为勒让德函数，有

$$
\left\{
\begin{aligned}
&P_0\left(\cos\theta\right)=1\\\\
&P_1\left(\cos\theta\right)=\cos\theta\\\\
&P_2\left(\cos\theta\right)=\frac{1}{2}\left(3\cos^2\theta-1\right)\\\\
&P_3\left(\cos\theta\right)=\frac{1}{2}\left(5\cos^2\theta-3\right)\\\\
&\dotsb\dotsb
\end{aligned}
\right.
$$

* 在使用电势法求解电场分布时，可根据边界条件

$$
\left\{
\begin{aligned}
\varphi_1&=\varphi_2\\\\
\varepsilon_1\frac{\partial \varphi_1}{\partial r}&=\varepsilon_2\frac{\partial \varphi_2}{\partial r}
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;来消去待定系数

* 半径为$$R_0$$的导体球对于位于$$a$$处的一点电荷的感应电荷$$(Q',b)$$为

$$
Q'=-\frac{R_0}{a}Q,\ \ \ \ \ b=\frac{R_0^2}{a}
$$

[返回目录](#0.0)

---

### <h03 id='3.0'>第三章 静磁场</h03>

[返回目录](#0.0)

* 磁矢势

* 在没有电流元的地方，可以引入磁标势，则磁场强度可以表示为$$\vec{H}=-\nabla\varphi_m$$，有

$$
\mathrm{d}\varphi_m=\frac{\mathrm{d}\vec{m}\cdot\vec{r}}{4\pi r^3}=\frac{I}{4\pi}\frac{\vec{r}\cdot\mathrm{d}\vec{S}'}{r^3}=\frac{I}{4\pi}\mathrm{d}\Omega
$$

[返回目录](#0.0)

---

### <h04 id='4.0'>第四章 电磁波的传播</h40>

[返回目录](#0.0)

* 在真空中，若设电流密度$$\vec{J}$$和电荷密度$$\rho$$为$$0$$，则麦克斯韦方程组可以表示为

$$
\left\{
\begin{aligned}
&\nabla\times\vec{E}=-\frac{\partial \vec{B}}{\partial t}\\\\
&\nabla\times\vec{H}=\frac{\partial \vec{D}}{\partial t}\\\\
&\nabla\cdot\vec{D}=0\\\\
&\nabla\cdot\vec{B}=0
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联立1、2式有

$$
\left\{
\begin{aligned}
&\nabla^2\vec{E}-\mu_0\varepsilon_0\frac{\partial^2\vec{E}}{\partial t^2}=\nabla^2\vec{E}-\frac{1}{c^2}\frac{\partial^2\vec{E}}{\partial t^2}=0\\\\
&\nabla^2\vec{B}-\mu_0\varepsilon_0\frac{\partial^2\vec{B}}{\partial t^2}=\nabla^2\vec{B}-\frac{1}{c^2}\frac{\partial^2\vec{B}}{\partial t^2}=0
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中利用了公式

$$
\nabla\times\left(\nabla\times\vec{E}\right)=\nabla\left(\nabla\cdot\vec{E}\right)-\nabla^2\vec{E}=-\nabla^2\vec{E}\\\\
\nabla\times\left(\nabla\times\vec{B}\right)=\nabla\left(\nabla\cdot\vec{B}\right)-\nabla^2\vec{B}=-\nabla^2\vec{B}
$$

* 考虑角频率为$$\omega$$的电磁波，则其电场和磁场可以表示为

$$
\left\{
\begin{aligned}
\vec{E}\left(\vec{x},t\right)&=\vec{E}\left(x\right)\mathrm{e}^{-i\omega t}\\\\
\vec{B}\left(\vec{x},t\right)&=\vec{B}\left(x\right)\mathrm{e}^{-i\omega t}
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;代入麦克斯韦方程组，则有

$$
\left\{
\begin{aligned}
&\nabla\times\vec{E}=i\omega\mu\vec{H}\\\\
&\nabla\times\vec{H}=-i\omega\varepsilon\vec{E}\\\\
&\nabla\cdot\vec{E}=0\\\\
&\nabla\cdot\vec{H}=0
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联立1、2式有

$$
\nabla\times\left(\nabla\times\vec{E}\right)=\omega^2\mu\varepsilon\vec{E}\Leftrightarrow\nabla^2\vec{E}+k^2\vec{E}=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$k=\omega\sqrt{\mu\varepsilon}$$。解出$$\vec{E}$$后，$$\vec{B}$$可以表示为

$$
\vec{B}=-\frac{i}{k}\sqrt{\mu\varepsilon}\nabla\times\vec{E}
$$

* 考虑平面电磁波的表达式

$$
\left\{
\begin{aligned}
\vec{E}\left(\vec{x},t\right)&=\vec{E}_0\mathrm{e}^{i\left(\vec{k}\cdot\vec{x}-\omega t\right)}\\\\
\vec{B}\left(\vec{x},t\right)&=\vec{B}_0\mathrm{e}^{i\left(\vec{k}\cdot\vec{x}-\omega t\right)}
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则$$\vec{B}$$与$$\vec{E}$$的关系为

$$
\vec{B}=-\frac{i}{k}\sqrt{\mu\varepsilon}\nabla\times\vec{E}=\sqrt{\mu\varepsilon}\frac{\vec{k}}{k}\times\vec{E}=\sqrt{\mu\varepsilon}\vec{e}_k\times\vec{E}=\frac{1}{v}\vec{e}_k\times\vec{E}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此平面电磁波电场与磁场的振幅比为

$$
\left|\frac{\vec{E}}{\vec{B}}\right|=\frac{1}{\sqrt{\mu\varepsilon}}=v\\\\
\left|\frac{\vec{E}}{\vec{B}}\right|=\frac{1}{\sqrt{\mu_0\varepsilon_0}}=c
$$

* 电磁波在介质界面处会发生折射和反射。设电磁波沿$$z$$方向从介质1入射到介质2，二者的相对介电常数分别为$$\varepsilon_1$$和$$\varepsilon_2$$，介质光速分别为$$v_1$$和$$v_2$$，电磁波入射角、反射角和折射角分别为$$\theta_0$$、$$\theta_1$$和$$\theta_2$$，则由于电场强度$$\vec{E}$$在界面处的切向分量连续，有

$$
\vec{e}_n\times\left(\vec{E}_0\mathrm{e}^{i\vec{k}_0\cdot\vec{r}}+\vec{E}_1\mathrm{e}^{i\vec{k}_2\cdot\vec{r}}\right)=\vec{e}_n\times\vec{E}_2\mathrm{e}^{i\vec{k}_2\cdot\vec{r}}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于$$\vec{r}$$的任意性，上式成立的条件是

$$
\vec{k}_0\cdot\vec{r}=\vec{k}_1\cdot\vec{r}=\vec{k}_2\cdot\vec{r}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;设电场在$$y$$方向无分量，则上式等价于

$$
k_{0x}=k_{1x}=k_{2x}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;即

$$
k_0\sin\theta_0=k_1\sin\theta_1=k_2\sin\theta_2
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据电磁波频率与速度的关系

$$
k_0=k_1=\frac{\omega}{v_1},\ \ \ \ \ k_2=\frac{\omega}{v_2}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;代入上式可得

$$
\theta_0=\theta_1,\ \ \ \ \ \frac{\sin\theta_0}{\sin\theta_2}=\frac{\sin\theta_1}{\sin\theta_2}=\frac{v_1}{v_2}=\frac{\sqrt{\mu_2\varepsilon_2}}{\sqrt{\mu_1\varepsilon_1}}=\frac{n_2}{n_1}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此即为反射与折射的波矢和角度关系

* 下面考虑入射波、反射波和折射波的振幅，假定界面自由电流密度为$$0$$时。当$$\vec{E}$$垂直于入射面，$$\vec{H}$$平行于入射面时，有

$$
E_0+E_1=E_2\\\\
H_0\cos\theta_0-H_1\cos\theta_1=H_2\cos\theta_2
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将$$H=\sqrt{\varepsilon/\mu}E$$代入可得

$$
\sqrt{\varepsilon_1}\left(E_0-E_1\right)\cos\theta_1=\sqrt{\varepsilon_2}E_2\cos\theta_2
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;结合反射角与折射角的关系，有

$$
\left\{
\begin{aligned}
\frac{E_1}{E_0}&=-\frac{\sin\left(\theta_0-\theta_2\right)}{\sin\left(\theta_0+\theta_2\right)}\\\\
\frac{E_2}{E_0}&=\frac{2\cos\theta_0\sin\theta_2}{\sin\left(\theta_0+\theta_2\right)}
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当$$\vec{H}$$垂直于入射面，$$\vec{E}$$平行于入射面时，有

$$
H_0+H_1=H_2\\\\
E_0\cos\theta_0-E_1\cos\theta_1=E_2\cos\theta_2
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将$$H=\sqrt{\varepsilon/\mu}E$$代入可得

$$
\sqrt{\varepsilon_1}\left(E_0+E_1\right)=\sqrt{\varepsilon_2}E_2
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;结合反射角与折射角的关系，有

$$
\left\{
\begin{aligned}
\frac{E_1}{E_0}&=\frac{\tan\left(\theta_0-\theta_2\right)}{\tan\left(\theta_0+\theta_2\right)}\\\\
\frac{E_2}{E_0}&=\frac{2\cos\theta_0\sin\theta_2}{\sin\left(\theta_0+\theta_2\right)\cos\left(\theta_0-\theta_2\right)}
\end{aligned}
\right.
$$

* 在导体中应用麦克斯韦方程组$$\nabla\cdot\vec{D}=\rho$$，可得到导体中电荷密度与电场的微分方程为

$$
\varepsilon\nabla\cdot\vec{E}=\rho
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;结合微分形式欧姆定律$$\vec{J}=\sigma\vec{E}$$，可以得到

$$
\nabla\cdot\vec{J}=\frac{\sigma}{\varepsilon}\rho
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;而由于电荷密度的变化与电流密度满足关系

$$
\frac{\partial \rho}{\partial t}=-\nabla\cdot\vec{J}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;有

$$
\frac{\partial \rho}{\partial t}=-\nabla\cdot\vec{J}=-\frac{\sigma}{\varepsilon}\rho
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;求解此微分方程，可以得到

$$
\rho\left(t\right)=\rho_0\mathrm{e}^{-\frac{\sigma}{\varepsilon}t}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\tau=\sigma/\rho$$，称为电荷密度随时间衰减的特征时间

* 在导体中，麦克斯韦方程组可以写作

$$
\left\{
\begin{aligned}
&\nabla\times\vec{E}=-\frac{\partial \vec{B}}{\partial t}\\\\
&\nabla\times\vec{H}=\vec{J}+\frac{\partial \vec{D}}{\partial t}\\\\
&\nabla\cdot\vec{D}=0\\\\
&\nabla\cdot\vec{B}=0
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于一频率为$$\omega$$的电磁波，可令

$$
\vec{D}=\varepsilon\vec{E},\ \ \ \ \ \vec{B}=\mu\vec{H}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则麦克斯韦方程组等价于

$$
\left\{
\begin{aligned}
&\nabla\times\vec{E}=i\omega\mu\vec{H}\\\\
&\nabla\times\vec{H}=-i\omega\varepsilon\vec{E}+\sigma\vec{E}\\\\
&\nabla\cdot\vec{E}=0\\\\
&\nabla\cdot\vec{H}=0
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此可以在形式上引入“复电容率”

$$
\varepsilon'=\varepsilon+i\frac{\sigma}{\omega}
$$

* 电磁波在导体表面会发生反射与折射，在垂直入射时，有

$$
E+E'=E'',\ \ \ \ \ H-H'=H''
$$

[返回目录](#0.0)

---

### <h05 id='5.0'>第五章 电磁波的辐射</h05>

[返回目录](#0.0)

* 考虑真空中的电磁波，麦克斯韦方程组为

$$
\left\{
\begin{aligned}
&\nabla\times\vec{E}=-\frac{\partial \vec{B}}{\partial t}\\\\
&\nabla\times\vec{H}=\vec{J}+\frac{\partial \vec{D}}{\partial t}\\\\
&\nabla\cdot\vec{D}=\rho\\\\
&\nabla\cdot\vec{B}=0
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于$$\vec{B}$$是无源的，可以引入磁矢势$$\vec{A}$$，有$$\vec{B}=\nabla\times\vec{A}$$。代入1式，则有

$$
\nabla\times\vec{E}=-\nabla\times\frac{\partial\vec{A}}{\partial t}\Leftrightarrow\nabla\times\left(\vec{E}+\frac{\partial\vec{A}}{\partial t}\right)=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;说明括号内的矢量为无旋的，因此可以用标势的负梯度来描述：

$$
\vec{E}+\frac{\partial\vec{A}}{\partial t}=-\nabla\varphi
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此电场可以表示为

$$
\vec{E}=-\nabla\varphi-\frac{\partial \vec{A}}{\partial t}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此处的$$\varphi$$不再是传统意义上的电势

* 推迟势公式为

$$
\vec{A}\left(\vec{x},t\right)=\frac{\mu_0}{4\pi}\int_V\frac{\vec{J}\left(\vec{x}',t-\frac{r}{c}\right)}{r}\mathrm{d}V'
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若电流$$\vec{J}$$是一定频率的交变电流，即有

$$
\vec{J}\left(\vec{x}',t\right)=\vec{J}\left(x'\right)\mathrm{e}^{-i\omega t}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;结合上述两式，有

$$
\vec{A}\left(\vec{x},t\right)=\frac{\mu_0}{4\pi}\int_V\frac{\vec{J}\left(x'\right)\mathrm{e}^{i\left(kr-\omega t\right)}}{r}\mathrm{d}V'
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若令

$$
\vec{A}\left(\vec{x},t\right)=\vec{A}\left(\vec{x}\right)\mathrm{e}^{-i\omega t}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则有

$$
\vec{A}\left(\vec{x}\right)=\frac{\mu_0}{4\pi}\int_V\frac{\vec{J}\left(x'\right)\mathrm{e}^{ikr}}{r}\mathrm{d}V'
$$

* 电偶极辐射：将推迟势展开，则第一项可以表示为

$$
\vec{A}\left(\vec{x}\right)=\frac{\mu_0\mathrm{e}^{ikR}}{4\pi R}\int_V\vec{J}\left(\vec{x}'\right)\mathrm{d}V'
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;设电流密度表示为$$\vec{J}=\sum_i n_iq_i\vec{v}_i$$，则有

$$
\int_V\vec{J}\left(\vec{x}'\right)\mathrm{d}V'=\sum_iq_i\vec{v}_i=\frac{\mathrm{d}}{\mathrm{d}t}\sum q_i\vec{x}_i=\frac{\mathrm{d}\vec{p}}{\mathrm{d}t}=\dot{\vec{p}}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$p$$为电偶极矩，因此推迟势的第一项代表振荡电偶极矩产生的辐射，即有

$$
\vec{A}\left(\vec{x}\right)=\frac{\mu_0\mathrm{e}^{ikR}}{4\pi R}\dot{\vec{p}}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;算符$$\nabla$$作用时，仅需对相因子作用，即有

$$
\begin{aligned}
&\nabla\rightarrow ik\vec{e}_R\\\\
&\frac{\partial}{\partial t}\rightarrow -i\omega
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由此可得辐射场

$$
\left\{
\begin{aligned}
&\vec{B}=\nabla\times\vec{A}=\frac{i\mu_0k}{4\pi R}\mathrm{e}^{ikR}\vec{e}_R\times\dot{\vec{p}}=\frac{\mathrm{e}^{ikR}}{4\pi\varepsilon_0 c^3R}\ddot{\vec{p}}\times\vec{e}_R\\\\
&\vec{E}=\frac{ic}{k}\nabla\times\vec{B}=c\vec{B}\times\vec{e}_R=\frac{\mathrm{e}^{ikR}}{4\pi\varepsilon_0 c^2R}\left(\ddot{\vec{p}}\times\vec{e}_R\right)\times\vec{e}_R
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在球坐标系中，有

$$
\left\{
\begin{aligned}
&\vec{B}=\frac{1}{4\pi\varepsilon_0 c^3R}\ddot{\vec{p}}\mathrm{e}^{ikR}\sin\theta\vec{e}_\varphi\\\\
&\vec{E}=\frac{1}{4\pi\varepsilon_0 c^2R}\ddot{\vec{p}}\mathrm{e}^{ikR}\sin\theta\vec{e}_\theta
\end{aligned}
\right.
$$

* 电磁波的平均辐射功率为

$$
\bar{\vec{S}}=\frac{1}{2}\mathrm{Re}\left(\vec{E}^*\times\vec{H}\right)
$$

* 电磁场的动量密度为

$$
\vec{g}=\varepsilon_0\vec{E}\times\vec{B}=\frac{1}{c^2}\vec{S}
$$

[返回目录](#0.0)

---

### <h11 id='1.1'>第一章 费马原理与变折射率光学</h11>

[返回目录](#0.0)

* 折射定律：

$$
n_1\sin i_1=n_2\sin i_2
$$

[返回目录](#0.0)

---

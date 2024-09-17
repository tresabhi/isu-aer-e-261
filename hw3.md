# AERE 261 HW 3

Abhigyaan Deep

Hello, grader of my homework! In order to preserve my sanity, I am moving away from clunky Google Docs. I am now trying out Markdown and $\LaTeX$ with the GitHub flavor so my homeworks should be prettier for you and easier for me to write.

## Knowns

$M_{\infty}=0.27$

$V_{\infty}=89.6m/s$

$\rho=0.993kg/m^3$

$\mu=1.7*10^{-5}\frac{kg}{m*s}$

$b=12.4m$

$S=22.9m^2$

## 1. (a)

$$
AR=\frac{b^2}{S}=\frac{(12.4m)^2}{22.9m^2}=6.71
$$

## 1. (b)

More info that we got:

$\alpha_{\text{stall}}=17.5\deg$

$\alpha_{L=0}=-1.19\deg$

$a_0=0.119\deg^{-1}$

$e=0.92$

I'm going to use the degree version of the formula to extend the 2D airfoil to a 3D wing.

$$
a=\frac{a_0}{1+\frac{57.3\deg a_0}{\pi e AR}}=\frac{0.119\deg^{-1}}{1+\frac{57.3\deg*0.119\deg^{-1}}{\pi*0.92*6.71}}=0.0880\deg^{-1}
$$

Now for $C_L$

$$
C_L=a(\alpha-\alpha_{L=0})=0.0880\deg^{-1}(\alpha+1.19\deg)
$$

## 1. (c)

$$
\alpha=\alpha_{\text{stall}}=17.5\deg
$$

$$
C_L=0.0880\deg^{-1}(17.5\deg+1.19\deg)=1.643
$$

## 1. (d)

Given

$m_\text{full}=1680kg$

$g=9.81m/s^2$

Converting mass to force (or weight):

$$
L=W=m_\text{full}g=1680kg*9.81m/s^2=16480N=16.48kN
$$

Rewriting $C_L$ in terms of $L$

$$
L=\frac{1}{2}\rho_\infty V_\infty^2 S C_L
$$

$$
C_L=\frac{2L}{\rho_\infty V_\infty^2 S}=\frac{2*16.48kN}{0.993kg/m^3 * (89.6m/s)^2 * 22.9m^2}=0.1805
$$

## 1. (e)

Pulling this from up above:

$C_{L,\text{stall}}=1.643$

$L=16.48kN$

Solving for $V_\infty$ with $C_L$ equal to the stall value:

$$
W=\frac{1}{2}\rho_\infty V_\infty^2 S C_{L,\text{stall}}
$$

$$
V_\infty=\sqrt{\frac{2W}{\rho_\infty S C_{L,\text{stall}}}}=\sqrt{\frac{2*16.48kN}{0.993kg/m^3 * 22.9m^2 * 1.643}}=29.7m/s
$$

## 1. (f)

There is no wing sweep so $\Lambda=0$

And AR from above: $AR=6.71$

$$
e_0=1.78(1-0.045AR^{0.68})-0.64=1.78(1-0.045*6.71^{0.68})-0.64=0.8477
$$

## 1. (g)

$$
K=\frac{1}{piARe}=\frac{1}{pi*6.71*0.8477}=0.0560
$$

And now the drag coefficient:

$$
C_D=C_{D,0}+KC_L^2
$$

From last homework: $C_{d,0}=0.006$

$$
C_D=0.006+0.0560*(0.1805)^2=0.00782
$$

## 2. (a)

$$
A_{top}=\frac{1}{2}(103.5in)(53.9in)+(207.5in)(53.9in)=13970in^2=9.013m^2
$$

$$
A_{side}=(39.4in)(69.3in)+(138.2in)(66in)+\frac{1}{2}(103.5in)(66in)=15267in^2=9.8497m^2
$$

$$
S_{\text{wet,fuselage}}=3.4\left(\frac{A_{top}+A_{side}}{2}\right)=3.4\left(\frac{9.013m^2+9.8497m^2}{2}\right)=32.1 m^2
$$

## 2. (b)

Given

$A_{\text{{max}}}=2.22m^2$

$l=7.9m$

$S_\text{wet}=32.26 m^2$ (value given in the question differs a negligible amount from my calculations so I am going with the one provided in the question)

$R=9.67*10^6$

$t/c=0.15$

This is from up above

$S_\text{exposed,wing}=32.1 m^2$

This is from the estimation document

$Q_c=1.0$

Assuming laminar flow

$$
C_f=\frac{1.328}{\sqrt{R}}=\frac{1.328}{\sqrt{9.67*10^6}}=0.0004271
$$

$$
f=\frac{l}{d}=\frac{l}{\sqrt{(4/\pi)A_{\text{{max}}}}}=\frac{7.9m}{\sqrt{(4/\pi)*2.22m^2}}=4.699
$$

$$
FF_{\text{fuselage}}=0.9+\frac{5}{f^{1.5}}+\frac{f}{400}=0.9+\frac{5}{4.699^{1.5}}+\frac{4.699}{400}=1.403
$$

$$
S_\text{wing}=[1.977+0.52(t/c)]S_\text{exposed,wing}=[1.977+0.52(0.15)](32.1 m^2)=65.97 m^2
$$

$$
C_{\text{D,fuselage}}=C_f FF Q_c \frac{S_\text{wet}}{S_\text{wing}}=0.0004271 * 1.403 * 1.0* \frac{32.26 m^2}{65.97 m^2}=0.000293
$$

## 2. (c)

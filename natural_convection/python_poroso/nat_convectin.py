#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Este código es una implementación del capítulo 6 (convección natural) del líbro de Mohamad, 
# adaptando las propiedades del medio poroso y las aproximaciones del término de fuerza del 
# artículo: A multiple-relaxation-time lattice Boltzmann model for convection heat transfer 
# in porous media de Qing Liu, Ya-Ling He, Qing Li, Wen-Quan Tao

# Autores del código: Benjamín S. Noyola García, Suemi Rodriguez Romo


from numpy import *
from numpy import linalg as LA
from modulos_nat import colisionf, propagacion, c_fronf, calc_rho_u_v ,colisiong,c_frong,calc_T
import sys, time

n=101 #número de filas
m=101 #número de columnas

cx=array([0.0,1.0,0.0,-1.0,0.0,1.0,-1.0,-1.0,1.0]) #componente en x
cy=array([0.0,0.0,1.0,0.0,-1.0,1.0,1.0,-1.0,-1.0]) #componente en y
w=array([4./9.,1./9.,1./9.,1./9.,1./9.,1./36.,1./36.,1./36.,1./36.]) #factor de peso omega
tref=0.5
uo=0.0
sumvelo=0.0
rhoo=6.00
dx=1.0
dy=dx
dt=1.0
tw=1.0
ra=1.0e5
pr=0.71
visco=0.02
alpha=visco/pr
pr=visco/alpha
gbeta=ra*visco*alpha/(float(m*m*m))
Re=uo*m/alpha
omega=1.0/(3.*visco+0.5)
omegat=1.0/(3.*alpha+0.5)
mstep=150000

f=zeros([9,n,m])
feq=zeros([9,n,m])
g=zeros([9,n,m])
geq=zeros([9,n,m])
TF=zeros([9,n,m])
rho=zeros([n,m])
u=zeros([n,m])
v=zeros([n,m])
th=zeros([n,m])
rho[:,:]=rhoo
for i in range(n):
    for j in range(m):
        for k in range(9):
            TF[k]=gbeta*(th[i,j]-tref)*cy[k]
#programa principal............................................................
for kk in range(mstep):
    f=colisionf(u,v,f,feq,rho,omega,w,cx,cy,n,m,th,gbeta,TF)  #campo de flujo
    f=propagacion(f,n,m)
    f=c_fronf(f,n,m)
    rho, u, v, TF = calc_rho_u_v(f,rho,u,v,cx,cy,n,m,w,gbeta,th,visco)
#    
    g=colisiong(u,v,g,geq,th,omegat,w,cx,cy,n,m)    #campo de temperatura
    g=propagacion(g,n,m)
    g=c_frong(g,tw,w,n,m)
    th=calc_T(g,n,m)

 
norvel=sqrt(u**2 + v**2)
strf=zeros([n,m])
strf[0,0]=0.0
for j in range(m):
    rhoav=0.5*(rho[0,j-1]+rho[0,j])
    if j != 0.0: strf[0,j] = strf[0,j-1]-rhoav*0.5*(v[0,j-1]+v[0,j])
    for i in range(1,n):
        rhom=0.5*(rho[i,j]+rho[i-1,j])
        strf[i,j]=strf[i-1,j]+rhom*0.5*(u[i-1,j]+u[i,j])
#strf=-1*strf        
    
print g
print "rho",rho
print "u",u
print "v",v
print "T",th
savetxt('Temp.txt', th,fmt='%.4f') # Se guarda la temperatura
savetxt('rho.txt', rho,fmt='%.4f') # Se guarda la densidad
savetxt('velx.txt', u,fmt='%.10f') # Se guarda la velocidad x
savetxt('vely.txt', v,fmt='%.10f') # Se guarda la velocidad y
savetxt('norvel.txt', norvel,fmt='%.10f') # Se guarda la velocidad y
savetxt('strf.txt', strf,fmt='%.10f') # Se guarda strf
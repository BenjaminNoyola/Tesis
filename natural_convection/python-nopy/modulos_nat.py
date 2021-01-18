#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Benjamín S. Noyola García
# Tema: modulos de change_phase.py
from numpy import *
from numba import jit

#campo de temperatura..........................................................
@jit
def colisionf(u,v,f,feq,rho,omega,w,cx,cy,n,m,th,gbeta):
    feq=zeros([9,n,m])
    tref=0.50
    for i in range(n):
        for j in range(m):
            t1=u[i,j]*u[i,j]+v[i,j]*v[i,j]
            for k in range(9):
                t2=u[i,j]*cx[k]+v[i,j]*cy[k]
                force=3.*w[k]*gbeta*(th[i,j]-tref)*cy[k]*rho[i,j]
                if(i==0 or i==n): force =0.0
                if(j==0 or j==m): force =0.0
                feq[k,i,j]=rho[i,j]*w[k]*(1.0+3.0*t2+4.50*t2*t2-1.50*t1)
                f[k,i,j]=omega*feq[k,i,j]+(1.-omega)*f[k,i,j]+force
    return f


@jit(nopython=True, parallel=True)
def propagacion(f,n,m):
    for i in range(n):
        for j in range(m-1,0,-1):
            f[1,i,j] = f[1,i,j-1]       #derecha a izquierda
        for j in range(m-1):
            f[3,i,j] = f[3,i,j+1]       #izquierda a derecha
    
    for i in range(n-1):                #de arriba hacia abajo
        for j in range(m):
            f[2,i,j] = f[2,i+1,j]
        for j in range(m-1,0,-1):
            f[5,i,j] = f[5,i+1,j-1]
        for j in range(m-1):
            f[6,i,j] =f[6,i+1,j+1]
    
    for i in range(n-1,0,-1):           #de abajo hacia arriba
        for j in range(m):
            f[4,i,j] = f[4,i-1,j]
        for j in range(m-1):
            f[7,i,j] = f[7,i-1,j+1]
        for j in range(m-1,0,-1):
            f[8,i,j] = f[8,i-1,j-1]
    return f



@jit(nopython=True, parallel=True)
def c_fronf(f,n,m):
    for i in range(n):          
        f[1,i,0] = f[3,i,0]     #frontera oeste
        f[5,i,0] = f[7,i,0]
        f[8,i,0] = f[6,i,0]
    
        f[3,i,m-1] = f[1,i,m-1] #frontera este
        f[6,i,m-1] = f[8,i,m-1]
        f[7,i,m-1] = f[5,i,m-1]
    
    for j in range(m):
        f[2,n-1,j] = f[4,n-1,j] #frontera sur
        f[5,n-1,j] = f[7,n-1,j]
        f[6,n-1,j] = f[8,n-1,j]
        
        f[4,0,j] = f[2,0,j]     #frontera norte
        f[7,0,j] = f[5,0,j]
        f[8,0,j] = f[6,0,j]
    return f


@jit
def calc_rho_u_v(f,rho,u,v,cx,cy,n,m):
    rho = f.sum(axis=0)   
    for i in range(n):
        for j in range(m):
            usum=0.0
            vsum=0.0
            for k in range(9):
                usum=usum + f[k,i,j]*cx[k]
                vsum=vsum + f[k,i,j]*cy[k]
            u[i,j] = usum/rho[i,j]
            v[i,j] = vsum/rho[i,j]
    return rho,u,v
#campo de temperatura................................................................
@jit
def colisiong(u,v,g,geq,th,omegat,w,cx,cy,n,m):
    geq=zeros([9,n,m])
    for i in range(n):
        for j in range(m):
            for k in range(9):
                geq[k,i,j]=th[i,j]*w[k]*(1.0+3.0*(u[i,j]*cx[k]+v[i,j]*cy[k]))
                g[k,i,j]=omegat*geq[k,i,j]+(1.0-omegat)*g[k,i,j]
    return g



@jit(nopython=True, parallel=True)
def c_frong(g,tw,w,n,m):
    for i in range(n):
        g[1,i,0] = tw*(w[1]+w[3])-g[3,i,0]  #condición de frontera oeste
        g[5,i,0] = tw*(w[5]+w[7])-g[7,i,0]
        g[8,i,0] = tw*(w[8]+w[6])-g[6,i,0]
#
        g[3,i,m-1] = -g[1,i,m-1]             #condición de frontera oeste
        g[6,i,m-1] = -g[8,i,m-1]
        g[7,i,m-1] = -g[5,i,m-1]        
    
    for j in range(m):
        g[0,0,j]=g[0,1,j]                    #condición de frontera norte
        g[1,0,j]=g[1,1,j]
        g[2,0,j]=g[2,1,j]
        g[3,0,j]=g[3,1,j]
        g[4,0,j]=g[4,1,j]
        g[5,0,j]=g[5,1,j]
        g[6,0,j]=g[6,1,j]
        g[7,0,j]=g[7,1,j]
        g[8,0,j]=g[8,1,j]        
#
        g[0,n-1,j] = g[0,n-2,j]              #condición de frontera sur
        g[1,n-1,j] = g[1,n-2,j]
        g[2,n-1,j] = g[2,n-2,j]
        g[3,n-1,j] = g[3,n-2,j]
        g[4,n-1,j] = g[4,n-2,j]
        g[5,n-1,j] = g[5,n-2,j]
        g[6,n-1,j] = g[6,n-2,j]
        g[7,n-1,j] = g[7,n-2,j]
        g[8,n-1,j] = g[8,n-2,j]        

    return g


@jit
def calc_T(g,n,m):
    T = g.sum(axis=0)
    return T
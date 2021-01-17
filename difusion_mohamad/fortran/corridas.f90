! The LBM code
parameter (n=100,m=100)
real f(0:8,0:n,0:m),feq, dx, dy
real rho(0:n,0:m),x(0:n),y(0:m)
real w(0:8)
integer i,j
open(2,file='Qresu')
open(3,file='midtlbmtc')
!
dx=1.0
dy=dx
x(0)=0.0
y(0)=0.0
do i=1,n
	x(i)=x(i-1)+dx
end do

do j=1,m
	y(j)=y(j-1)+dy
end do
 
dt=1.0
tw=1.0
alpha=0.25
csq=(dx*dx)/(dt*dt)
omega=1.0/(3.*alpha/(csq*dt)+0.5)
mstep=400
w(0)=4./9.
do i=1,4
	w(i)=1./9.
end do

do i=5,8
	w(i)=1./36.
end do

do j=0,m
	do i=0,n
		rho(i,j)=0.0 ! initial field
	end do
end do

do j=0,m    !comienza calculando la función de distribución
	do i=0,n
		do k=0,8
			f(k,i,j)=w(k)*rho(i,j)
			if(i.eq.0) f(k,i,j)=w(k)*tw
		end do
	end do
end do

do kk=1,mstep
	do j=0,m
		do i=0,n
			sum=0.0
			do k=0,8
				sum=sum+f(k,i,j)
			end do
			rho(i,j)=sum
		end do
	end do
	print *,rho(0,m/2)  !Cominza calculando la temperatura de cada lattice

	do j=0,m
		do i=0,n
			do k=0,8    !Se aplica la colisión
				feq=w(k)*rho(i,j)   
				f(k,i,j)=omega*feq+(1.-omega)*f(k,i,j)
			end do
		end do
	end do

! streaming
	do j=m,0,-1
		do i=0,n
			f(2,i,j)=f(2,i,j-1)
			f(6,i,j)=f(6,i+1,j-1)
		end do
	end do

	do j=m,0,-1
		do i=n,0,-1
			f(1,i,j)=f(1,i-1,j)
			f(5,i,j)=f(5,i-1,j-1)
		end do
	end do

	do j=0,m
		do i=n,0,-1
			f(4,i,j)=f(4,i,j+1)
			f(8,i,j)=f(8,i-1,j+1)
			print*, f(8,i,j)
		end do
	end do



end do


end

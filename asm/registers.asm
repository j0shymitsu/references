section .text
global _start

_start:

mov eax, 0x55555555
mov eax, 0
mov ax, 0x5555
mov eax, 0
mov ah, 0x55
mov eax, 0
mov al, 0x55

mov eax, 1
int 0x80
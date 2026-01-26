; Writes hello world to the console using only system calls. Runs on 64-bit 
; linux only. To assembly and run:
;     nasm -felf64 hello_world.s && ld hello_world.o && ./a.out


  global _start
  section .text
_start:
  mov rax, 1      ; System call for write
  mov rdi, 1      ; FIle handle 1 is stdout
  mov rsi, msg    ; Address of string to output
  mov rdx, 27;    ; Number of bytes
  syscall         ; Invoke OS to do the write 
  mov rax, 60     ; System call for exit
  mov rdi, 0      ; Exit code 0
  syscall         ; Invoke OS to exit

  section .data
msg: db "Hello Linux Assembly world!", 10   ; Note newline at end

section .text         		;declare this section to include executable instructions

global my_memset      		;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push 	rbp      	;saves the base pointer for the previous function's stack frame
        mov 	rbp, rsp  	;moves up the base pointer to the top of the stack to create a new frame

        ;;;;;;;;;;;;;;;;;;;;;
        ;your code goes here!
        ;;;;;;;;;;;;;;;;;;;;;

	;sets parameter
	mov 	r11, rdi	;takes param 1 (char *str) and stores it in a regsiter
	;mov	rax, rsi	;takes param 2 (char val)  and stores it
	mov	[rbp-8], rsi	;takes param 2 (char val) and stores it on the stack
	mov	rdx, rdx	;takes param 3 (int str1)  and stores it in a regsiter

	;sets local variable
	mov     rcx, 0		;sets int i = 0 for the for loop counter
	; gets char val from the stack
	mov	al, [rbp-8]

.loop1:
	;conditional statement: i<str1
	cmp	rcx, rdx
	jge	.end1

	;set command:  str[i] = val
	mov	[r11+rcx], al

	;increments i by 1 for loop conditional: i++
	add	rcx, 1
	jmp 	.loop1
.end1:
        leave         		;moves down the stack pointer to the current base pointer,
                      		;and restores our saved base pointer, effectively
                      		;restoring our previous stack frame
        ret           		;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;;;;;;;;;;;;;;;;;;;;;
        ;your code goes here!
        ;;;;;;;;;;;;;;;;;;;;;

	;sets parameter
	mov	r11, rdi	;takes param 1 (char *dst) and stores it
	mov	rax, rsi	;takes param 2 (char *src) and stores it
	mov	rdx, rdx	;takes param 3 (int len)   and stores it

	;sets local variable
	mov	rcx, 0

.loop2:
	;conditional statement: i<len
	cmp	rcx, rdx
	jge	.end2

	;set command: dst[i] = src[i]
	mov	r8, [rsi+rcx]
	mov	[rbp-8], r8
	mov	al, [rbp-8]
	mov	[r11+rcx], al

	;increments i by 1 for loop conditional: i++
	add	rcx, 1
	jmp	.loop2

.end2:
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!

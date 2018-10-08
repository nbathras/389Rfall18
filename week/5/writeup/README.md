Writeup 5 - Binaries I
======

Name: Noah Bathras
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Noah Bathras

## Assignment 5 Writeup

I struggled a lot with this project because I did not have much experience with coding in assembly before and the language is not very intuitive.  Because of this, I started the project by first implementing as simple of methods as I could.  I first implemented a function that just returned a value, then I moved to returning the parameter that was passed into the method, and then I moved to modifying a single character in a pointer that was passed in with a constant character value.  After I completed those three tasks I attempted to tackle the project as a whole.

The way I approached the first method, was first I wanted to store all of the parameter values in the appropriate registers.  I stored the first parameter (char *str) in r11, the second parameter (char val) into on the stack at [rbp-8], and the third parameter (int str1) into rdx.  I stored char val on the stack because I wanted to be able to get out small bytes segments.  After I stored all the parameters, I declared in local variable rcx to 0 which represents the i variable along with storing [rbp-8] into al so that I can access that character value.  I stored this in rcx because generally rcx is the counter register.  Then we get into the loop, which first checks if rcx < rdx or i < str1 if it is we move onto the body of the loop if it is not we jump down to .end1 label.  In the loop we run the command:

mov	[r11+rcx], al

which tries to the store the value in al or char val into the memory location that r11 or *str points to plus rcx or i.  The plus rcx is what moves to the next character.  After the move I add one to rcx to keep track of the count and then jump back up to the .loop1 label to start the loop again.  Once the loop condition fails, we jump down to the .end1 which returns to function.
When writing this method I ran into a problem where I was attempting to copy values into the str pointer, but when I did I kept losing everything after the end of the string.  For example, when I ran the following code:

> ...
>
> mov	r11, rdi	;takes param 1 (char *str) and stores it
>
> mov	rax, rsi	;takes param 2 (char val) and stores it
>
> ...
>
> mov	rcx, 0		;sets int i = 0
>
> ...
>
> mov	[r11+rcx], rax	;attempting to do str[i] = val
>
> ...

I get: *Hello zzzzz* when I should be getting *Hello zzzzz!*

However, when I change the mov line to:

> mov	byte [r11+rcx], 77 ;attempting to do str[i] = 'a'

I got: *Hello aaaaa!*

Which keeps the ending of the exclamation point of the string.  I fixed this problem by storing the char value on the stack instead of in the register, so I could move an exact amount of memory into where [r11+rcx] was pointing instead of the entire 64 bit register.

The way I approached the second method was very similar to the first method.  I started off by storing the three parameters char *dst, char *src, int len into the registers r11, rax, and rdx.  I created the same local variable i in rcx and set that to zero.  I had the same loop structure as function one.  The main difference was instead of getting the character value outside of the loop I did that instead the loop because the character value kept changing.  I did this by doing

> (1) mov		r8, [rsi+rcx]
>
> (2) mov		[rbp-8], r8
>
> (3) mov		al, [rbp-8]
>
> (4) mov		[r11+rcx], al

This command stores the character value at [rsi+rcx] or src[i] into r8 which is then stored on the stack.  I am then able to pull the single character from the stack into al using line (3).  Once the character value is stored in al, the same move command as the my_memset function is used, (4).  This copies each character to the correct position in the string.
When completing this method, I ran into the same problem as with function one where after replacing the characters in the string it would cut off the end of the string.

After completing the coding for the project, I went through all of my variables to make sure I was keeping with System V x86-64 calling conventions and only clobber the registers that were allowed.


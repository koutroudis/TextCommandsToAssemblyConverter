L0:
addi,$sp,$sp,56

move,$s0,$sp

L1:
sw,$ra,-0($sp)

L2:
lw,$t1,-20($sp)

lw,$t2,-24($sp)

add,$t1,$t1,$t2

sw,$t1,-32($sp)

L3:
lw,$t1,-32($sp)

li,$t2,1

blt,$t1,$t2,L6

L4:
j,L23

L5:
lw,$t1,-24($sp)

li,$t2,5

blt,$t1,$t2,L8

L6:
j,L23

L7:
lw,$t1,-28($sp)

li,$t2,1

beq,$t1,$t2,L10

L8:
j,L16

L9:
lw,$t1,-20($sp)

li,$t2,5

add,$t1,$t1,$t2

sw,$t1,-36($sp)

L10:
li,$t1,2

lw,$t2,-28($sp)

div,$t1,$t1,$t2

sw,$t1,-40($sp)

L11:
lw,$t1,-40($sp)

lw,$t2,-36($sp)

mul,$t1,$t1,$t2

sw,$t1,-44($sp)

L12:
lw,$t1,-44($sp)

lw,$t0,-24($sp)

sw,$t1,($t0)

L13:
lw,$t0,-24($sp)

lw,$t1,($t0)

lw,$t0,-8($sp)

sw,$t1,($t0)

L14:
j,L22

L15:
li,$t1,0

sw,$t1,-28($s0)

L16:
addi,$fp,$sp,48

lw,$t1,-20($sp)

sw,$t1,-20($fp)

L17:
addi,$t0,$sp,-16

sw,$t0,-16($fp)

L18:
addi,$t0,$sp,-48

sw,$t0,-8($fp)

L19:
sw,$sp,-4($fp)

addi,$sp,$sp,48

jal,L3

addi,$sp,$sp,-48

L20:
lw,$t0,-48($sp)

lw,$t1,($t0)

lw,$t0,-8($sp)

sw,$t1,($t0)

L21:
j,L3

L22:
lw,$ra,-0($sp)

jr,$ra

L23:
li,$t1,3

sw,$t1,-20($s0)

L24:
li,$t1,2

sw,$t1,-16($s0)

L25:
addi,$fp,$sp,28

lw,$t1,-20($sp)

sw,$t1,-20($fp)

L26:
addi,$t0,$sp,-16

sw,$t0,-16($fp)

L27:
addi,$t0,$sp,-28

sw,$t0,-8($fp)

L28:
sw,$sp,-4($fp)

addi,$sp,$sp,28

jal,L3

addi,$sp,$sp,-28

L29:
lw,$t1,-28($sp)

lw,$t0,-24($sp)

sw,$t1,($t0)

L30:
L31:

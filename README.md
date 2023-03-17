# GISC
## Grid Instruction Set Computer

## Description:
proof of concept
8-bits GISC Quantum Computer
General Purpose
composed of 4 instructions

## ISA (Instruction Set Architecture)
- Set: Assign value to a register
- Cpy: Copy from one grid register to another
- Phy: Copy from one phys register to grid register
- Fly: Jump to another instruction if the jump condition is true

\* Grid Register connects to Grid Registers, Phys Registers and physical layer output
\* Phys Register connects to Grid Registers and physical layer input


| ISA | Dec | Bin | Architecture | Example | Usage(Dec) |Usage(Bin)
| :--:|:-:| :-: | :----: | :---- |:-: |:-:|
| Set |1| 01 | <_Set_> <_GRegA_>  <_Value_> | Assign 3 to grid register 1 || 01001011 |
| Cpy |2| 10 | <_Cpy_> <_GRegA_>  <_GRegB_> | Copy 3 from grid register 1 to grid register 2 || 10010001 |
| Phy |3| 11 | <_Phy_> <_GRegA_>  <_PRegB_> | Copy 3 from phy register 4 to grid register 1 || 11001100 |
| Fly |0| 00 | <_Fly_> <_DCare_>  <_DCare_> | Jump to another instruction || 00000000 |

\* GReg: Grid Register
\* PReg: Phys Register
\* DCare: Don't Care
\* Dec: Decimal
\* Bin: Binary







## Specification
Length of ISA



Number of Quantum bits
Number of Classical bits
Depth of Logic Gates
Depth of Basis Gates


Sample Input


Sample Output


Architecture

------------------------------------------------------------
## Key Components

### Qfe (Quantum Flip Engine)
<_Image of Qfe_>


### Opcode


### Arith

### Flip

### Mask

### Shift
<_Image of Equal>

### Equal

### Greater

### Add

### Multiplication (e.g 3bits 3*4)
<p align="left">
  <img src="quantumMultiplication.png" width="350" title="hover text">
</p>

### VM

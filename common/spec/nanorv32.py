#!/usr/bin/python
# -*- coding: utf-8 -*-
#import AutoVivification as av
#spec = av.AutoVivification()

spec['nanorv32']['cpu']['num_std_regs'] = 32

spec['nanorv32']['cpu']['special_regs'] = 'npc' # Fixme
spec['nanorv32']['cpu']['endianess'] = 'little'
spec['nanorv32']['cpu']['wordsize'] = '32'

# {{{ Instruction format

spec['nanorv32']['inst_type']['R-type']['format'] = {
    'opcode1': {'size': 7, 'offset': 0, 'decode': True},
    'rd': {'size': 5, 'offset': 7},
    'rs1': {'size': 5, 'offset': 15},
    'rs2': {'size': 5, 'offset': 20},
    'func3': {'size': 12, 'offset': 3, 'decode': True},
    'func7': {'size': 7, 'offset': 25, 'decode': True},
    }

spec['nanorv32']['inst_type']['I-type']['format'] = {

    'opcode1': {'size': 7, 'offset': 0, 'decode': True},
    'rd': {'size': 5, 'offset': 7},
    'rs1': {'size': 5, 'offset': 15},
    'imm12': {'size': 12, 'offset': 20},
    'func3': {'size': 3, 'offset': 12, 'decode': True},
    }

spec['nanorv32']['inst_type']['S-type']['format'] = {

    'opcode1': {'size': 7, 'offset': 0, 'decode': True},
    'imm12lo': {'size': 5, 'offset': 7},
    'rs1': {'size': 5, 'offset': 15},
    'rs2': {'size': 5, 'offset': 20},
    'func3': {'size': 3, 'offset': 12, 'decode': True},
    'imm12hi': {'size': 7, 'offset': 25},
    }

spec['nanorv32']['inst_type']['SB-type']['format'] = {

    'opcode1': {'size': 7, 'offset': 0, 'decode': True},
    'immsb1': {'size': 5, 'offset': 7},
    'rs1': {'size': 5, 'offset': 15},
    'rs2': {'size': 5, 'offset': 20},
    'func3': {'size': 3, 'offset': 12, 'decode': True},
    'immsb2': {'size': 7, 'offset': 25},
    }

spec['nanorv32']['inst_type']['U-type']['format'] = \
    {'opcode1': {'size': 7, 'offset': 0, 'decode': True},
     'rd': {'size': 5, 'offset': 7},
     'imm20': {'size': 20,
               'offset': 12}}

spec['nanorv32']['inst_type']['UJ-type']['format'] = \
    {'opcode1': {'size': 7, 'offset': 0, 'decode': True},
     'rd': {'size': 5, 'offset': 7},
     'imm20uj': {'size': 20,
                'offset': 12}}

# ALU shift format

spec['nanorv32']['inst_type']['AS-type']['format'] = {
    'opcode1': {'size': 7, 'offset': 0, 'decode': True},
    'rd': {'size': 5, 'offset': 7},
    'func3': {'size': 3, 'offset': 12, 'decode': True},
    'rs1': {'size': 5, 'offset': 15},
    'shamt': {'size': 5, 'offset': 20},
    'func7': {'size': 7, 'offset': 25, 'decode': True},
    }


# Fence-format

#spec['nanorv32']['inst_type']['F-type']['format'] = {
#    'opcode1': {'size': 7, 'offset': 0, 'decode': True},
#    'rd': {'size': 5, 'offset': 7},
#    'rs1': {'size': 5, 'offset': 15, 'decode': True},
#    'func3': {'size': 3, 'offset': 12, 'decode': True},
#    'func4': {'size': 4, 'offset': 28, 'decode': True},
#    }

# System format
# when all fields are defined
spec['nanorv32']['inst_type']['SYS1-type']['format'] = {
    'opcode1': {'size': 7, 'offset': 0, 'decode': True},
    'sys1_rd': {'size': 5, 'offset': 7, 'decode': True},
    'sys2_rs1': {'size': 5, 'offset': 15, 'decode': True},
    'func3': {'size': 3, 'offset': 12, 'decode': True},
    'func12': {'size': 12, 'offset': 20, 'decode': True},
    }

spec['nanorv32']['inst_type']['SYS2-type']['format'] = {
    'opcode1': {'size': 7, 'offset': 0, 'decode': True},
    'rd': {'size': 5, 'offset': 7},
    'sys2_rs1': {'size': 5, 'offset': 15, 'decode': True},
    'func3': {'size': 3, 'offset': 12, 'decode': True},
    'func12': {'size': 12, 'offset': 20, 'decode': True},
    }

################################################################
#   Instruction decoding description
################################################################

spec['nanorv32']['rv32i']['fence']['desc'] = {
    'inst_type' : 'SYS1-type',
    'decode' : {
        'opcode1' : 0b0001111,
        'sys1_rd' : 0b00000,
        'sys1_rs1': 0b00000,
        'func3'   : 0b000,
        'func12'   : 0b000000000000
    }
}
spec['nanorv32']['rv32i']['fence_i']['desc'] = {
    'inst_type' : 'SYS1-type',
    'decode' : {
        'opcode1' : 0b0001111,
        'sys1_rd' : 0b00000,
        'sys1_rs1': 0b00000,
        'func3'   : 0b001,
        'func12'   : 0b000000000000
    }
}

spec['nanorv32']['rv32i']['scall']['desc'] = {
    'inst_type' : 'SYS1-type',
    'decode' : {
        'opcode1' : 0b1110011,
        'sys1_rd' : 0b00000,
        'sys1_rs1': 0b00000,
        'func3'   : 0b000,
        'func12'   : 0b000000000000
    }
}

spec['nanorv32']['rv32i']['sbreak']['desc'] = {
    'inst_type' : 'SYS1-type',
    'decode' : {
        'opcode1' : 0b1110011,
        'sys1_rd' : 0b00000,
        'sys1_rs1': 0b00000,
        'func3'   : 0b000,
        'func12'   : 0b000000000001
    }
}


spec['nanorv32']['rv32i']['rdcycle']['desc'] = {
    'inst_type' : 'SYS2-type',
    'decode' : {
        'opcode1' : 0b1110011,
        'sys2_rs1': 0b00000,
        'func3'   : 0b010,
        'func12'   : 0b110000000000
    }
}

spec['nanorv32']['rv32i']['rdcycleh']['desc'] = {
    'inst_type' : 'SYS2-type',
    'decode' : {
        'opcode1' : 0b1110011,
        'sys2_rs1': 0b00000,
        'func3'   : 0b010,
        'func12'   : 0b110010000000
    }
}

spec['nanorv32']['rv32i']['rdtime']['desc'] = {
    'inst_type' : 'SYS2-type',
    'decode' : {
        'opcode1' : 0b1110011,
        'sys2_rs1': 0b00000,
        'func3'   : 0b010,
        'func12'   : 0b110000000001
    }
}

spec['nanorv32']['rv32i']['rdtimeh']['desc'] = {
    'inst_type' : 'SYS2-type',
    'decode' : {
        'opcode1' : 0b1110011,
        'sys2_rs1': 0b00000,
        'func3'   : 0b010,
        'func12'   : 0b110010000001
    }
}

spec['nanorv32']['rv32i']['rdinstret']['desc'] = {
    'inst_type' : 'SYS2-type',
    'decode' : {
        'opcode1' : 0b1110011,
        'sys2_rs1': 0b00000,
        'func3'   : 0b010,
        'func12'   : 0b110000000010
    }
}

spec['nanorv32']['rv32i']['rdinstreth']['desc'] = {
    'inst_type' : 'SYS2-type',
    'decode' : {
        'opcode1' : 0b1110011,
        'sys2_rs1': 0b00000,
        'func3'   : 0b010,
        'func12'   : 0b110010000010
    }
}





# Below is code that has been generated from the riscv-opcodes projects
# using the opcodes2py.py script (under common/scripts)
# You can run it with the following command :
# ./opcodes2py.py --opcodes=../../riscv-opcodes/opcodes
#-I inst : beq of type SB-type
# -I-        SB-type  match found beq 0 0x18 3
#-I inst : beq of type SB-type
# -I-        SB-type  match found beq 0 0x18 3

spec['nanorv32']['rv32i']['beq']['desc'] = {
    'inst_type' : 'SB-type',
    'decode' : {
        'opcode1' : 0b1100011,
        'func3'   : 0b0
    }
}
#-I inst : bne of type SB-type
# -I-        SB-type  match found bne 1 0x18 3

spec['nanorv32']['rv32i']['bne']['desc'] = {
    'inst_type' : 'SB-type',
    'decode' : {
        'opcode1' : 0b1100011,
        'func3'   : 0b1
    }
}
#-I inst : blt of type SB-type
# -I-        SB-type  match found blt 4 0x18 3

spec['nanorv32']['rv32i']['blt']['desc'] = {
    'inst_type' : 'SB-type',
    'decode' : {
        'opcode1' : 0b1100011,
        'func3'   : 0b100
    }
}
#-I inst : bge of type SB-type
# -I-        SB-type  match found bge 5 0x18 3

spec['nanorv32']['rv32i']['bge']['desc'] = {
    'inst_type' : 'SB-type',
    'decode' : {
        'opcode1' : 0b1100011,
        'func3'   : 0b101
    }
}
#-I inst : bltu of type SB-type
# -I-        SB-type  match found bltu 6 0x18 3

spec['nanorv32']['rv32i']['bltu']['desc'] = {
    'inst_type' : 'SB-type',
    'decode' : {
        'opcode1' : 0b1100011,
        'func3'   : 0b110
    }
}
#-I inst : bgeu of type SB-type
# -I-        SB-type  match found bgeu 7 0x18 3

spec['nanorv32']['rv32i']['bgeu']['desc'] = {
    'inst_type' : 'SB-type',
    'decode' : {
        'opcode1' : 0b1100011,
        'func3'   : 0b111
    }
}
#-I inst : jalr of type I-type
# -I-        I-type  match found jalr 0 0x19 3

spec['nanorv32']['rv32i']['jalr']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b1100111,
        'func3'   : 0b0
    }
}
#-I inst : jal of type UJ-type
# -I-        UJ-type  match found jal 0x1b 3

spec['nanorv32']['rv32i']['jal']['desc'] = {
    'inst_type' : 'UJ-type',
    'decode' : {
        'opcode1' : 0b1101111
    }
}
#-I inst : lui of type U-type
# -I-        U-type  match found lui 0x0D 3

spec['nanorv32']['rv32i']['lui']['desc'] = {
    'inst_type' : 'U-type',
    'decode' : {
        'opcode1' : 0b110111
    }
}
#-I inst : auipc of type U-type
# -I-        U-type  match found auipc 0x05 3

spec['nanorv32']['rv32i']['auipc']['desc'] = {
    'inst_type' : 'U-type',
    'decode' : {
        'opcode1' : 0b10111
    }
}
#-I inst : addi of type I-type
# -I-        I-type  match found addi 0 0x04 3

spec['nanorv32']['rv32i']['addi']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b0
    }
}
#-I inst : slli of type AS-type
# -I-        AS-type  match found slli 0 1 0x04 3

spec['nanorv32']['rv32i']['slli']['desc'] = {
    'inst_type' : 'AS-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b1,
        'func7'   : 0b0
    }
}
#-I inst : slti of type AS-type
# -I-        I-type  match found slti 2 0x04 3

spec['nanorv32']['rv32i']['slti']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b10
    }
}
#-I inst : sltiu of type I-type
# -I-        I-type  match found sltiu 3 0x04 3

spec['nanorv32']['rv32i']['sltiu']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b11
    }
}
#-I inst : xori of type I-type
# -I-        I-type  match found xori 4 0x04 3

spec['nanorv32']['rv32i']['xori']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b100
    }
}
#-I inst : srli of type AS-type
# -I-        AS-type  match found srli 0 5 0x04 3

spec['nanorv32']['rv32i']['srli']['desc'] = {
    'inst_type' : 'AS-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b101,
        'func7'   : 0b0
    }
}
#-I inst : srai of type AS-type
# -I-        AS-type  match found srai 16 5 0x04 3

spec['nanorv32']['rv32i']['srai']['desc'] = {
    'inst_type' : 'AS-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b101,
        'func7'   : 0b0100000
    }
}
#-I inst : ori of type I-type
# -I-        I-type  match found ori 6 0x04 3

spec['nanorv32']['rv32i']['ori']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b110
    }
}
#-I inst : andi of type I-type
# -I-        I-type  match found andi 7 0x04 3

spec['nanorv32']['rv32i']['andi']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b10011,
        'func3'   : 0b111
    }
}
#-I inst : add of type R-type
# -I-       R-type match found add 0 0 0x0C 3

spec['nanorv32']['rv32i']['add']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b0,
        'func7'   : 0b0
    }
}
#-I inst : sub of type R-type
# -I-       R-type match found sub 32 0 0x0C 3

spec['nanorv32']['rv32i']['sub']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b0,
        'func7'   : 0b100000
    }
}
#-I inst : sll of type R-type
# -I-       R-type match found sll 0 1 0x0C 3

spec['nanorv32']['rv32i']['sll']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b1,
        'func7'   : 0b0
    }
}
#-I inst : slt of type R-type
# -I-       R-type match found slt 0 2 0x0C 3

spec['nanorv32']['rv32i']['slt']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b10,
        'func7'   : 0b0
    }
}
#-I inst : sltu of type R-type
# -I-       R-type match found sltu 0 3 0x0C 3

spec['nanorv32']['rv32i']['sltu']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b11,
        'func7'   : 0b0
    }
}
#-I inst : xor of type R-type
# -I-       R-type match found xor 0 4 0x0C 3

spec['nanorv32']['rv32i']['xor']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b100,
        'func7'   : 0b0
    }
}
#-I inst : srl of type R-type
# -I-       R-type match found srl 0 5 0x0C 3

spec['nanorv32']['rv32i']['srl']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b101,
        'func7'   : 0b0
    }
}
#-I inst : sra of type R-type
# -I-       R-type match found sra 32 5 0x0C 3

spec['nanorv32']['rv32i']['sra']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b101,
        'func7'   : 0b100000
    }
}
#-I inst : or of type R-type
# -I-       R-type match found or 0 6 0x0C 3

spec['nanorv32']['rv32i']['or']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b110,
        'func7'   : 0b0
    }
}
#-I inst : and of type R-type
# -I-       R-type match found and 0 7 0x0C 3

spec['nanorv32']['rv32i']['and']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b111,
        'func7'   : 0b0
    }
}
# MUL/DIV
#-M inst : and of type R-type
# -M-       R-type match found and 0 7 0x0C 3

spec['nanorv32']['rv32i']['mul']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b000,
        'func7'   : 0b0000001
    }
}
spec['nanorv32']['rv32i']['mulh']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b001,
        'func7'   : 0b0000001
    }
}
spec['nanorv32']['rv32i']['mulhsu']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b010,
        'func7'   : 0b0000001
    }
}
spec['nanorv32']['rv32i']['mulhu']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b011,
        'func7'   : 0b0000001
    }
}
spec['nanorv32']['rv32i']['div']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b100,
        'func7'   : 0b0000001
    }
}
spec['nanorv32']['rv32i']['divu']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b101,
        'func7'   : 0b0000001
    }
}
spec['nanorv32']['rv32i']['rem']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b110,
        'func7'   : 0b0000001
    }
}
spec['nanorv32']['rv32i']['remu']['desc'] = {
    'inst_type' : 'R-type',
    'decode' : {
        'opcode1' : 0b110011,
        'func3'   : 0b111,
        'func7'   : 0b0000001
    }
}


#-I inst : lb of type I-type
# -I-        I-type  match found lb 0 0x00 3

spec['nanorv32']['rv32i']['lb']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b0
    }
}
#-I inst : lw of type I-type
# -I-        I-type  match found lw 2 0x00 3

spec['nanorv32']['rv32i']['lw']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b10
    }
}
#-I inst : ld of type I-type
# -I-        I-type  match found ld 3 0x00 3

spec['nanorv32']['rv32i']['ld']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b11
    }
}
#-I inst : lbu of type I-type
# -I-        I-type  match found lbu 4 0x00 3

spec['nanorv32']['rv32i']['lbu']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b100
    }
}
#-I inst : lhu of type I-type
# -I-        I-type  match found lhu 5 0x00 3

spec['nanorv32']['rv32i']['lhu']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b101
    }
}


spec['nanorv32']['rv32i']['lh']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b001
    }
}

#-I inst : lwu of type I-type
# -I-        I-type  match found lwu 6 0x00 3

spec['nanorv32']['rv32i']['lwu']['desc'] = {
    'inst_type' : 'I-type',
    'decode' : {
        'opcode1' : 0b11,
        'func3'   : 0b110
    }
}
#-I inst : sb of type S-type
# -I-        S-type  match found sb 0 0x08 3

spec['nanorv32']['rv32i']['sb']['desc'] = {
    'inst_type' : 'S-type',
    'decode' : {
        'opcode1' : 0b100011,
        'func3'   : 0b0
    }
}
#-I inst : sh of type S-type
# -I-        S-type  match found sh 1 0x08 3

spec['nanorv32']['rv32i']['sh']['desc'] = {
    'inst_type' : 'S-type',
    'decode' : {
        'opcode1' : 0b100011,
        'func3'   : 0b1
    }
}
#-I inst : sw of type S-type
# -I-        S-type  match found sw 2 0x08 3

spec['nanorv32']['rv32i']['sw']['desc'] = {
    'inst_type' : 'S-type',
    'decode' : {
        'opcode1' : 0b100011,
        'func3'   : 0b10
    }
}
#-I inst : sd of type S-type
# -I-        S-type  match found sd 3 0x08 3

spec['nanorv32']['rv32i']['sd']['desc'] = {
    'inst_type' : 'S-type',
    'decode' : {
        'opcode1' : 0b100011,
        'func3'   : 0b11
    }
}
#-I inst : fence of type F-type
#-I inst : fence.i of type F-type
#-I inst : scall of type SYS-type
#-I inst : sbreak of type SYS-type


spec['nanorv32']['cpu']['csr']['cycle'] = {
    'desc' : 'Cycle counter for RDCYCLE instruction',
    'addr' : 0xC00,
    'access' : 'URO',
    'verilog_name' : 'cycle_cnt_low' # to avoid some conflicts
}

spec['nanorv32']['cpu']['csr']['time'] = {
    'desc' : 'Timer for RDTIME instruction',
    'addr' : 0xC01,
    'access' : 'URO',
    'verilog_name' : 'time_cnt_low' # to avoid some conflicts
}

spec['nanorv32']['cpu']['csr']['instret'] = {
    'desc' : 'Instruction retired counter for RDINSTRET instruction',
    'addr' : 0xC02,
    'access' : 'URO',
    'verilog_name' : 'instret_cnt_low'
}

spec['nanorv32']['cpu']['csr']['cycleh'] = {
    'desc' : 'Upper 32-bits part of cycle',
    'addr' : 0xC80,
    'access' : 'URO',
    'verilog_name' : 'cycle_cnt_high' # to avoid some conflicts
}

spec['nanorv32']['cpu']['csr']['timeh'] = {
    'desc' : 'Upper 32-bits part of time',
    'addr' : 0xC81,
    'access' : 'URO',
    'verilog_name' : 'time_cnt_high'
}

spec['nanorv32']['cpu']['csr']['instreth'] = {
    'desc' : 'Upper 32-bits part of instret',
    'addr' : 0xC82,
    'access' : 'URO',
    'verilog_name' : 'instret_cnt_high'
}

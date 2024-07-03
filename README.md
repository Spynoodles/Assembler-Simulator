# Assembler-Simulator

Custom Assembler and Simulator for ISA

This project implements a custom assembler and simulator for a specific ISA (Instruction Set Architecture) using Python. The assembler translates assembly code into machine code, while the simulator executes the generated machine code.
Features

Assembler

    Handles assembly instructions, labels, and variables.
    Supports error handling for syntax errors and illegal instructions.
    Generates binary output for error-free assembly code.

Simulator

    Loads binaries generated by the assembler.
    Executes instructions starting from address 0 until encountering a "hlt" instruction.
    Outputs the program counter and register values after each instruction execution.
    Displays the memory dump after halting execution.

Components
1. Assembler

    Input: Assembly program text file.
    Output: Binaries of the instructions and error notifications.

2. Simulator

    Input: Binary file generated by the assembler.
    Output: Execution details (program counter, register values) and memory dump.

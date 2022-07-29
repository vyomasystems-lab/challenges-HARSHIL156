# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def mux_basic_test(dut):
    """Test for mux"""

    A = 1
    S = 0

    # input driving
    dut.inp0.value = A
    dut.sel.value = S

    await Timer(2, units='ns')
    
    assert dut.out.value == A, "Mux result is incorrect for input {A} and sel {S}. because {OUT}!={out}".format( A=int(dut.inp0.value), S=int(dut.sel.value),OUT=int(dut.out.value), out=int(dut.inp0.value))
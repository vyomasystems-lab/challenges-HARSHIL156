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
    dut.a.value = A
    dut.b.value = B

    await Timer(2, units='ns')
    
    assert dut.sum.value == A+B, "Adder result is incorrect: {A} + {B} != {SUM}, expected value={EXP}".format(
            A=int(dut.a.value), B=int(dut.b.value), SUM=int(dut.sum.value), EXP=A+B)


@cocotb.test()
async def mux_randomised_test(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(5):

        A = random.randint(0, 15)
        B = random.randint(0, 15)

        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
        assert dut.sum.value == A+B, "Randomised harshil test failed with: {A} + {B} = {SUM}".format(
            A=dut.a.value, B=dut.b.value, SUM=dut.sum.value)
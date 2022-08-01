# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0
import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    await FallingEdge(dut.clk) 
    dut.accNumber.value=0b000000000001
    dut.pin.value =0b0000
    await FallingEdge(dut.clk) 


    assert dut.error.value == 1, "Account number or password is wrong "
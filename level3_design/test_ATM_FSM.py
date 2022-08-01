# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0
import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
parameter 
@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """
    clock = Clock(dut.clk, 5, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    accoutno=000000002689
    dut.accNumber.value = accountno
    dut.pin.value = 0b0100
      

    assert dut.error.value == 1, "hi"
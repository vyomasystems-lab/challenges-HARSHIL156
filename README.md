# challenges-HARSHIL156
challenges-HARSHIL156 created by GitHub Classroom
# 
# Level-1 Design-1 MUX Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![WhatsApp Image 2022-08-01 at 11 44 45 AM](https://user-images.githubusercontent.com/92382856/182146531-cf6f4c08-5fd7-4504-9dd8-c6ab9f25af5d.jpeg)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes 5 bit selection line and 2 bit 32 input lines with 2 bit

The values are assigned to the input port using 
```
  A = 1
    S = 0

    # input driving
    dut.inp0.value = A
    dut.sel.value = S
```

The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:
```
assert dut.out.value == A, "Mux result is incorrect for selected {S}(selectionline) and {A}(input0). because given (input0){OUT}!=(recieved o/p){out}".format( A=int(dut.inp0.value), S=int(dut.sel.value),OUT=int(dut.out.value), out=int(dut.inp0.value))
                     AssertionError: Mux result is incorrect for selected 0(selectionline) and 1(input0). because given (input0)0!=(recieved o/p)1
```
## Test Scenario **(Important)**
- Test Inputs: inp0=1 sel=0
- Expected Output: out=1
- Observed Output in the DUT out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
begin
    case(sel)
      5'b00000: out = 2'b00;  //bug
      ....
      ....
    endcase
 end
```
For the mux design, the logic should be ``out = inp0`` instead of ``out = 2'b00`` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![WhatsApp Image 2022-08-01 at 5 50 00 PM](https://user-images.githubusercontent.com/92382856/182146402-1d54b199-0f43-4426-90f2-6be73941287b.jpeg)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?


# Level-1 Design-2 FSM SEQUENCE DETECTOR Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![WhatsApp Image 2022-08-01 at 11 44 45 AM](https://user-images.githubusercontent.com/92382856/182146844-79bef112-f41d-4edb-a632-6c4d0d4ff4e1.jpeg)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 4-bit inputs *a* and *b* and gives 5-bit output *sum*

The values are assigned to the input port using 
```
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await FallingEdge(dut.clk) 
    dut.inp_bit.value=1
    await FallingEdge(dut.clk) 
    dut.inp_bit.value=0
    await FallingEdge(dut.clk) 
    dut.inp_bit.value=1
    await FallingEdge(dut.clk) 
    dut.inp_bit.value=1
    await FallingEdge(dut.clk) 
    
    assert dut.seq_seen.value == 1, "FSM sequence for {Current_state}(current state)== {SEQ1011}(detect_seq_state) but  {Seq_seen}(seq_seen) != 1".format( Current_state=int(dut.current_state.value),SEQ1011=dut.SEQ_1011.value,Seq_seen=dut.seq_seen.value)
```

The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:
```
assert dut.seq_seen.value == 1, "FSM sequence for {Current_state}(current state)== {SEQ1011}(detect_seq_state) but  {Seq_seen}(seq_seen) != 1".format( Current_state=int(dut.current_state.value),SEQ1011=dut.SEQ_1011.value,Seq_seen=dut.seq_seen.value)
                     AssertionError: FSM sequence for 4(current state)== 4(detect_seq_state) but  0(seq_seen) != 1
```
## Test Scenario **(Important)**
- Test Inputs: inp_bit = 1011 // after every clock one bit is assigned
- Expected Output: seq_seen = 1
- Observed Output in the DUT seq_seen=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
  assign seq_seen = current_state == SEQ_1011 ? 0 : 0;

```
For this fsm design, the logic should be ``assign seq_seen = current_state == SEQ_1011 ? 1 : 0;`` instead of `` assign seq_seen = current_state == SEQ_1011 ? 0 : 0; `` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![WhatsApp Image 2022-08-01 at 5 58 08 PM](https://user-images.githubusercontent.com/92382856/182147778-dc24016c-3eac-48d8-bc04-9d9c066d7587.jpeg)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?


# Level-3 ATM-FSM Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![WhatsApp Image 2022-08-01 at 11 44 45 AM](https://user-images.githubusercontent.com/92382856/182146889-bf01ed08-6778-479b-911f-5cac3c413800.jpeg)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 4-bit inputs *a* and *b* and gives 5-bit output *sum*

The values are assigned to the input port using 
```
  dut.accNumber.value=0b000000000000
    dut.pin.value =0b0000
    await FallingEdge(dut.clk)
    assert dut.isAuthenticated.value == 1, "Account number or password is wrong "
```

The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:
```
assert dut.isAuthenticated.value == 1, "Account number or password is wrong "
                     AssertionError: Account number or password is wrong 
```
## Test Scenario **(Important)**
- Test Inputs: accNumber = 0b000000000000
- Expected Output: isAuthenticated = 1
- Observed Output in the DUT isAuthenticated = 0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
  //initializing the database with arbitrary accounts
  initial begin
    acc_database[0] = 12'b1; pin_database[0] = 4'b0000; bug 
```
For this atm fsm design, the account database has wrong account details in that

## Design Fix
Updating the design and re-running the test makes the test pass.

![WhatsApp Image 2022-08-01 at 5 38 30 PM](https://user-images.githubusercontent.com/92382856/182148389-19738ea9-ba82-4615-bd27-f17faf1c53ee.jpeg)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?


module tb_inverter;
  
  // 1. Signals to drive and monitor the Device Under Test (DUT)
  logic in_sig;
  logic out_sig;
  
  // 2. Instantiate the DUT (connect signals to ports)
  inverter uut (
    .in(in_sig),
    .out(out_sig)
  );
  
  // 3. Stimulus generation (the test procedure)
  initial begin
    
    // Monitor changes in real time
    $monitor("Time=%0t | in=%b -> out=%b", $time, in_sig, out_sig);
    
    // Apply fundamental test vectors
    in_sig = 1'b0;
    #10; 			// Wait 10 time units
    
    in_sig = 1'b1;
    #10;			// Wait 10 time units
    
    $finish;		// Terminate simulation
  end
  
endmodule

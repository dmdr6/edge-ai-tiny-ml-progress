module tb_xnor_gate;
  
  // 1. Signals to drive the Device Under Test (DUT)
  logic a_sig;
  logic b_sig;
  logic out_sig;
  
  // 2. Instantiate the XNOR Gate
  xnor_gate uut (
    .a(a_sig),
    .b(b_sig),
    .out(out_sig)
  );
  
  // 3. Truth table verification
  initial begin
    $display("------------------");
    $display("Time | A | B | Out");
    $display("------------------");
    
    // Combination 00
    a_sig = 1'b0; b_sig = 1'b0; #10;
    $display("%0t   | %b | %b | %b", $time, a_sig, b_sig, out_sig);
    
    // Combination 01
    a_sig = 1'b0; b_sig = 1'b1; #10;
    $display("%0t   | %b | %b | %b", $time, a_sig, b_sig, out_sig);
    
    // Combination 10
    a_sig = 1'b1; b_sig = 1'b0; #10;
    $display("%0t   | %b | %b | %b", $time, a_sig, b_sig, out_sig);
    
    // Combination 11
    a_sig = 1'b1; b_sig = 1'b1; #10;
    $display("%0t   | %b | %b | %b", $time, a_sig, b_sig, out_sig);
    
    $display("------------------");
    $finish;
  end
  
endmodule

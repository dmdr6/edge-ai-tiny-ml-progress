module tb_mux_2to1;
  
  // Signals to drive the DUT
  logic in0_sig;
  logic in1_sig;
  logic sel_sig;
  logic out_sig;
  
  // Instantiate the 2-to-1 Mux
  mux_2to1 uut (
    .in0(in0_sig),
    .in1(in1_sig),
    .sel(sel_sig),
    .out(out_sig)
    );
  
  // Systematic routing verification
  initial begin
    $display("--------------------------------");
    $display("Time | Sel | In1 | In0 | Out (Expected)");
    $display("--------------------------------");
    
    // Test Case 1: Select in0 (sel = 0), where in0=0, in1=1
    in0_sig = 1'b0; in1_sig = 1'b1; sel_sig = 1'b0; #10;
    $display("%0t  |  %b  |  %b  |  %b  |  %b", $time, sel_sig, in1_sig, in0_sig, out_sig);
    
    // Test Case 2: Switch to select in1 (sel = 1), keeping same inputs
    sel_sig = 1'b1; #10;
    $display("%0t  |  %b  |  %b  |  %b  |  %b", $time, sel_sig, in1_sig, in0_sig, out_sig);

    // Test Case 3: Change data inputs (in0=1, in1=0), select in0 (sel = 0)
    in0_sig = 1'b1; in1_sig = 1'b0; sel_sig = 1'b0; #10;
    $display("%0t  |  %b  |  %b  |  %b  |  %b", $time, sel_sig, in1_sig, in0_sig, out_sig);

    // Test Case 4: Keep data inputs, select in1 (sel = 1)
    sel_sig = 1'b1; #10;
    $display("%0t  |  %b  |  %b  |  %b  |  %b", $time, sel_sig, in1_sig, in0_sig, out_sig);

    $display("--------------------------------");
    $finish;
  end

endmodule

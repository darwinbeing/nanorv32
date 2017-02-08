#include "Vnanorv32_simpleahb.h"
#include "verilated.h"
#include "verilated_vcd_c.h"

int main(int argc, char **argv, char **env) {
    int i;
    int clk;
    Verilated::commandArgs(argc, argv);
    // init top verilog instance
    Vnanorv32_simpleahb* top = new Vnanorv32_simpleahb;
    // init trace dump
    Verilated::traceEverOn(true);
    VerilatedVcdC* tfp = new VerilatedVcdC;
    // top->trace (tfp, 99);
    tfp->open ("verilator.vcd");
    // initialize simulation inputs
    top->clk_in = 0;
    top->rst_n = 1;

    // run simulation for 100 clock periods
    for (i=0; i<20; i++) {
        top->rst_n = (i > 2);
        // dump variables into VCD file and toggle clock
        for (clk=0; clk<2; clk++) {
            tfp->dump (2*i+clk);
            top->clk_in = !top->clk_in;
            top->eval ();
        }

        if (Verilated::gotFinish())  exit(0);
    }
    tfp->close();
    exit(0);
}

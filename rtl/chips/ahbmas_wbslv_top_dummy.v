// Fake Whisbone to AHB protocol converter
// used from testbench to access the debug system of the Nrv32
// without using SWD/JTAG commands but just AHB read/write tasks

`timescale 1 ns / 1 ns

module ahbmas_wbslv_top_dummy (

                         hclk,hresetn,
                         // AHB Master Interface (Connect to AHB Slave)
                         haddr,htrans,hwrite,hsize,
                         hburst,hwdata,hrdata,hready,hresp,

                         // WISHBONE Slave Interface (Connect to WB Master)
                         data_o, data_i, addr_i,clk_i,rst_i,
                         cyc_i, stb_i, sel_i, we_i, ack_o
                         );


   //PARAMETER
   parameter AWIDTH = 32,DWIDTH = 32;//Address Width,Data Width

   //INPUTS AND OUTPUTS
   // --------------------------------------
   //Top level ports for AHB
   input hresetn;		 //AHB Clk
   input hclk;		 //AHB Active Low Reset

   // AHB Master Interface (Connect to AHB Slave)
   input [DWIDTH-1:0] hrdata;		//Read data bus

   //Transfer Response	from AHB Slave
   input [1:0]        hresp;
   input              hready;

   //Address and Control Signals
   output [AWIDTH-1:0] haddr;		//Address
   output              hwrite;					//Write/Read Control
   output [2:0]        hsize;				//Size of Data Control
   output [2:0]        hburst;				//Burst Control
   output [31:0]       hwdata;			//Write data bus
   output [1:0]        htrans;				//Transfer type


   // --------------------------------------
   // WISHBONE Slave Interface (Connect to WB Master)
   output [DWIDTH-1:0] data_o;   //Wishbobe Data Ouput
   output              ack_o;	   //Wishbone Acknowledge

   input [DWIDTH-1:0]  data_i;   //Wishbone Data Input
   input [AWIDTH-1:0]  addr_i;   //Wishbone Address Input
   input               cyc_i;    //Wishbone Cycle Input
   input               stb_i;	   //Wishbone Strobe Input
   input [3:0]         sel_i;	   //Wishbone Selection Input
   input               we_i;	   //Wishbone Write/Read Control
   input               clk_i;	   //Wishbone Clk Input
   input               rst_i;	   //Wishbone Active High Reset Input

   // reg signal are expected to be overriden
   // from testbench code

   reg [AWIDTH-1:0]    haddr;
   reg                 hwrite;
   reg [2:0]           hsize;
   reg [2:0]           hburst;
   reg [31:0]          hwdata;
   reg [1:0]           htrans;
   wire [DWIDTH-1:0]   data_o;
   wire                ack_o;

   assign data_o = 0;
   assign ack_o  = 0;


   initial begin
      #1;
      haddr = 0;
      hwrite = 0;
      hsize = 0;
      htrans = 0;
      hwdata = 0;
      hburst = 0;
   end




endmodule

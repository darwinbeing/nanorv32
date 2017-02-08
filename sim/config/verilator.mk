# Verilator specific makefile



VERILATOR_EXTRA_V_SRC=$(wildcard $(TEST_DIR)/*.v)

ifeq ($(VERILATOR_EXTRA_V_SRC),)
VERILATOR_VCD_EXTRA_MODULE=
else
VERILATOR_VCD_EXTRA_MODULE=-DVCD_EXTRA_MODULE=,$(TEST)
endif
_VERILATOR_OPTS += --top-module nanorv32_simpleahb
_VERILATOR_OPTS += $(VERILOG_DEFINES)
_VERILATOR_OPTS += -DNO_RAM_INIT=1
_VERILATOR_OPTS += $(SIMULATOR_VERILATOR_OPTIONS)
_VERILATOR_OPTS += $(SIMULATOR_VERILATOR_WARNINGS)
_VERILATOR_OPTS += -DTB=$(SIMULATION_TESTBENCH_NAME)
_VERILATOR_OPTS += $(VERILATOR_VCD_EXTRA_MODULE) -f verilator_file_list.txt $(VERILATOR_EXTRA_V_SRC)



_VERILATOR_SIM += $(VERILOG_PARAMETER)
_VERILATOR_SIM += +program_memory=$(TEST_DIR)/$(TEST).vmem

verilator_rtl_build:
	@python $(TOP)/common/files/main.py --topdir=$(TOP)  --verilator=$(TEST_DIR)/verilator_file_list.txt
	cd $(TEST_DIR)  && verilator $(_VERILATOR_OPTS)  --exe  $(TOP)/sim/verilator/main.cpp
	# $(TOP)/sim/verilator/verilated.cpp

verilator_rtl_elab:
	cd $(TEST_DIR) && make -C obj_dir -f Vnanorv32_simpleahb.mk Vnanorv32_simpleahb

verilator_rtl_sim:
	cd $(TEST_DIR) && ./obj_dir/Vnanorv32_simpleahb   $(_VERILATOR_SIM)
	$(SIMULATOR_VERILATOR_GUI)

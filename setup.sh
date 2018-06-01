

# --------------------------------------------------------------------------------------------------------
# Define the LArSoft version we wish to use
# --------------------------------------------------------------------------------------------------------

export MY_VERSION=v06_77_00
export MY_COMP=e15
export MY_TYPE=prof

# --------------------------------------------------------------------------------------------------------

# Setup uboonecode with the required LArSoft version
source /grid/fermiapp/products/dune/setup_dune.sh
setup dunetpc ${MY_VERSION} -q ${MY_COMP}:${MY_TYPE}

# Setup for running on the grid
source /grid/fermiapp/products/common/etc/setups.sh
setup jobsub_client

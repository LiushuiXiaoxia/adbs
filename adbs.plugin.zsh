# Check if python3 is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

# Path to the Python script
BATCH_ADB_SCRIPT="$ZSH_CUSTOM/plugins/adbs/adbs.py"

# Add batch-adb as a shell command
alias adbs="$PYTHON_CMD $BATCH_ADB_SCRIPT"
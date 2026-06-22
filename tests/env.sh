# Setup the environment for testing python-sanlock.

# Disable privileged operations, allowing to run sanlock daemon as
# non-privileged user.
export SANLOCK_PRIVILEGED=0

# Use temporary sanlock run dir, usable for non-privileged user.  This
# is used by sanlock daemon to create a lockfile and socket, and by
# sanlock clients for communicating with the daemon.
export SANLOCK_RUN_DIR=/tmp/sanlock

# Ensure USER is set (containers often omit it).
export USER=${USER:-$(id -un)}

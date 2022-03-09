#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/sim2real/ep_ws/src/sim2real_ep/image_pipeline-noetic/camera_calibration"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/sim2real/ep_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/sim2real/ep_ws/install/lib/python3/dist-packages:/home/sim2real/ep_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/sim2real/ep_ws/build" \
    "/usr/bin/python3" \
    "/home/sim2real/ep_ws/src/sim2real_ep/image_pipeline-noetic/camera_calibration/setup.py" \
    egg_info --egg-base /home/sim2real/ep_ws/build/sim2real_ep/image_pipeline-noetic/camera_calibration \
    build --build-base "/home/sim2real/ep_ws/build/sim2real_ep/image_pipeline-noetic/camera_calibration" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/sim2real/ep_ws/install" --install-scripts="/home/sim2real/ep_ws/install/bin"

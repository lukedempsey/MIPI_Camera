import arducam_mipicamera as arducam
import v4l2 #sudo pip install v4l2
import time
import cv2 #sudo apt-get install python-opencv

def align_down(size, align):
    return (size & ~((align)-1))

def align_up(size, align):
    return align_down(size + align - 1, align)

if __name__ == "__main__":
    camera = arducam.mipi_camera()
    camera_interface = arducam.CAMERA_INTERFACE()
    camera_interface.i2c_bus=0
    camera_interface.camera_num = 1
    camera_interface.sda_pins=(28,0)
    camera_interface.scl_pins=(29,1)
    camera_interface.led_pins=(30,2)
    camera_interface.shutdown_pins=(31,3)
    print("Open camera...")
    camera.init_camera2(camera_interface)
    print("Setting the resolution...")
    fmt = camera.set_resolution(800,600)
    print("Current resolution is {}".format(fmt))
    c = 0
    while cv2.waitKey(10) != 27:
        c+=1
        print(f"Frame: {c}")
        frame = camera.capture(encoding = 'i420')
        print(f"Size: {frame.alloc_size}")

    # Release memory
    del frame
    print("Close camera...")
    camera.close_camera()
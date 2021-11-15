https://drive.google.com/file/d/1bzWKC7B9o-m8VURcbXgIRyXGH5aRr9et/view?usp=sharing

* gtk err

sudo apt install libcanberra-gtk-module libcanberra-gtk3-module





# StartDL_Jetson 

Jetpack 4.4 =<

줏어모은 Nvidia Jetson 에 사용하면 좋은 것들 리스트.

# recommend pwm fan on always

sudo sh -c 'echo 50 > /sys/devices/pwm-fan/target_pwm'

# 현재 repository 설치 git clone

git clone https://github.com/katebrighteyes/StartDL_Jetson

cd StartDL_Jetson

sudo chmod 777 *.sh

# 1. Python Dev

sudo apt-get install libpython3-dev python3-numpy

2~3 minutes


# 2. PyTorch

./install-pytorch.sh

about 40 minutes


# 3. G-Streamer for OpenCV

./install_gstreamer.sh

# torch to trt

./install_torch2trt.sh

# Install Tensorflow 1.x

pb -> uff Convert uff 변환 툴을 사용하기 위해서는 tensorflow 설치가 우선 되어야합니다.

./install_tensorflow_1.x.sh

# jtop

무조건 설치하자
apt-get install python-pip

sudo -H pip install -U jetson-stats

----------------------------------
* gtk err

sudo apt install libcanberra-gtk-module libcanberra-gtk3-module

----------------
sudo jetson_clocks

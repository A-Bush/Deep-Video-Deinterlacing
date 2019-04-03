### Architecture
TensorFlow Implementation of ["Real-time Deep Video Deinterlacing"](https://arxiv.org/abs/1708.00187)

<a href="http://tensorlayer.readthedocs.io">
<div align="center">
	<img src="images/model.png" width="100%"/>
</div>
</a>


### Run
Prepare
```bash
virtualenv -p /usr/bin/python3.5 venv
. venv/bin/activate
pip install -r requirements.txt
deactivate
```

List files to deinterlace
```bash
find /home/ubuntu/pngs/folder -type f -iname "*png" | sort > images.txt
mkdir output
```

Start deinterlacing
```
. venv/bin/activate
python runDeinterlacing.py --input_list=/path/to/images.txt --output=/path/to/output --gpu=0
deactivate
``` 

### Author
- [lszhuhaichao](https://github.com/lszhuhaichao)

### Citation
If you find this project useful, we will be grateful if you cite our paper

```
@article{zhu2017real,
  title={Real-time Deep Video Deinterlacing},
  author={Zhu, Haichao and Liu, Xueting and Mao, Xiangyu and Wong, Tien-Tsin},
  journal={arXiv preprint arXiv:1708.00187},
  year={2017}
}
```

### License
- For academic and non-commercial use only.


### Comparison

*TSNet_single_load* MacBook Intel UHD Graphics 630 1536 MB
```
DEVICE: /gpu:0
time: 032.14 sec file: 9009.png
time: 035.33 sec file: 653.png
time: 029.76 sec file: 10064.png
```

*TSNet* MacBook Intel UHD Graphics 630 1536 MB
```
DEVICE: /gpu:0
time: 030.53 sec file: 9009.png
time: 030.90 sec file: 653.png
time: 029.26 sec file: 10064.png
```

*TSNet_single_load*  MacBookPro Intel Core i7-8750H @ 2.2Ghz
```
DEVICE: /cpu:0
time: 036.46 sec file: 9009.png
time: 032.35 sec file: 653.png
time: 035.21 sec file: 10064.png
```

*TSNet* MacBookPro Intel Core i7-8750H @ 2.2Ghz
```
DEVICE: /cpu:0
time: 036.32 sec file: 9009.png
time: 034.14 sec file: 653.png
time: 033.29 sec file: 10064.png
```
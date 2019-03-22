# Deep Video Deinterlacing

We run this code using Tensorflow.

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
find /home/ubuntu/pngs/folder -type f -iname "*png" > images.txt
mkdir output

```

- Start deinterlacing
```
. venv/bin/activate
python runDeinterlacing.py --input_list=images.txt --output=output
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

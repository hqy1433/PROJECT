# 基于Robomaster SDK的编队程序

### 物料清单:

- 6台**步兵形态**的EP机器人

- 1台电脑(需要部署**Robomaster SDK**环境)    [部署教程](https://robomaster-dev.readthedocs.io/zh-cn/latest/python_sdk/multi_robot_ep.html)

- 1个较为**牛逼的路由器**

### 仓库内程序:

- GET_SN.py  —————  扫描当前网络下的所有机器人

- PROJECT.py  —————  编队主程序

- Program_Library.py  —————  编队的程序库

- SCAN_KEYWORD.py  —————  显示联网的二维码

- STAND_BY.py  —————  可使机器人待机

- text.py  —————  方便编写接下的程序

### 流程:

1. 电脑接入网络 在"**SCAN_KEYWORD.py**"中填上自己的**SSID**和**PASSWORD** 生成二维码

2. 机器人上电 中控切换模式为**路由器模式**

3. 给机器人扫码 使机器人连上网络  运行“**GET_SN.py**”查看六台的连接状态

4. 给机器人摆好**位子**

5. **修改SN** 运行“**PROJECT.py**”

### 位子摆放:

参考[视频](https://www.bilibili.com/video/BV1PH4y1L79d/?share_source=copy_web&vd_source=f061840d46a938a2d997b4efc7084d82)

### 可能会遇到的问题

- **机器人编队网络要求较高** 建议路由器下只有机器人设备 电脑用网线连接路由器 (不推荐使用手机热点，网络环境不佳可能导致报错)

- 机器人扫描二维码时，**无需确认机器人灯效情况**，只要路由器后台显示连接或者使用扫描有显示就行

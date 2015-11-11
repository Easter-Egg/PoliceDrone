# PoliceDrone

15.10.05
  - 스크립트 출처 : https://github.com/bashardawood/L3G4200D-Python
  - i2c 통신 설정방법 : http://astrobeano.blogspot.kr/2014/01/gy-80-orientation-sensor-on-raspberry-pi.html
  - GPIO를 신경쓰지 않고 무작정 연결하다가 무언가가 타는 냄새를 맡음(!) 천만다행으로 센서에는 문제가 없음
  - GPIO 제대로 연결하고 기울기 센서값 테스팅 스크립트 수행(Python - gyro.py)

--
15.10.12
  - 스크립트 출처 : https://github.com/rasplay/RPiHY28bShield
  - 웨어러블 디바이스로 이용하기 위해 라즈베리파이에 LCD 패널을 연결 및 설정
  - 라즈비안 커널 업데이트 발생하는 오류로 무한 재부팅 >> 스크립트를 하나씩 수동으로 수행

--
15.10.13
  - 스크립트를 수동으로 수행하여 2.8 LCD 패널 연결 성공 (+ 터치 인식도 성공)

--
15.10.15 
  - 웨어러블 디바이스 파트의 GUI 프로그램 구현을 위해 wxPython으로 선택 (I2C 관련 자료가 Python 오픈소스로 많이 존재함)

--
15.10.17
  - wxPython의 간단한 예제 수행 >> button, toggle button

--
15.10.27
  - 기본 ui 구현 (버튼 배치)
  - 버튼 이벤트 처리(연결, LED)
  
--
15.11.11
  - 소켓을 이용한 서버(드론)와 클라이언트(웨어러블) 통신 간단 구현
  - Up, Down, Ctrl 버튼 이벤트 간단 구현

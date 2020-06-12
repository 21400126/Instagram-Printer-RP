Instagram-Printer-RP 목적
==============================

기존 코드는 Raspberry Pi와 Polaroid Pogo라는 휴대용 블루투스 프린터를 위해 작성됐었다.


Polaroid Pogo는 단종됐을 뿐 아니라 블루투스 프린터보다는 로컬/네트워크  프린터가 접근이 쉬울 것이라고 판단해 로컬 프린터를 위한 코드로 변경하였다.


Instagram의 사진을 저장해주고, 사용자가 사진을 출력하길 원한다면 연결된 프린터로 사진을 출력해주는 코드이다.




프로그램 장점
---------------------

Instagram에 업데이트되는 사진들을 저장하기 위해서는 원본 사진을 저장하는 것이 아니라, 캡쳐를 하여 저장하여야 한다.



따라서 원본만큼 좋은 화질을 유지하지 못한다. 하지만, 본 프로그램을 사용할 시에는 원본의 이미지를 가져와서 저장하기 때문에 원본화질을 그대로 저장할 수 있다는 장점이 있다.




프로그램 요구조건 & 실행
-------------------

코드를 실행시키기 위해서 필요한 몇 가지가 있다.


1. python2 -> python3

코드는 python3를 기준으로 작성됐기 때문에, Raspberry pi에서 실행하기 위해서는 python을 python2가 아닌 python3로 upgrade해야 한다.


2. urllib 라이브러리

 pip install urllib를 통해 설치 가능


Option. Local printer & CUPS : 사진을 저장한 후, 인쇄하기 위해서는 Raspberry pi와 연결된 프린터가 필요하다. 인쇄 할 필요가 없다면 프린터는 필요가 없다.


프로그램을 실행하기 위한 코드는 다음과 같다.

	python print.py InstagramLink FileNameToSave

예시)

	python print.py https://www.instagram.com/p/B\_RsWY3HZWP/ SeojoonPark
   
<img src= "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/93810746_1175396686131524_1870466887554263304_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=0J_fE_cbqYUAX_WMHf9&oh=e0fe2ccb7abb8db1d0f1f16f8ce13a44&oe=5F0CD41B" width="50%" height="50%">




참고
----------------------

Rasberrypi 파이썬3이상 업그레이드: <https://godpeople.or.kr/board/3409846>


Raspberrypi로 네트워크 프린터 만들기: <https://blog.naver.com/PostView.nhn?blogId=renucs&logNo=221337532824&from=search&redirect=Log&widgetTypeCall=true&directAccess=false>

License
-------

    Raspberry Pi Instagram Printer
    Copyright (C) 2013 Jonathan King

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

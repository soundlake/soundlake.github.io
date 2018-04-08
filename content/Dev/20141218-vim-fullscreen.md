Title: MacVim 전체화면 깨짐 해결
Date: 2014-12-18 10:00
Modified: 2018-04-08 02:00
Slug: macvim-fullscreen
Lang: ko
Tags: vim, MacVim, Mac

Mac 업데이트 후, MacVim 전체화면을 실행하면 화면 오른쪽에 밝은 색의 막대가 생겨났다.

![밝은 색 막대가 생긴 MacVim 전체화면모드]({filename}/images/20141218_screen.png)

한동안 좀 짜증이 났지만 그래도 견딜만 해서 참았다가, 오늘 생각난 김에 이것도 해결. 멕북은 화면 베젤이 까만 색이니 화면이 어두운데 거기 한 부분만 밝으니 여간 신경쓰이는 게 아니었다.

한참 찾다가 결국 [두둥!](https://code.google.com/p/macvim/issues/detail?id=454)

결국 해결 방법은,
    1. 설정창을 열자. MacVim -> Preference..(Cmd+,)
    2. Advanced 탭으로.
    3. Prefer native fullscreen mode.. 를 비 활성화.
    4. Full screen mode 풀었다가 다시 돌아오면,
    5. 짜잔. 해결.

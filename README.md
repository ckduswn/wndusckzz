# 리눅스 명령어 중에서 top, ps, jobs, kill 명령어에 대해서 조사해보자!
**1. 리눅스 명령어 top**
- *명령어 top이란?*
  
  - 리눅스 상의 모든 운영체제에서 현재 실행 중인 프로세스와 시스템 자원 사용량을 실시간으로 업데이트하여 보여줌으로써 모니터링을 돕는 도구. ps와 달리 지속적인 모니터링 기능을 한다.
  - 상위에는 CPU 사용량과 메모리 사용량 등의 요약 정보가 나타나며, 하단에는 실행 중인 각 프로세스의 상세 정보가 표시되어 특히 CPU, 메모리, 디스크 활동 등 다양한 측면에서 시스템의 성능 파악에 유용.
  - 특정 서비스 가동 시 얼마나 많은 자원을 소모하는지, 무엇이 문제이고 자원 배분을 늘려야 하는지 등 근본적인 해결책을 줌.
  - ***cf*** ) 윈도우 운영체제 사용 시 프로그램이나 컴퓨터가 렉에 걸렸을 때 작업관리자를 통해 프로그램이나 응답 없는 파일을 종료시킬 때나, gpu, 메모리 체크 시 사용하는 작업관리자 기능과 유사.

- *명령어 사용법* : `TOP` 입력.

- *명령어 사용 결과*

  | 명 | 결과 |
  |------------------|------------------|
  |`PID`(프로세스 ID) | 각 프로세스의 고유한 식별 번호. 해당 프로세스 식별 시 사용. |
  |`USER`(사용자) | 프로세스를 실행한 사용자 계정. |
  | `PR`(우선순위) | 프로세스 실행 우선순위를 나타냄. PR값이 낮을수록 더 높은 우선 순위를 나타냄. |
  |`NI`(우선 순위 변경) | 사용자에 의해 변경된 프로세스의 우선 순위를 나타냄. |
  | `VIRT`(가상 메모리 사용량) | 프로세스가 사용하는 가상 메모리 크기 표시. (단위:KB) |
  | `RES`(실제 메모리 사용량) | 프로세스가 실제로 점유 중인 물리적 메모리 크기 표시. (단위:KB) |
  | `SHR`(공유 메모리 사용량) | 다른 프로세스와 공유하고 있는 메모리 크기 표시. (단위:KB) |
  | `S`(상태) | 프로세스의 현재 상태를 나타냄. ('R':실행 중/'S':슬립 중/'Z':좀비 상태) |
  | `% CPU`(CPU 사용률) | 프로세스가 CPU를 사용하는 비율을 백분율로 나타냄. |
  | `% MEM`(메모리 사용률) | 프로세스가 메모리를 사용하는 비율을 백분율로 나타냄. |
  | `TIME+(누적 CPU 시간)` | 프로세스가 실행되며 사용한 누적 CPU 시간 표시. |
  | `COMMAND`(명령어) | 프로세스를 실행한 명령어 혹은 프로그램을 나타냄. |


 - [출처](https://ubuntu2304.tistory.com/entry/%EB%A6%AC%EB%88%85%EC%8A%A4%EB%A7%88%EC%8A%A4%ED%84%B0-%EB%A6%AC%EB%88%85%EC%8A%A4-top-%EB%AA%85%EB%A0%B9%EC%96%B4%EC%99%80-CPU-%EC%84%B1%EB%8A%A5-%EB%B6%84%EC%84%9D)

    
**2. 리눅스 명령어 ps**

- *명령어 ps(Process Status)란?*

  - 현재 사용 중인 프로세스 목록과 상태를 출력하여 보여줌.
    사용자가 실행한 프로세스 외에도 사용자 관리, 메모리 관리, 네트워크, 접속 관리 등 다양한 기능을 수행하는 많은 프로세스가 실행됨.
  - ***cf*** ) 윈도우의 작업관리자나 tasklist와 유사.
 
- *사용법(+옵션)* : `ps [option]`
   - ***cf*** ) 이때 옵션이 다수 존재함. 유닉스 계열, BSD 계열, GNU 계열이 다 다르다. 자신의 계열이 아니라고 해서 사용이 불가한 것은 아니지만, 원하는 프로세스의 상태를 출력하기 위해선 정확한 옵션 값을 출력해야 하므로 표기법이 다르다는 것을 명심할 것.
   - System V_유닉스에서 주로 쓰이는 명령어
     + `-A` 모든 프로세스 출력. `-e`와 동일.
     + `-a` 세션 리더 및 터미널과 관련되지 않은 프로세스를 제외한 나머지 프로세스들을 출력.
     + `-r` 현재 포그라운드에서 실행 중인 프로세스 출력.
     + `-f` 완전 포맷으로 출력. 프로세스의 자세한 정보를 출력함.
     + `-l` 긴 포맷으로 출력.
     + `ps -u uid`  uid로 특정한 사용자에 대한 모든 프로세스의 정보를 출력.
     + `ps -p pid` pid로 지정한 특정 프로세스의 정보를 출력.
 
  - BSD에서 주로 쓰이던 명령어
    + `T` 이 터미널과 관련된 현재 사용자의 프로세스를 출력. t 옵션에서 아무것도 주지 않은 것과 같음.
    + `a` 이 터미널과 관련된 모든 사용자의 프로세스를 출력.
    + `u` 프로세스의 소유자 정보를 기준으로 출력.
    + `x` 터미널과 관련되지 않은 모든 프로세스를 출력.
    + `f` 프로세스 상속 관계를 트리 구조로 출력.
    + `ww` 넓게 출력.
   
- *ps명령의 결과*

| 명 | 결과 |
|--------------|---------------|
| `PID`(프로세스 ID) | 각 프로세스의 고유한 식별 번호. 해당 프로세스 식별 시 사용. |
| `TTY` | 프로세스가 실행된 터미널의 종류와 번호. |
| `TIME` | 프로세스 실행 시간. |
| `CMD` | 실행되고 있는 프로그램의 이름(명령). |


- *도움말* : `ps 01--help all`


- [출처1](https://onecoin-life.com/28), [출처2](https://marisara.tistory.com/entry/%EB%A6%AC%EB%88%85%EC%8A%A4-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-ps)

**3. 리눅스 명령어 jobs**

- *명령어 jobs란?*
  + shell에서는 프로세스를 작업(job)단위로 관리함. 이떄 명령어 jobs는 현재 shell 세션에서 실행시킨 백그라운드 작업의 목록을 출력함으로써 작업 상태를 표시.
  + 포그라운드foreground와 백그라운드background두 가지 방식으로 동작.

- ***cf) 프로세스 실행 방식 : 포그라운드foreground와 백그라운드background***
  + **포그라운드foreground**
 
    
   ![스크린샷 2024-06-01 152855](https://github.com/ckduswn/wndusckzz/assets/171252819/873de4f2-a405-4ad9-ba59-49e4fc40a150)

    + 터미널에서 작업 시 사용자가 명령을 입력하면 이를 해석 및 실행 후 결과를 화면에 출력.
    + 사용자는 출력된 결과를 확인 후 다른 명령어를 입력하는 대화식 작업을 수행. 이렇게 사용자가 입력한 명령이 실행되어 결과가 출력될 때까지 기다려야 하는 방식을 포그라운드 방식이라고 하며, 이러한 방식으로 처리되는 프로세스를 포그라운드 프로세스라고 함.

    작업이 종료되는 시점까지 다른 쉘 명령어를 수행할 수 없고 대기. 포그라운드에서 실행 중인 작업은 ctrl+c로 종료.



  + **백그라운드background**
 
    
   ![스크린샷 2024-06-01 152920](https://github.com/ckduswn/wndusckzz/assets/171252819/caf6b91d-5df0-4a55-b818-23b63df5c3fd)

    + 작업을 하는 동시에 다른 명령어들을 실행시킬 수 있어 한 터미널에서 여러 개의 프로세스를 동시에 실행시킬 수 있음, 이를 멀티 태스킹-multi tasking-이라고 함.
    + 이처럼 백그라운드 방식으로 처리되는 프로세스를 백그라운드 프로세스라고 하며, 명령의 실행 시간이 많이 걸릴 것으로 예상되거나 명령 실행 후 다른 작업을 수행해야 할 경우 사용.
    + 실행시키기 위해 뒤에 **&**를 붙여주어야 하고, 다른 명령어를 추가적으로 입력할 수 있음.
    + ***cf*** ) 백그라운드 방식으로 실행해도 사용자의 터미널 세션이 종료되면 실행 중인 프로세스도 종료됨. 이를 방지하기 위해 작업 시간이 오래 걸리는 작업인 경우 `nohup`명령어를 이용하여 백그라운드로 실행하면 사용자의 터미널 세션이 종료되어도 작업이 종료될 때까지 프로세스를 실행시킬 수 있음.


    
- *작업 환경 변경*
  - 포그라운드foreground > 백그라운드background : `fg %[작업번호]`
  - 백그라운드background > 포그라운드foreground : `ctrl+z`로 작업 일시중단 후, `bg %[작업번호]`
 
- *사용법(+옵션) : `jobs [option]`*
  + `-l` 프로세스 그룹 ID를 state 필드 앞에 출력.
  + `-n` 프로세스 그룹 중 대표 프로세스 ID를 출력.
  + `-p' 각 프로세스 ID에 대해 한 행씩 출력.
  + 'COMMAND` 지정한 명령어를 실행.
 
- *jobs로 출력되는 백그라운드background 작업의 상태값*
  - `Running` 작업 진행 중.
  - `Done` 정상 종료. 작업이 완료되어 0을 반환.
    + `Done(code)` 정상 종료. 0이 아닌 코드를 반환.
  - `Stopped` 일시 중단.
    + `Stopped(SIGTSTP)` SIGTSTP시그널이 작업을 일시 중단.
    + `Stopped(SIGSTOP)` SIGSTOP시그널이 작업을 일시 중단.
    + `Stopped(SIGTTIN)` SIGTTIN시그널이 작업을 일시 중단.
    + `Stopped(SIGTTOU)` SIGTTOU시그널이 작업을 일시 중단.
 
-[출처1](https://hbase.tistory.com/265), [출처2](https://imjeongwoo.tistory.com/71), [출처3](https://velog.io/@dnflekf2748/%EB%A6%AC%EB%88%85%EC%8A%A4-%EA%B8%B0%EC%B4%88-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%EA%B3%BC-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4)

**4. 리눅스 명령어 kill**

- *명령어 kill이란?*
  + 특정 프로세스에 작업 중지, 실행 종료, 대기, 재시작, 강제 종료 등의 시그널을 전달하는 명령어.
  + 사용하기 위해서는 먼저 종료하려는 프로세스의 PID(프로세스 아이디)알아야 함. 일반적으로 PS 명령어를 사용하여 현재 실행 중인 프로세스 목록을 확인한 후, 종료하려는 프로세스의 PID를 찾고 kill 명령어를 사용하여 해당 PID의 프로세스를 종료함.
-  *사용법(+옵션) : `kill [option]`
  + `kill -시그널번호(시그널명) %작업번호`
  + `kill -시그널번호(시그널명) PID`
  + `man kill` kill 명령어의 자세한 설명과 사용 가능한 옶션을 확인할 수 있는 명령어.

  + `-s <signal>` 특정 시그널을 사용하여 프로세스 종료. 기본적으로 SIGTERM 시그널 사용.
    + `SIGHUP` 재시작 시 사용.
    + `SIGNT` 실행 중지 시그널. `Ctrl+c`
    + `SIGKILL` 프로세스 강제 종료.
    + `SIGTERM` 프로세스 정상종료(기본 명령).
    + `SIGCONT` 정지된 프로세스 실행.
    + `SIGSTOP` 터미널에서 입력되는 정지 시그널.
    + `SIGTSTP` 실행 정지 후 재실행 대기. `Ctrl+z`
      
  + `-l` `--list` 지원되는 시그널 목록 출력.
  + `-a` `--all` 현재 사용자에 속한 모든 프로세스를 종료.
  + `-q` `--queue` 프로세스에 시그널을 바로 보내는 대신 대기열에 추가.
  + `kill -g <PID>` SIGKILL시그널을 사용하여 강제로 프로세스를 종료. 프로세스를 멈추는 가장 강력한 방법이지만, 프로세스가 올바르게 정리되지 않을 수 있고 데이터 손실이 발생할 수 있음.
  + `killall <프로세스명>` 특정 프로세스 이름을 가진 모든 프로세스를 종료.


- [출처1](https://gr-st-dev.tistory.com/210), [출처2](https://velog.io/@dnflekf2748/%EB%A6%AC%EB%88%85%EC%8A%A4-%EA%B8%B0%EC%B4%88-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%EA%B3%BC-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4)
    

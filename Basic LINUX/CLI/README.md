# LINUX CLI

## LINUX Structure
| 디렉터리  | 역할        | 쉽게 설명               |
| ----- | --------- | ------------------- |
| /     | 최상위 루트    | 모든 것의 시작            |
| /home | 사용자 폴더    | Windows의 `C:\Users` |
| /root | 관리자 홈     | root 전용 홈           |
| /bin  | 기본 실행파일   | ls, cp 같은 명령어       |
| /sbin | 관리자 명령어   | reboot, mount       |
| /etc  | 설정 파일     | 시스템 설정 모음           |
| /usr  | 프로그램 모음   | 대부분의 앱 설치 위치        |
| /var  | 자주 변하는 파일 | 로그, 캐시              |
| /tmp  | 임시 파일     | 재부팅하면 삭제됨           |
| /dev  | 장치 파일     | 하드디스크, USB          |
| /proc | 시스템 정보    | CPU, 메모리 정보         |
| /boot | 부팅 파일     | 커널, GRUB            |
| /opt | 추가 패키지 설치     | ROS            |

## LINUX Command
### File/Directory
| 명령어   | 옵션      | 예시                | 설명        |
| ----- | ------- | ----------------- | --------- |
| pwd   | -       | `pwd`             | 현재 위치 출력  |
| ls    | -l / -a | `ls -la`          | 파일 목록 보기  |
| cd    | 경로      | `cd folder`       | 디렉토리 이동   |
| cd    | -       | `cd ~`            | 홈 디렉토리 이동 |
| mkdir | -p      | `mkdir -p a/b`    | 폴더 생성     |
| touch | -       | `touch file.txt`  | 파일 생성     |
| rm    | -r / -f | `rm -rf folder`   | 파일/폴더 삭제  |
| cp    | -r      | `cp -r dir1 dir2` | 복사        |
| mv    | -       | `mv a.txt b.txt`  | 이동/이름변경   |


### Check File
| 명령어  | 옵션      | 예시                   | 설명           |
| ---- | ------- | -------------------- | ------------ |
| cat  | -       | `cat file.txt`       | 전체 출력        |
| less | -       | `less file.txt`      | 페이지 단위 보기    |
| head | -n      | `head -n 5 file.txt` | 앞부분 보기       |
| tail | -n / -f | `tail -f log.txt`    | 뒷부분 / 실시간 보기 |

*cat > file (overwrite) / cat >> file (add)

### Search
| 명령어  | 옵션    | 예시                    | 설명    |
| ---- | ----- | --------------------- | ----- |
| find | -name | `find . -name "*.py"` | 파일 검색 |
| grep | -r    | `grep -r "hello" .`   | 내용 검색 |


### Network
| 명령어  | 옵션        | 예시                           | 설명      |
| ---- | --------- | ---------------------------- | ------- |
| ssh  | user@host | `ssh user@server`            | 서버 접속   |
| scp  | -r        | `scp file user@server:/path` | 파일 전송   |
| ping | -         | `ping google.com`            | 네트워크 확인 |

### SystemStatus
| 명령어  | 옵션  | 예시          | 설명      |
| ---- | --- | ----------- | ------- |
| top  | -   | `top`       | CPU 사용량 |
| df   | -h  | `df -h`     | 디스크 용량  |
| du   | -sh | `du -sh *`  | 폴더별 용량  |
| free | -h  | `free -h`   | 메모리 확인  |
| ps   | aux | `ps aux`    | 프로세스 확인 |
| kill | PID | `kill 1234` | 프로세스 종료 |

### Permission
| 명령어   | 옵션         | 예시                         | 설명     |
| ----- | ---------- | -------------------------- | ------ |
| ls    | -l         | `ls -l`                    | 권한 보기  |
| chmod | 숫자         | `chmod 600 file`           | 권한 변경  |
| chown | user:group | `chown gidong:gidong file` | 소유자 변경 |

* chmod : owner - group - others ( 4:write, 2:read, 1 execute) chmod 755 filename
* +,- : add permisson, supprimer permission

### Others
| 명령어   | 설명     |
| ----- | ------ |
| /    | root 디렉토리    |
| ~    | home 디렉토리    |
| .    | 현재 디렉토리    |
|..    | 상위 디렉토리    |

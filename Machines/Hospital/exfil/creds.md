## credentials found on source code or scripts
```
mysql://root:my$qls3rv1c3!@localhost:3306/hospital
hospital\drbrown:chr!$br0wn
```

## mysql
```
MariaDB [hospital]> select * from users;
+----+-----------+--------------------------------------------------------------+---------------------+
| id | username  | password                                                     | created_at          |
+----+-----------+--------------------------------------------------------------+---------------------+
|  1 | admin     | $2y$10$caGIEbf9DBF7ddlByqCkrexkt0cPseJJ5FiVO1cnhG.3NLrxcjMh2 | 2023-09-21 14:46:04 |
|  2 | patient   | $2y$10$a.lNstD7JdiNYxEepKf1/OZ5EM5wngYrf.m5RxXCgSud7MVU6/tgO | 2023-09-21 15:35:11 |
|  3 | saps      | $2y$10$nlFUadyFpoQb/FbjE5Ojle/NC.Guvu5TebvhU9I7ImXuqSOf3ij.C | 2023-11-19 09:48:16 |
|  4 | yepian520 | $2y$10$VL/cbu2FvWs7UeA6wqOCluJwllV4fPsT9Ut1qvH7P0P.D6wn2fN4e | 2023-11-19 09:49:33 |
|  5 | gnos1s    | $2y$10$9i4ZoalEvJ.slqKdWcI1B.SKJgRWWYn1kfvabHOHYi88zjUwfKo6W | 2023-11-19 09:52:31 |
|  6 | yepian    | $2y$10$zbua51SnkONb4w7NrhbJfOjKRmH92ZLYGtkeb5a2UCp/ibr/G5Pvu | 2023-11-19 09:54:37 |
|  7 | offsec    | $2y$10$5VkZyntF4zvie2iOxnKDk.gsamsq2DvStdeecckxtHz4j4V4Mc8.G | 2023-11-19 09:55:14 |
|  8 | test      | $2y$10$IKNy/79vfLSwR48lnxPYmezX80y9J134YZ5RbAUD5RkZXl4h3Q7QW | 2023-11-19 10:00:57 |
|  9 | yutian    | $2y$10$oKXZ7xjSfMlznPo7VZztP..TD.J8TWv4a2DXpoq/UbK4G/vXHGtK6 | 2023-11-19 10:02:53 |
| 10 | inersin   | $2y$10$YS42vD2FVJRxYf7M0xqO7.QzTT91/lJ51xktvsT6vBjnA/.9g3oN6 | 2023-11-19 10:03:49 |
| 11 | something | $2y$10$y8LviR7tU9E/uE7YWWZUMOF/mONP2qCcB8IF88rbjSZzSMmqaD4mS | 2023-11-19 10:14:03 |
| 12 | rock      | $2y$10$Mh4ekQ2SQALrJRe39IzU7ubsMW7TrhETvZcGLwyL1YzP0g0/wDlf6 | 2023-11-19 10:16:25 |
| 13 | iluyepian | $2y$10$0j8aDxwZRTxOpr4qGq9uleyji3dBd1P7ySXxUzCLfmk3RClxIMcN. | 2023-11-19 11:30:35 |
| 14 | jacky     | $2y$10$u9mjrxuY/CjTya17Hp3pZuuhh6i6zmqcb01DUNo9Tabs/i6SAYt6y | 2023-11-19 11:34:12 |
| 15 | h1        | $2y$10$qxeKb9vMmDOaueFxATfP2.RGcHfAhcGRUPzTBbn6UTsDy.omwp5B6 | 2023-11-19 12:20:51 |
+----+-----------+--------------------------------------------------------------+---------------------+
```

## /etc/shadow
```
root:$y$j9T$s/Aqv48x449udndpLC6eC.$WUkrXgkW46N4xdpnhMoax7US.JgyJSeobZ1dzDs..dD:19612:0:99999:7:::
drwilliams:$6$uWBSeTcoXXTBRkiL$S9ipksJfiZuO4bFI6I9w/iItu5.Ohoz3dABeF6QWumGBspUW378P1tlwak7NqzouoRTbrz6Ag0qcyGQxW192y/:19612:0:99999:7:::
```

## cracked from john
```
admin:123456
drwilliams:qwe123!@#
```

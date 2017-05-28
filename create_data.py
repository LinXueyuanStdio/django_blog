#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
create some records for demo database
'''
 
from mysite.wsgi import *
from blog.models import Source, SourceClass
import blog.models as m
 
def main():
    data=[
        ("https://www.java.com/" ," 英文网址： https://www.java.com/","Java"), 
        ("http://spring.io/" ," 英文网址： http://spring.io/","Spring"), 
        ("http://www.programcreek.com/" ,"中文网址：http://www.programcreek.com/","ProgramCreek"),
        ("http://www.onjava.com/" ," 英文网址： http://www.onjava.com/","ONJava"),
        ("http://javaranch.com/" ," 英文网址： http://javaranch.com/","JavaRanch"), 
        ("https://dzone.com/" ," 英文网址： https://dzone.com/","DZone"),
        ("http://java-source.net/" ," 英文网址： http://java-source.net/","Java-Source"), 
        ("http://java2s.com/" ," 英文网址： http://java2s.com/","Java2s"), 
        ("http://www.mybatis.org" ," 英文网址： http://www.mybatis.org","MyBatis"),
        ("http://www.blogjava.net/" ,"中文网址：http://www.blogjava.net/","BlogJava"), 
        ("http://hibernate.org/" ," 英文网址： http://hibernate.org/","Hibernate"),
        ("http://www.importnew.com/" ,"中文网址：http://www.importnew.com/","ImportNew"),
        ("https://www.javacodegeeks.com/" ," 英文网址： https://www.javacodegeeks.com/","JavaCodeGeeks"), 
        ("http://www.cjsdn.net/" ,"中文网址：http://www.cjsdn.net/","中国Java开发网"), 
        ("http://www.java-cn.com/" ,"中文网址：http://www.java-cn.com/","JAVA中文站社区"),
        ("http://www.javaxxz.com/" ,"中文网址：http://www.javaxxz.com/","JAVA学习者论坛"), 
        ("http://www.java1234.com/" ,"中文网址：http://www.java1234.com/","Java知识分享网"), 
        ("http://www.journaldev.com/" ," 英文网址： http://www.journaldev.com/","JournalDev"),
        ("http://www.java234.com/" ,"中文网址：http://www.java234.com/","Java开发者社区"),
        ("http://www.java17.cn/" ,"中文网址：http://www.java17.cn/","JAVA论坛"), 
        ("http://www.javazhijia.com/" ,"中文网址：http://www.javazhijia.com/","Java之家"), 
        ("http://www.java123.net/" ,"中文网址：http://www.java123.net/","Java平台"), 
        ("http://www.52itstyle.com/" ,"中文网址：http://www.52itstyle.com/","科帮网"), 
        ("http://www.javazx.com/" ,"中文网址：http://www.javazx.com/","Java自学网"), 
        ("http://www.javaweb.cc/" ,"中文网址：http://www.javaweb.cc/","Java学习网"), 
        ("http://www.open-open.com/" ,"中文网址：http://www.open-open.com/","Java开源大全"),
        ("http://www.jguru.com/" ," 英文网址： http://www.jguru.com/","jGuru")
    ]

    dbdata=[
        ("https://www.mysql.com/"," 英文网址： https://www.mysql.com/","MySQL"),
        ("http://www.askoracle.org/","中文网址：http://www.askoracle.org/","Ask Oracle社区"),
        ("http://www.searchdatabase.com.cn/","中文网址：http://www.searchdatabase.com.cn/","TechTarget数据库"),
        ("http://www.db2china.net/","中文网址：http://www.db2china.net/","DB2中国社区"),
        ("http://www.580top.com/","中文网址：http://www.580top.com/","580top数据库"),
        ("http://www.dba-china.com/","中文网址：http://www.dba-china.com/","DBA China"),
        ("http://www.accessoft.com/","中文网址：http://www.accessoft.com/","access软件网"),
        ("http://www.dwway.com/","中文网址：http://www.dwway.com/","数据仓库之路"),
        ("http://www.csdb.cn/","中文网址：http://www.csdb.cn/","中国科学院数据云"),
        ("http://www.itpub.net/","中文网址：http://www.itpub.net/","ITPUB技术论坛"),
        ("http://www.raincent.com/","中文网址：http://www.raincent.com/","网络大数据"),
        ("https://www.oracle.com/"," 英文网址： https://www.oracle.com/","Oracle"),
        ("http://www.mysql.cn/","中文网址：http://www.mysql.cn/","中文MySQL.CN"),
        ("http://db-engines.com/en/"," 英文网址： http://db-engines.com/en/","DB-Engines")
    ]
    androiddata=[
        ("https://www.android.com/"," 英文网址： https://www.android.com/","Android"),
        ("https://developer.android.com/"," 英文网址： https://developer.android.com/","Android Developers"),
        ("http://www.eoeandroid.com/","中文网址：http://www.eoeandroid.com/","EOE移动开发者论坛"),
        ("http://www.androidchina.net/","中文网址：http://www.androidchina.net/","Android开发中文站"),
        ("http://www.android-studio.org/","中文网址：http://www.android-studio.org/","Android中文社区"),
        ("http://www.jdzhao.com/","中文网址：http://www.jdzhao.com/","Android学习手册"),
        ("http://www.android-study.com/","中文网址：http://www.android-study.com/","Android学习网"),
        ("http://www.androiddevtools.cn/","中文网址：http://www.androiddevtools.cn/","AndroidDevTools"),
        ("http://android-arsenal.com/"," 英文网址： http://android-arsenal.com/","Android Arsenal"),
        ("http://www.apkbus.com/","中文网址：http://www.apkbus.com/","APKBUS"),
        ("https://www.genymotion.com/"," 英文网址： https://www.genymotion.com/","Genymotion"),
        ("http://androidannotations.org/"," 英文网址： http://androidannotations.org/","AndroidAnnotations"),
        ("http://www.fresco-cn.org/","中文网址：http://www.fresco-cn.org/","Fresco"),
        ("https://realm.io/"," 英文网址： https://realm.io/","Realm"),
        ("http://www.androidbootstrap.com/"," 英文网址： http://www.androidbootstrap.com/","Android Bootstrap")
    ]
    phpdata=[
        ("http://www.php.net/"," 英文网址： http://www.php.net/","PHP"),
        ("http://windows.php.net/downloads/releases/archives/"," 英文网址： http://windows.php.net/downloads/releases/archives/","PHP-官方软件包"),
        ("https://www.drupal.org/"," 英文网址： https://www.drupal.org/","Drupal"),
        ("http://drupalchina.cn/","中文网址：http://drupalchina.cn/","Drupal中国"),
        ("http://www.golaravel.com/","中文网址：http://www.golaravel.com/","Laravel"),
        ("http://www.onethink.cn/","中文网址：http://www.onethink.cn/","OneThink"),
        ("http://codeigniter.org.cn/","中文网址：http://codeigniter.org.cn/","CodeIgniter"),
        ("http://www.php1.cn/","中文网址：http://www.php1.cn/","第一PHP社区"),
        ("http://www.yiichina.com/","中文网址：http://www.yiichina.com/","Yii Framework"),
        ("http://www.phpchina.com/","中文网址：http://www.phpchina.com/","PHP China"),
        ("http://www.php100.com/","中文网址：http://www.php100.com/","PHP100"),
        ("http://www.discuz.net/","中文网址：http://www.discuz.net/","Discuz"),
        ("http://cakephp.org/"," 英文网址： http://cakephp.org/","CakePHP"),
        ("http://www.zend.com/"," 英文网址： http://www.zend.com/","Zend"),
        ("http://symfony.com/"," 英文网址： http://symfony.com/","Symfony"),
        ("https://phalconphp.com/","中文网址：https://phalconphp.com/","Phalcon"),
        ("http://codeigniter.org.cn/","中文网址：http://codeigniter.org.cn/","CodeIgniter 中国"),
        ("http://www.dedecms.com/","中文网址：http://www.dedecms.com/","织梦CMS"),
        ("http://www.agavi.org/"," 英文网址： http://www.agavi.org/","Agavi"),
        ("https://nette.org"," 英文网址： https://nette.org","Nette Framework"),
        ("https://typo3.org/"," 英文网址： https://typo3.org/","TYPO3"),
        ("https://wordpress.org/"," 英文网址： https://wordpress.org/","WordPress"),
        ("http://auraphp.com/"," 英文网址： http://auraphp.com/","Aura"),
        ("http://kohanaframework.org/"," 英文网址： http://kohanaframework.org/","Kohana"),
        ("http://www.slimframework.com/"," 英文网址： http://www.slimframework.com/","Slim Framework"),
        ("http://www.canphp.com/","中文网址：http://www.canphp.com/","Canphp"),
        ("http://www.ecshop.com/","中文网址：http://www.ecshop.com/","ECShop"),
        ("http://kphp.org/","中文网址：http://kphp.org/","Kphp"),
        ("http://www.popphp.org/"," 英文网址： http://www.popphp.org/","Pop PHP"),
        ("http://www.initphp.com/","中文网址：http://www.initphp.com/","InitPHP框架"),
        ("http://www.speedphp.com","中文网址：http://www.speedphp.com","SpeedPHP"),
        ("http://www.smarty.net/"," 英文网址： http://www.smarty.net/","Smarty"),
        ("http://guzzlephp.org/"," 英文网址： http://guzzlephp.org/","Guzzle"),
        ("http://docs.behat.org/"," 英文网址： http://docs.behat.org/","Behat"),
        ("http://flightphp.com/"," 英文网址： http://flightphp.com/","Flight"),
        ("https://www.webasyst.com/"," 英文网址： https://www.webasyst.com/","Webasyst"),
        ("http://medoo.in/"," 英文网址： http://medoo.in/","Medoo"),
        ("https://phpixie.com/"," 英文网址： https://phpixie.com/","PHPixie"),
        ("http://www.thinkphp.cn/","中文网址：http://www.thinkphp.cn/","ThinkPHP"),
        ("http://www.workerman.net/","中文网址：http://www.workerman.net/","Workerman"),
        ("http://www.laoxue6699.cn/","中文网址：http://www.laoxue6699.cn/","老学"),
        ("http://fuelphp.com/"," 英文网址： http://fuelphp.com/","FuelPHP")
    ]
    foredata=[
        ("https://www.w3.org/"," 英文网址： https://www.w3.org/","W3C","官方网站"),
        ("http://www.runoob.com/","中文网址：http://www.runoob.com/","菜鸟教程","在线文档"),
        ("http://www.bootcss.com/","中文网址：http://www.bootcss.com/","Bootstrap","前端框架"),
        ("http://www.qdfuns.com/","中文网址：http://www.qdfuns.com/","前端网","综合社区"),
        ("https://jquery.com/"," 英文网址： https://jquery.com/","jQuery","JS框架"),
        ("http://960.gs/"," 英文网址： http://960.gs/","960 Grid System","CSS框架"),
        ("http://www.cssmoban.com/","中文网址：http://www.cssmoban.com/","模板之家","模板下载"),
        ("http://fontawesome.io/"," 英文网址： http://fontawesome.io/","Font Awesome","图片图标"),
        ("http://mobilehtml5.org/"," 英文网址： http://mobilehtml5.org/","HTML5 compatibility","兼容测试"),
        ("https://dribbble.com/"," 英文网址： https://dribbble.com/","Dribbble","UI设计"),
        ("http://www.sublimetext.com/"," 英文网址： http://www.sublimetext.com/","Sublime Text","开发工具")
    ]
    givendata=[
        ("http://www.csdn.net/","中文网址：http://www.csdn.net/","CSDN","综合社区"),
        ("http://www.cnblogs.com/","中文网址：http://www.cnblogs.com/","博客园","技术博客"),
        ("http://www.imooc.com/","中文网址：http://www.imooc.com/","慕课网","在线视频"),
        ("http://www.w3school.com.cn/","中文网址：http://www.w3school.com.cn/","W3school","在线文档"),
        ("https://github.com/"," 英文网址： https://github.com/","GitHub","项目管理"),
        ("http://stackoverflow.com/"," 英文网址： http://stackoverflow.com/","Stack Overflow","程序开发")
    ]
    mdata=[
        ("https://www.microsoft.com/"," 英文网址： https://www.microsoft.com/","Microsoft"),
        ("http://msdn.itellyou.cn/","中文网址：http://msdn.itellyou.cn/","MSDN, 我告诉你"),
        ("http://fireasy.cn/","中文网址：http://fireasy.cn/","帆易动力"),
        ("http://www.ccrun.com/","中文网址：http://www.ccrun.com/","C++Builder 研究"),
        ("http://www.learncpp.com/"," 英文网址： http://www.learncpp.com/","Learn C++"),
        ("http://www.codecogs.com/"," 英文网址： http://www.codecogs.com/","CodeCogs"),
        ("http://prglab.com/","中文网址：http://prglab.com/","程序员实验室"),
        ("http://www.cplusplus.com/"," 英文网址： http://www.cplusplus.com/","cplusplus"),
        ("http://c.biancheng.net/","中文网址：http://c.biancheng.net/","C语言中文网"),
        ("http://www.cppfans.com/","中文网址：http://www.cppfans.com/","C++爱好者"),
        ("http://www.cprogramming.com/"," 英文网址： http://www.cprogramming.com/","cprogramming"),
        ("http://www.51aspx.com/","中文网址：http://www.51aspx.com/","Asp.net源码站")
    ]
    serverdata=[
        ("https://www.kernel.org/"," 英文网址： https://www.kernel.org/","Linux Kernel"),
        ("http://cn.ubuntu.com/","中文网址：http://cn.ubuntu.com/","Ubuntu中国官网"),
        ("http://www.linuxidc.com/","中文网址：http://www.linuxidc.com/","Linux公社"),
        ("http://linux.vbird.org/","中文网址：http://linux.vbird.org/","鳥哥的 Linux 私房菜"),
        ("http://www.linuxde.net/"," 英文网址： http://www.linuxde.net/","Linux Today"),
        ("http://www.centoscn.com/","中文网址：http://www.centoscn.com/","CentOS中文站"),
        ("https://www.centos.org/"," 英文网址： https://www.centos.org/","CentOS"),
        ("https://linux.cn/","中文网址：https://linux.cn/","Linux.中国"),
        ("http://www.server110.com/","中文网址：http://www.server110.com/","服务器之家"),
        ("http://www.linuxdiyf.com/","中文网址：http://www.linuxdiyf.com/","红联Linux门户"),
        ("http://www.linuxdown.net/","中文网址：http://www.linuxdown.net/","Linux下载站"),
        ("https://www.linuxmint.com/"," 英文网址： https://www.linuxmint.com/","Linux Mint"),
        ("http://www.debian.org/","中文网址：http://www.debian.org/","Debian"),
        ("https://getfedora.org/"," 英文网址： https://getfedora.org/","Fedora"),
        ("http://www.mageia.org/","中文网址：http://www.mageia.org/","Mageia"),
        ("https://www.archlinux.org/"," 英文网址： https://www.archlinux.org/","Arch Linux"),
        ("http://puppylinux.com/"," 英文网址： http://puppylinux.com/","Puppy Linux"),
        ("https://www.deepin.org/","中文网址：https://www.deepin.org/","深度操作系统"),
        ("http://www.freebsd.org/","中文网址：http://www.freebsd.org/","FreeBSD"),
        ("https://www.gentoo.org/"," 英文网址： https://www.gentoo.org/","Gentoo Linux"),
        ("https://coreos.com/"," 英文网址： https://coreos.com/","CoreOS"),
        ("https://www.linuxliteos.com/"," 英文网址： https://www.linuxliteos.com/","Linux Lite"),
        ("https://www.clearos.com/"," 英文网址： https://www.clearos.com/","ClearOS"),
        ("http://www.pclinuxos.com/"," 英文网址： http://www.pclinuxos.com/","PCLinuxOS"),
        ("http://ubuntustudio.org/","中文网址：http://ubuntustudio.org/","Ubuntu Studio"),
        ("http://www.chinaunix.net/","中文网址：http://www.chinaunix.net/","Unix技术网"),
        ("http://www.linuxeden.com/","中文网址：http://www.linuxeden.com/","Linux伊甸园"),
        ("http://linux.chinaunix.net/","中文网址：http://linux.chinaunix.net/","Linux时代"),
        ("http://www.cnubuntu.com/","中文网址：http://www.cnubuntu.com/","Ubuntu中文站"),
        ("http://www.linuxeye.com/","中文网址：http://www.linuxeye.com/","LinuxEye"),
        ("http://www.kylinos.cn/","中文网址：http://www.kylinos.cn/","银河麒麟"),
        ("http://www.cncentos.com/","中文网址：http://www.cncentos.com/","CentOS中文论坛")
    ]
    appledata=[
        ("http://www.apple.com/"," 英文网址： http://www.apple.com/","Apple"),
        ("http://www.cocoachina.com/","中文网址：http://www.cocoachina.com/","CocoaChina"),
        ("http://www.codeios.com/","中文网址：http://www.codeios.com/","iOS开发者"),
        ("https://www.objc.io/"," 英文网址： https://www.objc.io/","objc.io"),
        ("http://nshipster.com/","中文网址：http://nshipster.com/","NSHipster"),
        ("http://nshipster.cn/","中文网址：http://nshipster.cn/","NSHipster中文版"),
        ("http://petersteinberger.com/"," 英文网址： http://petersteinberger.com/","Peter Steinberger"),
        ("http://oleb.net/"," 英文网址： http://oleb.net/","Ole Begemann"),
        ("https://www.mikeash.com/"," 英文网址： https://www.mikeash.com/","mikeash"),
        ("https://designthencode.com/"," 英文网址： https://designthencode.com/","Design Then Code"),
        ("https://objccn.io/","中文网址：https://objccn.io/","ObjC 中国"),
        ("http://www.mac52ipod.cn/","中文网址：http://www.mac52ipod.cn/","苹果fans博客"),
        ("http://www.devdiv.com/","中文网址：http://www.devdiv.com/","DevDiv"),
        ("http://dev.iphonetw.net/","中文网址：http://dev.iphonetw.net/","iDevTW"),
        ("http://www.iliunian.com/","中文网址：http://www.iliunian.com/","ios 移动"),
        ("http://letsswift.com/","中文网址：http://letsswift.com/","Let us Swift"),
        ("http://www.swiftv.cn/","中文网址：http://www.swiftv.cn/","SwiftV课堂"),
        ("http://www.lanrenios.com/","中文网址：http://www.lanrenios.com/","懒人ios代码库"),
        ("http://www.iosappx.com/","中文网址：http://www.iosappx.com/","苹果iOS开发者联盟"),
        ("https://maniacdev.com/"," 英文网址： https://maniacdev.com/","iOS App"),
        ("https://iosdev.tools/"," 英文网址： https://iosdev.tools/","iOS Dev Tools"),
        ("http://iosdevelopertips.com/"," 英文网址： http://iosdevelopertips.com/","iOSDeveloperTips"),
        ("http://code4app.com/","中文网址：http://code4app.com/","Code4App")
    ]
    otherdata=[
        ("http://mirrors.sohu.com/"," 英文网址： http://mirrors.sohu.com/","搜狐-软件包"),
        ("http://www.verysource.com/","中文网址：http://www.verysource.com/","VerySource 非常源码"),
        ("http://www.51cto.com/","中文网址：http://www.51cto.com/","51CTO"),
        ("http://www.jb51.net/","中文网址：http://www.jb51.net/","脚本之家"),
        ("http://www.oschina.net/","中文网址：http://www.oschina.net/","开源中国"),
        ("http://www.iteye.com/","中文网址：http://www.iteye.com/","ITeye"),
        ("https://segmentfault.com/","中文网址：https://segmentfault.com/","SegmentFault"),
        ("http://www.tutorialspoint.com/"," 英文网址： http://www.tutorialspoint.com/","Tutorials"),
        ("http://www.lemonapp.tk","中文网址：http://www.lemonapp.tk","Twilight博客"),
        ("http://www.mycodes.net/","中文网址：http://www.mycodes.net/","源码之家"),
        ("http://www.tiobe.com/"," 英文网址： http://www.tiobe.com/","TIOBE")
    ]
    baiduyundata=[
        ("http://pan.baidu.com/s/1bFhyaU","Android开发快速入门60个源代码案例","q053","2017-01-18"),
        ("http://pan.baidu.com/s/1boPVdzL","jQuery基础视频教程（400M）","kskh","2017-01-18"),
        ("http://pan.baidu.com/s/1o7CHzzs","CSS3开发视频教程（2GB）","z9y7","2017-01-18"),
        ("http://pan.baidu.com/s/1jIhrLn4","EasyUI入门视频教程（4GB）","qx4y","2017-01-18"),
        ("http://pan.baidu.com/s/1i5Hl7oh","老男孩python开发基础8期（20GB）","5mpg","2017-01-18"),
        ("http://pan.baidu.com/s/1i5E3KzF","LAMP_李捷_Redis视频教程（700M）","ogpj","2017-01-18"),
        ("http://pan.baidu.com/s/1sl2IePf","孙鑫C++开发视频教程（4GB）","x4nj","2017-01-18"),
        ("http://pan.baidu.com/s/1eSr9nj0","C#高级教程包含源码视频PPT(3GB)","dl57","2017-01-18"),
        ("http://pan.baidu.com/s/1hr74bEs","韩顺平linux开发视频教程（2GB）","w4dr","2017-01-18"),
        ("http://pan.baidu.com/s/1nuSs9uh","Python开发视频汇总（35GB）","7d23","2017-01-18"),
        ("http://pan.baidu.com/s/1bProse","Oracle开发视频（3GB）","bnkk","2017-01-18"),
        ("http://pan.baidu.com/s/1qX89Buk","iOS开发视频_无线互联（2GB）","z8sc","2017-01-18"),
        ("http://pan.baidu.com/s/1nuIPmxN","linux_路由开发技术视频（3GB）","wtzf","2017-01-18"),
        ("http://pan.baidu.com/s/1eS7OwZS","Linux_C语言编程入门（5GB）","x8o1","2017-01-18"),
        ("http://pan.baidu.com/s/1nvO4Z4t","Linux学习视频_源码_PDF（3GB）","ln4s","2017-01-18"),
        ("http://pan.baidu.com/s/1hs5czVe","PHP从入门到精通_韩顺平（20GB）","4ddw","2017-01-18"),
        ("http://pan.baidu.com/s/1dFMJ2q1","Cocos2dx游戏开发工程师（6GB）","nrjb","2017-01-18"),
        ("http://pan.baidu.com/s/1nvLhrLJ","Ruby电子书汇总（喜欢就去买正版）","fp9k","2017-01-18"),
        ("http://pan.baidu.com/s/1pKN4OOV","Ruby基础开发视频（280M）","s9ll","2017-01-18"),
        ("http://pan.baidu.com/s/1hrW6E12","郝斌Java开发视频1-107个（4GB）","92rw","2017-01-18"),
        ("http://pan.baidu.com/s/1o88UgHW","马哥linux全套视频教程（5GB）","4umu","2017-01-18"),
        ("http://pan.baidu.com/s/1nu7ZXC9","零基础1小时建站教程（1GB）","kcxm","2017-01-18"),
        ("http://pan.baidu.com/s/1dF42O4T","传智播客2014年Java完整版（70GB）","esid","2017-01-18"),
        ("http://pan.baidu.com/s/1kVyQQCv","Java基础入门视频教程（2GB）","m6jg","2017-01-18"),
        ("http://pan.baidu.com/s/1o8tvjOA","吴超hadoop视频初中高级全套（5GB）","9pwa","2017-01-18"),
        ("http://pan.baidu.com/s/1dFf0uf3","C#视频教程合集(总计111课程文件)","8rgv","2017-01-18"),
        ("http://pan.baidu.com/s/1i4GVAV7","Android开发视频教程大全（4GB）","v4q3","2017-01-18"),
        ("http://pan.baidu.com/s/1bLTC8u","HTML5入门视频教程（400M）","bp47","2017-01-18"),
        ("http://pan.baidu.com/s/1skJxjrv","Bootstrap基础视频教程（200M）","9mti","2017-01-18"),
        ("http://pan.baidu.com/s/1qXDZ7ZY","EasyUI入门视频教程（2GB）","n7qk","2017-01-18"),
        ("http://pan.baidu.com/s/1qYQ0XOC","JavaWeb高级视频教程（7GB）","dxuz","2017-01-18"),
        ("http://pan.baidu.com/s/1qYyGGZq","Java基础入门视频汇总（8GB）","bw0t","2017-01-18"),
        ("http://pan.baidu.com/s/1bp3Ram7","C#开发27本PDF（喜欢就去买正版）","iky2","2017-01-18"),
        ("http://pan.baidu.com/s/1i5JTMwH","Java开发PDF汇总（喜欢就去买正版）","3ifl","2017-01-18"),
        ("http://pan.baidu.com/s/1nvS9hNj","数据库PDF汇总（喜欢就去买正版）","uvdr","2017-01-18"),
        ("http://pan.baidu.com/s/1eRCYg2A","设计模式文档汇总（喜欢就去买正版）","hvcc","2017-01-18"),
        ("http://pan.baidu.com/s/1slTMSs1","韩顺平_Java三大框架开发全套（20G）","o11q","2017-01-18")
    ]
    #m.Source.objects.all().delete()
    c = SourceClass.objects.get_or_create(src_class='百度云资源')[0]

    # 创建 10 篇新闻
    for srcurl,srctitle,secret,time in baiduyundata:
        source = Source.objects.get_or_create(
            src_class = c,
            src_title=srctitle,
            src_url=srcurl,
            src_hint=srcurl,
            src_marks=secret
        )[0]

 
if __name__ == '__main__':
    main()
    print("Done!")
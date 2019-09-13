${error} = 0;
$LastExitCode = 1;

& python c:/Users/ege.okumus/Desktop/test/MyTest.py 1 2>&1 >InternetExplorerTestReult.txt

if($LastExitCode -eq '1'){
${error}=1;

}

& python c:/Users/ege.okumus/Desktop/test/MyTest.py 2 2>&1 >GoogleChromeTestResult.txt

if($LastExitCode -eq '1'){
${error}=2;

}

& python c:/Users/ege.okumus/Desktop/test/MyTest.py 3 2>&1 >FirefoxTestResult.txt

if($LastExitCode -eq '1'){
${error}=3;

}

& python c:/Users/ege.okumus/Desktop/test/MyTest.py 4 2>&1 >SafariTestResult.txt

if($LastExitCode -eq '1'){
${error}=4;

}

if(${error} -eq '1'){


  
} 


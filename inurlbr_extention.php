<?php
class SQLDB extends SQLite3 {

	function __construct(){
		$this->database = 'output/PWR_inurl_DB.sqlite3';
		$this->open($this->database);
		$this->Backup = $this->GetBackupSql();
		$this->Install_DB_Schema();

	}

	function Install_DB_Schema(){
		foreach($this->Backup as $CommandToInstall){
			$this->query($CommandToInstall);
		}
		foreach($this->GetEngines() as $id => $engine){
			$this->query('INSERT INTO SearchEngines(id,engine) VALUES ("'.$id.'","'.$engine.'");');
		}
	}

	function ToDB($columns,$data,$tablename){
		#ToDB('ip,ports,raw_loot,script','"82.75.163.96","80:5900:666:777","sdfgfgsdgfsdg"','dig');
		$this->InsertQ = "Insert into ".$tablename." (".$columns.") VALUES (".$data.");";
		echo "Inserted in to SQLite-DB : ".$this->database;
		return $this->InsertQ;	
	}

	function GetBackupSql(){
		return $backup =explode(';',"
			BEGIN TRANSACTION;
			CREATE TABLE IF NOT EXISTS `used-dork-log` (
				`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
				`dork`	TEXT UNIQUE,
				`engine`	TEXT,
				`count`	INTEGER
			);
			CREATE TABLE IF NOT EXISTS `ext-com-log` (
				`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
				`command`	TEXT UNIQUE,
				`target`	TEXT,
				`count`	INT ( 100 )
			);
			CREATE TABLE IF NOT EXISTS `SearchEngines` (
				`id`	TEXT,
				`engine`	TEXT UNIQUE,
				`rank`	INTEGER,
				`usage_count`	INTEGER,
				PRIMARY KEY(`id`)
			);
			CREATE TABLE IF NOT EXISTS `BigDump` (
				`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
				`ip`	TEXT UNIQUE,
				`ports`	TEXT,
				`raw_loot`	TEXT,
				`script`	TEXT,
				`www`	TEXT
			);
			COMMIT;
			");
	}
	
	function GetEngines(){
		return array("1"=>"GOOGLE1","2"=>"BING","3"=>"YAHOO1","4"=>"ASK","5"=>"HAO123","6"=>"GOOGLE2","7"=>"LYCOS","8"=>"UOL","9"=>"YAHOO2","10"=>"SAPO","11"=>"DMOZ","12"=>"GIGABLAST","13"=>"NEVER","14"=>"BAIDU","15"=>"YANDEX","16"=>"ZOO","17"=>"HOTBOT","18"=>"ZHONGSOU","19"=>"HKSEARCH","20"=>"EZILION","21"=>"SOGOU","22"=>"DUCK","23"=>"BOOROW","24"=>"GOOGLE3","e1"=>"TOR FIND","e2"=>"ELEPHANT","e3"=>"TORSEARCH","e4"=>"WIKILEAKS","e5"=>"OTN","e6"=>"EXPLOITS");
	}

}



$commandolijstje = array('columns:','data:','tablename:');
$opties = getopt('h::', $commandolijstje);
var_dump($opties);
if($opties['tablename'] != '' ){
	$T = new SQLDB();
	$T->query($T->ToDB($opties['columns'],$opties['data'],$opties['tablename']));	
}  
//  ./inurlbr_extention.php --columns 'ip,raw_loot,script,www' --'"82.75.163.96","sdfgfgsdgfsdg","www.test.nl"' --tablename 'BigDump'
//	./inurlbr.php -s scan20180318.lst --dork-file '/root/stuff/tools/PWR_inurl/Dorks/sqli_dorks.lst' --tor-random --exploit-get "'0x27%27" --exploit-vul-id 1,2,3,5,15,14,11 --custom-config K00B404.conf -q 1,2,3,4,5,6 --mp 10 --blacklist '.fleurlis.,.katun.'

// php ./inurlbr_extention.php --columns "ip,ports,raw_data,script" --data "12.33.24.63,80:8080,wegergrtwokvcozxcozaqa,inurlbr" --tablename "inurlbr"
// function Log_Used_Dorks($dork,$engine){

//   	error_reporting(0);
//  	//echo $dork;
//   	$count=1;
// 	if($dork != ''){
// 	  $db = new SQLDB();
// 	  //echo "SELECT `count` FROM `used-dork-log` WHERE `dork` = '".$dork."';";
// 	  $checkrow = $db->query("SELECT `count` FROM `used-dork-log` WHERE `dork` = '".$dork."';")->fetchArray(SQLITE3_ASSOC);
// 	  //var_dump($checkrow);
// 	  if(!$checkrow){
// 	    $db->query('INSERT INTO `used-dork-log` (`dork`,`engine`,`count`) VALUES ("'.$dork.'","'.$engine.'","'.$count.'");');  
// 	  }else{
// 	    $count = $count + $checkrow['count'];
// 	    $db->query('UPDATE `used-dork-log`  SET `count` = "'.$count.'" WHERE `dork` = "'.$dork.'";');  
// 	  }
// 	}else{die('empty dork');}

//   error_reporting(0);    
// }

// function DB_Log_ext_command($com,$out){
// 	error_reporting(0);
// 	//echo $com;
// 	$count=1;
// 	$db = new SQLDB();
// 	//echo 'SELECT `count` FROM `ext-com-log` WHERE `command` = "'.$com.'";';
// 	$checkrow = $db->query("SELECT `count` FROM `ext-com-log` WHERE `command` = '".htmlspecialchars($com)."';")->fetchArray(SQLITE3_ASSOC);
// 	//var_dump($checkrow);
// 	if(!$checkrow){
// 	$db->query('INSERT INTO `ext-com-log`(`command`,`output`,`count`) VALUES ("'.htmlspecialchars($com).'","'.$out.'","'.$count.'");');  
// 	}else{
// 	$count = $count + $checkrow['count'];
// 	$db->query('UPDATE `ext-com-log` SET `count` = "'.$count.'" WHERE `command` = "'.htmlspecialchars($com).'";');  
// 	}

// 	error_reporting(0);

// 	}

?>
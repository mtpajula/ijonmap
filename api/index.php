<?php

//error_reporting(E_ALL);
//ini_set('display_errors', '1');

//Define our id-key pairs
$applications = array(
	'000' => '000',
);
//include our models
//include_once 'models/Item.php';

//wrap the whole thing in a try-catch block to catch any wayward exceptions!
try {
	//*UPDATED*
	//get the encrypted request
	//$enc_request = $_REQUEST['enc_request'];
	
	//get the provided app id
	$app_id = $_REQUEST['app_id'];
    
	//check first if the app id exists in the list of applications
	if( !isset($applications[$app_id]) ) {
		throw new Exception('Application does not exist!');
	}
	
	//decrypt the request
	//$params = json_decode(trim(mcrypt_decrypt( MCRYPT_RIJNDAEL_256, $applications[$app_id], base64_decode($enc_request), MCRYPT_MODE_ECB )));
	
    $params = $_REQUEST;
    
	//check if the request is valid by checking if it's an array and looking for the controller and action
    /*
    if( $params == false || isset($params->controller) == false || isset($params->action) == false ) {
		throw new Exception('Request is not valid');
	}
    */
	
	//cast it into an array
	//$params = (array) $params;
	
	//get the controller and format it correctly so the first
	//letter is always capitalized
	$controller = ucfirst(strtolower($params['controller']));
	
	//get the action and format it correctly so all the
	//letters are not capitalized, and append 'Action'
	$action = strtolower($params['action']).'Action';

	//check if the controller exists. if not, throw an exception
	if( file_exists("controllers/{$controller}.php") ) {
		include_once "controllers/{$controller}.php";
	} else {
		throw new Exception('Controller is invalid.');
	}
	
	//create a new instance of the controller, and pass
	//it the parameters from the request
	$controller = new $controller($params);
	
	//check if the action exists in the controller. if not, throw an exception.
	if( method_exists($controller, $action) === false ) {
		throw new Exception('Action is invalid.');
	}
	
	//execute the action
	$result['data'] = $controller->$action();
	$result['success'] = true;
	
} catch( Exception $e ) {
	//catch any exceptions and report the problem
	$result = array();
	$result['success'] = false;
	$result['errormsg'] = $e->getMessage();
}

//echo the result of the API call
echo json_encode($result);
exit();

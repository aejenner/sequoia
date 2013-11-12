<?php

include_once "model.php";
include_once "view.php";
include_once "controller.php";

class Controller {

  public $model;
  public $view;
  public $controller;

  function __construct() {
    $this->controller = $this;
  }

  //take a request from GET in JSON and make into an instance of request
  function receiveRequest($requestAsJSON) {
    //FIXME
  }

  //switch on $request.type and call various handlers
  function handleRequest($request) {
    //FIXME
  }

  //handlers

}

class Request {
  //can't be bothered to make vars private
  public $type; //type of request
  public $uid; //user id
  public $auth; //some kind of authentication gibberish
  //anything else needed?
}

?>

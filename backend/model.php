<?php

include_once "model.php";
include_once "view.php";
include_once "controller.php";

//this syntax should look familiar!
class Model {

  public $model;
  public $view;
  public $controller;

  private $database;

  function __construct($db_server, $db, $db_username, $db_pass) {
    $this->model = $this;
    //FIXME open database connection
  }

  function __destruct() {
    //FIXME close database conenction
  }

function doThing($param) {
  return "idk";
}

}

?>


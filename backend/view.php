<?

include_once "model.php";
include_once "view.php";
include_once "controller.php";

class View {

  public $model;
  public $view;
  public $controller;

  function __construct() {
    $this->view = $this;
  }

}

//TODO implement a class for output data

?>

<?php

include_once "model.php";
include_once "view.php";
include_once "controller.php";

//think of this as main()
$m = new Model("server", "database", "user", "pass");
$v = new View();
$c = new Controller();

$m->view = $v;
$m->controller = $c;
$v->model = $m;
$v->controller = $c;
$c->model = $m;
$c->view = $v;

//TODO FIXME send get request to controller

//REMOVE FIXME
phpinfo(); //just outputting SOMETHING so we can see it working

?>

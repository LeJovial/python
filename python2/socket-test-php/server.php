<?php
$threadsClients = [];

function instanceServeur($client, $infosClient) {
    $adresseIP = $infosClient[0];
    $port = $infosClient[1];
    echo "Instance de serveur prêt pour $adresseIP:$port\n";
    $message = "";
    while (strtoupper($message) !== "FIN") {
        $message = socket_read($client, 255, PHP_BINARY_READ);
        echo "Message reçu du client $adresseIP:$port : $message\n";
        socket_write($client, "Message reçu", strlen("Message reçu"));
    }
    echo "Connexion fermée avec $adresseIP:$port\n";
    socket_close($client);
}

$serveur = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_bind($serveur, '0.0.0.0', 50000);
socket_listen($serveur, 5);

while (true) {
    $client = socket_accept($serveur);
    socket_getpeername($client, $adresseIP, $port);
    $infosClient = [$adresseIP, $port];
    $threadsClients[] = new Thread('instanceServeur', $client, $infosClient);
}
socket_close($serveur);

class Thread extends Threaded {
    private $callback;
    private $args;

    public function __construct($callback, ...$args) {
        $this->callback = $callback;
        $this->args = $args;
    }
    public function run() {
        call_user_func_array($this->callback, $this->args);
    }
}
?>
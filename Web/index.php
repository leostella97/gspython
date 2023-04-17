<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Gerador de Senhas</title>
</head>
<body>
	<div>
	<h1>Gerador de Senhas</h1>
	<form action="" method="post">
		Tamanho da senha: <input type="number" name="tamanho" min="1" max="100"><br><br>
		<input type="submit" value="Gerar Senha">
	</form>
	<br>
	<?php
		if ($_SERVER["REQUEST_METHOD"] == "POST") {
			$tamanho = $_POST["tamanho"];
			$senha = shell_exec("python gerador_de_senhas.py $tamanho");
			// var_dump($senha);
			echo "Senha gerada: $senha";
		}
	?>
<br><br><br>
<footer>
	<a target="_blank" href="https://leonardostella.lesttech.com.br/">Desenvolvido por Leonardo Stella</a>
</footer>
</div>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
</body>
</html>


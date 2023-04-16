<!DOCTYPE html>
<html>
<head>
	<title>Gerador de Senhas</title>
</head>
<body>
	<h1>Gerador de Senhas</h1>
	<form action="" method="post">
		Tamanho da senha: <input type="number" name="tamanho" min="1" max="100"><br><br>
		<input type="submit" value="Gerar Senha">
	</form>
	<br>
	<?php
		if ($_SERVER["REQUEST_METHOD"] == "POST") {
			$tamanho = $_POST["tamanho"];
			$senha = exec("python3 gerador_de_senhas.py $tamanho");
			echo "Senha gerada: $senha";
		}
	?>
</body>
</html>

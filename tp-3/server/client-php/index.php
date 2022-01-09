<html>
    <head>
        <title>IAO</title>
    </head>

    <body>
        <h1>Docker - IAO</h1>

        <ul>
            <?php
                $json = file_get_contents('http://back-end:8000/api/v1/products/');
                $products = json_decode($json);

                echo"<table border='1' cellspacing='0' colspacing='0' width='50%'>";
                echo "
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Qty</th>
                        <th>Created at</th>
                    </tr>
                ";

                foreach($products as $product){
                    //echo "<li>$product->name --- $product->description --- $product->qty --- <i>$product->get_created_at</i> </li><br>";
                    echo "
                    <tr>
                        <td>$product->id</td>
                        <td>$product->name </td>
                        <td>$product->description</td>
                        <td>$product->qty</td>
                        <td>$product->get_created_at</td>
                    </tr>
                ";
                }
                echo "</table>";

            ?>
        </ul>
    </body>
</html>
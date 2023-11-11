<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* div ke ander jitne bhi p hoge na unko apply hota hai ye  */
        /* div p{
            color:white;
            background-color:black
        } */

        /* div ke imidate aur div ke ander ke p ko apply hota hai   */
        /* div > p{
            color:white;
            background-color:black
        } */

        /* table ke ander ka the ko apply hoga ye wali css  */
        /* div table tr > th {
            color:white;
            background-color:black;
            border: 1px solid black;
        } */

        /* jis p tag ke upper div hoga usko wo apply hogi css  */
        div + p{
            color:white;
            background-color:black
        }
    </style>
</head>
    <title>Advanced selector in css </title>
<body>
    <div class="container">
        <div class="item">
            <table>
                <tr>
                    <th>Name</th>
                </tr>
                <tr>
                    <td>Vishal </td>
                </tr>
            </table>
            <p>This is table sibling</p>
        </div>
        <p>This is item paragrah</p>
    </div>
    <p>This is outer paragrah </p>
</body>
</html>
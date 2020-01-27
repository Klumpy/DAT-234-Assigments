function decrypt-char($a){
    $number = [int][char]$a
    # decrement by 1 to decrypt
    $number=$number-1;
    return [char]$number
}

function encrypt-char($a){
    $number = [int][char]$a
    # increment by 1 to encrypt
    $number=$number+1;
    return [char]$number
}


function decrypt-message($string){
    #Convert string to array of chars
    $array = $string.ToCharArray()
    $decrypted = @(0) * $array.length

    #iterate over every char in string
    for($i = 0; $i -lt $array.length; $i++){
        #decrypt char
        $decrypted[$i] = decrypt-char($array[$i])
    }

    echo "Message: $decrypted"
}

function encrypt-message($string){
    #Convert string to array of chars
    $array = $string.ToCharArray()
    $encrypted = @(0) * $array.length

    #iterate over every char in string
    for($i = 0; $i -lt $array.length; $i++){
        #encrypt char
        $encrypted[$i] = encrypt-char($array[$i])
    }

    echo "Message: $encrypted"
}


#Lagde en sterkere encryption ved å bruke en enkel XOR
#og en "key" den sammenligner med.
function encrypt_strong($plaintext, $key){
    
    $byteArray = [System.Text.Encoding]::ASCII.GetBytes($plaintext)
    $KeyArray = [System.Text.Encoding]::ASCII.GetBytes($key)
    $cypherArray = @(0) * $byteArray.length

    $keyposition = 0
    for($i = 0; $i -lt $byteArray.length; $i++){
        
        # XOR cypher med key
        $cypherArray[$i] = [byte]($byteArray[$i] -bxor $KeyArray[$keyposition])

        $keyposition = $keyposition+1;
        if ($keyposition -eq $key.Length) {
            $keyposition = 0;
        }
    }
    echo "$cypherArray"
}

function decrypt_strong($byteArray, $key){
    $KeyArray = [System.Text.Encoding]::ASCII.GetBytes($key)
    $cypherArray = @(0) * $byteArray.length

    $keyposition = 0
    for($i = 0; $i -lt $byteArray.length; $i++){
        
        # XOR cypher med key
        $cypherArray[$i] = [byte]($byteArray[$i] -bxor $KeyArray[$keyposition])

        $keyposition = $keyposition+1;
        if ($keyposition -eq $key.Length) {
            $keyposition = 0;
        }
    }
    
    #Gjøres om tilbake til "Char"
    $charArray = @(0) * $cypherArray.length
    for($j = 0; $j -lt $cypherArray.length; $j++){
        $charArray[$j] = ([char]$cypherArray[$j])
    }
    echo "$charArray"
}


function selectTask{
    $task=Read-Host "1 = decrypt predefined message`n2 = encrypt`n3 = decrypt`n4 = encrypt strong`n5 = decrypt strong`n"
    if($task -eq 1){
    $message = "Lfzcpbse!opu!gpvoe/!Qsftt!G2!up!dpoujovf"
    decrypt-message $message
    }
    elseif($task -eq 2){
    $encryptMessage=Read-Host "Enter message to encrypt: "
    encrypt-message $encryptMessage
    }
    elseif($task -eq 3){
    $decryptMessage=Read-Host "Enter message to decrypt: "
    decrypt-message $decryptessage
    } 
    elseif($task -eq 4){
    $encryptStrong=Read-Host "Enter message to strongly encrypt: "
    $key = Read-Host "Enter key: "
    encrypt_strong $encryptStrong $key
    } 
    elseif($task -eq 5){
    $decryptStrong=Read-Host "Enter message to strongly decrypt: "
    $key = Read-Host "Enter key: "
    $decryptStrongArray = $decryptStrong -split ' '
    decrypt_strong $decryptStrongArray $key
    } else { echo "Bad number" }
}

selectTask
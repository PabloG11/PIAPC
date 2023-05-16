try{
	  # Script de PowerShell que obtiene información basica de un equipo

        # lo guarda en un archivo csv

        # Posteriormente envia ese archivo a través de correo electronico

        # usando una cuenta de gmail.


        $computer = hostname

        $query = Get-WmiObject -Class win32_computersystem -ComputerName $computer

        $name = $query.Name

        $make = $query.Manufacturer

        $model = $query.Model

        $ram = $query.TotalPhysicalMemory/1Gb

        $os = (Get-WmiObject -Class win32_operatingsystem -ComputerName $computer).Caption

        $cpu = (Get-WmiObject -Class Win32_processor -ComputerName $computer).Name

        $users = $query.Username

        #

        # Llenando array para generación de csv

        #

        $Object = New-Object PSObject

        $Object | Add-Member -MemberType NoteProperty -Name "ComputerName" -Value $name

        $Object | Add-Member -MemberType NoteProperty -Name "Make" -Value $make

        $Object | Add-Member -MemberType NoteProperty -Name "Model" -Value $model

        $Object | Add-Member -MemberType NoteProperty -Name "RAM" -Value $ram

        $Object | Add-Member -MemberType NoteProperty -Name "OS" -Value $os

        $Object | Add-Member -MemberType NoteProperty -Name "CPU" -Value $cpu

        $Object | Add-Member -MemberType NoteProperty -Name "LoggedOnUsers" -Value $users

        $array = $Object

        $array | Export-Csv -Path C:\Users\******\Desktop\******\test.csv -NoTypeInformation # Aqui se genera archivo csv

        #

        # Para Envio de correo

        #

        $Username = "******@gmail.com"; # Aqui va tu cuenta de gmail

        $Password = "******";      # Aqui va tu password de aplicación

        $path = "C:\Users\******\Desktop\******\test.csv";       # Aqui va la ruta de el archivo csv generado previamente



        function Send-ToEmail([string]$email, [string]$attachmentpath){



            $message = new-object Net.Mail.MailMessage;

            $message.From = "******@gmail.com"; # Aqui va tu cuenta de gmail.

            $message.To.Add($email);

            $message.Subject = "Envio de información de equipo."; #Asunto del correo

            $message.Body = "INFO DE EQUIPO"; #Cuerpo o Mensaje del correo.

            $attachment = New-Object Net.Mail.Attachment($attachmentpath);

            $message.Attachments.Add($attachment);



            $smtp = new-object Net.Mail.SmtpClient("smtp.gmail.com", "587");

            $smtp.EnableSSL = $true;

            $smtp.Credentials = New-Object System.Net.NetworkCredential($Username, $Password);

            $smtp.send($message);

            write-host "Mail Sent" ; 

            $attachment.Dispose();

         }

        Send-ToEmail  -email "******@uanl.edu.mx" -attachmentpath $path; # En email pones el destinatario
}catch{ $_ | Out-File .\logs.txt -Append}
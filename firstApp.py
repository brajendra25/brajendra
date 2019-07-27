import clr
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from lxml.html import parse
#Import librabry for Window form from .Net
SWF = clr.AddReference("System.Windows.Forms")
print (SWF.Location)
import System.Windows.Forms as WinForms
from System.Drawing import Size, Point,Color,Font,Icon


class pythonApp(WinForms.Form):
    
    def __init__(self):
        self.BackColor = Color.LightBlue
        self.Text = "DNA CRYPTOGRAPHY"
        #ico = Icon("E:\Brajendra\logo.jpg");
        #self.Icon = ico
        self.AutoScaleBaseSize = Size(3, 5)
        self.ClientSize = Size(400, 117)
        h = WinForms.SystemInformation.CaptionHeight
        self.MinimumSize = Size(400, (207 + h))
        
        # Create the auth button
        self.button = WinForms.Button()
        self.button.Location = Point(250, 10)
        self.button.Size = Size(100, 10)
        self.button.TabIndex = 2
        self.button.Text = "Click Me!"

        # Register the event handler
        self.button.Click += self.button_Click
           
        
        self.AuthLabel = WinForms.Label()
        self.AuthLabel.Text = "Authentication :";
        self.AuthLabel.Name = "Auth";
        self.AuthLabel.Location = Point(10, 2);
        self.AuthLabel.Height = 5;
        self.AuthLabel.Width = 100;
        self.AuthLabel.ForeColor = Color.Blue;
        # Create the Authentication text box
        self.textbox = WinForms.TextBox()
        self.textbox.Id="authString"
        self.textbox.Text = ""
        self.textbox.TabIndex = 1
        self.textbox.Size = Size(200, 80)
        self.textbox.Location = Point(10, 10)
        
        # Create the Authentication Successfull text box
        self.textbox2 = WinForms.TextBox()
        self.textbox2.Id="txt2"
        self.textbox2.Text = ""
        self.textbox2.TabIndex = 3
        self.textbox2.Size = Size(200, 80)
        self.textbox2.Location = Point(10, 20)
        
        self.InputLabel = WinForms.Label()
        self.InputLabel.Text = "Input :";
        self.InputLabel.Name = "Auth";
        self.InputLabel.Location = Point(10, 30);
        self.InputLabel.Height = 5;
        self.InputLabel.Width = 100;
        self.InputLabel.ForeColor = Color.Blue;
        
        # Create the multi text box
        self.multiLineText1 = WinForms.TextBox()
        self.multiLineText1.Id="txt2"
        self.multiLineText1.Text = ""
        self.multiLineText1.TabIndex = 4
        self.multiLineText1.Multiline = bool('true')
        self.multiLineText1.AcceptsReturn = bool('true')
        self.multiLineText1.AcceptsTab = bool('true')
        self.multiLineText1.WordWrap = bool('true')
        self.multiLineText1.Size = Size(300, 30)
        self.multiLineText1.Location = Point(10, 40)
        self.multiLineText1.Visible = bool('false');
        
          # Create the button
        self.buttonEncrypted = WinForms.Button()
        self.buttonEncrypted.Location = Point(10, 75)
        self.buttonEncrypted.Size = Size(50, 10)
        self.buttonEncrypted.TabIndex = 5
        self.buttonEncrypted.Text = "Encrypted!"
       
        self.dynamicLabel = WinForms.Label()
        self.dynamicLabel.Text = "Dna Output:";
        self.dynamicLabel.Name = "DNA";
        self.dynamicLabel.Location = Point(10, 90);
        self.dynamicLabel.Height = 10;
        self.dynamicLabel.Width = 100;
        self.dynamicLabel.ForeColor = Color.Blue;
          # Create the multi text box
        self.multiLineOutput = WinForms.TextBox()
        self.multiLineOutput.Id="txtOutput"
        self.multiLineOutput.Text = ""
        self.multiLineOutput.TabIndex = 6
        self.multiLineOutput.Multiline = bool('true')
        self.multiLineOutput.AcceptsReturn = bool('true')
        self.multiLineOutput.AcceptsTab = bool('true')
        self.multiLineOutput.WordWrap = bool('true')
        self.multiLineOutput.Size = Size(300, 30)
        self.multiLineOutput.Location = Point(10, 100)
        
         # Create the button for decrypt
        self.buttonDecrypted = WinForms.Button()
        self.buttonDecrypted.Location = Point(10, 135)
        self.buttonDecrypted.Size = Size(50, 10)
        self.buttonDecrypted.TabIndex = 5
        self.buttonDecrypted.Text = "Decrypted!"
        
         # Create the text box
        self.textboxMsg = WinForms.TextBox()
        self.textboxMsg.Id="txtMsg"
        self.textboxMsg.Text = ""
        self.textboxMsg.TabIndex = 8
        self.textboxMsg.Size = Size(200, 100)
        self.textboxMsg.Location = Point(10, 160)
        
        
        self.buttonEncrypted.Click += self.buttonEncrypted_Click
        self.buttonDecrypted.Click += self.buttonDecrypted_Click

        
        # Add the controls to the form
        self.AcceptButton = self.button
        self.Controls.Add(self.AuthLabel)
        self.Controls.Add(self.button)
        self.Controls.Add(self.textbox)
        self.Controls.Add(self.textbox2)
        self.Controls.Add(self.InputLabel)
        
        self.Controls.Add(self.multiLineText1)
        self.Controls.Add(self.buttonEncrypted)
        self.Controls.Add(self.dynamicLabel)
        self.Controls.Add(self.multiLineOutput)
        self.Controls.Add(self.buttonDecrypted)
        self.Controls.Add(self.textboxMsg)
        #End
      
    
    #Logic for Encryption and Decryption
    
    def button_Click(self, sender, args):
        if __name__ == '__main__':
            '''user login values'''
            dict = {'7500':"1",'7089':"2",'123':'3'}
            flag=0
            a=self.textbox.Text
            for i in dict.keys():
            #print("i",i)
                if(i==a):
                    flag = 1
                if flag==1:
                    self.textbox2.Text = "User is Authenticaticated !!"
                    self.textbox2.ForeColor = Color.Green;
                else:
                    self.textbox2.Text = "User not Authenticaticated:"
                    self.textbox2.ForeColor = Color.Red;
         
    def buttonEncrypted_Click(self, sender, args):
        text = self.multiLineText1.Text
        key ='uni'
        global keyValue
        while len(text) % 16 != 0:           #checking the length of the text
            text += 'X'
        cipher = AES.new(SHA256.new(key.encode()).digest())               #using key on the message to be encrypted
        encrypted = cipher.encrypt(text.encode())  
        encryptedString= base64.b64encode(encrypted).decode() 
        str=encryptedString
        keyValue = encryptedString
        list=[]
        for i in range(len(str)):
            a=str[i]
            b='{0:08b}'.format(ord(a),'b') #changing each letter of the message into binary form along the length.
            list.append(b)
        dict = {'A' :'00','C' : '01','G':'10','T': '11'}
        str1 = ''.join(list)
        split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
        rev_subs = { v:k for k,v in dict.items()}
        str2 = ''.join([rev_subs.get(item,item) for item in (split_string(str1,2))])
        self.multiLineOutput.Text = str2
     
    def buttonDecrypted_Click(self, sender, args):
        text = keyValue
        key = 'uni'
        cipher = AES.new(SHA256.new(key.encode()).digest())
        decrypted = cipher.decrypt(base64.b64decode(text))  
        #decrypting the message using the same key
        retvaue = decrypted.decode().rstrip('X')
        self.textboxMsg.Text = retvaue
        #self.textboxMsg.ForeColor = Color.Green;
        
 #End
 
    def run(self):
        WinForms.Application.Run(self)
       
def main():
    form = pythonApp()
    app = WinForms.Application
    app.Run(form)


if __name__ == '__main__':
    main()
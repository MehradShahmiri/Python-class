class time:
    def __init__(self,hourv=0,minutev=0,secondv=0):
        self.hour=hourv
        self.minute=minutev
        self.second=secondv
    def show(self):
        return str(self.hour)+':'+str(self.minute)+':'+str(self.second)
    def __str__(self):
        return str(self.hour)+':'+str(self.minute)+':'+str(self.second)
    def __repr__(self):
        return str(self.hour)+':'+str(self.minute)+':'+str(self.second)
    
    def __add__(self,other):
        plushour=self.hour+other.hour
        plusminute=self.minute+other.minute
        plussecond=self.second+other.second
        if plussecond>59:
            plussecond -=60
            plusminute +=1
        if pluminute>59:
            plusminute -=60
            plushour +=1
        return str(plushour)+':'+str(plusminute)+':'+str(plussecond)

    def __sub__(self,other):
        minhour=self.hour-other.hour
        minminute=self.minute-other.minute
        minsecond=self.second-other.second
        return str(minhour)+':'+str(minminute)+':'+str(minsecond)
    def __lt__(self,other):
        s1=self.hour*3600+self.minute*60+self.second
        s2=other.hour*3600+other.minute*60+other.second
        if s1<s2:
          return 'true'
        else:
          return 'false'
    def __gt__(self,other):
        s1=self.hour*3600+self.minute*60+self.second
        s2=other.hour*3600+other.minute*60+other.second
        if s1>s2:
          return 'true'
        else:
          return 'false'
    def __eq__(self, other):
        if self.hour==other.hour and self.minute==other.minute and self.second==other.second:
          return "true"
        else:
          return "false"      

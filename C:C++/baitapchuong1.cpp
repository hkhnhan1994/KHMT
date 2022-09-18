#include <iostream>
using namespace std;
class human{
    protected:
        string name;
        int age;
        string characteristic;
    public:
        
        human(string _name, int _age, string _character)
        {
            name=_name;
            age=_age;
            characteristic=_character;
        }
        
        virtual void eat()=0;
        virtual void move()=0;
        virtual void fuck()=0;
};
class women:public human{
    public:
        women(string _name, int _age, string _character):human(_name,_age,_character){}
        int v1,v2,v3;
        virtual bool Ispregnant(){
            return 1;
        };
        virtual void eat(){
            cout<<"like a wonderful bird";
        }
        virtual void move(){
            cout<<"moving sneakily like a snake";
        }
        virtual void fuck(){
            cout<< "burning like a crazy cow";
        }
};
int main(){
    women helena("helena",23,"funny");
    human* girl1= new women("helena",23,"funny");
    human* girl2= new women("andy",23,"angry");
    human* group_woman[2]={girl1,girl2};
    for (int i=0;i<2;i++)
        group_woman[i]->fuck();
    return 0;
}
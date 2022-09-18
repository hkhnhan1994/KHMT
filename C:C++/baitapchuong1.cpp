#include <iostream>
using namespace std;
class human{
    protected:
        char* name;
        int age;
        int characteristic;
    public:
        
        human(string _name, int _age, int _character)
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
        women();
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
    women helena=new women();

    return 0;
}
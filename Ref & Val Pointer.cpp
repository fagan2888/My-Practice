
class Foo{
    public:
    
    int bar;
    
    int calcFooBar1 (int val , int mult ){
        bar = val * mult ;
        val = bar;
        return bar ;
    }

    int calcFooBar2 (int & val , int & mult ){
        bar = val * mult ;
        val = bar;
        return bar ;
    }

    int calcFooBar3 (int * val , int * mult ){
        bar = (* val) * (* mult );
        val = &bar;
        return bar ;
    }
    
    int calcFooBar4 ( const int & val , const int & mult ){
        bar = val * mult ;
        val = bar;
        return bar ;
    }
};

int main (int argc , const char * argv []) {

Foo f;
int val = 1.0;
int mult = 5.0;

int ret = f. calcFooBar1 (val , mult );

std :: cout << val << std :: endl ;
std :: cout << mult << std :: endl ;
std :: cout << ret << std :: endl ;

val = 1.0;
mult = 5.0;

ret = f. calcFooBar2 (val , mult );

std :: cout << val << std :: endl ;
std :: cout << mult << std :: endl ;
std :: cout << ret << std :: endl ;

val = 1.0;
mult = 5.0;

ret = f. calcFooBar3 (& val , & mult );

std :: cout << val << std :: endl ;
std :: cout << mult << std :: endl ;
std :: cout << ret << std :: endl ;

ret4 = f. calcFooBar4 (val , mult );

return 0;
}

# Backend Manager for Django

Módulo Backend para aplicaciones web SaaS seguras escritas en Django 1.7 y con la elegancia de Bootstrap 3.

Por medio de este Backend podrás gestionar las diferentes partes del sistema: usuarios, perfiles, recursos, permisos, módulos, planes SaaS, menús, asociaciones, empresas, sedes, logs, seguridad, internacionalización y mucho más!.

Ahora, cuando inicias un proyecto comenzarás directamente a atender(implementar) los requisitos de tu nuevo sistema, ya que Backengo se encargó de todo el trabajo inicial repetitivo de todo proyecto de software así como de los componentes o librerías que necesitas antes de comenzar a desarrollar una aplicación web moderna y segura.

Este Backend es el entregable más importante de todo UN MARCO DE TRABAJO para desarrollar app WEB MODERNAS Y SEGURAS denominado "ScrumSAD".


![desktop](https://github.com/submitconsulting/backengo/blob/master/media/test_images/img1.png)
![mobile](https://github.com/submitconsulting/backengo/blob/master/media/test_images/img3.png)
## Documentation


- [Diseño UML][uml]
- [Guía del desarrollador][manual]
- [Demo en línea][demo]

Usuario: `admin`

Password: `12345`

[uml]: http://backengo-model.appspot.com
[demo]: http://educaci-dns.com:8001/
[manual]: https://github.com/submitconsulting/backengo/blob/master/Backengo---Manual.docx?raw=true

## How to Get Started

1 Install python 2.7.x, for win check Path

>C:\Python27\Scripts;C:\Python27;

2 clone this repo or download .zip file

3 install all the necessary packages (best done inside of a virtual environment)

    $pip install -r requirements.txt

  para instalar pip revise [Guía del desarrollador][manual]

4 run the app

    $python manage.py runserver


## How to Get Started Professionally

### virtualenv install

    D:\>pip install virtualenv

### create app structure (optional)

    D:\>md dev\apps\backengo-root
    D:\>cd dev\apps\backengo-root
    D:\dev\apps\backengo-root>

```
D:\>
└── dev
    └── apps
        └── backengo-root

```

### virtualenv installing

    D:\dev\apps>pip install virtualenv

#### creating virtualenv

    D:\dev\apps\backengo-root>virtualenv veb
    New python executable in veb\Scripts\python.exe
    Installing setuptools, pip...done.

### activating virtualenv

    D:\dev\apps\backengo-root>veb\Scripts\activate
    (veb) D:\dev\apps\backengo-root>

### installing requirements

    (veb) D:\dev\apps\backengo-root>cd backengo
    (veb) D:\dev\apps\backengo-root\backengo>pip install -r requirements.txt

### runing
    
    (veb) D:\dev\apps\backengo-root\backengo>python manage.py runserver

### Final structure (optional)


```
D:\dev\apps
└── backengo-root
    ├── backengo
    │   └── manage.py
    └── veb
        └── Scripts 
            └── activate.bat   
```
 backengo, es la carpeta descompriminda descargada de github como backengo-master


## Dev commands:
  
    

    D:\>
    dev\apps\backengo-root\veb\Scripts\activate
    cd dev\apps\backengo-root\backengo

    (veb) D:\dev\apps\backengo-root\backengo>python -m django-admin makemessages -l es_PE 

    (veb) D:\dev\apps\backengo-root\backengo>python -m django-admin makemessages -d djangojs -l es_PE --ignore=admin

    (veb) D:\dev\apps\backengo-root\backengo>python -m django-admin compilemessages

    (veb) D:\dev\apps\backengo-root\backengo>python manage.py makemigrations params
    (veb) D:\dev\apps\backengo-root\backengo>python manage.py migrate params

  For makemessages or compilemessages, configure gettext-utils and add Path 
  >D:\dev\apps\backengo-root\veb\Scripts;C:\gettext-utils\gettext-tools-0.17\bin;
  
  View https://docs.djangoproject.com/en/dev/topics/i18n/translation/#gettext-on-windows 

Backup/load database
-------------------
See in the settings.py setting for FIXTURE_DIRS

    $python manage.py dumpdata > fixtures/ini_data.json
    $python manage.py loaddata ini_data


Clean/restore database
-------------------
Run the following command:

    $python manage.py flush


exec

  >delete from django_content_type;

  >delete from auth_permission;

 
And run the following command:

    $python manage.py loaddata ini_data


3rd-Party Apps/Libraries/Plugins
--------------------------------

This app uses the following:

* Twitter Bootstrap 3 (http://getbootstrap.com)
* Django Crispy Forms (http://django-crispy-forms.readthedocs.org/en/latest)



## Author

- Angel Sullon Macalupu (asullom@gmail.com)

## Contributors

See https://github.com/submitconsulting/backengo/contributors

## Important

* Todas las vistas están basadas en clases (class-based views)
* `django_migrations` es nuevo en django 1.7.x 



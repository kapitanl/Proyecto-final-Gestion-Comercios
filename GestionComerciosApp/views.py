from django.shortcuts import render
from django.template import Context
# Create your views here.


def home(request):
    return render(request, 'home.html')

def localidades(request):

    lugares = ['Resistencia','Avia Terai','Campo Largo','Charata','Colonia Elisa','Colonia Benitez','Colonias Unidad','Comandancia Frías','Concepción del Bermejo','Coronel Du Graty','Corzuela','El Paranacito','El Sauzalito','Fortin Belgrano','Ganacedo','Gral. José de San Martín','General Pinedo','Hermoso Campo','Isla Soto','Juan José Castelli','La Clotilde','La Escondida','La Leonesa','La Tigra','La Verde','Las Breñas','Las Garcitas','Las Hacheras','Las Palmas','Los Frentones','Machagai','Makallé','Margarita Belén','Miraflores','Misión Nueva Pompeya','Napenay','Pampa del Indio','Pampa del Infierno','Presidencia de la Plaza','Presidencia Roca','Puerto Bermejo','Puerto Las Palmas','Puerto Tirol','Quitilipi','San Bernardo','Paraje San Fernando','Santa Sylvina','Taco Pozo','Tres Isletas','Villa Ángela','Villa Berthet','Villa Río Bermejito']

    return render(request, 'localidades.html', {"lugares":lugares})
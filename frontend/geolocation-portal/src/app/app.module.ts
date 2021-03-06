import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { MapComponent } from './map/map.component';
import { MenuComponent } from './menu/menu.component';
import { MDBBootstrapModule } from 'angular-bootstrap-md';
import { MapNavComponent } from './map-nav/map-nav.component';
import { VorschlagComponent } from './vorschlag/vorschlag.component';
import { ImpressumComponent } from './impressum/impressum.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule }    from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';

   



@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    MapComponent,
    MenuComponent,
    MapNavComponent,
    VorschlagComponent,
    ImpressumComponent

 
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MDBBootstrapModule.forRoot(),
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [CookieService],
  bootstrap: [AppComponent]
})
export class AppModule { }

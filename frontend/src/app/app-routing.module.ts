import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ImageStoreComponent } from './pages/dashboard/image-store/image-store.component';
import { AboutComponent } from './pages/dashboard/about/about.component';
import { SettingsComponent } from './pages/dashboard/settings/settings.component';
import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';

const routes: Routes = [
    {
      path: 'home',
      component: ImageStoreComponent,
      data: { title: 'Home' }
    },
    { path: '',
      redirectTo: '/home',
      pathMatch: 'full'
    },
    {
        path: 'about',
        component: AboutComponent,
        data: { title: 'About' }
    },
    {
        path: 'settings',
        component: SettingsComponent,
        data: { title: 'Settings' }
    },
    {path: '404', component: PageNotFoundComponent},
    {path: '**', redirectTo: '/404'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

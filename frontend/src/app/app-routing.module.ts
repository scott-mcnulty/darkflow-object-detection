import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ImageStoreComponent } from './pages/image-store/image-store.component';
import { AboutComponent } from './pages/about/about.component';
import { SettingsComponent } from './pages/settings/settings.component';
import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';
import { FeedComponent } from './pages/feed/feed.component';

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
        path: 'feed',
        component: FeedComponent,
        data: { title: 'Feed' }
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

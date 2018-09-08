import { Component } from '@angular/core';

@Component({
  selector: 'app-nav',
  templateUrl: './app-nav.component.html',
  styleUrls: ['./app-nav.component.scss']
})
export class AppNavComponent {
  public nav = [
    {
      titleKey: 'app_nav_home',
      path: '/'
    },
    {
      titleKey: 'app_nav_browse',
      path: '/browse-page'
    },
    {
      titleKey: 'app_nav_build',
      path: '/build-page'
    }
  ];
}

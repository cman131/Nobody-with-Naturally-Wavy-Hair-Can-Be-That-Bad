import { NgModule } from '@angular/core';
import { CollectionSearchService } from './shared/services/collection-search.service';

// Specify entry components, module-level providers, etc. here.
@NgModule({
  providers: [
    CollectionSearchService
  ],
  entryComponents: [
  ]
})
export class AppExtrasModule { }

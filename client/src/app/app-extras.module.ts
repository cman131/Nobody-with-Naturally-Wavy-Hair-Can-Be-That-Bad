import { NgModule } from '@angular/core';
import { CollectionSearchService } from './shared/services/collection-search.service';
import { ProDataService } from './shared/services/pro-data.service';

// Specify entry components, module-level providers, etc. here.
@NgModule({
  providers: [
    CollectionSearchService,
    ProDataService
  ],
  entryComponents: [
  ]
})
export class AppExtrasModule { }

export class SettingsForm {
  constructor (
      public cameraServerHostname: string,
      public cameraServerPort: string,
      public inferenceServerHostname: string,
      public inferenceServerPort: string
  ) {}
}

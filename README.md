# langanki
Tool for exporting foreign-language vocabulary to Anki

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

1. Install Anki - https://apps.ankiweb.net
2. Instal AnkiConnect add-on https://ankiweb.net/shared/info/2055492159
3. Enable Google Sheets API - https://www.youtube.com/watch?v=bu5wXjz2KvU

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/Pojmajo/langanki.git
   ```
2. Prepare Virtual Environment
3. Install required packages
   ```sh
   pip install -r requirements.txt
   ```
   
### Google Sheets
1. Prepare spreadsheet called 'langanki' which is going to be used by langanki App.
2. Name worksheets (tabs at the bottom) accordingly to language i.e. 'Spanish' to include
audio to the Back of our AnkiCards. 
Worksheet name would also be name of an AnkiDeck.

* First column words to translate _A_ - AnkiCard Front
* Second column translated words _B_ - AnkiCard Back
3. To ease word translation we can use Google Sheets formula for 
   ```sh
   =GOOGLETRANSLATE(cell with text, “source language”, “target language”)
   ```
   
### Usage
1. Open AnkiApp (A temporary solution until the app opens on its own)
2. Verify that you are logged to your Anki account to allow for Deck synchronization with AnkiWeb
3. Send following command. -i google -> is for selecting supported Importer.
   ```sh
   python langanki.py -i google
   ```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. 
Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. 
You can also simply open an issue.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [AnkiConnect](https://foosoft.net/projects/anki-connect/)

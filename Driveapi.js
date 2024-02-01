const {google} = require('googleapis');
const OAuth2 = google.auth.OAuth2;

const oauth2Client = new OAuth2(
    "261723641977-c5a1jii2irbi1th2skue4qsvvp21p9gr.apps.googleusercontent.com",
    "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",
  "https://google.com"
);

oauth2Client.setCredentials({
  refresh_token: YOUR_REFRESH_TOKEN
});

const drive = google.drive({
  version: 'v3',
  auth: oauth2Client
});

async function checkNewFolders(lastChecked) {
  const res = await drive.files.list({
    q: `mimeType='application/vnd.google-apps.folder' and createdTime > '${lastChecked}'`,
    fields: 'nextPageToken, files(id, name, createdTime)',
    spaces: 'drive',
  });

  const folders = res.data.files;
  if (folders.length) {
    console.log('New folders:', folders);
  } else {
    console.log('No new folders found.');
  }
}

// YYYY-MM-DDTHH:MM:SSZ 형식의 마지막 확인 시간
const lastChecked = '2023-01-01T00:00:00Z';
checkNewFolders(lastChecked);

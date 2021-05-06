function doPost(e) {
  return process(e);
}

function doGet(e) {
  return process(e);
}

function process(e) {
  const values =  e.parameter.values;
  
  var sh = SpreadsheetApp.openById("1jS6wBqMgd9iUxuqlhMbuwaBLNI5F1zUQuMasn4xc46w").getSheetByName("Sheet1");
  
  if(values != null) {
     sh.getRange("A1").setValue(values);
     return ContentService.createTextOutput("200");
  } else {
     return ContentService.createTextOutput(sh.getRange("A1").getValues()[0]);
  }
}

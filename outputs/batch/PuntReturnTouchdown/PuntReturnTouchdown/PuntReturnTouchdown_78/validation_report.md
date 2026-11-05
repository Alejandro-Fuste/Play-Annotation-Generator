# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_78`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_78/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 64 |
| Player Tracks | 64 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 157 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 749 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 158: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 749 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [65-229] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [233-276] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-325] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-412] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-167] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-176] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-249] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-388] for track '2' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-83] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-236] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-156] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-168] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-227] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-216] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [220-276] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-364] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-257] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-219] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-293] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-134] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-457] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [65-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-153] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-189] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-450] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-193] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-425] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-117] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-429] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-471] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [476-493] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-162] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [65-115] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-391] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-671] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-17] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-64] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-126] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-140] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-306] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [309-321] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-452] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-386] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [389-421] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [426-745] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-220] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-428] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-454] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-240] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-260] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-314] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-438] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-296] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-321] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [325-328] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-444] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-453] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-351] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-378] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [397-408] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-428] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-455] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-443] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-506] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-567] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-617] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [620-624] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [630-640] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [642-645] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [648-714] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [434-503] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [505-749] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-623] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-465] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [470-508] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [475-477] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-488] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-483] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [487-489] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-506] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-521] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-623] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [627-667] for track '46' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [673-675] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [677-682] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [685-686] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [690-692] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [698-749] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-548] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-568] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-600] for track '48' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [607-612] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [617-619] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-560] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-592] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [569-597] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [600-623] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [574-627] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [634-636] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [581-610] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [617-694] for track '54' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [631-635] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [637-650] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [653-654] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [689-690] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [705-706] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [639-640] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [646-650] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [693-739] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [738-743] for track '61' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
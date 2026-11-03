# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_101`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_101/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [9-184] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-269] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [111-184] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-219] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-235] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-245] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-261] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-299] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-285] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-290] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [75-246] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [248-249] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [252-264] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-102] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-299] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [9-183] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-95] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-293] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-38] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-126] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-255] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [259-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-237] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-287] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-121] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-299] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [9-260] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [9-183] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-221] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-235] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-126] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-250] for track '19' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [264-289] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [291-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-113] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-60] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-91] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-254] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-264] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-277] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-284] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-289] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-299] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-150] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-183] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-276] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-295] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-286] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-298] for track '40' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
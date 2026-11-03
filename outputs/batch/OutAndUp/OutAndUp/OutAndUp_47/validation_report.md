# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_47`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 143 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 49: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PassBlock' range [28-80] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-57] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SellOut' range [96-97] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [126-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-47] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-54] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-82] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-57] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-86] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-207] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-47] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-71] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-273] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [279-282] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-54] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-68] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-78] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-241] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [244-279] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [281-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-54] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-78] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-48] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-78] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [85-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-54] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-48] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [84-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-47] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [50-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-71] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [74-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-144] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-37] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-78] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-172] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-237] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-57] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [131-132] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 144, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [144-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-228] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-78] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-18] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-48] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-54] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-69] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-102] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-167] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-125] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-144] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-126] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-144] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-144] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-212] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-250] for track '30' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [253-292] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-164] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-243] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-264] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-279] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-295] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-161] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-235] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-299] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-231] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-255] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-279] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-293] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-240] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-251] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-276] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-282] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-289] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '41' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
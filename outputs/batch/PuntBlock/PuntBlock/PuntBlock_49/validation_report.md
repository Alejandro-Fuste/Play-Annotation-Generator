# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_49`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [0-164] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-190] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-217] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-31] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-16] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-57] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-72] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-175] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-189] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [0-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-217] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-33] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-190] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [70-169] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [172-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-192] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-212] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-225] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-219] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-106] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-16] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-46] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-41] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-86] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-139] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [141-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-135] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-211] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-127] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-137] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-139] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-229] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-190] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-195] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-193] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-228] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [210-216] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '37' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
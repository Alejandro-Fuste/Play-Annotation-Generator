# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_40`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_40/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureRecovery' for track '2' has invalid range: start=199, end=133. Clamping end to start.
> - Action 'Action_PuntBall' range [54-154] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-221] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-133] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-298] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-45] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-220] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-241] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-236] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-81] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-72] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-188] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-172] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-194] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-23] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-30] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-172] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-134] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-14] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-18] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-23] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-26] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-39] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-220] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-170] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-195] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-219] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-35] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-126] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-245] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [249-251] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-20] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-73] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-172] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-52] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-88] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-290] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-222] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-111] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-117] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-130] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-116] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-229] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-296] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-122] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-130] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-216] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-201] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-211] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-222] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-251] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-257] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-159] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-189] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-200] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-175] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-236] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-291] for track '37' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
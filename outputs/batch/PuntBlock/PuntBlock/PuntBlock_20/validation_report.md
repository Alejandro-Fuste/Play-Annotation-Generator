# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_20`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_20/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [29-225] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-274] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-266] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-280] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-87] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-97] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-122] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-176] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-183] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-315] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [82-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-123] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-135] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-356] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-194] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-209] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [29-42] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-52] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-108] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-219] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-197] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-80] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-290] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-359] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [55-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-359] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-245] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-333] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-280] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [290-292] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-300] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-310] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-314] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-359] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-178] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-217] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-285] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-358] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-176] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-176] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-346] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-276] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-282] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-335] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-359] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-351] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-359] for track '34' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
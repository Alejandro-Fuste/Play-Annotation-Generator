# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_63`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_63/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 128: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureRecovery' for track '8' has invalid range: start=144, end=137. Clamping end to start.
> - Action 'Action_None' range [1-187] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-102] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-40] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-52] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-102] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-101] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [1-162] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-18] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [52-68] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [70-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-55] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-197] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-113] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-48] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-19] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-29] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-178] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-162] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-239] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-115] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-134] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-141] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-162] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-133] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-222] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-223] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-238] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-207] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-217] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-224] for track '35' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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
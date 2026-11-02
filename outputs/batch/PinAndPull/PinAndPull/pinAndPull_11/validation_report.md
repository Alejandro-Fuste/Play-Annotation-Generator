# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `pinAndPull_11`
- **Input XML**: `outputs/batch/PinAndPull/pinAndPull/pinAndPull_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PinAndPull.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 24: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '1' (RT) duration 95 frames exceeds threshold 90 frames [start=35, end=129].
> - Validation warning: Action 'Action_PullBlock' for track '4' (RG) duration 95 frames exceeds threshold 90 frames [start=35, end=129].
> - Action 'Action_None' range [32-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [35-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-130] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [68-168] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [35-64] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-38] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-48] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-102] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-48] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-92] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-169] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-152] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [80-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-162] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-194] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-201] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-174] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-201] for track '20' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-151] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-174] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-181] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-191] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-209] for track '25' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
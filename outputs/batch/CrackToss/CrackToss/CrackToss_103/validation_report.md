# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_103`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_103/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 249 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
> - Action 'Action_None' range [123-218] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-249] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-235] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [121-157] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [159-207] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-249] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-145] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [154-212] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [214-215] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [217-249] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-249] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [123-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [126-207] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-238] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-158] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-195] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-199] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-230] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-232] for track '31' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
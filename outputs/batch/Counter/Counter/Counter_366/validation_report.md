# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_366`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_366/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_DownBlock' range [109-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-246] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-177] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-177] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-163] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-181] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-269] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-169] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [109-149] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-253] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-113] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [143-248] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [268-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [109-145] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [148-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-105] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [109-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [119-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-194] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-186] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-213] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-220] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-258] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-252] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-269] for track '27' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
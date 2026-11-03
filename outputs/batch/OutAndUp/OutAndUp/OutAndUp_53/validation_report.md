# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_53`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [26–41], lower_priority='Action_PassBlock' annotated_start=29, effective_Action_PassBlock_start=42.
> - Action 'Action_None' range [26-87] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-190] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-241] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-129] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-168] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-176] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-190] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-256] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [114-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [116-241] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [121-241] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [250-252] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [163-191] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [193-258] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-267] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-250] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-241] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [29-250] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-226] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [134-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [138-145] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-241] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-250] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-234] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-241] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-256] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-221] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-246] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-241] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-260] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-258] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-267] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-247] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-250] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-252] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-255] for track '36' has 1 frames without a visible bounding box.
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
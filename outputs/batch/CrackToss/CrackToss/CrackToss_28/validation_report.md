# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_28`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_28/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 298 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
> - Segment 'Action_BallSnap' for track '5' has invalid range: start=124, end=33. Clamping end to start.
> - Action 'Action_None' range [124-184] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-123] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-183] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-219] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-260] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [124-166] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-157] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-173] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-214] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-213] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-266] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-209] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [127-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-219] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-181] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [169-298] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-123] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-231] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-35] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [127-211] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-233] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-188] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-151] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-194] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-123] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-161] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [166-298] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-258] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-281] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-243] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-245] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-282] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-239] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-250] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-289] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-298] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
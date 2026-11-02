# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_103`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_103/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_BallCarry' for track '14' has invalid range: start=180, end=139. Clamping end to start.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [149–160], lower_priority='Action_ZoneBlock' annotated_start=152, effective_Action_ZoneBlock_start=161.
> - Action 'Action_None' range [149-195] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-220] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-295] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-336] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-359] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [152-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [176-229] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-295] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [149-188] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-216] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-261] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-290] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-235] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-232] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-307] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [311-338] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-351] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-254] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-305] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [152-216] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [152-207] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [131-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-194] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-299] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-359] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-213] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-359] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-148] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [161-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-359] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-177] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-290] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-307] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-350] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [215-307] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-347] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-344] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-354] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-355] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-327] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-336] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-353] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
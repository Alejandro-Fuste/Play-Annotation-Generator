# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_42`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_42/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [100–110], lower_priority='Action_ZoneBlock' annotated_start=103, effective_Action_ZoneBlock_start=111.
> - Action 'Action_None' range [100-215] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [129-144] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [148-193] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [108-124] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-245] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-221] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-119] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-151] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [119-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-171] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-250] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-23] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-242] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-225] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-177] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-213] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-207] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-212] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-269] for track '22' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
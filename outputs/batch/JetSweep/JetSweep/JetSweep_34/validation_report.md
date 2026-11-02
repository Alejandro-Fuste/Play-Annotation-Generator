# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_34`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_34/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 28 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [77–84], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=85.
> - Action 'Action_None' range [77-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-192] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [224-261] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-268] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [271-299] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-191] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-217] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-188] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-257] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-257] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-208] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-256] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-233] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [77-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-207] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-268] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-170] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-198] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-254] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-272] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [107-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-241] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-267] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-125] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-207] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-203] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-256] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-298] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-215] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-226] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-258] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-270] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-291] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-299] for track '31' has 1 frames without a visible bounding box.
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
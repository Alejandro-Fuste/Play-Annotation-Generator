# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_228`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_228/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 27 |
| Ball Tracks | 1 |
| CSV events parsed | 21 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [217–231], lower_priority='Action_ZoneBlock' annotated_start=220, effective_Action_ZoneBlock_start=232.
> - Segment 'Action_Handoff' for track '7' has invalid range: start=227, end=216. Clamping end to start.
> - Action 'Action_None' range [217-272] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-379] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [220-281] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-373] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-248] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-342] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-203] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-208] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [220-351] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [358-383] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-291] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-290] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-278] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [220-233] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [238-297] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-350] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-379] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-310] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [223-297] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-258] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-285] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-389] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-370] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-377] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-384] for track '27' has 1 frames without a visible bounding box.
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
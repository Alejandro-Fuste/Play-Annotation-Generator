# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_127`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_127/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [4–21], lower_priority='Action_ZoneBlock' annotated_start=7, effective_Action_ZoneBlock_start=22.
> - Action 'Action_None' range [4-285] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-288] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [51-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [216-233] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [236-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-34] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-275] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-140] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-101] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-216] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [7-13] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-116] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [7-16] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-299] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-143] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-268] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-225] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-249] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-273] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [278-284] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-291] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
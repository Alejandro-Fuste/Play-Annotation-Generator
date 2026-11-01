# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_249`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_249/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 498: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - Row 498: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 498: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [10–27], lower_priority='Action_ZoneBlock' annotated_start=13, effective_Action_ZoneBlock_start=28.
> - Action 'Action_None' range [10-187] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-216] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-223] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [59-229] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [231-241] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [248-250] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-224] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [10-27] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-91] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-225] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-226] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-51] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-217] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-30] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-50] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-55] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-163] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-202] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-234] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-31] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-40] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-91] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-21] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-68] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-226] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-214] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-259] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-252] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-268] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-253] for track '31' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
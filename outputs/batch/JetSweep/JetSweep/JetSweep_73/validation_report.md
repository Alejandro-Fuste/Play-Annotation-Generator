# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_73`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_73/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 107 frames exceeds threshold 90 frames [start=47, end=153].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (LT) duration 107 frames exceeds threshold 90 frames [start=47, end=153].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (C) duration 107 frames exceeds threshold 90 frames [start=47, end=153].
> - Action 'Action_None' range [46-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-385] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-312] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-320] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-411] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-385] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-116] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-350] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-350] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-336] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-93] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-104] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-116] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-149] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-216] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-229] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-123] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-164] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-176] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-202] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-403] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-354] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [78-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-156] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-223] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-364] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-73] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-401] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-388] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-347] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-200] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-411] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-358] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-360] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-212] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-395] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-256] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-345] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-408] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-395] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-415] for track '36' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
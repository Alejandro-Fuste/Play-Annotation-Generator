# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_259`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_259/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 158 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [5–20], lower_priority='Action_ZoneBlock' annotated_start=8, effective_Action_ZoneBlock_start=21.
> - Action 'Action_None' range [5-60] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-105] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [110-116] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [5-27] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-70] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-77] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-127] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-171] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-101] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-129] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [5-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-208] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-121] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-37] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-67] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-97] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [8-69] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-85] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-110] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-151] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [5-137] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-107] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [8-38] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-95] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-129] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-211] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-35] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-78] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 91, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [91-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [32-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [58-91] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-95] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-144] for track '16' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-195] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-187] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [8-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-153] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-65] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-106] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-38] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-137] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [139-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-172] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [8-25] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-65] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-8] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-18] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-26] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-34] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-135] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-56] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-78] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-90] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-97] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-107] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-107] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-125] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-172] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-207] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-233] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-131] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-117] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-209] for track '29' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-129] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-141] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-147] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-214] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-234] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-215] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-227] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '38' has 1 frames without a visible bounding box.
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
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.